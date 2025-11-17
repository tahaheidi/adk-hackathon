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

import os
import yaml

def read_spec(file_path: str) -> dict:
    """Reads a spec.yaml file and returns its content."""
    with open(file_path, 'r') as f:
        return yaml.safe_load(f)

def read_code(file_path: str) -> str:
    """Reads a code file and returns its content."""
    with open(file_path, 'r') as f:
        return f.read()