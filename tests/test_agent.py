import sys
import os
from dotenv import load_dotenv
from langchain_core.messages import HumanMessage

# Add src to path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../')))

from src.agents.graph import graph

load_dotenv()

def test_chat():
    print("--- Starting Console Test ---")
    if not os.getenv("GROQ_API_KEY") or os.getenv("GROQ_API_KEY") == "your_groq_api_key_here":
        print("ERROR: GROQ_API_KEY is missing in .env")
        return

    queries = [
        "What is the sick leave policy?",
        "My employee ID is EMP001. How much sick leave do I have?",
    ]

    for q in queries:
        print(f"\nUser: {q}")
        try:
            result = graph.invoke({"messages": [HumanMessage(content=q)]})
            print(f"AI: {result['messages'][-1].content}")
        except Exception as e:
            print(f"Error: {e}")

if __name__ == "__main__":
    test_chat()
