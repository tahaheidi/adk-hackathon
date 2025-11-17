from google.adk.tools.long_running_tool import LongRunningFunctionTool

def generate_spec():
    """Starts a conversation with a human to generate a spec file."""
    return {
        "status": "pending",
        "message": "I need to generate a spec file. Please provide the requirements."
    }

def save_spec(spec_content: str) -> str:
    """Saves the provided spec content to a file named spec.yaml."""
    with open("spec.yaml", "w") as f:
        f.write(spec_content)
    return "Successfully saved spec to spec.yaml"
