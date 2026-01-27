# Activity 2: Extension

In this activity, you'll extend the graph by adding a new **node** OR **tool** (or both).

**Important:** Complete this activity BEFORE testing in Activity 3. You need the extension in place to test the full system.

---

## Part 1: Extension Choice

### What Are You Adding?

- [ ] New node in `graph.py`
- [ ] New tool in `tools.py`
- [ ] Both

### Extension Name

**Name:** REPLACE_ME (e.g., `format_recipe`, `validate_input`, `calculate_budget`)

### Purpose

REPLACE_ME - What problem does this extension solve? Why is it necessary for your application?

### Why This Type?

REPLACE_ME - Why did you choose a node vs. a tool (or both)? What factors influenced your decision?

---

## Part 2: Design

### Input/Output Contract

**For a node:**
- What state does it read from? REPLACE_ME
- What state does it update? REPLACE_ME
- Where does it fit in the graph flow? REPLACE_ME

**For a tool:**
- What arguments does it accept? REPLACE_ME
- What does it return? REPLACE_ME
- When should the LLM call it? REPLACE_ME

### Pseudocode/Logic

```
REPLACE_ME - Write pseudocode or describe the logic in plain English
```

### Additional Prompts Needed?

If you're adding a node, does it need its own system prompt? (e.g., `prompts/validator_prompt.md`)

REPLACE_ME - Describe any additional prompts you need to create.

---

## Part 3: Implementation

### Code Location

**File(s) modified:** REPLACE_ME (e.g., `ai_in_loop/graph.py`, `ai_in_loop/tools.py`)

### Key Code Snippet

Paste the most important part of your implementation (not the entire file):

```python
REPLACE_ME - Paste the key lines that implement your extension
```

### How It Integrates

REPLACE_ME - Explain how your extension connects to the existing graph. If a node, how does it connect via edges? If a tool, how is it added to the TOOLS list?

---

## Part 4: Safety Considerations

**Important:** Tools execute code based on LLM-generated input, which is unpredictable. Review the `safe_eval` function in `tools.py` to see how the existing `python_calc` tool handles this safely.

### Security Checklist (for tools)

If you added a tool, verify these:

- [ ] **Never use `eval()` or `exec()`** on LLM input - use AST parsing or explicit validation
- [ ] **Always return strings** - never raise unhandled exceptions
- [ ] **Validate input types** - check that arguments are the expected type before using
- [ ] **Bound numeric inputs** - prevent memory exhaustion from extreme values
- [ ] **No file system access** based on LLM input without strict path validation
- [ ] **No network requests** based on LLM input without URL validation

### What Could Go Wrong?

REPLACE_ME - What are the potential failure modes? What inputs could break it?

### How Do You Handle Errors?

REPLACE_ME - How does your extension handle invalid inputs or unexpected situations?

### For Tools: Input Validation

If you added a tool, describe your input validation:

REPLACE_ME - What checks do you perform? What happens with malformed arguments?

---

## Part 5: Testing (Quick Verification)

Before Activity 3's thorough testing, do a quick sanity check.

### Does It Compile?

```bash
python -c "from ai_in_loop.graph import build_app; print('Graph builds OK')"
```

**Result:** REPLACE_ME (pass/fail)

### Does It Run?

Try a basic interaction that should trigger your extension.

**Test input:** REPLACE_ME

**Did extension fire?** REPLACE_ME (yes/no/unsure)

**Output:** REPLACE_ME

---

## Checklist

Before moving to Activity 3:

- [ ] Extension is implemented in the appropriate file
- [ ] Code compiles without errors
- [ ] Extension has clear documentation in code (docstrings/comments)
- [ ] Safety considerations are addressed
- [ ] Quick verification shows it basically works
