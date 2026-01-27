# Activity 3: How Prompt Specificity Affects Tool Decisions

In this activity, you'll observe how different system prompts affect whether the model searches unnecessarily and whether it falls back to its built-in knowledge for out-of-scope questions.

**This is an exploratory experiment.** LLM behavior can vary between runs. Whatever you observe is a valid finding — your job is to document and analyze what you see.

---

## The Three Prompts

We've provided three system prompts that vary in how much context they give the model.

### 1. Empty Prompt (`prompts/empty.md`)

No instructions at all. The model has tools available but no guidance on when to use them.

### 2. Generic Prompt (`prompts/generic_prompt.md`)

Tells the model it has access to documents and can use built-in knowledge, but doesn't specify what the documents contain.

### 3. Specific Prompt (`prompts/specific_prompt.md`)

Tells the model it has access to the Federalist Papers specifically, and when to use built-in knowledge for out-of-scope questions.

---

## The Experiment

You'll test all three prompts with a question that is clearly **outside** the scope of the Federalist Papers.

### Test Question

Use this question (or choose a similar one about modern facts):

> "What is the height of the Willis Tower in Chicago?"

---

## Experiment 1: Empty Prompt

1. Set the system prompt in your `.env` file:
   ```
   SYSTEM_PROMPT_FILE=prompts/empty.md
   ```
2. Start the chat interface: `python -m ai_in_loop.cli chat`

Ask the Willis Tower question and observe what happens.

**Did the model search?** REPLACE_ME (yes/no)

**Did the model answer the question?** REPLACE_ME (yes/no — and if yes, did it use built-in knowledge or did you have to prompt it?)

**CLI output:**
```
REPLACE_ME - Paste the output
```

---

## Experiment 2: Generic Prompt

1. Set the system prompt in your `.env` file:
   ```
   SYSTEM_PROMPT_FILE=prompts/generic_prompt.md
   ```
2. Start the chat interface: `python -m ai_in_loop.cli chat`

Ask the same question and observe what happens.

**Did the model search?** REPLACE_ME (yes/no)

**Did the model answer the question?** REPLACE_ME (yes/no — and if yes, did it use built-in knowledge automatically or ask first?)

**CLI output:**
```
REPLACE_ME - Paste the output
```

---

## Experiment 3: Specific Prompt

1. Set the system prompt in your `.env` file:
   ```
   SYSTEM_PROMPT_FILE=prompts/specific_prompt.md
   ```
2. Start the chat interface: `python -m ai_in_loop.cli chat`

Ask the same question and observe what happens.

**Did the model search?** REPLACE_ME (yes/no)

**Did the model answer the question?** REPLACE_ME (yes/no — and did it indicate the answer came from built-in knowledge?)

**CLI output:**
```
REPLACE_ME - Paste the output
```

---

## Results Summary

| Prompt | Searched? | Answered? | Used built-in knowledge? |
|--------|-----------|-----------|--------------------------|
| Empty | REPLACE_ME | REPLACE_ME | REPLACE_ME |
| Generic | REPLACE_ME | REPLACE_ME | REPLACE_ME |
| Specific | REPLACE_ME | REPLACE_ME | REPLACE_ME |

---

## Analysis

### Wasted Searches

REPLACE_ME - Which prompts led to "wasted" searches (searching for something that couldn't possibly be in the Federalist Papers)? Why do you think this happened?

### Built-in Knowledge Fallback

REPLACE_ME - Which prompts successfully used built-in knowledge to answer the question? Did any require you to explicitly ask?

### The Value of Specificity

REPLACE_ME - How did telling the model what documents it has access to (the Federalist Papers) change its behavior? What are the benefits of this specificity?

---

## Key Insight

REPLACE_ME - In 2-3 sentences, summarize what you learned about how prompt specificity affects an AI's tool use decisions.

---

## Reflection

REPLACE_ME - When building AI applications with tools, what information should you include in the system prompt to help the model make good decisions about when to use its tools?
