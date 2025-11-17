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

import asyncio
import os

from agent import edit_proposal_agent
from dotenv import load_dotenv
from google.adk.runners import InMemoryRunner
from google.genai import types

async def main():
    # Load environment variables from .env file
    load_dotenv()

    # Get the API key from the environment
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise ValueError("GOOGLE_API_KEY not found in environment or .env file.")

    # Initialize the runner
    runner = InMemoryRunner(agent=edit_proposal_agent)

    # Get audit findings from user
    audit_findings = input("Audit Findings: ")

    # Start the conversation
    print("Starting edit proposal...")
    response = await runner.run_async(new_message=f"Here are the audit findings: {audit_findings}")

    # This is where the human-in-the-loop logic will go
    # For now, just print the response
    for event in response:
        if event.content.parts and event.content.parts[0].text:
            print(f"{event.author}: {event.content.parts[0].text}")

if __name__ == "__main__":
    asyncio.run(main())
