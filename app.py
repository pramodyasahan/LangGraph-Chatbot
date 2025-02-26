from fastapi import FastAPI  # Import FastAPI for creating the web service
from pydantic import BaseModel  # Import BaseModel for request validation
from typing import List  # Import List for type hinting
from langchain_community.tools.tavily_search import TavilySearchResults  # Import Tavily search tool
import os  # Import os for environment variable handling
from langgraph.prebuilt import create_react_agent  # Import function to create the AI agent
from langchain_groq import ChatGroq  # Import Groq LLM model
from dotenv import load_dotenv  # Import dotenv to load environment variables

# Load environment variables from .env file
load_dotenv()

# Retrieve Tavily API key from environment variables
tavily_api_key = os.environ["TAVILY_API_KEY"]

# Define supported model names
MODEL_NAMES = [
    "llama3-70b-8192",
    "mixtral-8x7b-32768"
]

# Initialize Tavily search tool with max 2 results
tool_tavily = TavilySearchResults(max_results=2, api_key=tavily_api_key)

# List of tools available to the AI agent
tools = [tool_tavily]

# Create a FastAPI application instance
app = FastAPI(title="LangGraph AI Agent")


# Define request body structure using Pydantic
class RequestState(BaseModel):
    model_name: str  # The name of the LLM model to use
    system_prompt: str  # The system prompt to modify agent behavior
    messages: List[str]  # List of messages in the conversation


# Define a POST endpoint for chat requests
@app.post("/chat")
def chat_endpoint(request: RequestState):
    # Validate model name
    if request.model_name not in MODEL_NAMES:
        return {"error": "Invalid model name. Please select a valid model."}

    # Initialize the Groq LLM model
    llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"), model_name=request.model_name)

    # Create the AI agent with the specified tools and system prompt
    agent = create_react_agent(llm, tools=tools, state_modifier=request.system_prompt)

    # Prepare the state with user messages
    state = {"messages": request.messages}

    # Invoke the agent with the provided state
    result = agent.invoke(state)

    return result  # Return the response from the AI agent


# Run the FastAPI application when the script is executed directly
if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="127.0.0.1", port=8000)
