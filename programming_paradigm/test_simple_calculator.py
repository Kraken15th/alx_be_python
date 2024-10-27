import unittest
from simple_calculator import SimpleCalculator


class TestSimpleCalculator(unittest.TestCase):

    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        """Test the addition method with various inputs."""
        self.assertEqual(self.calc.add(2, 3), 5)
        self.assertEqual(self.calc.add(-1, 1), 0)
        self.assertEqual(self.calc.add(10.5, 5.2), 15.7)

    def test_subtraction(self):
        """Test the subtraction method with various inputs."""
        self.assertEqual(self.calc.subtract(5, 2), 3)
        self.assertEqual(self.calc.subtract(10, -2), 12)
        self.assertEqual(self.calc.subtract(3.1, 1.5), 1.6)

    def test_multiplication(self):
        """Test the multiplication method with various inputs."""
        self.assertEqual(self.calc.multiply(4, 3), 12)
        self.assertEqual(self.calc.multiply(-2, 5), -10)
        self.assertEqual(self.calc.multiply(2.5, 4), 10)

    def test_division(self):
        """Test the division method with various inputs."""
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-6, 3), -2)
        self.assertIsNone(self.calc.divide(7, 0))  # Test division by zero


if __name__ == "__main__":
    unittest.main()
