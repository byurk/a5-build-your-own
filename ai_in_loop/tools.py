"""Tool definitions for the AI-in-the-Loop application.

This module defines tools that can be used by the LLM via LangGraph's
tool calling capabilities. Tools are defined using LangChain's @tool
decorator for model-agnostic compatibility.
"""

from __future__ import annotations

import ast
import math
import operator
from typing import Any, TYPE_CHECKING

from langchain_core.tools import tool

if TYPE_CHECKING:
    from .config import Config

# Module-level config reference for search_docs tool
_search_config: Config | None = None


def set_search_config(cfg: Config) -> None:
    """Set config for search_docs tool. Called at startup."""
    global _search_config
    _search_config = cfg


# Safe operators for math expressions
SAFE_OPERATORS: dict[type, Any] = {
    # Arithmetic operators
    ast.Add: operator.add,
    ast.Sub: operator.sub,
    ast.Mult: operator.mul,
    ast.Div: operator.truediv,
    ast.FloorDiv: operator.floordiv,
    ast.Mod: operator.mod,
    ast.Pow: operator.pow,
    ast.USub: operator.neg,
    ast.UAdd: operator.pos,
    # Comparison operators
    ast.Lt: operator.lt,
    ast.Gt: operator.gt,
    ast.Eq: operator.eq,
    ast.NotEq: operator.ne,
    ast.LtE: operator.le,
    ast.GtE: operator.ge,
}

# Safe math functions and constants
SAFE_FUNCTIONS: dict[str, Any] = {
    # Built-in functions
    "abs": abs,
    "round": round,
    "min": min,
    "max": max,
    "sum": sum,
    "len": len,
    # Math module functions
    "sqrt": math.sqrt,
    "sin": math.sin,
    "cos": math.cos,
    "tan": math.tan,
    "log": math.log,
    "log10": math.log10,
    "log2": math.log2,
    "exp": math.exp,
    "floor": math.floor,
    "ceil": math.ceil,
    "pow": math.pow,
    # Combinatorics
    "factorial": math.factorial,
    "comb": math.comb,
    "perm": math.perm,
    # Inverse trigonometric functions
    "asin": math.asin,
    "acos": math.acos,
    "atan": math.atan,
    "atan2": math.atan2,
    # Math constants
    "pi": math.pi,
    "e": math.e,
}


class SafeEvalError(Exception):
    """Raised when expression evaluation fails or is unsafe."""

    pass


def _safe_eval_node(node: ast.AST) -> Any:
    """Recursively evaluate an AST node using only safe operations.

    Args:
        node: An AST node to evaluate

    Returns:
        The computed value

    Raises:
        SafeEvalError: If the expression contains unsupported operations
    """
    # Numbers
    if isinstance(node, ast.Constant):
        if isinstance(node.value, (int, float)):
            return node.value
        raise SafeEvalError(f"Unsupported constant type: {type(node.value).__name__}")

    # Names (variables/constants like pi, e)
    if isinstance(node, ast.Name):
        if node.id in SAFE_FUNCTIONS:
            return SAFE_FUNCTIONS[node.id]
        raise SafeEvalError(f"Unknown variable: {node.id}")

    # Binary operations (a + b, a * b, etc.)
    if isinstance(node, ast.BinOp):
        op_type = type(node.op)
        if op_type not in SAFE_OPERATORS:
            raise SafeEvalError(f"Unsupported operator: {op_type.__name__}")
        left = _safe_eval_node(node.left)
        right = _safe_eval_node(node.right)
        return SAFE_OPERATORS[op_type](left, right)

    # Unary operations (-x, +x)
    if isinstance(node, ast.UnaryOp):
        op_type = type(node.op)
        if op_type not in SAFE_OPERATORS:
            raise SafeEvalError(f"Unsupported unary operator: {op_type.__name__}")
        operand = _safe_eval_node(node.operand)
        return SAFE_OPERATORS[op_type](operand)

    # Comparison operations (5 > 3, 2 < 3 < 5, x == y, etc.)
    if isinstance(node, ast.Compare):
        left = _safe_eval_node(node.left)
        for op, comparator in zip(node.ops, node.comparators):
            op_type = type(op)
            if op_type not in SAFE_OPERATORS:
                raise SafeEvalError(f"Unsupported comparison operator: {op_type.__name__}")
            right = _safe_eval_node(comparator)
            if not SAFE_OPERATORS[op_type](left, right):
                return False
            left = right  # For chained comparisons like 2 < 3 < 5
        return True

    # Function calls (sqrt(x), sin(x), etc.)
    if isinstance(node, ast.Call):
        if not isinstance(node.func, ast.Name):
            raise SafeEvalError("Only simple function calls are supported")
        func_name = node.func.id
        if func_name not in SAFE_FUNCTIONS:
            raise SafeEvalError(f"Unknown function: {func_name}")
        func = SAFE_FUNCTIONS[func_name]
        if not callable(func):
            raise SafeEvalError(f"{func_name} is not a function")
        args = [_safe_eval_node(arg) for arg in node.args]
        return func(*args)

    # Lists/tuples for functions like min, max, sum
    if isinstance(node, ast.List) or isinstance(node, ast.Tuple):
        return [_safe_eval_node(elt) for elt in node.elts]

    raise SafeEvalError(f"Unsupported expression type: {type(node).__name__}")


