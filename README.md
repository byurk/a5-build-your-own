# AI-in-the-Loop - A5: Build Your Own

In this assignment, you'll create your own AI-powered application by choosing a domain, providing your own documents, crafting system prompts, and extending the graph with new functionality.

## What You'll Build

You will:
1. **Choose an application** - something interesting, useful, or entertaining
2. **Provide your own documents** - at least 5 documents to serve as the knowledge base
3. **Craft system prompts** - main prompt + any node-specific prompts
4. **Extend the graph** - add a new node OR tool (or both)
5. **Test and optimize** - iterate on prompts after building your extension

---

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
4. Set `SYSTEM_PROMPT_FILE=prompts/application_prompt.md`

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

---

## Assignment Activities

### Activity 1: Application Setup (docs/activity1_setup.md)

Choose your application, gather 5+ documents, and create your initial system prompt.

1. Decide on your application domain
2. Add at least 5 documents to `resources/`
3. Create your system prompt at `prompts/application_prompt.md`
4. Verify that `search_docs` works with your documents

### Activity 2: Extension (docs/activity2_extension.md)

Add a new node OR tool to extend the system's capabilities.

1. Design your extension (what problem does it solve?)
2. Implement it in `graph.py` or `tools.py`
3. Document the implementation and safety considerations
4. Do a quick verification that it works

**Important:** Complete this BEFORE Activity 3's testing.

### Activity 3: Testing & Optimization (docs/activity3_testing.md)

Test the full system and iterate on your prompts.

1. Conduct 3+ test conversations
2. Identify issues and iterate on prompts
3. Document before/after comparisons
4. Analyze tool usage patterns

### Activity 4: Demonstration (docs/activity4_demo.md)

Create a polished demonstration and reflect on your design.

1. Provide a 3-5 turn demo transcript
2. Show evidence your extension fired
3. Reflect on design decisions
4. Connect to earlier assignments

### AI Dev Log Entry (docs/ai_dev_log.md)

Add an entry documenting your work this week.

---

## Example Application Ideas

### Easier (Node-focused)

#### 1. Recipe Assistant
- **Description:** Help users find and format recipes from a personal collection
- **Extension:** `format_recipe` node that structures output (ingredients list, steps, timing)
- **Documents:** Family recipes, cuisine blogs, cookbook excerpts (copy/paste to .txt)

#### 2. Study Guide Generator
- **Description:** Create study materials from course content
- **Extension:** `generate_questions` node that produces quiz questions after retrieval
- **Documents:** Your own course notes, lecture slides (as text), textbook summaries

#### 3. Personal Writing Coach
- **Description:** Get feedback on writing based on style guides
- **Extension:** `style_check` postprocessing node that flags issues
- **Documents:** Style guides (APA, Chicago), your own past essays for examples

#### 4. Club/Organization FAQ Bot
- **Description:** Answer questions about a club, team, or student org
- **Extension:** `citation_formatter` node that standardizes source references
- **Documents:** Bylaws, meeting minutes, event policies, member handbooks

#### 5. Game Rules Reference
- **Description:** Answer questions about board game or video game rules
- **Extension:** `clarify_rule` node that identifies ambiguous rules and asks for context
- **Documents:** Rulebooks, FAQ pages, strategy guides (copy to .txt)

### Moderate (Node or Simple Tool)

#### 6. Code Documentation Helper
- **Description:** Help understand a codebase from its documentation
- **Extension:** `format_code` tool that wraps code snippets in proper markdown
- **Documents:** README files, API docs, code comments extracted to text

#### 7. Research Summary Assistant
- **Description:** Summarize and compare academic papers in a field
- **Extension:** `extract_sections` node that identifies abstract, methods, results
- **Documents:** Academic papers (PDF supported), literature review notes

#### 8. Local Resource Guide
- **Description:** Answer questions about campus or local community resources
- **Extension:** `categorize_response` node that tags answers by type (food, health, etc.)
- **Documents:** Campus guides, local business info, community resource lists

### More Challenging (Tool with Safety Considerations)

