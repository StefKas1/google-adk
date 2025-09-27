from google.adk.agents import Agent
from google.adk.tools import google_search  # Import the tool

from dotenv import load_dotenv

# 1. Might need elevated privileges
# 2. cd into: src/adk-streaming/app
# src/adk-streaming
# └── app/ # the web app folder
#     ├── .env # Gemini API key
#     └── google_search_agent/ # Agent folder
#         ├── __init__.py # Python package
#         └── agent.py # Agent definition
# 3. Run one of the following commands to
# a) launch the dev UI: adk web
# b) chat with your agent via termninal: adk run google_search_agent
# c) create a local FastAPI server, enabling you to test local cURL requests
# before you deploy your agent: adk api_server

load_dotenv()
root_agent = Agent(
    # A unique name for the agent.
    name="basic_search_agent",
    # Choose a model that supports
    # - Google search tool (supported by: gemini-2.5-flash)
    # - Live API: enables low-latency, two-way voice and video interactions with Gemini (not supported by: gemini-2.5-flash)
    # https://cloud.google.com/vertex-ai/generative-ai/docs/live-api
    model="gemini-2.5-flash",  # Choose a model that supports Google search tool
    # A short description of the agent's purpose.
    description="Agent to answer questions using Google Search.",
    # Instructions to set the agent's behavior.
    instruction="You are an expert researcher. You always stick to the facts.",
    # Add google_search tool to perform grounding with Google search.
    tools=[google_search],
)
