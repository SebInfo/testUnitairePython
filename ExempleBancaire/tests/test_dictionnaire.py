import unittest

class TestDictionnaire(unittest.TestCase):
    def setUp(self):
        # Préparation des données de test
        self.sample_dict = {
            "id": 1,
            "nom": "Jean Dupont",
            "age": 30,
            "adresse": {
                "rue": "10 rue de Paris",
                "ville": "Paris",
                "code_postal": "75000"
            }
        }

    def test_cle_existe(self):
        # Vérifier qu'une clé spécifique existe
        self.assertIn("nom", self.sample_dict)
        self.assertIn("adresse", self.sample_dict)

    def test_valeurs_correctes(self):
        # Vérifier les valeurs d'une clé
        self.assertEqual(self.sample_dict["nom"], "Jean Dupont")
        self.assertEqual(self.sample_dict["age"], 30)

    def test_adresse(self):
        # Vérifier des données imbriquées
        self.assertEqual(self.sample_dict["adresse"]["ville"], "Paris")
        self.assertEqual(self.sample_dict["adresse"]["code_postal"], "75000")

    def test_types(self):
        # Vérifier les types des valeurs
        self.assertIsInstance(self.sample_dict["id"], int)
        self.assertIsInstance(self.sample_dict["nom"], str)
        self.assertIsInstance(self.sample_dict["adresse"], dict)

    def test_modification(self):
        # Tester une modification du dictionnaire
        self.sample_dict["age"] = 35
        self.assertEqual(self.sample_dict["age"], 35)

    def test_cle_absente(self):
        # Tester l'absence d'une clé
        self.assertNotIn("prenom", self.sample_dict)

if __name__ == "__main__":
    unittest.main()
