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

Add a new tool to extend the system's capabilities.

1. Design your extension (what problem does it solve?)
2. Implement it in `graph.py` and `tools.py`
3. Document the implementation and safety considerations
4. Do a quick verification that it works

**Important:** Complete this BEFORE Activity 3's testing.

### Activity 3: Testing & Optimization (docs/activity3_testing.md)

Test the full system and iterate on your prompts.

1. Conduct 3+ test conversations
2. Identify issues and iterate on prompts
3. Document before/after comparisons
4. Analyze tool usage patterns

### Activity 4: Reflection (docs/activity4_reflection.md)

Reflect on your design decisions and what you learned.

1. Why was your application a good fit for RAG?
2. Why did you choose this tool?
3. What did you learn about prompt design?
4. Key takeaways

### AI Dev Log Entry (docs/ai_dev_log.md)

Add an entry documenting your work this week.

---

## Example Application Ideas

Your extension is a **new tool** in `tools.py`. Choose a tool that:

1. **Naturally complements your documents**—the tool should use information that appears in the documents
2. **Adds value over the LLM alone**—the calculation should be something LLMs get wrong

**Good fit:** User reads about the Declaration of Independence → RAG returns historical article with the date July 4, 1776 → User asks "What day of the week was that?" → Tool calculates Thursday using Zeller's formula.

**Poor fit:** User reads classic novels → RAG returns literary content → Tool calculates reading time from word count. Reading time is book-related, but users asking about literature in a way that is supported by the RAG system want to understand themes, characters, and meaning—not how long it takes to read.

**Why tools beat LLMs for certain tasks:**
- **Date arithmetic** - Leap years, month lengths, day-of-week calculations are error-prone
- **Complex parsing** - Roman numerals with subtractive notation (IV, IX, XL)
- **Lookup + calculation** - Inflation adjustment requires CPI tables
- **Fractional exponents** - Growth rate formulas like (final/initial)^(1/years) often go wrong

### 1. Historical Events Guide
- **Tool:** `day_of_week(year, month, day)` - returns the weekday for any historical date
- **Why non-trivial?** Zeller's formula is non-trivial; LLMs frequently get day-of-week wrong for historical dates.
- **Example flow:** User reads about the Declaration of Independence (July 4, 1776), asks "What day of the week was that?"
- **Documents:** Historical articles, timelines, primary sources
- **Source:** [Library of Congress](https://www.loc.gov/collections/), Wikipedia articles (copy to .txt)

### 2. Biography Helper
- **Tool:** `age_at_event(birth_year, birth_month, birth_day, event_year, event_month, event_day)` - exact age in years
- **Why non-trivial?** Date arithmetic with leap years and month boundaries. LLMs are often off by a year.
- **Example flow:** User reads Lincoln's biography (born Feb 12, 1809), asks "How old was he at inauguration (March 4, 1861)?"
- **Documents:** Biographies, historical timelines
- **Source:** [Library of Congress](https://www.loc.gov/collections/), Wikipedia biographies (copy to .txt)

### 3. Classical History Guide
- **Tool:** `roman_to_arabic(numeral)` - convert Roman numerals to integers
- **Why non-trivial?** Subtractive notation (IV=4, IX=9, XL=40, CM=900) requires parsing logic, not just symbol lookup.
- **Example flow:** User reads about Roman history, doc mentions "MDCCLXXVI", user asks "What year is that?"
- **Documents:** Classical history texts, architectural guides, museum references
- **Source:** [Library of Congress](https://www.loc.gov/collections/), Wikipedia articles on Roman history (copy to .txt)

### 4. Historical Economics Guide
- **Tool:** `adjust_for_inflation(amount, from_year, to_year)` - convert historical prices to modern dollars
- **Why non-trivial?** Requires CPI lookup table plus calculation. LLMs give vague estimates; this gives accurate values.
- **Example flow:** User reads "Model T cost $825 in 1908" and asks "What would that be today?" Tool calculates ~$27,000.
- **Documents:** Historical texts, biographies, old newspapers, economic history
- **Source:** [Project Gutenberg](https://www.gutenberg.org/) historical texts, [FRASER Economic History](https://fraser.stlouisfed.org/)

### 5. Historical Data Analysis
- **Tool:** `growth_rate(initial_value, final_value, years)` - calculates average annual growth rate (CAGR)
- **Why non-trivial?** Formula: rate = (final/initial)^(1/years) - 1. The fractional exponent trips up LLMs.
- **Example flow:** User reads "US population was 5.3 million in 1800 and 76 million in 1900" and asks "What was the annual growth rate?" Tool calculates ~2.7% per year.
- **Documents:** Economic history, demographic texts, business histories, development reports
- **Source:** [FRASER Economic History](https://fraser.stlouisfed.org/), [Our World in Data](https://ourworldindata.org/), historical statistics

---

## Tool Safety Requirements

Tools execute code based on LLM-generated input, which is unpredictable.

**Most tools (typed parameters):**
- Use type hints (e.g., `def my_tool(x: float)`) - LangChain validates types automatically
- Add range checks for unreasonable values (e.g., negative weights, dates in year 9999)
- If something goes wrong, return an error message string instead of crashing

**Expression evaluators only:**
- If your tool accepts arbitrary expressions (like a calculator), use AST parsing
- **Avoid `eval()` or `exec()`** - see `safe_eval` in tools.py for the safe pattern
- Most student tools won't need this - use typed parameters instead

**General safety:**
- Your tool shouldn't need file or network access - use `search_docs` for document retrieval
- Error messages should be helpful but not expose system details

**LLM integration:**
- Tool docstrings affect how/when the LLM calls them
- Be specific about expected input format in the docstring
- Test that the LLM actually uses your tool appropriately

See `docs/activity2_extension.md` for detailed examples of both patterns.

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
| `docs/activity4_reflection.md` | Design reflection |
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

See [docs/code_review_rubric.md](docs/code_review_rubric.md) for grading criteria.

### Presentation (3-5 slides + live demo)

You will begin your code review with a short presentation covering:
- What your application does and who it's for
- Your document collection (what topics, why these sources)
- Your custom tool (what it does, why it's needed)

Then give a live demonstration showing document retrieval and your tool in action.

### Questions

After your presentation, the instructor will select from these questions. Be prepared to show specific parts of your code when answering.

#### Your Application
1. Why did you choose this domain? What makes it a good fit for RAG?
2. What gaps exist in your document collection? What would you add?
3. What would a response look like without document retrieval?

#### Your Tool
4. What problem does your tool solve? Why might the LLM not handle this reliably on its own?
5. Walk through the key lines of your implementation
6. Did you use typed parameters or AST parsing? Why was that the right choice?
7. What value ranges do you check? Why are those the right bounds?
8. Demonstrate your error handling by calling your tool directly with a bad value (see tip below)
9. How did you test your tool? What did you discover?

#### Prompt Engineering
10. How did you decide what to put in the system prompt vs. tool docstrings?
11. What changes did you make to your prompts after testing? Why?
12. How does your system prompt affect when the LLM calls your tool?
13. Show an example where prompt changes improved behavior

#### Safety & Architecture
14. Why does `safe_eval` use AST parsing instead of `eval()`?
15. Why is it better for tools to return error strings instead of raising exceptions?
16. What does `tools_condition` do in the graph?
17. How is conversation history maintained across turns?
18. What are the costs of passing all messages every invocation?

**Tip for question 8:** You can call your tool directly to test error handling:
```bash
python -c "from ai_in_loop.tools import your_tool; print(your_tool.invoke({'param': bad_value}))"
```

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
