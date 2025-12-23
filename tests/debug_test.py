import sys
import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from src.agents.graph import graph

load_dotenv()

def simple_test():
    print("--- Simple Test ---")
    query = "What is the sick leave policy?"
    print(f"\nUser: {query}")
    try:
        result = graph.invoke(
            {"messages": [HumanMessage(content=query)]},
            config={"recursion_limit": 50}
        )
        print(f"\nAll messages in result:")
        for i, msg in enumerate(result['messages']):
            print(f"{i+1}. {type(msg).__name__} ({getattr(msg, 'name', 'no-name')}): {msg.content[:100]}...")
        
        print(f"\nFinal AI response: {result['messages'][-1].content}")
    except Exception as e:
        print(f"Error: {e}")
        import traceback
        traceback.print_exc()

if __name__ == "__main__":
    simple_test()
