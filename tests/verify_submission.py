from __future__ import annotations

from pathlib import Path


REQUIRED_FILES = [
    Path("docs/ai_dev_log.md"),
    Path("docs/activity1_research.md"),
    Path("docs/activity2_prompt_design.md"),
    Path("docs/activity3_tool_decisions.md"),
    Path("docs/activity4_reflection.md"),
    Path("prompts/my_assistant.md"),
    Path("prompts/generic_prompt.md"),
    Path("prompts/specific_prompt.md"),
]

PLACEHOLDER_TOKENS = [
    "REPLACE_ME",
    "TODO",
]

# Required fields for ai_dev_log.md
DEV_LOG_REQUIRED_FIELDS = [
    "**Date:**",
    "**Goal:**",
    "**Tool used:**",
    "**Changes Made:**",
    "**Result:**",
]

# Required sections for activity1_research.md
ACTIVITY1_SECTIONS = [
    "## Research Topic",
    "## Research Session Transcript",
    "## Log File Evidence",
    "## Analysis",
]

# Required sections for activity2_prompt_design.md
ACTIVITY2_SECTIONS = [
    "## Your Custom Prompt",
    "## Testing Your Prompt",
    "## Comparison",
    "## Final Prompt",
]

# Required sections for activity3_tool_decisions.md
ACTIVITY3_SECTIONS = [
    "## Experiment 1: Empty Prompt",
    "## Experiment 2: Generic Prompt",
    "## Experiment 3: Specific Prompt",
    "## Results Summary",
    "## Analysis",
    "## Key Insight",
]

# Required sections for activity4_reflection.md
ACTIVITY4_SECTIONS = [
    "## Memory: Multi-turn Conversation",
    "## Grounding: RAG and Document Retrieval",
    "## Shaping Behavior: Tools, Prompts, and Retrieval",
    "## Looking Forward",
    "## Course Arc Reflection",
]

# Required sections for my_assistant.md (student-created prompt)
MY_ASSISTANT_SECTIONS = [
    "# Persona",
    "# Task",
    "# Citations",
]

# Minimum content lengths per file
MIN_LENGTHS = {
    "docs/ai_dev_log.md": 100,
    "docs/activity1_research.md": 700,
    "docs/activity2_prompt_design.md": 700,
    "docs/activity3_tool_decisions.md": 800,
    "docs/activity4_reflection.md": 400,
    "prompts/my_assistant.md": 300,
    "prompts/generic_prompt.md": 100,
    "prompts/specific_prompt.md": 150,
}


def check_file(
    path: Path,
    min_length: int = 50,
    required_fields: list[str] | None = None,
) -> list[str]:
    """Check a file for basic requirements and optional required fields.

    Args:
        path: Path to file to check
        min_length: Minimum content length required
        required_fields: Optional list of field markers that must be present

    Returns:
        List of problems found (empty if all checks pass)
    """
    problems: list[str] = []

    if not path.exists():
        problems.append(f"Missing required file: {path}")
        return problems

    text = path.read_text(encoding="utf-8").strip()

    if len(text) < min_length:
        problems.append(f"{path} looks too short ({len(text)} chars, need {min_length}) - did you fill it in?")

    # Check for required fields if specified
    if required_fields:
        for field in required_fields:
            if field not in text:
                problems.append(f"{path} missing required section: {field}")

    # Check for placeholders
    for token in PLACEHOLDER_TOKENS:
        if token in text:
            problems.append(f"{path} still contains placeholder token '{token}'")
            break

    return problems


def main() -> int:
    problems: list[str] = []

    for f in REQUIRED_FILES:
        file_key = str(f)
        min_len = MIN_LENGTHS.get(file_key, 50)

        if f.name == "ai_dev_log.md":
            problems.extend(check_file(f, min_length=min_len, required_fields=DEV_LOG_REQUIRED_FIELDS))
        elif f.name == "activity1_research.md":
            problems.extend(check_file(f, min_length=min_len, required_fields=ACTIVITY1_SECTIONS))
        elif f.name == "activity2_prompt_design.md":
            problems.extend(check_file(f, min_length=min_len, required_fields=ACTIVITY2_SECTIONS))
        elif f.name == "activity3_tool_decisions.md":
            problems.extend(check_file(f, min_length=min_len, required_fields=ACTIVITY3_SECTIONS))
        elif f.name == "activity4_reflection.md":
            problems.extend(check_file(f, min_length=min_len, required_fields=ACTIVITY4_SECTIONS))
        elif f.name == "my_assistant.md":
            problems.extend(check_file(f, min_length=min_len, required_fields=MY_ASSISTANT_SECTIONS))
        else:
            problems.extend(check_file(f, min_length=min_len))

    if problems:
        print("Submission Verification: PROBLEMS FOUND")
        print()
        for p in problems:
            print(f"  - {p}")
        print()
        print(f"Found {len(problems)} issue(s). Please fix and try again.")
        return 1

    print("Submission Verification: OK")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
