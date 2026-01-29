# AI-in-the-Loop - A5: Build Your Own

In this assignment, you'll create your own AI-powered application by choosing a domain, providing your own documents, crafting system prompts, and extending the graph with new functionality.

## What You'll Build

You will:
1. **Choose an application** - something interesting, useful, or entertaining
2. **Provide your own documents** - at least 5 documents to serve as the knowledge base
3. **Craft a system prompt** - define your assistant's persona and behavior
4. **Add a custom tool** - extend the assistant with a new computation it can perform
5. **Test and optimize** - iterate on prompts and tool design

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

Your extension is a **new tool** in `tools.py`. Difficulty is based on **safety complexity** - how much input validation and error handling is required.

### Easy Tools (Minimal Safety)

Simple inputs, straightforward validation, few edge cases.

#### 1. Cooking Assistant
- **Tool:** `convert_cooking_temp(fahrenheit)` - converts F to C for oven temperatures
- **Safety:** Validate numeric input, check reasonable range (100-600°F)
- **Documents:** Recipes, cooking technique guides
- **Source:** [Project Gutenberg Cookbooks](https://www.gutenberg.org/ebooks/subject/1184)

#### 2. Fitness FAQ Bot
- **Tool:** `calculate_bmi(weight_kg, height_m)` - compute BMI from metric inputs
- **Safety:** Validate positive numbers, reasonable ranges
- **Documents:** Exercise guides, health information
- **Source:** [CDC Healthy Weight](https://www.cdc.gov/healthy-weight/)

#### 3. Reading Time Estimator
- **Tool:** `reading_time(word_count)` - estimate minutes to read (assumes 200 wpm)
- **Safety:** Validate positive integer
- **Documents:** Articles, book excerpts on a topic you're interested in
- **Source:** [Project Gutenberg](https://www.gutenberg.org/) or [OpenStax Textbooks](https://openstax.org/)

#### 4. Study Helper
- **Tool:** `pomodoro_check(minutes_studied)` - returns whether it's time for a break
- **Safety:** Validate positive number
- **Documents:** Study technique guides, course notes
- **Source:** Your own course materials, [MIT OpenCourseWare](https://ocw.mit.edu/)

### Medium Tools (Moderate Safety)

More validation, multiple inputs, or more edge cases.

#### 5. Historical Events Guide
- **Tool:** `years_between(year1, year2)` - calculate years between events
- **Safety:** Validate integers, handle BC/AD (negative years), check order
- **Documents:** Historical articles, timelines, primary sources
- **Source:** [Library of Congress](https://www.loc.gov/collections/), Wikipedia articles (copy to .txt)

#### 6. Nutrition Assistant
- **Tool:** `calculate_calories(protein_g, carbs_g, fat_g)` - compute total calories
- **Safety:** Validate three numeric inputs, check non-negative
- **Documents:** Nutrition guides, dietary information
- **Source:** [USDA FoodData Central](https://fdc.nal.usda.gov/)

#### 7. Tip Calculator Bot
- **Tool:** `split_bill(total, tip_percent, num_people)` - calculate per-person amount
- **Safety:** Validate three inputs, handle zero people, round currency
- **Documents:** Personal finance guides, etiquette guides
- **Source:** [Investor.gov Financial Literacy](https://www.investor.gov/additional-resources/information/youth/teachers-classroom-resources/what-investing)

#### 8. Travel Planning Assistant
- **Tool:** `days_until(date_string)` - days from today to a future date
- **Safety:** Parse date string (handle multiple formats or require specific format), handle past dates
- **Documents:** Travel guides, destination information
- **Source:** [National Park Service](https://www.nps.gov/), [Wikivoyage](https://www.wikivoyage.org/)

### Hard Tools (Significant Safety)

Complex inputs, many failure modes, or careful parsing required. Study `safe_eval` in `tools.py` before attempting.

#### 9. Compound Interest Calculator
- **Tool:** `compound_interest(principal, rate, years, compounds_per_year)`
- **Safety:** Four numeric inputs, validate ranges (rate as decimal vs percent), handle edge cases (0 years, continuous compounding)
- **Documents:** Financial literacy guides, investment basics
- **Source:** [Investor.gov](https://www.investor.gov/)

#### 10. Unit Converter (Multi-Unit)
- **Tool:** `convert_units(value, from_unit, to_unit)` - convert between various units
- **Safety:** Validate unit strings against whitelist, handle incompatible units (can't convert kg to meters), many unit types
- **Documents:** Science guides, cooking references, technical manuals
- **Source:** [NIST Units](https://www.nist.gov/pml/owm/metric-si/si-units), [OpenStax Physics](https://openstax.org/details/books/college-physics-2e)

---

## Tool Safety Requirements

Tools execute code based on LLM-generated input, which is unpredictable. Study `safe_eval` in `tools.py` before writing your own tool.

**Input validation:**
- Validate ALL inputs - type, range, format
- Never trust that the LLM will send correct arguments
- **NEVER use `eval()` or `exec()`** - this allows arbitrary code execution
- **NEVER access files or URLs** based on raw LLM input without strict validation

**Error handling:**
- Always return strings (LangChain requirement)
- Never raise unhandled exceptions - return error messages instead
- Error messages should be helpful but not expose system details

**LLM integration:**
- Tool docstrings affect how/when the LLM calls them
- Be specific about expected input format in the docstring
- Test that the LLM actually uses your tool appropriately

**Study `tools.py` thoroughly** - the existing `python_calc` tool demonstrates safe input handling with AST parsing.

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
| `ai_in_loop/tools.py` | Your new tool |

Then verify your submission:

```bash
python tests/verify_submission.py
```

If that prints `Submission Verification: OK`, you're good to submit.

**The verification script checks:**
- All required files exist with minimum content
- No placeholder tokens remain (`REPLACE_ME`, `TODO`)
- Required sections are present
- New tool exists (more than 2 `@tool` decorators in tools.py)
- Resources directory has 5+ documents

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
