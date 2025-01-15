"""
Lesson 4 - Math
This test module demonstrates Python math operations through practical examples.

Objectives:
- Define the terms operator and operand
- Evaluate math operations in Python using the seven numeric operators
- Recall the order that math operators are evaluated in Python
- Predict the result type of operations involving integer and float type operands
"""

import pytest

class TestLesson4Math:
    def test_basic_arithmetic(self):
        # Addition
        assert 5 + 3 == 8
        assert 5.0 + 3 == 8.0  # Note the float result
        
        # Subtraction
        assert 10 - 4 == 6
        
        # Multiplication
        assert 3 * 4 == 12
        
        # Division (always returns float)
        assert 8 / 2 == 4.0
        
    def test_advanced_operators(self):
        # Integer division
        assert 7 // 2 == 3
        
        # Modulus (remainder)
        assert 7 % 3 == 1
        
        # Exponentiation
        assert 2 ** 3 == 8
        
    def test_operator_precedence(self):
        # PEMDAS demonstration
        result = 2 + 3 * 4
        assert result == 14  # multiplication happens before addition
        
        result = (2 + 3) * 4
        assert result == 20  # parentheses override normal precedence