# AI-in-the-Loop - A4: RAG + Multi-turn Chat

This assignment introduces **Retrieval-Augmented Generation (RAG)** and **multi-turn conversation**. You'll explore how grounding an LLM in specific documents (the Federalist Papers) changes its responses, and how system prompts shape its behavior.

## Recommended Python

- **Python 3.13.x** (course standard)

## First-Time Setup

### 1) Create + activate a venv

**macOS / Linux**
```bash
python3.13 -m venv .venv
source .venv/bin/activate
```

**Windows (PowerShell)**
```powershell
py -3.13 -m venv .venv
.\.venv\Scripts\Activate.ps1
```

### 2) Install deps

```bash
python -m pip install --upgrade pip
pip install -r requirements.txt
pip install -e .
```

### 3) Configure Gemini

1. Copy `.env.example` to `.env`
2. Set `GEMINI_API_KEY=...` (from Google AI Studio)
3. Set `USE_GEMINI=1`
4. Leave `SYSTEM_PROMPT_FILE=prompts/empty.md` (Activity 1 uses the empty prompt)

Never commit `.env`.

### 4) Verify setup

```bash
pytest -q
python -m ai_in_loop.doctor
python -m ai_in_loop.cli chat
```

## Returning to Work

Activate your venv before working:

**macOS / Linux**
```bash
source .venv/bin/activate
```

**Windows (PowerShell)**
```powershell
.\.venv\Scripts\Activate.ps1
```

## What's New in A4

### Multi-turn Conversation

The `chat` command now maintains conversation history across turns. The assistant remembers what you discussed earlier in the session, enabling:
- Follow-up questions that reference previous answers
- Building a research narrative across multiple exchanges
- Clarification and refinement of earlier responses

### Document Retrieval (RAG)

The assistant has access to the **Federalist Papers** - 85 essays written by Hamilton, Madison, and Jay in 1787-1788. When you ask questions, it can search these documents using the `search_docs` tool:

```
You: What does Madison say about factions?
Tool call: search_docs(query="Madison factions")
Tool result: Source: federalist_10.txt
Content: AMONG the numerous advantages promised by a well-constructed Union...
```

This grounds the assistant's responses in specific historical documents rather than relying solely on its training data.

### System Prompts

You can customize the assistant's behavior by setting `SYSTEM_PROMPT_FILE` in your `.env` file:

```
# Use the provided example prompt
SYSTEM_PROMPT_FILE=prompts/generic_prompt.md

# Or use your custom prompt (you'll create this in Activity 2)
SYSTEM_PROMPT_FILE=prompts/my_assistant.md
```

Then run: `python -m ai_in_loop.cli chat`

## CLI Commands

```bash
# Interactive multi-turn chat
python -m ai_in_loop.cli chat

# Single prompt (for quick tests)
python -m ai_in_loop.cli demo --prompt "Your prompt here"
```

When the LLM uses tools, you'll see output like:
```
Tool call: search_docs(query="separation of powers")
Tool result: Source: federalist_47.txt
Content: ...
```

Tool calls and results are also logged to `logs/runs.jsonl`.

---

## Assignment Activities

### Activity 1: Exploring Multi-turn RAG

Conduct a 5+ turn research session on a topic from the Federalist Papers.

1. Open `docs/activity1_research.md`
2. Run `python -m ai_in_loop.cli chat`
3. Complete a research investigation on your chosen topic
4. Document how conversation builds across turns and when the model uses `search_docs`

**Key discoveries to make:**
- How multi-turn conversation enables deeper research
- When and why the model searches documents
- How well the model cites its sources

### Activity 2: Design Your System Prompt

Create a custom system prompt to improve the research experience.

1. Open `docs/activity2_prompt_design.md`
2. Review the example in `prompts/generic_prompt.md`
3. Create your own prompt at `prompts/my_assistant.md`
4. Test and compare behavior with your custom prompt

**What you'll learn:**
- How system prompts shape AI behavior
- The relationship between persona, task, and response style
- How to iterate on prompt design

### Activity 3: Prompt Specificity and Tool Decisions

Explore how telling the model about its document collection affects tool use.

1. Open `docs/activity3_tool_decisions.md`
2. Test three provided prompts (empty, generic, specific) with an out-of-scope question
3. Observe how each prompt affects searching behavior and built-in knowledge usage
4. Analyze how prompt specificity affects tool decision-making

**Key insight:**
When the model knows what's in its document collection, it makes better decisions about when searching will be useful and when to use built-in knowledge instead.

### Activity 4: Reflection

Connect A4 to earlier assignments through metacognitive reflection.

1. Open `docs/activity4_reflection.md`
2. Reflect on how multi-turn conversation changed your interaction
3. Consider how RAG compares to the model's training data
4. Synthesize what you've learned about shaping AI behavior

### AI Dev Log Entry

1. Open `docs/ai_dev_log.md`
2. Complete Entry 4 for this week

---

## Submission (A4)

Complete all required files:

| File | Description |
|------|-------------|
| `docs/activity1_research.md` | Document your multi-turn research session |
| `docs/activity2_prompt_design.md` | Document your prompt design process |
| `docs/activity3_tool_decisions.md` | Document your 3-prompt experiment |
| `docs/activity4_reflection.md` | Reflect on A4 and course arc |
| `docs/ai_dev_log.md` | Add Entry 4 reflecting on this week |
| `prompts/my_assistant.md` | Your custom system prompt |

Then verify your submission:

```bash
python tests/verify_submission.py
```

If that prints `Submission Verification: OK`, you're good to submit.

**The verification script checks:**
- All required files exist
- Minimum content lengths are met
- No placeholder tokens remain (`REPLACE_ME`, `TODO`)
- Required sections are present

---

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `USE_GEMINI` | `0` | Set to `1` to use Gemini API |
| `GEMINI_API_KEY` | - | Required when USE_GEMINI=1 |
| `GEMINI_MODEL` | `gemini-2.5-flash` | Model to use |
| `GEMINI_THINKING_BUDGET` | `0` | For Gemini 2.5: token budget (0 = disabled) |
| `GEMINI_THINKING_LEVEL` | `none` | For Gemini 3+: none, low, medium, high |
| `SYSTEM_PROMPT_FILE` | `prompts/empty.md` | Path to system prompt |
| `RESOURCES_DIR` | `resources` | Directory containing documents |
| `CHUNK_SIZE` | `1000` | Characters per document chunk |
| `CHUNK_OVERLAP` | `100` | Overlap between chunks |

## Resources Directory

The `resources/` directory contains the Federalist Papers:
- 85 essays in `.txt` format
- Written 1787-1788 by Hamilton, Madison, and Jay
- Topics include: separation of powers, federalism, the judiciary, executive power, factions, and more

### About the Federalist Papers

The Federalist Papers are a collection of 85 essays written to persuade New York voters to ratify the proposed U.S. Constitution. Alexander Hamilton conceived the project and recruited James Madison and John Jay as co-authors. Published anonymously under the pen name "Publius," these essays remain among the most important texts for understanding the original intent behind the Constitution.

Key themes include:
- **Federalist No. 10** (Madison): The dangers of factions and how a large republic can control them
- **Federalist No. 51** (Madison): Separation of powers and checks and balances ("If men were angels, no government would be necessary")
- **Federalist No. 78** (Hamilton): The role of the judiciary and judicial review
- **Federalist No. 70** (Hamilton): The case for a strong executive branch

These documents provide rich material for exploring how an AI research assistant can help you investigate primary sources.
