"""Integration tests for the tool-calling graph.

Tests the full flow of the LangGraph application with tool calling,
using MockChatModel to simulate LLM behavior without API calls.

These tests are designed to be extension-tolerant: they validate that
the core framework works while allowing students to add nodes/tools.
"""

import pytest
from langchain_core.messages import HumanMessage, AIMessage, ToolMessage

from ai_in_loop.config import Config
from ai_in_loop.graph import build_app, run_once


@pytest.fixture
def mock_config():
    """Create a Config that uses MockChatModel."""
    return Config(
        use_gemini=False,
        gemini_api_key=None,
        gemini_model="gemini-2.5-flash",
        temperature=0.7,
        thinking_level=None,
        thinking_budget=0,
        system_prompt_file="prompts/empty.md",
        resources_dir="resources",
        chunk_size=1000,
        chunk_overlap=100,
    )


class TestGraphCompiles:
    """Tests that the graph builds and runs without errors."""

    def test_graph_builds_without_error(self, mock_config):
        """Test that the graph compiles successfully."""
        app = build_app(mock_config)
        assert app is not None

    def test_graph_accepts_message(self, mock_config):
        """Test that the graph can process a basic message."""
        app = build_app(mock_config)
        result = app.invoke({"messages": [HumanMessage(content="Hello")]})

        # Should have at least the input and one response
        messages = result["messages"]
        assert len(messages) >= 2
        assert isinstance(messages[0], HumanMessage)


class TestGraphWithToolCalls:
    """Tests for graph execution with tool calls."""

    def test_math_prompt_triggers_tool_call(self, mock_config):
        """Test that a math prompt triggers a tool call."""
        app = build_app(mock_config)
        result = app.invoke({"messages": [HumanMessage(content="Calculate 5 + 3")]})

        messages = result["messages"]

        # Should have at least 3 messages: human, AI with tool call, tool result, final AI
        assert len(messages) >= 3

        # Check that there's a tool message (result from python_calc)
        tool_messages = [m for m in messages if isinstance(m, ToolMessage)]
        assert len(tool_messages) > 0

        # The tool should have calculated the expression
        tool_result = tool_messages[0].content
        assert "8" in str(tool_result)

    def test_non_math_prompt_produces_response(self, mock_config):
        """Test that a non-math prompt produces a response without errors."""
        app = build_app(mock_config)
        result = app.invoke({"messages": [HumanMessage(content="Hello, how are you?")]})

        messages = result["messages"]

        # Should have at least 2 messages: human and some response
        assert len(messages) >= 2

        # Should have at least one AI message in the response
        ai_messages = [m for m in messages if isinstance(m, AIMessage)]
        assert len(ai_messages) >= 1

    def test_run_once_with_math(self, mock_config):
        """Test run_once convenience function with math prompt."""
        result = run_once("What is 10 * 5?", mock_config)

        # The result should be a string
        assert isinstance(result, str)
        # Should have some content
        assert len(result) > 0

    def test_run_once_without_tools(self, mock_config):
        """Test run_once without triggering tools."""
        result = run_once("Hello world", mock_config)

        assert isinstance(result, str)
        # With mock model, should contain [MOCK]
        assert "[MOCK]" in result

    def test_complex_math_expression(self, mock_config):
        """Test with a more complex math prompt."""
        app = build_app(mock_config)
        result = app.invoke({
            "messages": [HumanMessage(content="Calculate 25 * 4")]
        })

        messages = result["messages"]

        # Find tool result
        tool_messages = [m for m in messages if isinstance(m, ToolMessage)]
        if tool_messages:
            # Should contain 100
            assert "100" in str(tool_messages[0].content)


class TestGraphMessageFlow:
    """Tests for message flow through the graph."""

    def test_messages_are_accumulated(self, mock_config):
        """Test that messages accumulate correctly in state."""
        app = build_app(mock_config)
        result = app.invoke({
            "messages": [HumanMessage(content="Calculate 2 + 2")]
        })

        messages = result["messages"]

        # First message should be the human message
        assert isinstance(messages[0], HumanMessage)
        assert "2 + 2" in messages[0].content

    def test_system_prompt_not_in_output(self, mock_config):
        """Test that system prompt doesn't appear in output messages."""
        # Use empty prompt config (already set in mock_config)
        app = build_app(mock_config)
        result = app.invoke({
            "messages": [HumanMessage(content="Hello")]
        })

        messages = result["messages"]

        # System message should not be in the output
        # (it's prepended internally but not stored in state)
        from langchain_core.messages import SystemMessage
        system_messages = [m for m in messages if isinstance(m, SystemMessage)]
        assert len(system_messages) == 0


class TestGraphWithValidation:
    """Tests related to validation integration."""

    def test_tool_result_format(self, mock_config):
        """Test that tool results are properly formatted."""
        app = build_app(mock_config)
        result = app.invoke({
            "messages": [HumanMessage(content="Calculate sqrt(144)")]
        })

        messages = result["messages"]
        tool_messages = [m for m in messages if isinstance(m, ToolMessage)]

        if tool_messages:
            # Result should be a string
            assert isinstance(tool_messages[0].content, str)
            # Should contain "12" (sqrt of 144)
            assert "12" in tool_messages[0].content
