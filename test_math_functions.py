# test_math_functions.py
import unittest
from math_functions import addition,racice_carre, cosinus, sinus
import math


class TestMathFunctions(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(addition(3, 4), 7)
        self.assertEqual(addition(-1, 5), 4)
        self.assertEqual(addition(0, 0), 0)

    def test_square_root(self):
        self.assertEqual(racice_carre(16), 4)
        self.assertAlmostEqual(racice_carre(2), math.sqrt(2), places=5)
        with self.assertRaises(ValueError):
            racice_carre(-1)

    def test_cosine(self):
        self.assertAlmostEqual(cosinus(math.pi), -1, places=5)
        self.assertAlmostEqual(cosinus(0), 1, places=5)
        self.assertAlmostEqual(cosinus(math.pi / 2), 0, places=5)

    def test_sine(self):
        self.assertAlmostEqual(sinus(0), 0, places=5)
        self.assertAlmostEqual(sinus(math.pi / 2), 1, places=5)
        self.assertAlmostEqual(sinus(math.pi), 0, places=5)

if __name__ == '__main__':
    unittest.main()
