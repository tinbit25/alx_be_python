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

    def test_subtraction(self):
        """Test the subtraction method."""
        self.assertEqual(self.calc.subtract(5, 3), 2)
        self.assertEqual(self.calc.subtract(3, 5), -2)
        self.assertEqual(self.calc.subtract(0, 0), 0)

    def test_multiply(self):
    self.assertEqual(self.calc.multiply(2, 3), 6)  # Basic multiplication
    self.assertEqual(self.calc.multiply(-2, 3), -6)  # Negative number
    self.assertEqual(self.calc.multiply(0, 5), 0)  # Multiplying by zero
    self.assertEqual(self.calc.multiply(-2, -3), 6)  # Multiplying two negative numbers


    def test_divide(self):
        """Test the divide method."""
        self.assertEqual(self.calc.divide(10, 5), 2)
        self.assertEqual(self.calc.divide(5, 2), 2.5)
        self.assertIsNone(self.calc.divide(5, 0))  # Division by zero

    def test_divide_with_non_numeric(self):
        """Test division with non-numeric input."""
        with self.assertRaises(ValueError):
            self.calc.divide("ten", 2)

if __name__ == '__main__':
    unittest.main()
