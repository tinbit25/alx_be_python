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
        # Typical cases
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-3, 4), -12)
        self.assertEqual(self.calc.multiply(-3, -4), 12)
        
        # Edge cases
        self.assertEqual(self.calc.multiply(0, 5), 0)  # Multiplying by zero
        self.assertEqual(self.calc.multiply(5, 0), 0)  # Multiplying with zero reversed
        self.assertEqual(self.calc.multiply(0, 0), 0)  # Zero * Zero
        
        # Large number cases
        self.assertEqual(self.calc.multiply(1_000_000, 2), 2_000_000)
        self.assertEqual(self.calc.multiply(-1_000_000, 2), -2_000_000)
        
        # Floating-point multiplication
        self.assertEqual(self.calc.multiply(0.1, 0.2), 0.02)

    def test_divide(self):
        """Test the division method."""
        # Typical cases
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-10, 2), -5)
        self.assertEqual(self.calc.divide(10, -2), -5)
        self.assertEqual(self.calc.divide(-10, -2), 5)
        
        # Edge case: division by zero
        self.assertIsNone(self.calc.divide(10, 0), "Division by zero should return None")
        
        # Edge case: zero numerator
        self.assertEqual(self.calc.divide(0, 5), 0)
        self.assertEqual(self.calc.divide(0, -5), 0)
        
        # Large number cases
        self.assertEqual(self.calc.divide(1_000_000, 2), 500_000)
        self.assertEqual(self.calc.divide(-1_000_000, 2), -500_000)
        
        # Small divisor cases
        self.assertAlmostEqual(self.calc.divide(1, 1e-9), 1e9, places=5)
        self.assertAlmostEqual(self.calc.divide(-1, 1e-9), -1e9, places=5)

        # Floating-point division
        self.assertAlmostEqual(self.calc.divide(1, 3), 0.33333, places=5)  # Precision test for floating point

if __name__ == "__main__":
    unittest.main()
