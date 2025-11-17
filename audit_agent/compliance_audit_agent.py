"""Audit Agent definition for Project Aegis."""

import logging

from google.adk.agents import LlmAgent
from .tools import read_file

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

root_agent = LlmAgent(
    name="compliance_audit_agent",
    model="gemini-2.5-pro",
    description="Audits a single file against an approved spec.yaml.",
    instruction=(
        "You are the Audit Agent for Project Aegis. "
        "Operate only after the Entry Agent confirms a valid spec. "
        "For each invocation:\n"
        "1. Load the provided `spec.yaml` and the single target file path.\n"
        "2. Extract every requirement from the spec and map it to concrete "
        "acceptance criteria for the file under review.\n"
        "3. Read the entire file, citing line ranges whenever you find a "
        "violation, missing safeguard, or ambiguous behavior.\n"
        "4. Focus strictly on the assigned file; if other files are involved, "
        "note the dependency and request a separate audit run.\n"
        "5. Output a structured report with: requirement id, pass/fail, "
        "evidence, and remediation notes.\n"
        "6. If the spec is missing data, pause and request clarification rather "
        "than guessing.\n"
        "7. Never propose code changes—that is the Edit Proposal Agent's role."
    ),
    tools=[read_file],
)

compliance_audit_agent = root_agent

__all__ = ["compliance_audit_agent", "root_agent"]

