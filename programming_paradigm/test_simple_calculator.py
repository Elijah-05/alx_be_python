import unittest
from simple_calculator import SimpleCalculator

class Test_Simple_Calculator(unittest.TestCase):
    def setUp(self):
        """Set up the SimpleCalculator instance before each test."""
        self.calc = SimpleCalculator()

    def test_addition(self):
        self.assertEqual(self.calc.add(5, 3), 8)
        self.assertEqual(self.calc.add(-1, 4), 3)
    
    def test_subtraction(self):
        self.assertEqual(self.calc.subtract(4,3), 1)
        self.assertEqual(self.calc.subtract(2, 5), -3)

    def test_multiplication(self):
        self.assertEqual(self.calc.multiply(3, 4), 12)
        self.assertEqual(self.calc.multiply(-2, 5), -10)
        self.assertEqual(self.calc.multiply(-3, -6), 18)
        self.assertEqual(self.calc.multiply(0, 100), 0)

    def test_division(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(-9, 3), -3)
        self.assertEqual(self.calc.divide(-12, -3), 4)

        # Division by zero case
        self.assertIsNone(self.calc.divide(5, 0))
        self.assertIsNone(self.calc.divide(0, 0))

    def test_division_floats(self):
        self.assertAlmostEqual(self.calc.divide(7, 2), 3.5)
        self.assertAlmostEqual(self.calc.divide(1, 4), 0.25)