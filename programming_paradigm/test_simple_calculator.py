import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(0, 0), 0)
        self.assertEqual(self.calc.add(-5, -3), -8)

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(10, 5), 5)
        self.assertEqual(self.calc.subtract(0, 5), -5)
        self.assertEqual(self.calc.subtract(-5, -5), 0)
        self.assertEqual(self.calc.subtract(100, 50), 50)

    def test_multiplication(self):
        """Test the multiplication method."""
        # Standard multiplication cases
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-3, 4), -12)
        self.assertEqual(self.calc.multiply(-3, -4), 12)

        # Edge cases for zero multiplication
        self.assertEqual(self.calc.multiply(0, 5), 0)  # 0 * number
        self.assertEqual(self.calc.multiply(5, 0), 0)  # number * 0
        self.assertEqual(self.calc.multiply(0, 0), 0)  # 0 * 0

        # Large numbers multiplication
        self.assertEqual(self.calc.multiply(1000000, 2), 2000000)
        self.assertEqual(self.calc.multiply(-1000000, 2), -2000000)

    def test_division(self):
        """Test the division method."""
        # Typical division cases
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(10, -2), -5)
        self.assertEqual(self.calc.divide(-10, -2), 5)

        # Edge case for division by zero
        with self.assertRaises(ValueError):  # Updated to raise an exception for divide by zero
            self.calc.divide(10, 0)

        # Zero as numerator
        self.assertEqual(self.calc.divide(0, 5), 0)
        self.assertEqual(self.calc.divide(0, -5), 0)

        # Large numbers division
        self.assertEqual(self.calc.divide(1000000, 2), 500000)
        self.assertEqual(self.calc.divide(-1000000, 2), -500000)

        # Division with small divisors
        self.assertAlmostEqual(self.calc.divide(1, 1e-9), 1e9, places=5)
        self.assertAlmostEqual(self.calc.divide(-1, 1e-9), -1e9, places=5)

        # Floating-point division and precision
        self.assertAlmostEqual(self.calc.divide(1, 3), 0.33333, places=5)

if __name__ == "__main__":
    unittest.main()
