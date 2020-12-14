# -*- coding: utf-8 -*-
import json

class user:
    def __init__(self,pseudo):
        self.pseudo = pseudo
        self.historique = []

    def sauvegarde(self,pseudo,score):
        indice = self.niveau-1
        print("Voici le score de {0} de {1}".format(self.pseudo,self.score))
        with open('sauvegarde.json') as json_data_r:
            data_dict = json.load(json_data_r)
        
        for x in data_dict:
            if x == pseudo:
                for y in data_dict[x]["score"]:
                    if self.niveau == 1:
                        if data_dict[x]["score"][indice] < score:
                            data_dict[x]["score"][indice] = score
                            data_dict[x]["historique"][indice] = self.niveau
                            with open('sauvegarde.json','w') as json_data_w:
                                json.dump(data_dict,json_data_w)
                        break
                    elif self.niveau == 2:
                        if data_dict[x]["score"][indice] < score:
                            data_dict[x]["score"][indice] = score
                            data_dict[x]["historique"][indice] = self.niveau
                            with open('sauvegarde.json','w') as json_data_w:
                                json.dump(data_dict,json_data_w)
                        break
                    elif self.niveau == 3:
                        if data_dict[x]["score"][indice] < score:
                            data_dict[x]["score"][indice] = score
                            data_dict[x]["historique"][indice] = self.niveau
                            with open('sauvegarde.json','w') as json_data_w:
                                json.dump(data_dict,json_data_w)
                        break

    def delete(self,li_sauvegarde,pseudo,data_dict,index_delete):
        self.historique = li_sauvegarde
        for y in self.historique:
            del self.historique[index_delete]
            break
        data_dict[pseudo]["historique"] = self.historique

        with open('sauvegarde.json','w') as json_data_w:
            json.dump(data_dict,json_data_w)
