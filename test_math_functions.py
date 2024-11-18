# test_math_functions.py
import unittest
from math_functions import addition, racine_carre, cosinus, sinus, est_paire, log
import math

class TestMathFunctions(unittest.TestCase):

    def test_addition(self):
        self.assertEqual(addition(3, 4), 7)
        self.assertEqual(addition(-1, 5), 4)
        self.assertEqual(addition(0, 0), 0)

    def test_square_root(self):
        self.assertEqual(racine_carre(16), 4)
        self.assertAlmostEqual(racine_carre(2), math.sqrt(2), places=5)

    def test_cosine(self):
        self.assertAlmostEqual(cosinus(math.pi), -1, places=5)
        self.assertAlmostEqual(cosinus(0), 1, places=5)
        self.assertAlmostEqual(cosinus(math.pi / 2), 0, places=5)

    def test_sine(self):
        self.assertAlmostEqual(sinus(0), 0, places=5)
        self.assertAlmostEqual(sinus(math.pi / 2), 1, places=5)
        self.assertAlmostEqual(sinus(math.pi), 0, places=5)

    def test_paire(self):
        self.assertFalse(est_paire(9))
        self.assertFalse(est_paire(0.2))
        self.assertFalse(est_paire(7))

    def test_dans_la_liste(self):
        values = [1, 2, 3, 4, 5]
        self.assertIn(3, values)  # 3 est dans la liste
        self.assertIn(5, values)  # 5 est dans la liste
        self.assertFalse(10 in values)  # 10 n'est pas dans la liste

    def test_log(self):
        self.assertIsNone(log(-1))  # Logarithme de -1 n'est pas défini
        self.assertIsNotNone(log(10))


if __name__ == '__main__':
    unittest.main()
