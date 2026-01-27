# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Build & Test Commands

```bash
# Install dependencies (after activating venv)
pip install -r requirements.txt
pip install -e .

# Run all tests
pytest -q

# Run a single test file
pytest tests/test_tools.py -v

# Run a specific test
pytest tests/test_tools.py::TestSafeEval::test_basic_arithmetic -v

# Verify submission requirements
python tests/verify_submission.py

# Environment diagnostics
python -m ai_in_loop.doctor
```

## CLI Usage

```bash
# Interactive multi-turn chat
python -m ai_in_loop.cli chat

# Single prompt execution
python -m ai_in_loop.cli demo --prompt "Your prompt here"
```

## Architecture Overview

This is a LangGraph-based RAG (Retrieval-Augmented Generation) application with tool calling.

### Graph Structure (ai_in_loop/graph.py)

```
START → agent → [tools_condition] → tools → agent (loop) → END
```

- **agent node**: Invokes LLM with message history + optional system prompt
- **tools node**: LangGraph's `ToolNode` that executes tool calls
- **tools_condition**: Routes to tools node if LLM requested tool calls, otherwise to END

The graph uses `MessagesState` which accumulates messages across the conversation.

### Key Modules

- **graph.py**: Builds the LangGraph application. `TOOLS` list defines available tools. `build_app(cfg)` creates the compiled graph.
- **tools.py**: Tool definitions using `@tool` decorator. Contains `safe_eval()` for secure math evaluation via AST parsing.
- **retriever.py**: BM25 document retrieval from `resources/` directory. Singleton pattern with `get_retriever(cfg)`.
- **llm.py**: LLM abstraction with `MockChatModel` for testing without API calls.
- **config.py**: `Config` dataclass loaded from environment variables via `Config.from_env()`.

### Adding Extensions

**To add a node** (easier):
1. Define a function that takes `MessagesState` and returns `dict` with state updates
2. Add it with `graph.add_node("name", function)`
3. Wire edges appropriately

**To add a tool** (harder - requires safety):
1. Use `@tool` decorator from `langchain_core.tools`
2. Tool must return strings, never raise unhandled exceptions
3. Validate all inputs (see `safe_eval` as example of AST-based validation)
4. Add to `TOOLS` list in graph.py

### Testing with Mock Model

Set `USE_GEMINI=0` to use `MockChatModel` which provides deterministic responses for testing. The mock detects math requests and search requests via pattern matching.

## Assignment Structure

Students must:
1. Add 5+ documents to `resources/`
2. Create system prompt at `prompts/application_prompt.md`
3. Add a node to graph.py OR a tool to tools.py (baseline: 2 nodes, 2 tools)
4. Complete activity docs in `docs/`

The verification script checks for `graph.add_node(` count > 2 OR `@tool` decorator count > 2.
