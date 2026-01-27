# Activity 3: Testing & Optimization

In this activity, you'll thoroughly test your complete system (base + extension) and iterate on your prompts to improve performance.

---

## Part 1: Initial Testing

Conduct a multi-turn conversation (3-5 turns) to test your application and extension.

### Test Conversation 1: Happy Path

A conversation where everything works as expected.

```
REPLACE_ME - Paste your complete conversation here
```

**What worked well:** REPLACE_ME

**Did the extension fire?** REPLACE_ME (yes/no) - Include evidence from the output.

### Test Conversation 2: Edge Cases

A conversation that tests boundary conditions or unusual inputs.

```
REPLACE_ME - Paste your complete conversation here
```

**Issues discovered:** REPLACE_ME

**Did the extension handle edge cases?** REPLACE_ME

### Test Conversation 3: Extension-Focused

A conversation specifically designed to exercise your extension.

```
REPLACE_ME - Paste your complete conversation here
```

**Extension behavior:** REPLACE_ME - Describe how your extension performed.

---

## Part 2: Prompt Iteration

Based on your testing, improve your prompts.

### Main Application Prompt (`prompts/application_prompt.md`)

#### Before (Version 1)

```markdown
REPLACE_ME - Paste the relevant part of your original prompt
```

#### Issues Observed

REPLACE_ME - What problems did you notice? Did the assistant cite poorly? Use the wrong tone? Call tools inappropriately?

#### After (Version 2+)

```markdown
REPLACE_ME - Paste the relevant part of your improved prompt
```

#### What Changed and Why

REPLACE_ME - Explain specific changes you made and why you expected them to help.

### Node-Specific Prompts (If Applicable)

If you added a node with its own prompt, document iterations here:

**Prompt file:** REPLACE_ME (e.g., `prompts/validator_prompt.md`)

**Changes made:** REPLACE_ME

---

## Part 3: Before/After Comparison

Show concrete improvement from your prompt iterations.

### Same Query, Different Prompts

Pick a query that showed issues with your initial prompt.

**Query:** REPLACE_ME

#### Response with Version 1 Prompt

```
REPLACE_ME
```

**Problems:** REPLACE_ME

#### Response with Final Prompt

```
REPLACE_ME
```

**Improvements:** REPLACE_ME

---

## Part 4: Tool Usage Analysis

### When Does search_docs Fire?

REPLACE_ME - Describe the patterns you observed. What types of questions trigger document search?

### When Does Your Extension Fire?

REPLACE_ME - Describe when your extension activates. Is it appropriate?

### Tool Decision Quality

REPLACE_ME - Does the assistant make good decisions about when to use tools? Any cases where it should have used a tool but didn't (or vice versa)?

---

## Part 5: Remaining Issues

### Known Limitations

REPLACE_ME - What doesn't work perfectly? What would you improve with more time?

### Potential Future Extensions

REPLACE_ME - What additional nodes or tools would enhance your application?

---

## Checklist

Before moving to Activity 4:

- [ ] At least 3 test conversations documented
- [ ] Prompts have been iterated at least once
- [ ] Before/after comparison shows improvement
- [ ] Tool usage patterns are understood
- [ ] Known limitations are documented
