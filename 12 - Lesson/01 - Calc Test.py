import unittest

class Calculator:
    def __init__(self): pass
    def add(self, x, y): return x + y
    def subtract(self, x, y): return x - y
    def multiply(self, x, y): return x * y
    def divide(self, x, y):
        if y == 0: raise ValueError ("ნულზე გაყოფა არ შეიძლება!")
        return x / y

class TestCalculator(unittest.TestCase):
    def setUp(self):
        self.calc_instance = Calculator()

    def test_add(self):
        result = self.calc_instance.add(12, 3)
        self.assertEqual(result, 15)

    def test_subtract(self):
        result = self.calc_instance.subtract(8, 7)
        self.assertEqual(result, 1)

    def test_multiply(self):
        result = self.calc_instance.multiply(6, 6)
        self.assertEqual(result, 36)

    def test_divide(self):
        result2 = self.calc_instance.divide(10, 4)
        self.assertAlmostEqual(result2, 2.5)

    def test_divide_by_zero(self):
        with self.assertRaises(ValueError):
            self.calc_instance.divide(6, 0)

if __name__ == '__main__':
    unittest.main()