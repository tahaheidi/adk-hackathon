from google.adk import Agent
from audit_agent import tools

audit_agent = Agent(
    model="gemini-2.5-pro",
    name="audit_agent",
    description="Audits a single file against a spec.yaml.",
    instruction="You are an agent that audits a code file against a `spec.yaml` file. You have tools to read the spec and the code file. Use them to analyze the file for breaches of the spec.",
    tools=[
        tools.read_spec,
        tools.read_code,
        tools.extract_file_path,
    ],
)
