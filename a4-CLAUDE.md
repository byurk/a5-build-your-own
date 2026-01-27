# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Build & Test Commands

```bash
# Install dependencies (after activating venv)
pip install -r requirements.txt
pip install -e .

# Run all tests
pytest -q

# Run a single test
pytest tests/test_tools.py::TestPythonCalcTool::test_simple_calculation -v

# Environment diagnostics
python -m ai_in_loop.doctor

# Run demo
python -m ai_in_loop.cli demo
python -m ai_in_loop.cli demo --prompt "Calculate 25 * 4"

# Interactive chat (multi-turn with conversation history)
python -m ai_in_loop.cli chat

# Use a custom system prompt
SYSTEM_PROMPT_FILE=prompts/generic_prompt.md python -m ai_in_loop.cli chat

# Verify assignment submission
python tests/verify_submission.py
```

## Environment Setup

- Requires Python 3.13.x (course standard)
- Copy `.env.example` to `.env` and set `GEMINI_API_KEY`
- Set `USE_GEMINI=1` to use Gemini API (default is mock mode)

## Architecture

LangGraph-based LLM application with **tool calling** and **document retrieval**:

### Graph Structure

```
START → agent → [tools_condition] → tools → agent (loop) → END
```

The agent node invokes the LLM with bound tools. If the LLM returns tool calls, `tools_condition` routes to the `tools` node (ToolNode), which executes the tools and returns results. The agent then processes the results and either calls more tools or generates a final response.

### Multi-turn Chat

The `chat` command maintains conversation history across turns:
- Graph is built once before the loop
- `conversation_messages` list accumulates all messages
- Full history is passed to `graph_app.invoke()` each turn

### Core Modules

- **`ai_in_loop/config.py`**: `Config` dataclass loaded from environment variables
- **`ai_in_loop/llm.py`**: LangChain-based LLM abstraction layer
  - `get_llm(cfg)` returns a `BaseChatModel` (either `MockChatModel` or `ChatGoogleGenerativeAI`)
  - `MockChatModel` supports `bind_tools()` and recognizes math/search patterns for testing
- **`ai_in_loop/graph.py`**: LangGraph `StateGraph` with tool calling loop
  - `TOOLS = [python_calc, search_docs]` - available tools
  - `run_once()` is the entry point for single prompts
- **`ai_in_loop/tools.py`**: Tool definitions using `@tool` decorator
  - `python_calc`: Safe math expression evaluator using AST parsing
  - `search_docs`: BM25 keyword search over documents in `resources/`
- **`ai_in_loop/retriever.py`**: Document retrieval with BM25
  - Singleton pattern: loads documents once at startup via `get_retriever(cfg)`
  - Loads `.txt` and `.pdf` files from `resources/` directory
  - Chunks documents using `RecursiveCharacterTextSplitter`
  - `reset_retriever()` for testing
- **`ai_in_loop/logging_utils.py`**: JSONL logging to `logs/runs.jsonl`
- **`ai_in_loop/cli.py`**: Typer CLI with `demo` and `chat` commands

### Tool Implementation Pattern

Tools are defined using LangChain's `@tool` decorator:

```python
from langchain_core.tools import tool

@tool
def search_docs(query: str) -> str:
    """Search documents for information relevant to the query."""
    retriever = get_retriever(_search_config)
    results = retriever.invoke(query)
    return "\n\n---\n\n".join(
        f"Source: {doc.metadata.get('source', 'unknown')}\nContent: {doc.page_content}"
        for doc in results
    )
```

Tools requiring config use module-level state with a setter called at startup:
```python
_search_config: Config | None = None

def set_search_config(cfg: Config) -> None:
    global _search_config
    _search_config = cfg
```

## Environment Variables

| Variable | Default | Description |
|----------|---------|-------------|
| `USE_GEMINI` | `0` | Set to `1` to use Gemini API |
| `GEMINI_API_KEY` | - | Required when USE_GEMINI=1 |
| `GEMINI_MODEL` | `gemini-2.5-flash` | Model to use |
| `GEMINI_TEMPERATURE` | `0.7` | Generation temperature |
| `GEMINI_THINKING_BUDGET` | `0` | For Gemini 2.5: token budget (0 = disabled) |
| `GEMINI_THINKING_LEVEL` | `none` | For Gemini 3+: none, low, medium, high |
| `SYSTEM_PROMPT_FILE` | `prompts/empty.md` | Path to system prompt markdown file |
| `RESOURCES_DIR` | `resources` | Directory containing documents for search |
| `CHUNK_SIZE` | `1000` | Characters per document chunk |
| `CHUNK_OVERLAP` | `100` | Overlap between chunks |

## Resources Directory

The `resources/` directory contains documents for BM25 retrieval:
- Currently populated with 85 Federalist Papers (`.txt` files)
- Supports `.txt` and `.pdf` formats
- Documents are chunked and indexed at startup

## Testing

All tests use `MockChatModel` - no API key required:

| Test File | Description |
|-----------|-------------|
| `tests/test_smoke.py` | Basic smoke tests |
| `tests/test_tools.py` | Tool unit tests (safe_eval, python_calc) |
| `tests/test_tool_graph.py` | Graph integration tests with tool calling |
| `tests/test_retriever.py` | Retrieval tests (get_retriever, search_docs, reset) |

## Imports Reference

```python
# LangGraph
from langgraph.graph import StateGraph, START, END
from langgraph.graph.message import MessagesState
from langgraph.prebuilt import ToolNode, tools_condition

# LangChain
from langchain_core.tools import tool
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage, ToolMessage

# Retrieval
from langchain_community.retrievers import BM25Retriever
from langchain_community.document_loaders import DirectoryLoader, TextLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
```
