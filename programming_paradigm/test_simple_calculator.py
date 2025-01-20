import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Set up a SimpleCalculator instance for testing."""
        self.calculator = SimpleCalculator()

    def test_addition(self):
        """Test addition functionality."""
        self.assertEqual(self.calculator.add(1, 1), 2)
        self.assertEqual(self.calculator.add(-1, -1), -2)
        self.assertEqual(self.calculator.add(0, 5), 5)
        self.assertEqual(self.calculator.add(2.5, 2.5), 5.0)

    def test_subtraction(self):
        """Test subtraction functionality."""
        self.assertEqual(self.calculator.subtract(10, 5), 5)
        self.assertEqual(self.calculator.subtract(-1, -1), 0)
        self.assertEqual(self.calculator.subtract(0, 5), -5)
        self.assertEqual(self.calculator.subtract(2.5, 0.5), 2.0)

    def test_multiplication(self):
        """Test multiplication functionality."""
        self.assertEqual(self.calculator.multiply(3, 3), 9)
        self.assertEqual(self.calculator.multiply(-1, 1), -1)
        self.assertEqual(self.calculator.multiply(0, 10), 0)
        self.assertEqual(self.calculator.multiply(2.5, 2), 5.0)

    def test_divide(self):
        """Test division functionality."""
        self.assertEqual(self.calculator.divide(10, 2), 5)
        self.assertEqual(self.calculator.divide(-10, -2), 5)
        self.assertEqual(self.calculator.divide(2.5, 0.5), 5.0)
        with self.assertRaises(ValueError):  # Ensure division by zero raises an error
            self.calculator.divide(5, 0)

if __name__ == "__main__":
    unittest.main()
