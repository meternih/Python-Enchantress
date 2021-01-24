import unittest
from homework.test_simple_calc import add, subtract, multiply, divide


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 6), 8)
        self.assertEqual(add(5, -6), -1)
        self.assertEqual(add(1.2, 3.4), 4.6)

    def test_subtract(self):
        self.assertEqual(subtract(6, 6), 0)
        self.assertEqual(subtract(-6, 6), 0)
        self.assertEqual(subtract(6.6, 6.6), 13.2)

    def test_multiply(self):
        self.assertEqual(multiply(10, 10), 100)
        self.assertEqual(multiply(10, -10), -100)
        self.assertEqual(multiply(10.5, 10.5), 110.25)

    def test_divide(self):
        self.assertEqual(divide(15, 15), 1)
        self.assertEqual(divide(-15, 15), -1)
        self.assertEqual(divide(15, 6), 2.5)

    def test_divide_not_zero(self):
        with self.assertRaises(ValueError):
            divide(6, 0)


if __name__ == '__main__':
    unittest.main()
