import unittest
from simple_calculator import SimpleCalculator

class TestSimpleCalculator(unittest.TestCase):
    def setUp(self):
        """Initialize the calculator instance before each test."""
        self.calculator = SimpleCalculator()

    def test_addition(self):
        """Test the add method."""
        self.assertEqual(self.calculator.add(2, 3), 5)
        self.assertEqual(self.calculator.add(-1, -1), -2)
        self.assertEqual(self.calculator.add(0, 5), 5)

    def test_subtraction(self):
        """Test the subtract method."""
        self.assertEqual(self.calculator.subtract(5, 3), 2)
        self.assertEqual(self.calculator.subtract(0, 4), -4)
        self.assertEqual(self.calculator.subtract(10, 10), 0)

    def test_multiplication(self):
        """Test the multiply method."""
        self.assertEqual(self.calculator.multiply(2, 3), 6)
        self.assertEqual(self.calculator.multiply(-1, 5), -5)
        self.assertEqual(self.calculator.multiply(0, 5), 0)

    def test_division(self):
        """Test the divide method."""
        self.assertEqual(self.calculator.divide(6, 3), 2)
        self.assertEqual(self.calculator.divide(10, 2), 5)
        with self.assertRaises(ValueError):  # Ensure division by zero raises an error
            self.calculator.divide(5, 0)

if __name__ == "__main__":
    unittest.main()
