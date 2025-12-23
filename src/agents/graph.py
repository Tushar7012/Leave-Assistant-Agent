import os
import functools
from typing import Annotated, Sequence, TypedDict, Union, Literal
from langchain_groq import ChatGroq
from langchain_core.messages import BaseMessage, HumanMessage, AIMessage, SystemMessage
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from pydantic import BaseModel
from langgraph.graph import StateGraph, END
from langgraph.prebuilt import create_react_agent
from dotenv import load_dotenv

# Import our tools
from src.agents.tools import fetch_employee_data, policy_search_tool, send_email_tool

load_dotenv()

# --- 1. LLM Setup ---
llm = ChatGroq(temperature=0, model_name="llama-3.1-8b-instant")

# --- 2. Supervisor Agent ---
members = ["DataAgent", "PolicyAgent", "EmailAgent"]
options = ["FINISH"] + members

class Route(BaseModel):
    """Select the next role."""
    next: Literal["FINISH", "DataAgent", "PolicyAgent", "EmailAgent"]

class AgentState(TypedDict):
    messages: Sequence[BaseMessage]
    next: str

system_prompt = (
    "You are a supervisor tasked with managing a conversation between the"
    " following workers: {members}. Given the following user request,"
    " respond with the worker to act next. Each worker will perform a"
    " task and respond with their results and status."
    " SYSTEM INSTRUCTIONS:"
    " 1. If the user asks a question, route to the appropriate worker."
    " 2. Once a worker has responded with the information, you MUST respond with FINISH."
    " 3. Do NOT call the same worker twice in a row for the same query."
    " 4. If the worker's response answers the user's question, output FINISH immediately."
)

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", system_prompt),
        MessagesPlaceholder(variable_name="messages"),
        (
            "system",
            "Given the conversation above, who should act next?"
            " Or should we FINISH? Select one of: {options}",
        ),
    ]
).partial(options=str(options), members=", ".join(members))

# Define the supervisor node function
def supervisor_node(state):
    # Check if the last message is from a worker to force termination
    last_message = state["messages"][-1]
    
    # If the last message is from a known worker, we assume the task is done for this turn.
    # We return FINISH directly without consulting the LLM to avoid infinite loops or hallucinations.
    if isinstance(last_message, AIMessage) and hasattr(last_message, 'name') and last_message.name in members:
        return {"next": "FINISH"}

    # Use with_structured_output for robust parsing
    chain = prompt | llm.with_structured_output(Route)
    result = chain.invoke({"messages": state["messages"]})
    return {"next": result.next}

# --- 3. Construct Graph ---

# Create simpler agent functions that call the LLM with tools directly
def create_simple_agent(llm, tools, system_message):
    """Create a simple agent that uses tools via function calling"""
    def agent(state):
        # Get messages from state
        messages = state["messages"]
        
        # Prepare the system message + conversation history
        full_messages = [SystemMessage(content=system_message)] + list(messages)
        
        # Bind tools to LLM
        llm_with_tools = llm.bind_tools(tools)
        
        # Get response
        response = llm_with_tools.invoke(full_messages)
       
        # Check if there are tool calls
        if response.tool_calls:
            # Execute tool calls and collect results
            tool_results = []
            for tool_call in response.tool_calls:
                tool_name = tool_call["name"]
                tool_args = tool_call["args"]
                
                # Find and execute the tool
                for tool in tools:
                    if tool.name == tool_name:
                        tool_result = tool.invoke(tool_args)
                        tool_results.append(f"Tool '{tool_name}' returned: {tool_result}")
                        break
            
            # Prepare the final messages with tool results
            tool_messages_text = "\n\n".join(tool_results)
            
            # Create a simple prompt asking the LLM to format the response
            format_prompt = f"{system_message}\n\nThe tool execution returned the following information:\n{tool_messages_text}\n\nNow provide a clear response to the user based on this information."
            
            final_response = llm.invoke([SystemMessage(content=format_prompt)] + list(messages))
            return final_response.content
        else:
            return response.content
    
    return agent


# Create agent functions
data_agent = create_simple_agent(
    llm,
    [fetch_employee_data],
    "You are a Data Agent. Use fetch_employee_data to get employee information. Return the FULL details provided by the tool."
)

policy_agent = create_simple_agent(
    llm,
    [policy_search_tool],
   "You are a Policy Agent. Use policy_search_tool to search company policies. Return the FULL policy details found."
)

email_agent = create_simple_agent(
    llm,
    [send_email_tool],
    "You are an Email Agent. Use send_email_tool to send emails. Return the FULL confirmation message provided by the tool."
)

# Node wrapper functions
def agent_node(state, agent,name):
    result_content = agent(state)
    return {"messages": [AIMessage(content=result_content, name=name)]}

data_node = functools.partial(agent_node, agent=data_agent, name="DataAgent")
policy_node = functools.partial(agent_node, agent=policy_agent, name="PolicyAgent")
email_node = functools.partial(agent_node, agent=email_agent, name="EmailAgent")

workflow = StateGraph(AgentState)

workflow.add_node("Supervisor", supervisor_node)
workflow.add_node("DataAgent", data_node)
workflow.add_node("PolicyAgent", policy_node)
workflow.add_node("EmailAgent", email_node)

for member in members:
    workflow.add_edge(member, "Supervisor")

# Properly route the conditional edges with a routing function
def route_supervisor(state):
    next_step = state["next"]
    if next_step == "FINISH":
        return END
    return next_step

workflow.add_conditional_edges("Supervisor", route_supervisor)
workflow.set_entry_point("Supervisor")

graph = workflow.compile()
