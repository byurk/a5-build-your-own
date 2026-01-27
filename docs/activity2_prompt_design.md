# Activity 2: Design Your System Prompt

In this activity, you'll design your own system prompt to improve the research assistant experience.

## The Example Prompt

Review the provided example prompt in `prompts/generic_prompt.md`. It demonstrates:
- A **Persona** section defining who the assistant is
- A **Task** section describing what it should do
- A **Tool Usage** section guiding when to search
- A **Citations** section for source attribution
- A **Format** section for response style

---

## Your Custom Prompt

Create your own system prompt at `prompts/my_assistant.md`. Your prompt should:

1. Define a **unique persona** (not just "helpful research assistant")
2. Define a **specific task** tailored to your interests or research style
3. Keep or modify the **Tool Usage**, **Citations**, and **Format** sections

### Persona Design

**What persona did you choose?** REPLACE_ME

**Why did you choose this persona?** REPLACE_ME

### Task Design

**What specific task did you define?** REPLACE_ME

**How does this differ from the example prompt?** REPLACE_ME

---

## Testing Your Prompt

Test your custom prompt by returning to your Activity 1 topic, but explore a different angle you didn't fully investigate before. For example:
- If you researched "factions," ask about Madison's proposed solutions
- If you explored "separation of powers," focus on how the branches check each other
- If you studied "the judiciary," ask about lifetime appointments

1. Set the system prompt in your `.env` file:
   ```
   SYSTEM_PROMPT_FILE=prompts/my_assistant.md
   ```
2. Start the chat interface: `python -m ai_in_loop.cli chat`

### Test Conversation

Paste a conversation (3+ turns) using your custom prompt:

```
REPLACE_ME - Paste conversation using your custom prompt
```

---

## Comparison

### Behavior Differences

REPLACE_ME - How did the assistant's behavior change with your prompt compared to Activity 1 (which used the default empty prompt)? Be specific about differences you observed.

### Citation Changes

REPLACE_ME - Did your prompt improve or change how the assistant cites sources? Provide examples.

### Tool Usage Changes

REPLACE_ME - Did your prompt affect when or how the assistant uses the search tool?

### Unexpected Results

REPLACE_ME - Did anything happen that you didn't expect? Did your prompt have effects you didn't intend?

---

## Prompt Refinement

After testing, did you make any changes to your prompt? If so, describe what you changed and why:

REPLACE_ME - Describe any iterations you made to your prompt (or write "No changes made" if you kept your original)

---

## Final Prompt

Paste the final version of your `prompts/my_assistant.md` here:

```markdown
REPLACE_ME - Paste the complete contents of your my_assistant.md file
```
