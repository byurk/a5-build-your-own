# Activity 1: Exploring Multi-turn RAG

In this activity, you'll explore the new capabilities of our research assistant through a 5+ turn research session on the Federalist Papers.

## Getting Started

1. Set the system prompt in your `.env` file:
   ```
   SYSTEM_PROMPT_FILE=prompts/empty.md
   ```
2. Start the chat interface: `python -m ai_in_loop.cli chat`

   **Note:** We use the empty system prompt to observe baseline behavior. You'll design your own prompt in Activity 2.
2. Choose a topic from the Federalist Papers to investigate:
   - Separation of powers
   - Federalism (federal vs. state authority)
   - The judiciary
   - Factions and political parties
   - The executive branch
   - Representation and republicanism

## Research Topic

**Topic chosen:** REPLACE_ME

**Why this topic interests you:** REPLACE_ME

---

## Research Session Transcript

Conduct a 5+ turn conversation investigating your chosen topic. Copy and paste your full conversation below, including any tool call information shown in the CLI output.

```
REPLACE_ME - Paste your complete multi-turn conversation here (minimum 5 turns)
```

---

## Log File Evidence

Open `logs/runs.jsonl` and find entries from your research session. Each line is one chat turn. Paste 2-3 relevant log entries showing `search_docs` usage:

```json
REPLACE_ME - Paste log entries showing search_docs tool calls and results
```

---

## Analysis

### How Conversation Built Across Turns

REPLACE_ME - How did later turns build on information from earlier turns? Did the assistant remember context from your earlier questions? Provide specific examples from your transcript.

### Tool Usage Patterns

REPLACE_ME - When did the model decide to use `search_docs`? Were there questions where it didn't search? Why do you think it made those decisions?

### Citation Quality

REPLACE_ME - How well did the assistant cite its sources? Did it quote specific passages? Did it mention document names? Were there times it should have cited but didn't?

### What Worked Well

REPLACE_ME - What aspects of the research experience were helpful or effective?

### What Was Frustrating

REPLACE_ME - What aspects were frustrating or could be improved? Did the assistant ever give wrong information, fail to find relevant content, or misunderstand your questions?
