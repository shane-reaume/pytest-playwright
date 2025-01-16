from conftest import describe, it, page

@describe("Exercise 1a")
class TestExercise1a:
    @it("Should validate basic comparison operators")
    def test_comparison_operators(self, page):
        """Tests basic comparison operators in Python"""
        # Equal and not equal
        assert 10 != 5, "Not equal operator failed"
        assert 10 == 10, "Equal operator failed"
        
        # Greater than and greater than or equal
        assert 10 > 5, "Greater than operator failed"
        assert 10 >= 10, "Greater than or equal operator failed"
        
        # Less than and less than or equal
        assert 10 < 20, "Less than operator failed"
        assert 10 <= 10, "Less than or equal operator failed"

    @it("Should validate boolean operators")
    def test_boolean_operators(self, page):
        """Tests boolean operators and complex expressions"""
        # Basic boolean operations
        assert True and True, "AND operator with True values failed"
        assert True or False, "OR operator with mixed values failed"
        assert not False, "NOT operator failed"
        
        # Complex boolean expressions
        assert (True and False) == False, "Complex AND expression failed"
        assert (5 > 3) and (10 < 20), "Comparison with AND failed"
        assert (5 > 3) or (10 < 5), "Comparison with OR failed"
        assert not (5 == 5) == False, "Complex NOT expression failed"
        
        # Multiple conditions
        assert (5 > 3) and (10 < 20) and (10 == 10), "Multiple AND conditions failed"
        
        # Common mistakes and corrections
        # WRONG: assert 5 < 1 or 2  # This would be a syntax error
        # Correct:
        assert ((5 < 1) or (5 < 2)) == False, "Proper boolean comparison failed"

    @it("Should validate basic data types")
    def test_types(self, page):
        """
        The goal of this Challenge is to verify Python's basic data types
        """
        # None type
        assert type(None) is None.__class__

        # Boolean types
        assert type(True) is bool
        assert type(False) is bool

        # Numeric types
        assert type(1) is int
        assert type(1.0) is float
                
        # String types (all variations are str type)
        assert type("Hello") is str
        assert type('Hello') is str
        assert type("""Hello""") is str
        assert type('''Hello''') is str

        # isinstance is a built-in function that checks if an object is an instance of a class
        assert isinstance(None, type(None))
        assert isinstance(True, bool)
        assert isinstance(1, int)
        assert isinstance(1.0, float)
        assert isinstance("Hello", str)

@describe("Exercise 1b")
class TestExercise1b:
    @it("Should validate basic arithmetic operators")
    def test_basic_arithmetic(self):
        # Addition
        assert 5 + 3 == 8
        assert 5.0 + 3 == 8.0  # Note the float result
        assert -10 + 10 == 0 # note the negative first operand
        
        # Subtraction
        assert 10 - 4 == 6
        assert 10 - 3.4 == 6.6
        assert 5 - 8 == -3
        
        # Multiplication
        assert 3 * 4 == 12
        
        # Division (always returns float)
        assert 8 / 2 == 4.0
        assert 10 / 5 == 2.0

    @it("Should validate advanced operators")
    def test_advanced_operators(self):
        # Integer division
        assert 7 // 2 == 3
        
        # Modulus (remainder)
        assert 7 % 3 == 1
        
        # Exponentiation
        assert 2 ** 3 == 8

    @it("Should validate operator precedence")
    def test_operator_precedence(self):
        # PEMDAS demonstration
        result = 2 + 3 * 4
        assert result == 14  # multiplication happens before addition
        
        result = (2 + 3) * 4
        assert result == 20  # parentheses override normal precedence