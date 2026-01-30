from __future__ import annotations

from pathlib import Path


REQUIRED_FILES = [
    Path("docs/ai_dev_log.md"),
    Path("docs/activity1_setup.md"),
    Path("docs/activity2_extension.md"),
    Path("docs/activity3_testing.md"),
    Path("docs/activity4_reflection.md"),
    Path("prompts/application_prompt.md"),
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

# Required sections for activity1_setup.md
ACTIVITY1_SECTIONS = [
    "## Part 1: Choose Your Application",
    "## Part 2: Gather Your Documents",
    "## Part 3: Initial System Prompt",
    "## Part 4: Verification",
]

# Required sections for activity2_extension.md
ACTIVITY2_SECTIONS = [
    "## Part 1: Tool Choice",
    "## Part 2: Design",
    "## Part 3: Implementation",
    "## Part 4: Safety Considerations",
]

# Required sections for activity3_testing.md
ACTIVITY3_SECTIONS = [
    "## Part 1: Initial Testing",
    "## Part 2: Prompt Iteration",
    "## Part 3: Before/After Comparison",
    "## Part 4: Tool Usage Analysis",
]

# Required sections for activity4_reflection.md (now reflection-focused)
ACTIVITY4_SECTIONS = [
    "## Part 1: Application Choice",
    "## Part 2: Tool Choice",
    "## Part 3: Prompt Engineering",
    "## Part 4: Key Takeaways",
]

# Required sections for application_prompt.md
APPLICATION_PROMPT_SECTIONS = [
    "# Persona",
    "# Task",
    "# Citations",
]

# Minimum content lengths per file
MIN_LENGTHS = {
    "docs/ai_dev_log.md": 100,
    "docs/activity1_setup.md": 600,
    "docs/activity2_extension.md": 700,
    "docs/activity3_testing.md": 800,
    "docs/activity4_reflection.md": 400,
    "prompts/application_prompt.md": 300,
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


def check_tool_exists() -> list[str]:
    """Check that student added a new tool to tools.py.

    Baseline has 2 tools (python_calc, search_docs).
    Student must add at least one more.

    Returns:
        List of problems found (empty if new tool exists)
    """
    import re

    problems: list[str] = []

    tools_path = Path("ai_in_loop/tools.py")

    if not tools_path.exists():
        problems.append("Missing ai_in_loop/tools.py")
        return problems

    tools_code = tools_path.read_text(encoding="utf-8")

    # Count tools: look for @tool decorator at start of line (not in comments)
    # Match lines that start with @tool (with optional whitespace)
    tool_count = len(re.findall(r"^\s*@tool\s*$", tools_code, re.MULTILINE))

    # Baseline: 2 tools (python_calc, search_docs)
    # Student must add at least one more
    if tool_count <= 2:
        problems.append(
            f"New tool required: Add a tool to tools.py (currently {tool_count}, need more than 2). "
            f"See the README for example tool ideas."
        )

    return problems


def check_resources() -> list[str]:
    """Check that resources/ has at least 5 documents (no Federalist Papers).

    Returns:
        List of problems found (empty if resources are valid)
    """
    problems: list[str] = []

    resources_dir = Path("resources")
    if not resources_dir.exists():
        problems.append("Missing resources/ directory")
        return problems

    # Find all .txt and .pdf files
    txt_files = list(resources_dir.glob("**/*.txt"))
    pdf_files = list(resources_dir.glob("**/*.pdf"))
    all_docs = txt_files + pdf_files

    if len(all_docs) < 5:
        problems.append(
            f"Need at least 5 documents in resources/. Found {len(all_docs)}. "
            f"Add .txt or .pdf files for your application."
        )

    # Check for Federalist Papers (they should be replaced)
    federalist_docs = [d for d in all_docs if "federalist" in d.name.lower()]
    if federalist_docs:
        problems.append(
            f"Found Federalist Papers in resources/: {[d.name for d in federalist_docs[:3]]}... "
            f"Replace these with your own documents."
        )

    return problems


def main() -> int:
    problems: list[str] = []

    for f in REQUIRED_FILES:
        file_key = str(f)
        min_len = MIN_LENGTHS.get(file_key, 50)

        if f.name == "ai_dev_log.md":
            problems.extend(check_file(f, min_length=min_len, required_fields=DEV_LOG_REQUIRED_FIELDS))
        elif f.name == "activity1_setup.md":
            problems.extend(check_file(f, min_length=min_len, required_fields=ACTIVITY1_SECTIONS))
        elif f.name == "activity2_extension.md":
            problems.extend(check_file(f, min_length=min_len, required_fields=ACTIVITY2_SECTIONS))
        elif f.name == "activity3_testing.md":
            problems.extend(check_file(f, min_length=min_len, required_fields=ACTIVITY3_SECTIONS))
        elif f.name == "activity4_reflection.md":
            problems.extend(check_file(f, min_length=min_len, required_fields=ACTIVITY4_SECTIONS))
        elif f.name == "application_prompt.md":
            problems.extend(check_file(f, min_length=min_len, required_fields=APPLICATION_PROMPT_SECTIONS))
        else:
            problems.extend(check_file(f, min_length=min_len))

    # Check for new tool
    problems.extend(check_tool_exists())

    # Check resources directory
    problems.extend(check_resources())

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
