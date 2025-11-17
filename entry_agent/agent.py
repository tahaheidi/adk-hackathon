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
from spec_agent.agent import spec_agent
from audit_agent.agent import audit_agent
from entry_agent import tools

root_agent = Agent(
    model="gemini-2.5-flash",
    name="entry_agent",
    description="Agent that helps create audit code and create spec file used to audit code.",
    instruction="Check if user has provided a spec file in the input. If the file exists, you will delegate to the 'audit_agent'. If it does not exist, you will delegate to the 'spec_agent'.",
    tools=[
        tools.check_spec_exists,
    ],
    sub_agents=[
        spec_agent,
        audit_agent,
    ],
)
