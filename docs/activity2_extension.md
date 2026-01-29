# Activity 2: Tool Implementation

In this activity, you'll extend the assistant by adding a new **tool** to `tools.py`.

**Important:** Complete this activity BEFORE testing in Activity 3. You need the tool in place to test the full system.

---

## Part 1: Tool Choice

### Tool Name

**Name:** REPLACE_ME (e.g., `calculate_bmi`, `days_until`, `convert_temperature`)

### Purpose

REPLACE_ME - What computation does this tool perform? Why can't the LLM do this reliably on its own?

### Difficulty Level

- [ ] Easy (minimal safety) - simple inputs, basic validation
- [ ] Medium (moderate safety) - multiple inputs, more edge cases
- [ ] Hard (significant safety) - complex parsing, many failure modes

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

**Important:** Tools execute code based on LLM-generated input, which is unpredictable. Review the `safe_eval` function in `tools.py` to see how the existing `python_calc` tool handles this safely.

### Security Checklist

Verify these for your tool:

- [ ] **Never use `eval()` or `exec()`** on LLM input
- [ ] **Always return strings** - never raise unhandled exceptions
- [ ] **Validate input types** - check that arguments are the expected type before using
- [ ] **Bound numeric inputs** - prevent memory exhaustion from extreme values
- [ ] **No file system access** based on LLM input without strict path validation
- [ ] **No network requests** based on LLM input without URL validation

### What Could Go Wrong?

REPLACE_ME - What are the potential failure modes? What inputs could break it?

### How Do You Handle Errors?

REPLACE_ME - How does your tool handle invalid inputs? Show example error returns.

### Input Validation

REPLACE_ME - What specific checks do you perform on each argument? What happens with malformed input?

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

**Did tool fire?** REPLACE_ME (yes/no) - Look for "Tool call:" in the output

**Tool result:** REPLACE_ME

---

## Checklist

Before moving to Activity 3:

- [ ] Tool is implemented in `tools.py` with `@tool` decorator
- [ ] Tool is added to `TOOLS` list in `graph.py`
- [ ] Tool has a clear docstring explaining when to use it
- [ ] All inputs are validated
- [ ] Errors return strings (not exceptions)
- [ ] Quick verification shows the LLM calls your tool appropriately
