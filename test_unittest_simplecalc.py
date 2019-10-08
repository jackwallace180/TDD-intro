from simple_calc import SimpleCalc

import unittest

class Calctest(unittest.TestCase):

    calc = SimpleCalc()

    def test_add(self):
        self.assertEqual(self.calc.add(2,4), 6)

    def test_add2(self):
        self.assertEqual(self.calc.add(26,7), 33)

    def test_subtract(self):
        self.assertEqual(self.calc.subtract(6,4), 2)

    def test_subtract2(self):
        self.assertEqual(self.calc.subtract(6,3), 3)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(2,2), 4)

    def test_multiply2(self):
        self.assertEqual(self.calc.multiply(12,12), 144)

    def test_divide(self):
        self.assertEqual(self.calc.divide(10,2), 5)

    def test_divide2(self):
        self.assertEqual(self.calc.divide(220, 2), 110)





