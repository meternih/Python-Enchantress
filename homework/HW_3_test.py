import unittest
from homework.test_simple_calc import add, subtract, multiply, divide


class TestCalc(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 6), 8)
        self.assertEqual(add(5, -6), -1)
        self.assertEqual(add(1.2, 3.4), 4.6)

    def test_substract(self):
        self.assertEqual(subtract(6, 6), 0)
        self.assertEqual(subtract(-6, 6), 0)
        self.assertEqual(subtract(6.6, 6.6), 13.2)


    def test_multiply(self):
        self.assertEqual(multiply(10, 10), 100)
        self.assertEqual(multiply(10, -10), -100)
        self.assertEqual(multiply(10.5, 10.5), 107.1)

    def test_divide(self):
        self.assertEqual(divide(15, 15), 1)
        self.assertEqual(divide(-15, 15), -1)
        self.assertEqual(divide(15, 6), 2.5)


if __name__ == '__main__':
    unittest.main()