# simple_calculator.py

class SimpleCalculator:
    def add(self, a, b):
        """Return the sum of a and b."""
        return a + b

    def subtract(self, a, b):
        """Return the difference of a and b."""
        return a - b

    def multiply(self, a, b):
        """Return the product of a and b."""
        return a * b

    def divide(self, a, b):
        """Return the quotient of a and b. 
        Returns None if dividing by zero."""
        if b == 0:
            return None  # or raise ValueError("Cannot divide by zero.")
        return a / b