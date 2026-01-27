# Activity 4: Demonstration

In this activity, you'll create a polished demonstration of your application and reflect on your design decisions.

---

## Part 1: Demo Transcript

Provide a **3-5 turn conversation** that showcases your application working well. This should demonstrate:
- Your chosen application domain
- Document retrieval (`search_docs`)
- Your custom extension (node or tool)

### Full Transcript

```
REPLACE_ME - Paste your complete demonstration conversation here.

Include:
- Your messages
- Assistant responses
- Tool calls and results (as shown in the CLI)

This should be your best example of the system working as intended.
```

---

## Part 2: Extension Evidence

### Proof Your Extension Fired

Show specific evidence from the demo (or another test) that your extension was used.

**Evidence type:** REPLACE_ME (tool call shown in output / log file entry / state change visible in response)

**Specific evidence:**

```
REPLACE_ME - Paste the relevant output showing your extension in action
```

### What the Extension Contributed

REPLACE_ME - How did your extension improve the interaction? What would have been different without it?

---

## Part 3: Design Reflection

### Application Choice

**Why was this a good domain for RAG?**

REPLACE_ME - What made your document collection valuable? How does grounding in specific documents improve the assistant's responses?

**What would you choose differently?**

REPLACE_ME - If you started over, what application or documents might you choose? Why?

### Extension Choice

**Why this extension?**

REPLACE_ME - Reflect on why you chose this particular node/tool. Was it the right choice for your application?

**Node vs. Tool Decision**

REPLACE_ME - If you chose a node, would a tool have been better? If you chose a tool, was the added complexity worth it? What did you learn?

### Prompt Engineering

**What did you learn about prompt design?**

REPLACE_ME - What strategies worked? What didn't? How did specificity affect behavior?

**Main prompt vs. tool docstrings**

REPLACE_ME - How did you decide what to put in the system prompt vs. tool descriptions?

---

## Part 4: Technical Reflection

### Graph Architecture

**What does the graph abstraction give you?**

REPLACE_ME - How does LangGraph's node-and-edge model compare to making raw API calls? What are the benefits and drawbacks?

**How did you modify the graph?**

REPLACE_ME - Describe how your extension changed the graph structure (new node? new tool in TOOLS list? new edges?)

### Safety Considerations

**What safety measures did you implement?**

REPLACE_ME - How did you handle potential errors, invalid inputs, or edge cases?

**What risks remain?**

REPLACE_ME - What could still go wrong? What would you need to address for a production system?

---

## Part 5: Course Connections

### Connection to Earlier Assignments

REPLACE_ME - How does this assignment connect to what you learned in A1-A4? Reference specific concepts (prompt engineering, tool use, RAG, multi-turn conversation).

### Key Takeaways

REPLACE_ME - What are the 2-3 most important things you learned from building this application?

---

## Checklist

Before submission:

- [ ] Demo transcript shows 3-5 turn conversation
- [ ] Extension evidence is clear and specific
- [ ] All reflection questions are answered thoughtfully
- [ ] Connections to earlier assignments are made
- [ ] `verify_submission.py` passes
