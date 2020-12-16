import unittest
from fenetre_jouer import *
from fenetre_charger import *
from fenetre_profil import *
from niveau_base import *

with open('sauvegarde.json') as json_data_r:
        data_dict = json.load(json_data_r)

with open('vehicule.json') as json_data_r:
        data_car = json.load(json_data_r)


class TestProjet(unittest.TestCase):
    def __init__(self, methodName):
        super().__init__(methodName)
        self.data_dict= {"martin": {"historique": [1, 2, 3], "score": [1960, 1740, 1180]}, 
        "cyril": {"historique": [0, 0, 0], "score": [0, 0, 0]}, 
        "tata": {"historique": [1, 0, 0], "score": [1960, 0, 0]}}
        self.dict_classement1={'joueur': {0: 'martin', 1: 'cyril', 2: 'tata'}, 'niveau 1': {0: 1960, 1: 0, 2: 1960}}
        self.dict_classement2={'joueur': {0: 'martin', 1: 'cyril', 2: 'tata'}, 'niveau 2': {0: 1740, 1: 0, 2: 0}}
        self.dict_classement3={'joueur': {0: 'martin', 1: 'cyril', 2: 'tata'}, 'niveau 3': {0: 1180, 1: 0, 2: 0}}

    def test_Fenetre_Charger (self):
        self.assertEqual(type(self.dict_classement1), dict)
        self.assertEqual(type(self.dict_classement2), dict)
        self.assertEqual(type(self.dict_classement3), dict)
        #self.assertEqual(dict_classement1["joueur"][0], "martin")
        
    def test_jsonProfil (self):
        self.assertEqual(self.data_dict["martin"]["historique"][0], 1)
        self.assertEqual(self.data_dict["cyril"]["score"][0], 0)
        self.assertEqual(type(self.data_dict["martin"]["historique"]), list)
        self.assertEqual(type(self.data_dict["cyril"]["score"]), list)
        self.assertEqual(type(self.data_dict["cyril"]["score"][0]), int)

        self.assertIsNot(type(self.data_dict["martin"]["historique"]), dict)
        self.assertIsNot(self.data_dict["cyril"]["score"][0], 1)

    def test_jsonCar (self):
        self.assertEqual(type(data_car["niveau1"]["0"]["v1"]["couleur"]), str)
        self.assertEqual(type(data_car["niveau1"]["0"]["v1"]["orientation"]), str)
        self.assertEqual(data_car["niveau1"]["0"]["v1"]["orientation"], "h")

        self.assertIsNot(data_car["niveau1"]["0"]["v1"]["orientation"], "v")
        self.assertIsNot(type(data_car["niveau1"]["0"]["v1"]["orientation"]), int)

    def test_Jouer (self):
        pass
    
    def test_Profil (self):
        #self.assertEqual(Fenetre_profil(None, None, None, None, None, 0, None), 0)        
        pass

    def test_classementValue(self):
        self.assertGreater(self.data_dict["martin"]["score"][0], self.data_dict["cyril"]["score"][0])
        self.assertLess(self.data_dict["cyril"]["score"][0], self.data_dict["martin"]["score"][0])
    
    def test_supprimer(self):
        pass

    def test_score(self):
        index= 10
        while index > 0:
            ApplicationBase.ScoreJoueur(2000) 
            index -= 1
        self.assertEqual(, 1800)


if __name__ == '__main__':
    unittest.main()