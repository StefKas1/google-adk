import datetime
from zoneinfo import ZoneInfo
from google.adk.agents import LlmAgent
from google.adk.models.lite_llm import LiteLlm

from dotenv import load_dotenv

# 1. Might need elevated privileges
# 2. cd into src/
# src/      <-- navigate to this directory
#     multi_tool_agent_azure_open_ai/
#         __init__.py
#         agent.py
#         .env
# 3. Run one of the following commands to
# a) launch the dev UI: adk web
# b) chat with your agent via termninal: adk run multi_tool_agent_azure_open_ai
# c) create a local FastAPI server, enabling you to test local cURL requests
# before you deploy your agent: adk api_server


def get_weather(city: str) -> dict:
    """Retrieves the current weather report for a specified city."""
    if city.lower() == "new york":
        return {
            "status": "success",
            "report": (
                "The weather in New York is sunny with a temperature of 25°C (77°F)."
            ),
        }
    else:
        return {
            "status": "error",
            "error_message": f"Weather information for '{city}' is not available.",
        }


def get_current_time(city: str) -> dict:
    """Returns the current time in a specified city."""
    if city.lower() == "new york":
        tz_identifier = "America/New_York"
    else:
        return {
            "status": "error",
            "error_message": f"Sorry, I don't have timezone information for {city}.",
        }

    tz = ZoneInfo(tz_identifier)
    now = datetime.datetime.now(tz)
    report = f"The current time in {city} is {now.strftime('%Y-%m-%d %H:%M:%S %Z%z')}"
    return {"status": "success", "report": report}


load_dotenv()
root_agent = LlmAgent(
    name="weather_time_agent",
    model=LiteLlm(model="azure/gpt-4o"),
    description="Agent to answer questions about the time and weather in a city.",
    instruction="You are a helpful agent who can answer user questions about the time and weather in a city.",
    tools=[get_weather, get_current_time],
)
