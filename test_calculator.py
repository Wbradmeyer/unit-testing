import unittest
import calculator

class TestCalculator(unittest.TestCase):
    def test_add(self):
        self.assertEqual(calculator.add(1, 2), 3)
        self.assertEqual(calculator.add(-1, 1), 0)
        self.assertEqual(calculator.add(-1, -1), -2)
        self.assertEqual(calculator.add(0, 0), 0)
        self.assertNotEqual(calculator.add(1, 2), 2)

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

    def test_is_single_digit_even(self):
        self.assertTrue(calculator.is_single_digit_even(4, 2))
        self.assertFalse(calculator.is_single_digit_even(5, 2))
        self.assertFalse(calculator.is_single_digit_even(9, 2))
        self.assertFalse(calculator.is_single_digit_even(-4, -2))

    def test_is_in_num_list(self):
        self.assertIn(calculator.is_in_num_list(2), [1,2,3,4,5])
        self.assertIn(calculator.is_in_num_list(3), [1,2,3,4,5])

    def test_bigger_num(self):
        self.assertGreater(calculator.bigger_num(3), 2)

    def test_num_to_power_of(self):
        self.assertEqual(calculator.num_to_power_of(2, 2), 4)
        self.assertEqual(calculator.num_to_power_of(3, 2), 9)
        self.assertEqual(calculator.num_to_power_of(4, 4), 256)

    def test_is_square_root(self):
        self.assertTrue(calculator.is_square_root(4, 2))
        self.assertTrue(calculator.is_square_root(9, 3))
        self.assertTrue(calculator.is_square_root(64, 8))

if __name__ == '__main__':
    unittest.main()