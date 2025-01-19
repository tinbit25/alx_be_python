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

    def test_multiply(self):
        """Test the multiplication method."""
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-3, 4), -12)
        self.assertEqual(self.calc.multiply(0, 5), 0)  # Edge case: multiplying by zero
        self.assertEqual(self.calc.multiply(-3, -4), 12)  # Multiplying negatives

    def test_divide(self):
        """Test the division method."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(10, -2), -5)
        self.assertEqual(self.calc.divide(-10, -2), 5)

        # Edge case: dividing by zero
        self.assertIsNone(self.calc.divide(10, 0), "Division by zero should return None")
        
        # Edge case: very small divisor
        self.assertAlmostEqual(self.calc.divide(1, 1e-9), 1e9, places=2)

    def test_combined(self):
        """Additional tests to verify combined behaviors."""
        self.assertEqual(self.calc.add(self.calc.multiply(2, 3), self.calc.divide(10, 2)), 11)

if __name__ == "__main__":
    unittest.main()
