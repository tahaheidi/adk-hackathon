# Rules for creating an ADK Agent
You are an expert-level AI Agent Architect and Engineer specializing in the Agent Development Kit (ADK). 

[[calls]]
match = "when the user requests to create or implement a new ADK agent or tool"
tool = "context7"
args = ["/google/adk-python", "/google/adk-docs", "/google/adk-samples"]

## Folder structure and files
1. The project uses a Python virtual environment at `env/`. All commands (`pip`, `pytest`, `adk`, etc.) must be executed from within this environment (e.g., `env/bin/adk`). Create this environment if it does not already exist.
2. You should create a new sub-folder for the new agent
3. In the Agent folder, always create a __init__.py file that contains `from .import agent`
3. The main agent file should be called agent.py
4. The main agent should always be called root_agent
5. In the Agent folder, always create a .env file that includes the following:
```
# Choose Model Backend: 0 -> ML Dev, 1 -> Vertex AI
GOOGLE_GENAI_USE_VERTEXAI=1

# Vertex AI backend config
GOOGLE_CLOUD_PROJECT='cx-demo-312101'
GOOGLE_CLOUD_LOCATION='us-central1'
```

## Tools:
- If creating a Google Search tool, always use `tools=[google_search]`. Do not create a separate function. 

## Example Agent:
- Use a structure similar to the below when creating an agent:
```
import logging
from google.adk.agents import LlmAgent
from google.adk.tools import google_search

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

root_agent = LlmAgent(
    name="root_agent",
    description="An example AI Assistant",
    model="gemini-2.5-flash",
    instruction="""Answer any question""",
    tools=[google_search],
)
```

## Model Configuration
-  Always use `gemini-2.5-pro` for complex reasoning and summarization tasks, and `gemini-2.5-flash` for simpler tasks or when speed is a priority.

## ADK components, functions and best practices 
- Always refer to the llms-full.txt file which contains a guide to all the ADK’s components, functions, and best practices.

## Testing
- Do not try to test using `adk web'. Ask the user to test once you've created the agent.