def safe_eval(expression: str) -> float | int | bool:
    """Safely evaluate a mathematical expression.

    Uses AST parsing to only allow whitelisted operators and functions.
    No arbitrary code execution is possible.

    Args:
        expression: A math expression like "2 + 2" or "sqrt(16) * 3"

    Returns:
        The computed numeric result

    Raises:
        SafeEvalError: If the expression is invalid or contains unsafe operations
    """
    try:
        tree = ast.parse(expression, mode="eval")
    except SyntaxError as e:
        raise SafeEvalError(f"Invalid syntax: {e.msg}") from e

    return _safe_eval_node(tree.body)


@tool
def python_calc(expression: str) -> str:
    """Evaluate a mathematical expression safely.

    Use this tool to perform arithmetic, comparisons, or other mathematical
    computations.

    Supports:
    - Basic operators: +, -, *, /, **, //, %
    - Comparison operators: <, >, ==, !=, <=, >=
    - Trig functions: sin, cos, tan, asin, acos, atan, atan2
    - Other math: sqrt, log, log10, log2, exp, floor, ceil, pow
    - Combinatorics: factorial, comb, perm
    - Constants: pi, e

    Args:
        expression: A math expression like "2 + 2", "sqrt(16) * 3",
                   or "sin(pi / 2)". Use 'pi' and 'e' for constants.

    Returns:
        The computed result as a string, or an error message if evaluation fails.
    """
    try:
        result = safe_eval(expression)
        # Format nicely: avoid unnecessary decimals for whole numbers
        if isinstance(result, float) and result.is_integer():
            return str(int(result))
        return str(result)
    except SafeEvalError as e:
        return f"Error: {e}"
    except ZeroDivisionError:
        return "Error: Division by zero"
    except OverflowError:
        return "Error: Result too large"
    except ValueError as e:
        return f"Error: {e}"
    except Exception as e:
        return f"Error: Unexpected error - {type(e).__name__}: {e}"


@tool
def search_docs(query: str) -> str:
    """Search documents for information relevant to the query.

    Use this tool to find information from documents in the resources/ directory.

    Args:
        query: The search query describing what information you need.

    Returns:
        Relevant document passages with source info, or a message if none found.
    """
    from .retriever import get_retriever

    if _search_config is None:
        return "Error: Search not configured."

    retriever = get_retriever(_search_config)
    if retriever is None:
        return "No documents available. The resources/ directory may be empty."

    results = retriever.invoke(query)
    if not results:
        return "No relevant documents found."

    return "\n\n---\n\n".join(
        f"Source: {doc.metadata.get('source', 'unknown')}\nContent: {doc.page_content}"
        for doc in results
    )
