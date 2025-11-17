# Copyright 2025 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

from google.adk import Agent
from google.adk.tools.long_running_tool import LongRunningFunctionTool

def propose_edit(audit_findings: str):
    """Starts a conversation with a human to propose edits based on audit findings."""
    return {
        "status": "pending",
        "message": f"I have the following audit findings: {audit_findings}. I will now generate a proposal for edits."
    }

edit_proposal_agent = Agent(
    model="gemini-2.5-pro",
    name="edit_proposal_agent",
    description="Synthesizes audit findings into fix proposals and presents them to a human for approval.",
    instruction="You are an agent that generates code change proposals based on audit findings. Start by calling the `propose_edit` tool with the audit findings.",
    tools=[
        LongRunningFunctionTool(func=propose_edit),
    ],
)
