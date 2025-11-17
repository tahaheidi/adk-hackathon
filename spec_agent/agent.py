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
from .tools import generate_spec, save_spec

spec_agent = Agent(
    model="gemini-2.5-pro",
    name="spec_agent",
    description="Generates specification documents by talking to a human.",
    instruction="""
    You are an agent that helps generate specs in order to audit code files. You should ask user for feedback and then reiterate until the user is satisfied with the spec. Once the user is satisfied, you should save the spec file and return it.
    Here's an example of a spec.yaml file:
    ```yaml
    spec:
      - MUST NOT log any PHI (patient names, SSNs, medical records)
      - MUST allocate gpt-3.5-turbo to users with tier='free'
      - SHOULD validate all user inputs before processing
    ```
    """,
    tools=[
        LongRunningFunctionTool(func=generate_spec),
        save_spec,
    ],
)
