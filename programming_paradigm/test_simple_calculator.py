import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    """Unit tests for the SimpleCalculator class."""

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_add(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)  # Basic positive numbers
        self.assertEqual(self.calc.add(-1, 1), 0)  # Negative and positive number
        self.assertEqual(self.calc.add(-2, -3), -5)  # Both numbers negative
        self.assertEqual(self.calc.add(0, 5), 5)  # Adding zero
        self.assertEqual(self.calc.add(5.5, 4.5), 10.0)  # Floating-point addition

    def test_subtract(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(10, 5), 5)  # Basic positive numbers
        self.assertEqual(self.calc.subtract(-5, -5), 0)  # Both numbers negative
        self.assertEqual(self.calc.subtract(0, 5), -5)  # Subtracting from zero
        self.assertEqual(self.calc.subtract(5, 0), 5)  # Subtracting zero
        self.assertEqual(self.calc.subtract(5.5, 4.5), 1.0)  # Floating-point subtraction

    def test_multiply(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(3, 5), 15)  # Basic positive numbers
        self.assertEqual(self.calc.multiply(-3, 5), -15)  # Negative and positive number
        self.assertEqual(self.calc.multiply(-3, -5), 15)  # Both numbers negative
        self.assertEqual(self.calc.multiply(3, 0), 0)  # Multiplying by zero
        self.assertEqual(self.calc.multiply(3.5, 2), 7.0)  # Floating-point multiplication

    def test_divide(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(10, 2), 5.0)  # Basic division
        self.assertEqual(self.calc.divide(-10, 2), -5.0)  # Negative numerator
        self.assertEqual(self.calc.divide(10, -2), -5.0)  # Negative denominator
        self.assertEqual(self.calc.divide(-10, -2), 5.0)  # Both numbers negative
        self.assertEqual(self.calc.divide(5.5, 2.2), 2.5)  # Floating-point division
        self.assertEqual(self.calc.divide(0, 5), 0.0)  # Zero numerator

        # Division by zero
        self.assertIsNone(self.calc.divide(10, 0), "Expected None for division by zero.")
        self.assertIsNone(self.calc.divide(0, 0), "Expected None for 0 divided by 0.")

    def test_edge_cases(self):
        """Test additional edge cases."""
        self.assertEqual(self.calc.add(1e10, 1e10), 2e10)  # Very large numbers
        self.assertEqual(self.calc.subtract(1e-10, 1e-10), 0)  # Very small numbers
        self.assertEqual(self.calc.multiply(1e10, 1e-10), 1.0)  # Large and small numbers
        self.assertAlmostEqual(self.calc.divide(1, 3), 0.3333333333333333)  # Division result precision

if __name__ == "__main__":
    unittest.main()
