"""Spec Agent definition for Project Aegis."""

import logging

from google.adk.agents import LlmAgent
from .tools import write_file

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

root_agent = LlmAgent(
    name="spec_agent",
    model="gemini-2.5-pro",
    description="Collects requirements and produces approved spec.yaml files.",
    instruction=(
        "You are the Spec Agent for Project Aegis. "
        "Collaborate with the human requestor to draft a compliant `spec.yaml` "
        "before any audits begin. Always:\n"
        "1. Interview the human for functional goals, technical constraints, "
        "and compliance (HIPAA/GDPR) requirements.\n"
        "2. Structure the spec as YAML with bullet requirements starting with "
        "MUST/SHOULD/MAY statements.\n"
        "3. Cover logging rules, data handling, deployment boundaries, and any "
        "tooling mandates from the product requirements.\n"
        "4. Highlight open questions and mark them for human review.\n"
        "5. Wait for explicit approval before handing the spec back to the "
        "Entry Agent.\n"
        "6. Do not invent requirements—trace every item to human input or an "
        "existing policy document."
    ),
    tools=[write_file],
)

spec_agent = root_agent

__all__ = ["spec_agent", "root_agent"]

