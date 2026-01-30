# Activity 2: Tool Implementation

In this activity, you'll extend the assistant by adding a new **tool** to `tools.py`.

**Important:** Complete this activity BEFORE testing in Activity 3. You need the tool in place to test the full system.

---

## Part 1: Tool Choice

### Tool Name

**Name:** REPLACE_ME (e.g., `calculate_bmi`, `days_until`, `convert_temperature`)

### Purpose

REPLACE_ME - What computation does this tool perform? Why might the LLM not do this reliably on its own?

---

## Part 2: Design

### Arguments

What arguments does your tool accept?

| Argument | Type | Description | Validation needed |
|----------|------|-------------|-------------------|
| REPLACE_ME | REPLACE_ME | REPLACE_ME | REPLACE_ME |

### Return Value

REPLACE_ME - What does your tool return? (Must be a string)

### When Should the LLM Call It?

REPLACE_ME - Describe the situations where the LLM should use this tool. This will inform your docstring.

### Pseudocode/Logic

```
REPLACE_ME - Write pseudocode or describe the logic in plain English
```

---

## Part 3: Implementation

### Code Location

**File modified:** `ai_in_loop/tools.py`

### Key Code Snippet

Paste your tool implementation:

```python
REPLACE_ME - Paste your @tool decorated function
```

### Integration

REPLACE_ME - Did you add your tool to the `TOOLS` list in `graph.py`? How does the LLM know when to use it (via the docstring)?

---

## Part 4: Safety Considerations

**Important:** Tools execute code based on LLM-generated input, which is unpredictable.

### Two Patterns for Input Validation

**Pattern 1: Typed parameters (use this for most tools)**

When your tool takes specific parameters (numbers, strings with known meaning), use type hints and range checks:

```python
@tool
def fathoms_to_meters(fathoms: float) -> str:
    """Convert depth in fathoms to meters.

    Args:
        fathoms: Depth in fathoms (1 fathom = 6 feet, used for water depth).

    Returns:
        The depth in meters, or an error message.
    """
    # Type validation is automatic via the type hint above.
    # LangChain will reject non-numeric inputs before this code runs.

    # But we still need to check for reasonable values:
    if fathoms < 0:
        return "Error: depth cannot be negative"
    if fathoms > 10000:
        return "Error: depth unreasonably large"

    meters = fathoms * 1.8288
    return f"{meters:.2f} meters"
```

Here's another example with a string parameter:

```python
@tool
def base6_to_base7(number: str) -> str:
    """Convert a number from base 6 to base 7.

    Args:
        number: A string of digits in base 6 (only digits 0-5 are valid).

    Returns:
        The number in base 7, or an error message.
    """
    # We use str instead of int because "345" as a string preserves the
    # digit sequence. An int would be ambiguous (is 345 base-6 or base-10?).

    # Validate the string contains only valid base-6 digits
    if not number:
        return "Error: empty input"
    if not all(c in "012345" for c in number):
        return "Error: invalid base-6 number (only digits 0-5 allowed)"
    if len(number) > 20:
        return "Error: number too large"

    # Convert base 6 -> base 10 -> base 7
    base10 = int(number, 6)
    if base10 == 0:
        return "0"

    digits = []
    while base10:
        digits.append(str(base10 % 7))
        base10 //= 7
    return "".join(reversed(digits))
```

**Pattern 2: AST parsing (only for expression evaluators)**

The `python_calc` tool uses AST parsing because it accepts arbitrary math expressions like `"2 + 2"` or `"sqrt(16) * sin(pi/2)"`. The expression could be anything, so it parses the structure and only allows safe operations. See `safe_eval` in `tools.py`.

Most student tools should use **Pattern 1**. Only use Pattern 2 if you're building something that evaluates arbitrary expressions.

### Security Checklist

Verify these for your tool:

- [ ] **Use type hints** - declare parameter types (e.g., `def my_tool(x: float)`) so LangChain validates types automatically
- [ ] **Check value ranges** - type hints don't catch unreasonable values (e.g., `if weight < 0: return "Error: ..."`)
- [ ] **Always return strings** - if something goes wrong, return an error message instead of crashing
- [ ] **Avoid `eval()` or `exec()`** - if you need to evaluate expressions, use AST parsing (see `safe_eval` in tools.py)
- [ ] **Your tool shouldn't need file or network access** - use `search_docs` for document retrieval

### Design Rationale

**Why did you choose this approach?**

REPLACE_ME - Did you use typed parameters or AST parsing? Why is that the right choice for your tool?

**Why is your validation sufficient?**

REPLACE_ME - What value ranges did you check? Why are those the right bounds for your application?

---

## Part 5: Quick Verification

Before Activity 3's thorough testing, do a quick sanity check.

### Does It Compile?

```bash
python -c "from ai_in_loop.graph import build_app; print('Graph builds OK')"
```

**Result:** REPLACE_ME (pass/fail)

### Does It Run?

Try a basic interaction that should trigger your tool.

**Test input:** REPLACE_ME

**Did tool fire?** REPLACE_ME (yes/no) - Look for "Tool call:" in the output or check `logs/runs.jsonl`

**Tool result:** REPLACE_ME

