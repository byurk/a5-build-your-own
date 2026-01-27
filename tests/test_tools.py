"""Unit tests for tool definitions and safe evaluation.

Tests the python_calc tool and underlying safe_eval function
to ensure correct behavior for valid expressions and proper
rejection of unsafe operations.
"""

import pytest

from ai_in_loop.tools import python_calc, safe_eval, SafeEvalError


class TestSafeEval:
    """Tests for the safe_eval function."""

    def test_simple_arithmetic(self):
        """Test basic arithmetic operations."""
        assert safe_eval("2 + 2") == 4
        assert safe_eval("10 - 3") == 7
        assert safe_eval("4 * 5") == 20
        assert safe_eval("15 / 3") == 5.0
        assert safe_eval("2 ** 3") == 8
        assert safe_eval("17 // 5") == 3
        assert safe_eval("17 % 5") == 2

    def test_unary_operators(self):
        """Test unary plus and minus."""
        assert safe_eval("-5") == -5
        assert safe_eval("+5") == 5
        assert safe_eval("--5") == 5

    def test_complex_expressions(self):
        """Test expressions with multiple operations."""
        assert safe_eval("2 + 3 * 4") == 14
        assert safe_eval("(2 + 3) * 4") == 20
        assert safe_eval("10 / 2 + 3") == 8.0

    def test_float_numbers(self):
        """Test floating point numbers."""
        assert safe_eval("3.14 * 2") == pytest.approx(6.28)
        assert safe_eval("1.5 + 2.5") == 4.0

    def test_math_functions(self):
        """Test built-in math functions."""
        assert safe_eval("sqrt(16)") == 4.0
        assert safe_eval("abs(-5)") == 5
        assert safe_eval("round(3.7)") == 4
        assert safe_eval("floor(3.7)") == 3
        assert safe_eval("ceil(3.2)") == 4
        assert safe_eval("min(1, 2, 3)") == 1
        assert safe_eval("max(1, 2, 3)") == 3

    def test_math_constants(self):
        """Test math constants like pi and e."""
        assert safe_eval("pi") == pytest.approx(3.14159, rel=1e-4)
        assert safe_eval("e") == pytest.approx(2.71828, rel=1e-4)
        assert safe_eval("2 * pi") == pytest.approx(6.28318, rel=1e-4)

    def test_trigonometric_functions(self):
        """Test trig functions."""
        assert safe_eval("sin(0)") == 0.0
        assert safe_eval("cos(0)") == 1.0
        # sin(pi/2) should be 1
        result = safe_eval("sin(pi / 2)")
        assert result == pytest.approx(1.0, rel=1e-10)

    def test_logarithm_functions(self):
        """Test logarithm functions."""
        assert safe_eval("log(e)") == pytest.approx(1.0)
        assert safe_eval("log10(100)") == 2.0
        assert safe_eval("log2(8)") == 3.0

    def test_combinatorics(self):
        """Test combinatorics functions."""
        assert safe_eval("factorial(5)") == 120
        assert safe_eval("comb(5, 2)") == 10
        assert safe_eval("perm(5, 2)") == 20

    def test_inverse_trig_functions(self):
        """Test inverse trigonometric functions."""
        assert safe_eval("asin(0)") == 0.0
        assert safe_eval("acos(1)") == 0.0
        assert safe_eval("atan(0)") == 0.0
        assert safe_eval("atan2(1, 1)") == pytest.approx(0.7854, rel=1e-3)

    def test_comparison_operators(self):
        """Test comparison operators."""
        assert safe_eval("5 > 3") is True
        assert safe_eval("2 < 3") is True
        assert safe_eval("5 == 5") is True
        assert safe_eval("3 != 5") is True
        assert safe_eval("5 >= 5") is True
        assert safe_eval("3 <= 5") is True

    def test_chained_comparisons(self):
        """Test chained comparisons like 2 < 3 < 5."""
        assert safe_eval("2 < 3 < 5") is True
        assert safe_eval("1 < 2 < 3 < 4") is True
        assert safe_eval("3 < 5 <= 4") is False

    def test_invalid_syntax(self):
        """Test that syntax errors are caught."""
        with pytest.raises(SafeEvalError, match="Invalid syntax"):
            safe_eval("2 +")

    def test_unknown_variable(self):
        """Test that unknown variables are rejected."""
        with pytest.raises(SafeEvalError, match="Unknown variable"):
            safe_eval("x + 1")

    def test_unknown_function(self):
        """Test that unknown functions are rejected."""
        with pytest.raises(SafeEvalError, match="Unknown function"):
            safe_eval("foo(5)")

    def test_import_blocked(self):
        """Test that import statements are blocked."""
        with pytest.raises(SafeEvalError):
            safe_eval("__import__('os')")

    def test_attribute_access_blocked(self):
        """Test that attribute access is blocked."""
        with pytest.raises(SafeEvalError):
            safe_eval("pi.__class__")

    def test_lambda_blocked(self):
        """Test that lambda expressions are blocked."""
        with pytest.raises(SafeEvalError):
            safe_eval("(lambda x: x)(5)")


class TestPythonCalcTool:
    """Tests for the python_calc tool."""

    def test_tool_has_correct_name(self):
        """Test that the tool has the expected name."""
        assert python_calc.name == "python_calc"

    def test_tool_has_description(self):
        """Test that the tool has a description."""
        assert python_calc.description
        assert "mathematical" in python_calc.description.lower()

    def test_simple_calculation(self):
        """Test basic calculation through the tool."""
        result = python_calc.invoke({"expression": "2 + 2"})
        assert result == "4"

    def test_float_result_formatting(self):
        """Test that whole-number floats are formatted as integers."""
        result = python_calc.invoke({"expression": "10 / 2"})
        assert result == "5"  # Not "5.0"

    def test_actual_float_result(self):
        """Test that non-integer floats are preserved."""
        result = python_calc.invoke({"expression": "10 / 3"})
        assert "3.333" in result

    def test_error_handling(self):
        """Test that errors are returned as strings, not raised."""
        result = python_calc.invoke({"expression": "invalid syntax here"})
        assert "Error" in result

    def test_division_by_zero(self):
        """Test division by zero handling."""
        result = python_calc.invoke({"expression": "1 / 0"})
        assert "Error" in result
        assert "zero" in result.lower()

    def test_math_function(self):
        """Test math function through the tool."""
        result = python_calc.invoke({"expression": "sqrt(144)"})
        assert result == "12"

    def test_complex_expression(self):
        """Test a more complex expression."""
        result = python_calc.invoke({"expression": "(10 + 5) * 2 - 3"})
        assert result == "27"
