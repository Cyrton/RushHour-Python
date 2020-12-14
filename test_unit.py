import unittest
from fenetre_jouer import *
from fenetre_charger import *
from fenetre_profil import *

with open('sauvegarde.json') as json_data_r:
        data_dict = json.load(json_data_r)

with open('vehicule.json') as json_data_r:
        data_car = json.load(json_data_r)


class TestProjet(unittest.TestCase):
    def __init__(self, methodName):
        super().__init__(methodName)

    def test_Fenetre_Charger (self):
        self.assertEqual(type(dict_classement1), dict)
        self.assertEqual(type(dict_classement2), dict)
        self.assertEqual(type(dict_classement3), dict)
        #self.assertEqual(dict_classement1["joueur"][0], "martin")
        
    def test_jsonProfil (self):
        self.assertEqual(data_dict["martin"]["historique"][0], 1)
        self.assertEqual(data_dict["cyril"]["score"][0], 1910)
        self.assertEqual(type(data_dict["martin"]["historique"]), list)
        self.assertEqual(type(data_dict["cyril"]["score"]), list)
        self.assertEqual(type(data_dict["cyril"]["score"][0]), int)

        self.assertIsNot(type(data_dict["martin"]["historique"]), dict)
        self.assertIsNot(data_dict["cyril"]["score"][0], 1)

    def test_jsonCar (self):
        self.assertEqual(type(data_car["niveau1"]["0"]["v1"]["couleur"]), str)
        self.assertEqual(type(data_car["niveau1"]["0"]["v1"]["orientation"]), str)
        self.assertEqual(data_car["niveau1"]["0"]["v1"]["orientation"], "h")

        self.assertIsNot(data_car["niveau1"]["0"]["v1"]["orientation"], "v")
        self.assertIsNot(type(data_car["niveau1"]["0"]["v1"]["orientation"]), int)

    def test_Jouer (self):
        self.assertEqual(VerifPseudo(None, None, None, "", None), None)
    
    def test_Profil (self):
        self.assertEqual(Fenetre_profil(None, None, None, None, None, 0, None), 0)        


if __name__ == '__main__':
    unittest.main()