#### 9. Language Learning Helper
- **Description:** Help learn vocabulary and grammar for a specific language
- **Extension:** `conjugate_verb` tool (for a language with regular conjugation rules)
- **Documents:** Grammar guides, vocabulary lists, example sentences
- **Safety note:** Must validate input is actually a verb, handle unknown words

#### 10. Budget Tracker Assistant
- **Description:** Help with personal budgeting questions
- **Extension:** `budget_calc` tool that computes percentages, totals, savings rates
- **Documents:** Personal finance guides, budgeting templates, expense categories
- **Safety note:** Must handle currency formatting, validate numeric inputs

---

## Tool vs Node: Which Should You Choose?

> **Recommendation:** If this is your first time modifying an agentic system, **start with a node**. Add a tool only if your application genuinely requires new computation.

### Why Nodes Are Easier

**Simpler contract:**
- Nodes receive state, return state updates
- No direct LLM-generated input to validate
- Can use existing tool results

**Easier testing:**
- Can unit test with mock state
- Deterministic behavior possible
- No security surface to protect

### Why Tools Are Harder

**Safety requirements:**
- Tools execute code based on LLM output, which is unpredictable
- Must validate/sanitize ALL inputs (see `safe_eval` in tools.py - 100+ lines for math safety)
- Must handle malformed arguments gracefully
- Must never raise unhandled exceptions (return error strings instead)
- **NEVER use `eval()` or `exec()` on LLM input** - this allows arbitrary code execution
- **NEVER access files or URLs** based on raw LLM input without strict validation

**Output handling:**
- Tools must return strings (LangChain requirement)
- Complex results need serialization
- Error messages must be informative but safe

**LLM integration:**
- Tool descriptions affect how/when the LLM calls them
- Poor descriptions lead to misuse or non-use
- Testing requires observing LLM behavior

**Study `tools.py` thoroughly before attempting a new tool.**

---

## CLI Commands

```bash
# Interactive multi-turn chat
python -m ai_in_loop.cli chat

# Single prompt (for quick tests)
python -m ai_in_loop.cli demo --prompt "Your prompt here"
```

When the LLM uses tools, you'll see output like:
```
Tool call: search_docs(query="your query")
Tool result: Source: your_document.txt
Content: ...
```

Tool calls and results are also logged to `logs/runs.jsonl`.

---

## Submission

Complete all required files:

| File | Description |
|------|-------------|
| `docs/activity1_setup.md` | Application choice, documents, initial prompt |
| `docs/activity2_extension.md` | Extension implementation documentation |
| `docs/activity3_testing.md` | Testing transcripts, prompt iterations |
| `docs/activity4_demo.md` | Demonstration transcript + reflection |
| `docs/ai_dev_log.md` | Development log entry |
| `prompts/application_prompt.md` | Your custom system prompt |
| `resources/` | At least 5 documents for your application |
| `ai_in_loop/graph.py` or `tools.py` | Your extension code |

Then verify your submission:

```bash
python tests/verify_submission.py
```

If that prints `Submission Verification: OK`, you're good to submit.

**The verification script checks:**
- All required files exist with minimum content
- No placeholder tokens remain (`REPLACE_ME`, `TODO`)
- Required sections are present
- Extension exists (node or tool added)
- Resources directory has 5+ documents (no Federalist Papers)

---

## Code Review Preparation

Be prepared to answer questions about your implementation. Categories include:

### Graph Structure
- How does the graph flow from user message to response?
- What does `tools_condition` do?
- How would you add a preprocessing node?

### Tool Design & Safety
- Why does `safe_eval` use AST parsing instead of `eval()`?
- What happens if a tool receives invalid input?
- How do tool docstrings affect LLM behavior?

### System Prompts & LLM Behavior
- Where is the system prompt injected?
- When should guidance go in the prompt vs. tool docstring?

### Your Extension
- What problem does your extension solve?
- Walk through your implementation
- What inputs could break it?

### Architecture
- What does the graph abstraction provide over raw API calls?
- What are the costs of passing all messages every invocation?

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

---

## Resources Directory

The `resources/` directory starts empty. You must add your own documents:

- **Minimum 5 documents** required
- Supports `.txt` and `.pdf` formats
- Documents should be relevant to your chosen application

See `resources/README.md` for more details.
