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
        # self.assertEqual(calculator.divide(5, 0), 0)

    def test_multiply(self):
        self.assertEqual(calculator.multiply(2, 2), 4)
        self.assertEqual(calculator.multiply(2, -3), -6)
        self.assertEqual(calculator.multiply(-3, -3), 9)
        self.assertEqual(calculator.multiply(2, 0), 0)

    def test_count_list(self):
        self.assertEqual(calculator.count_by(1, 5), [1, 2, 3, 4, 5])
        self.assertEqual(calculator.count_by(2, 5), [2, 4, 6, 8, 10])
        self.assertEqual(calculator.count_by(3, 5), [3, 6, 9, 12, 15])

if __name__ == '__main__':
    unittest.main()