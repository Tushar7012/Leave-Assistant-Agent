import sys
import os
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS

# Add the project root to the system path to allow importing modules from src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../../')))

from src.agents.graph import graph

app = Flask(__name__)
# Enable CORS for frontend (allow all origins for production flexibility)
CORS(app)


@app.route("/")
def home():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message")
    if not user_message:
        return jsonify({"error": "No message provided"}), 400

    # Invoke the graph
    # We pass the user message as a HumanMessage
    from langchain_core.messages import HumanMessage
    
    initial_state = {"messages": [HumanMessage(content=user_message)]}
    
    # Run the graph
    try:
        final_state = graph.invoke(initial_state, config={"recursion_limit": 50})
        # Debug: Print the full message history to console
        print(f"DEBUG: Final State Messages: {final_state['messages']}")
        
        # Get the last message from the AI
        last_message = final_state["messages"][-1]
        response_text = last_message.content
        print(f"DEBUG: Response Text: {response_text}")
        
        return jsonify({"response": response_text})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(debug=True, port=5000)
