# Activity 1: Application Setup

In this activity, you'll choose your application domain, gather your documents, and create your initial system prompt.

## Part 1: Choose Your Application

### Application Name

**Name:** REPLACE_ME

### Description

REPLACE_ME - Describe your application in 2-3 sentences. What does it do? Who is it for?

### Why This Application?

REPLACE_ME - Why did you choose this application? What makes it interesting, useful, or entertaining?

---

## Part 2: Gather Your Documents

You must provide **at least 5 documents** (`.txt` or `.pdf`) in the `resources/` directory. These will be the knowledge base for your assistant.

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

### Test Document Retrieval

Run the CLI and ask a question that should trigger a search of your documents:

```bash
python -m ai_in_loop.cli chat
```

**Question asked:** REPLACE_ME - Use specific keywords that appear in your documents

**Did search_docs fire?** REPLACE_ME (yes/no) - Look for "Tool call: search_docs" in the output or check `logs/runs.jsonl`

**Result:** REPLACE_ME - Paste the response or describe what the assistant found

