# ADK Tutorial - Progressive Weather Bot (ADK Tools Version)

### Using `adk web` (Recommended for Interactive UI)

1.  **Navigate to the parent `adk-tutorial` directory** (the one containing the `step_1`, `step_2_...` folders).
2.  **Run the command:**
    ```bash
    adk web
    ```
3.  This will start a local web server and likely open a new tab in your browser.
4.  In the web UI, you'll find a dropdown menu (usually on the left). Use this dropdown to **select the agent step** you want to interact with (e.g., `step_1`, `step_2_gpt4`, `step_6`).
5.  Once selected, you can type messages in the chat interface to interact with the agent for that specific step.

### Using `adk run` (Command-Line Interaction)

The `adk run` command allows you to interact with an agent directly from your terminal. You typically specify the path to the agent file.

- **Example (running Step 1):**
  ```bash
  # Make sure you are in the main 'adk-tutorial' folder
  adk run step_1
  ```
- For detailed usage and options for `adk run`, please refer to the [Official ADK Documentation - Run Your Agent](https://google.github.io/adk-docs/get-started/quickstart/#terminal-adk-run).

### Using `adk api_server` (Exposing as API)

The `adk api_server` command starts a FastAPI server, exposing your agent via an API endpoint.

- **Example (serving Step 1):**
  ```bash
  # Make sure you are in the main 'adk-tutorial' folder
  adk api_server
  ```
- For detailed usage, API endpoint structure, and options for `adk api_server`, please consult the [Official ADK Documentation - Testing your Agents](https://google.github.io/adk-docs/get-started/testing/).

## Directory Structure

```
adk-tutorial/
├── step_1/
│   ├── __init__.py
│   ├── agent.py      # Agent definition for Step 1
│   └── .env          # API Key configuration for Step 1
├── step_2_anthropic/
│   ├── __init__.py
│   ├── agent.py      # Agent definition for Step 2 (Anthropic)
│   └── .env          # API Key configuration for Step 2 (Anthropic)
├── step_2_gpt4/
│   ├── __init__.py
│   ├── agent.py      # Agent definition for Step 2 (GPT-4)
│   └── .env          # API Key configuration for Step 2 (GPT-4)
├── step_3/
│   ├── __init__.py
│   ├── agent.py      # Agent definition for Step 3
│   └── .env          # API Key configuration for Step 3
├── step_5/
│   # ...
└── step_6/
    # ...
└── README.md         # This file
```

Each `step_X` directory is self-contained regarding its agent logic (`agent.py`) and required API keys (`.env`).

## A Note on Step 4 (Session State & Personalization)

You might notice that "Step 4: Adding Memory and Personalization with Session State" is not included in this version of the tutorial (designed for use with `adk web`, `adk api_server`, or `adk run`).

The demonstration of session state concepts in Step 4, particularly the direct manipulation of `InMemorySessionService` for illustrative purposes, is best experienced in an interactive notebook environment (like Google Colab). This allows for immediate code execution and inspection of state changes that are less direct when using the ADK's built-in server tools.

The subsequent steps in this folder-based tutorial (Step 5 onwards) build upon the concepts from Steps 1-3 and are designed to run correctly here, focusing on features like callbacks that are fully demonstrable with `adk web`/`run`.
