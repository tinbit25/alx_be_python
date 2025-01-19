import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_add(self):
        """Test the addition method."""
        # Basic addition of positive numbers
        self.assertEqual(self.calc.add(2, 3), 5)
        # Addition with negative and positive numbers
        self.assertEqual(self.calc.add(-1, 1), 0)
        # Addition of two negative numbers
        self.assertEqual(self.calc.add(-2, -3), -5)
        # Adding zero
        self.assertEqual(self.calc.add(0, 5), 5)
        # Floating-point addition
        self.assertEqual(self.calc.add(5.5, 4.5), 10.0)

    def test_subtract(self):
        """Test the subtraction method."""
        # Basic subtraction of positive numbers
        self.assertEqual(self.calc.subtract(10, 5), 5)
        # Subtraction with negative numbers
        self.assertEqual(self.calc.subtract(-5, -5), 0)
        # Subtracting from zero
        self.assertEqual(self.calc.subtract(0, 5), -5)
        # Subtraction of zero
        self.assertEqual(self.calc.subtract(5, 0), 5)
        # Floating-point subtraction
        self.assertEqual(self.calc.subtract(5.5, 4.5), 1.0)

    def test_multiply(self):
        """Test the multiplication method."""
        # Basic multiplication of positive numbers
        self.assertEqual(self.calc.multiply(3, 5), 15)
        # Multiplication with a negative number
        self.assertEqual(self.calc.multiply(-3, 5), -15)
        # Multiplying two negative numbers
        self.assertEqual(self.calc.multiply(-3, -5), 15)
        # Multiplying by zero
        self.assertEqual(self.calc.multiply(3, 0), 0)
        # Floating-point multiplication
        self.assertEqual(self.calc.multiply(3.5, 2), 7.0)

    def test_divide(self):
        """Test the division method."""
        # Basic division
        self.assertEqual(self.calc.divide(10, 2), 5.0)
        # Negative numerator
        self.assertEqual(self.calc.divide(-10, 2), -5.0)
        # Negative denominator
        self.assertEqual(self.calc.divide(10, -2), -5.0)
        # Both negative numbers
        self.assertEqual(self.calc.divide(-10, -2), 5.0)
        # Floating-point division
        self.assertEqual(self.calc.divide(5.5, 2.2), 2.5)
        # Zero numerator
        self.assertEqual(self.calc.divide(0, 5), 0.0)

        # Division by zero
        self.assertIsNone(self.calc.divide(10, 0), "Expected None for division by zero.")
        self.assertIsNone(self.calc.divide(0, 0), "Expected None for 0 divided by 0.")

    def test_edge_cases(self):
        """Test additional edge cases."""
        # Very large numbers
        self.assertEqual(self.calc.add(1e10, 1e10), 2e10)
        self.assertEqual(self.calc.subtract(1e10, 1e10), 0)
        self.assertEqual(self.calc.multiply(1e10, 1e-10), 1.0)
        self.assertAlmostEqual(self.calc.divide(1, 3), 0.3333333333333333)  # Floating-point precision

if __name__ == "__main__":
    unittest.main()
