import unittest
import calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(1, 2), 3)
        self.assertEqual(calculator.add(-1, 1), 0)
        self.assertEqual(calculator.add(-1, -1), -2)
        self.assertEqual(calculator.add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(calculator.subtract(5, 2), 3)
        self.assertEqual(calculator.subtract(1, 1), 0)
        self.assertEqual(calculator.subtract(-1, -1), 0)
        self.assertEqual(calculator.subtract(4, -2), 6)

    def test_divide(self):
        self.assertEqual(calculator.divide(10, 2), 5)
        self.assertEqual(calculator.divide(9, 3), 3)
        self.assertEqual(calculator.divide(-6, 2), -3)
        self.assertEqual(calculator.divide(0, 1), 0)
        with self.assertRaises(ZeroDivisionError):
            calculator.divide(10, 0)
        self.assertEqual(calculator.divide(5, 0), 0)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(2, 2), 4)
        self.assertEqual(calculator.multiply(2, -3), -6)
        self.assertEqual(calculator.multiply(-3, -3), 9)
        self.assertEqual(calculator.multiply(2, 0), 0)

if __name__ == '__main__':
    unittest.main()