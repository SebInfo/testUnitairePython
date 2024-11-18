import unittest
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))
from ExempleBancaire.src.classes.CompteBancaire import CompteBancaire



class TestCompteBancaire(unittest.TestCase):

    def setUp(self):
        # Préparer un compte bancaire avant chaque test
        self.account = CompteBancaire(100)  # Solde initial de 100
        print("setUp: Compte initialisé avec un solde de 100.")

    def tearDown(self):
        # Nettoyage après chaque test
        print(f"tearDown: Fin du test. Solde final : {self.account.solde}")
        self.account = None

    def test_depot(self):
        self.account.depot(50)
        self.assertEqual(self.account.solde, 150)  # 100 + 50
        print("Test dépôt réussi.")

    def test_retrait(self):
        self.account.retrait(30)
        self.assertEqual(self.account.solde, 70)  # 100 - 30
        print("Test retrait réussi.")

    def test_retrait_avec_fond_insuffisant(self):
        with self.assertRaises(ValueError) as context:
            self.account.retrait(150)
        # Vérifier le message exact de l'exception
        self.assertEqual(str(context.exception), "Impossible de "
                                                 "retirer cette somme les fonds sont insuffisants.")
        print("Test retrait fonds insuffisants réussi.")

    def test_depot_avec_montant_negatif(self):
        with self.assertRaises(ValueError):
            self.account.depot(-20)
        print("Test dépôt négatif réussi.")

if __name__ == "__main__":
    unittest.main()
