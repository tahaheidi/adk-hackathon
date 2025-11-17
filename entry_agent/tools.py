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

def check_spec_exists(file_path: str) -> bool:
    """Checks if a spec.yaml file exists in the same directory as the given file path."""
    dir_path = os.path.dirname(file_path)
    spec_path = os.path.join(dir_path, "spec.yaml")
    return os.path.exists(spec_path)
