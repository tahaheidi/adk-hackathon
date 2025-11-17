"""Entry Agent definition for Project Aegis."""

import logging

from google.adk.agents import LlmAgent
from .tools import read_file

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

root_agent = LlmAgent(
    name="entry_agent",
    model="gemini-2.5-flash",
    description="Routes work to either the Spec Agent or Audit Agent.",
    instruction=(
        "You are the Entry Agent"
        """
        
        Your only job is to determine if a spec.yaml file exists. 
        If it does, ask user if they want to use the current spec file with the specs that it contains - if yes then route to the audit agent. 
        If it does no or user wants to revise specs, route to the spec agent.
        """
    ),
    tools=[read_file],
)

entry_agent = root_agent

__all__ = ["entry_agent", "root_agent"]

