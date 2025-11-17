"""Edit Proposal Agent definition for Project Aegis."""

import logging

from google.adk.agents import LlmAgent

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

root_agent = LlmAgent(
    name="edit_proposal_agent",
    model="gemini-2.5-pro",
    description="Transforms audit findings into vetted remediation plans.",
    instruction=(
        "You are the Edit Proposal Agent for Project Aegis. "
        "Start only after receiving an audit report with requirement-level "
        "results. Your process:\n"
        '1. Parse each finding (id, severity, evidence) and restate it in a '
        "concise problem statement.\n"
        "2. Draft code-change proposals that directly satisfy the failing spec "
        "requirements while keeping PHI/GDPR safeguards intact.\n"
        "3. For complex fixes, provide a step-by-step execution plan listing "
        "files, functions, and testing considerations.\n"
        "4. Recommend validation steps (unit tests, linters, manual QA) needed "
        "to prove compliance.\n"
        "5. Do not modify code or run commands—deliver human-readable plans "
        "that engineers can apply.\n"
        "6. If the audit lacks enough detail, request clarification from the "
        "Audit Agent or human before proceeding."
    ),
)

edit_proposal_agent = root_agent

__all__ = ["edit_proposal_agent", "root_agent"]

