"""Tests for document retrieval functionality."""

import pytest
import tempfile
from pathlib import Path

from ai_in_loop.config import Config
from ai_in_loop.retriever import get_retriever, reset_retriever
from ai_in_loop.tools import search_docs, set_search_config


@pytest.fixture(autouse=True)
def reset_retriever_state():
    """Reset retriever singleton before each test."""
    reset_retriever()
    yield
    reset_retriever()


@pytest.fixture
def temp_resources_dir():
    """Create a temporary directory with test documents."""
    with tempfile.TemporaryDirectory() as tmpdir:
        # Create a test document
        test_file = Path(tmpdir) / "test.txt"
        test_file.write_text(
            "Python is a programming language. "
            "It is known for its simple syntax and readability. "
            "Python supports multiple programming paradigms."
        )
        yield tmpdir


@pytest.fixture
def empty_resources_dir():
    """Create an empty temporary directory."""
    with tempfile.TemporaryDirectory() as tmpdir:
        yield tmpdir


@pytest.fixture
def config_with_docs(temp_resources_dir):
    """Create a config pointing to the temp resources directory."""
    return Config(
        use_gemini=False,
        gemini_api_key=None,
        gemini_model="gemini-2.5-flash",
        temperature=0.7,
        thinking_level=None,
        thinking_budget=0,
        system_prompt_file="prompts/empty.md",
        resources_dir=temp_resources_dir,
        chunk_size=1000,
        chunk_overlap=100,
    )


@pytest.fixture
def config_empty_dir(empty_resources_dir):
    """Create a config pointing to an empty resources directory."""
    return Config(
        use_gemini=False,
        gemini_api_key=None,
        gemini_model="gemini-2.5-flash",
        temperature=0.7,
        thinking_level=None,
        thinking_budget=0,
        system_prompt_file="prompts/empty.md",
        resources_dir=empty_resources_dir,
        chunk_size=1000,
        chunk_overlap=100,
    )


@pytest.fixture
def config_missing_dir():
    """Create a config pointing to a non-existent directory."""
    return Config(
        use_gemini=False,
        gemini_api_key=None,
        gemini_model="gemini-2.5-flash",
        temperature=0.7,
        thinking_level=None,
        thinking_budget=0,
        system_prompt_file="prompts/empty.md",
        resources_dir="/nonexistent/path/to/resources",
        chunk_size=1000,
        chunk_overlap=100,
    )


class TestGetRetriever:
    """Tests for the get_retriever function."""

    def test_loads_documents_from_directory(self, config_with_docs):
        """Test that documents are loaded from the resources directory."""
        retriever = get_retriever(config_with_docs)
        assert retriever is not None

    def test_returns_none_for_missing_directory(self, config_missing_dir):
        """Test that None is returned when resources directory doesn't exist."""
        retriever = get_retriever(config_missing_dir)
        assert retriever is None

    def test_returns_none_for_empty_directory(self, config_empty_dir):
        """Test that None is returned when resources directory is empty."""
        retriever = get_retriever(config_empty_dir)
        assert retriever is None

    def test_singleton_pattern(self, config_with_docs):
        """Test that retriever is only created once (singleton)."""
        retriever1 = get_retriever(config_with_docs)
        retriever2 = get_retriever(config_with_docs)
        assert retriever1 is retriever2

    def test_search_returns_results(self, config_with_docs):
        """Test that search returns relevant results."""
        retriever = get_retriever(config_with_docs)
        assert retriever is not None

        results = retriever.invoke("Python programming")
        assert len(results) > 0
        # Check that the content contains relevant text
        content = results[0].page_content
        assert "Python" in content or "programming" in content


class TestSearchDocsTool:
    """Tests for the search_docs tool."""

    def test_tool_has_correct_name(self):
        """Test that the tool has the expected name."""
        assert search_docs.name == "search_docs"

    def test_tool_has_description(self):
        """Test that the tool has a description."""
        assert search_docs.description
        assert "search" in search_docs.description.lower()

    def test_search_without_config_returns_error(self):
        """Test that search fails gracefully without config."""
        from ai_in_loop import tools
        original_config = tools._search_config
        tools._search_config = None
        try:
            result = search_docs.invoke({"query": "test"})
            assert "Error" in result
        finally:
            tools._search_config = original_config

    def test_search_with_documents(self, config_with_docs):
        """Test that search works with loaded documents."""
        set_search_config(config_with_docs)
        result = search_docs.invoke({"query": "Python syntax"})
        assert "No documents available" not in result
        assert "Source:" in result

    def test_search_empty_directory(self, config_empty_dir):
        """Test that search handles empty directory gracefully."""
        reset_retriever()  # Reset to force re-initialization
        set_search_config(config_empty_dir)
        result = search_docs.invoke({"query": "test"})
        assert "No documents available" in result


class TestResetRetriever:
    """Tests for the reset_retriever function."""

    def test_reset_clears_singleton(self, config_with_docs):
        """Test that reset_retriever clears the singleton state."""
        # First, get a retriever
        retriever1 = get_retriever(config_with_docs)
        assert retriever1 is not None

        # Reset
        reset_retriever()

        # Get again - should reinitialize
        retriever2 = get_retriever(config_with_docs)
        assert retriever2 is not None
        # Note: They might be equal in content but are different instances
        # after reset due to re-initialization
