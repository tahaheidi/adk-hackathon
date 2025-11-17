import logging
from google.adk.agents import LlmAgent
from google.adk.tools import google_search
from .tools import request_human_review

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

root_agent = LlmAgent(
    name="root_agent",
    description="An agent that can request human review for a given draft.",
    model="gemini-2.5-flash",
    instruction="""You are an AI assistant that can request human review for a given draft. When the user provides a draft and asks for human review, use the 'request_human_review' tool to get feedback.""",
    tools=[google_search, request_human_review],
)
