from google.adk import Agent
from audit_agent import tools
import textwrap

audit_agent = Agent(
    model="gemini-2.5-pro",
    name="audit_agent",
    description="Audits a single file against a spec.yaml.",
    instruction=textwrap.dedent("""You are an agent that audits a code file against a spec file. 
        You have tools to read the spec and the code file. Use them to analyze the file for breaches of the spec.
        You need to extract the file paths for both the spec and the code file from the user input.
        Please ask for the required file paths if they are not provided by the user."""),
    tools=[
        tools.read_spec,
        tools.read_code,
    ],
)
