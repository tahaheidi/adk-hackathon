"""Custom FunctionTool implementations shared across Project Aegis agents."""

from pathlib import Path

from google.adk.tools import FunctionTool


def _read_file(file_path: str) -> str:
    """Returns the content of a UTF-8 text file."""
    try:
        return Path(file_path).read_text(encoding="utf-8")
    except Exception as exc:  # pragma: no cover - surfaced to the agent
        return f"Error reading {file_path}: {exc}"


def _write_file(file_path: str, content: str) -> str:
    """Writes UTF-8 text to disk and returns a status message."""
    try:
        Path(file_path).write_text(content, encoding="utf-8")
        return f"Successfully wrote to {file_path}"
    except Exception as exc:  # pragma: no cover - surfaced to the agent
        return f"Error writing to {file_path}: {exc}"


read_file: FunctionTool = FunctionTool(
    func=_read_file,
)

write_file: FunctionTool = FunctionTool(
    func=_write_file,
)

__all__ = ["read_file", "write_file"]
