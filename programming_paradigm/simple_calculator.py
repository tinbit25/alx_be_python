# simple_calculator.py

class SimpleCalculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b  # Ensure this is correct

    def divide(self, a, b):
        if b == 0:
            return None  # or raise ValueError("Cannot divide by zero.")
        return a / b  # Ensure this is correct