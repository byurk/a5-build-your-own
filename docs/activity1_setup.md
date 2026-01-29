# Activity 1: Application Setup

In this activity, you'll choose your application domain, gather your documents, and create your initial system prompt.

## Part 1: Choose Your Application

### Design Constraint

The existing graph follows a linear pattern: `agent → tools → agent → END`. If you add a node, it will run **on every turn** of the conversation. Choose an application where this makes sense.

**Good fit:** Applications where your extension improves every response (formatting, citations, disclaimers, structuring output).

**Poor fit:** Applications requiring conditional logic (e.g., "only generate quiz questions on first response") or complex state tracking.

See the README for example applications that fit this constraint.

### Application Name

**Name:** REPLACE_ME

### Description

REPLACE_ME - Describe your application in 2-3 sentences. What does it do? Who is it for?

### Why This Application?

REPLACE_ME - Why did you choose this application? What makes it interesting, useful, or entertaining?

### Extension Fit

REPLACE_ME - If you plan to add a node, explain why it makes sense to run on every turn. If you plan to add a tool, this constraint doesn't apply.

---

## Part 2: Gather Your Documents

You must provide **at least 5 documents** in the `resources/` directory. These will be the knowledge base for your assistant.

### Document List

| # | Filename | Description | Source |
|---|----------|-------------|--------|
| 1 | REPLACE_ME | REPLACE_ME | REPLACE_ME |
| 2 | REPLACE_ME | REPLACE_ME | REPLACE_ME |
| 3 | REPLACE_ME | REPLACE_ME | REPLACE_ME |
| 4 | REPLACE_ME | REPLACE_ME | REPLACE_ME |
| 5 | REPLACE_ME | REPLACE_ME | REPLACE_ME |

**Note:** Add more rows if you have more than 5 documents.

### Document Selection Rationale

REPLACE_ME - Explain why you chose these documents. How do they support your application? What topics do they cover? Are there any gaps you're aware of?

---

## Part 3: Initial System Prompt

Create your initial system prompt in `prompts/application_prompt.md`. You'll iterate on this in Activity 3.

### Prompt Design Decisions

**Persona:** REPLACE_ME - How should the assistant present itself? What tone and style?

**Task:** REPLACE_ME - What is the assistant's primary job? What should it do well?

**Tool Usage:** REPLACE_ME - When should the assistant search documents vs. use its own knowledge?

**Citations:** REPLACE_ME - How should the assistant cite sources from your documents?

**Format:** REPLACE_ME - How should responses be structured?

---

## Part 4: Verification

### Documents Load Successfully

Run the following to verify your documents are accessible:

```bash
python -m ai_in_loop.cli chat
```

Then ask: "What documents do you have access to?" or a relevant question about your content.

**Result:** REPLACE_ME - Did it work? Paste the response or describe what happened.

### search_docs Tool Works

Ask a question that requires searching your documents.

**Question asked:** REPLACE_ME

**Did search_docs fire?** REPLACE_ME (yes/no)

**Result summary:** REPLACE_ME - Brief description of what the assistant found.

---

## Checklist

Before moving to Activity 2, verify:

- [ ] Application name and description are clear
- [ ] At least 5 documents are in `resources/`
- [ ] Documents are `.txt` or `.pdf` format
- [ ] Initial prompt exists at `prompts/application_prompt.md`
- [ ] `search_docs` successfully retrieves from your documents
