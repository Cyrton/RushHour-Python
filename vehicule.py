# -*- coding: utf-8 -*-
"""
Created on Sun May 07 11:11:12 2017

@author: martin
"""
from tkinter import *
from PIL import Image
from pickle import dump, load
from random import *
import json


class vehicule:
    def __init__(self,unite, x, y):
        self.unite = unite
        self.x = x
        self.y = y

    def Niveau(self,unite,x,y):
        #Rectangles (invisible) se trouvant sur le cote de la grille afin de bloquer les rectangles a l'interieur de celle ci
        self.ext1 = self.canvas.create_rectangle(x+(-0.3*unite),y+(-100.4*unite),x+(29.9*unite),y+(-0.01*unite), outline="")
        self.ext2 = self.canvas.create_rectangle(x+(-100.4*unite),y+(-0.3*unite),x+(-0.01*unite),y+(29.9*unite), outline="")
        self.ext3 = self.canvas.create_rectangle(x+(-0.3*unite),y+(29.61*unite),x+(29.9*unite),y+(130*unite), outline="")
        self.ext4 = self.canvas.create_rectangle(x+(29.61*unite),y+(14.7*unite),x+(130*unite),y+(29.9*unite), outline="")
        self.ext5 = self.canvas.create_rectangle(x+(29.61*unite),y+(-0.3*unite),x+(130*unite),y+(9.9*unite), outline="")
        situation = randint(0, 2)
        print(situation)

        if self.niveau == 1:
            #Rectangles du "jeu" a proprement parlé
            if situation == 0:
                self.v1 = self.canvas.create_rectangle(x+(0*unite),y+(0*unite),x+(9.6*unite),y+(4.6*unite), fill="pale green2")
                self.v2 = self.canvas.create_rectangle(x+(0*unite),y+(5*unite),x+(9.6*unite),y+(9.6*unite), fill="pink")
                self.v3 = self.canvas.create_rectangle(x+(0*unite),y+(25*unite),x+(9.6*unite),y+(29.6*unite), fill="brown")
                self.v4 = self.canvas.create_rectangle(x+(10*unite),y+(0*unite),x+(14.6*unite),y+(9.6*unite), fill="dark orange")
                self.v5 = self.canvas.create_rectangle(x+(15*unite),y+(20*unite),x+(19.6*unite),y+(29.6*unite), fill="dark violet")
                self.v6 = self.canvas.create_rectangle(x+(20*unite),y+(0*unite),x+(29.6*unite),y+(4.6*unite), fill="sky blue")
                self.v7 = self.canvas.create_rectangle(x+(20*unite),y+(20*unite),x+(29.6*unite),y+(24.6*unite), fill="dark olive green")
                self.v8 = self.canvas.create_rectangle(x+(20*unite),y+(25*unite),x+(29.6*unite),y+(29.6*unite), fill="AntiqueWhite3")
                self.c1 = self.canvas.create_rectangle(x+(0*unite),y+(10*unite),x+(4.6*unite),y+(24.6*unite), fill="pale violet red3")
                self.c2 = self.canvas.create_rectangle(x+(5*unite),y+(15*unite),x+(19.6*unite),y+(19.6*unite), fill="royal blue4")
                self.c3 = self.canvas.create_rectangle(x+(25*unite),y+(5*unite),x+(29.6*unite),y+(19.6*unite), fill="Yellow2")
                self.carreRouge = self.canvas.create_rectangle(x+(5*unite),y+(10*unite),x+(14.6*unite),y+(14.6*unite), fill="red")

                #Permet de "grouper" nos differents objets
                self.rectH = [self.v1,self.v2,self.v3,self.carreRouge,self.c2,self.v6,self.v7,self.v8]
                self.rectV = [self.c1,self.v4,self.v5,self.c3]
                self.bloq =  [self.ext1,self.ext2,self.ext3,self.ext4,self.ext5]
                self.rectAll = self.rectH + self.rectV +self.bloq

            if situation == 1:
                self.v1 = self.canvas.create_rectangle(x+(0*unite),y+(0*unite),x+(9.6*unite),y+(4.6*unite), fill="pale green2")
                self.v2 = self.canvas.create_rectangle(x+(0*unite),y+(20*unite),x+(4.6*unite),y+(29.6*unite), fill="dark orange")
                self.v3 = self.canvas.create_rectangle(x+(20*unite),y+(20*unite),x+(29.6*unite),y+(24.6*unite), fill="sky blue")
                self.c1 = self.canvas.create_rectangle(x+(0*unite),y+(5*unite),x+(4.6*unite),y+(19.6*unite), fill="violet")
                self.c2 = self.canvas.create_rectangle(x+(15*unite),y+(5*unite),x+(19.6*unite),y+(19.6*unite), fill="dark blue")
                self.c3 = self.canvas.create_rectangle(x+(25*unite),y+(0*unite),x+(29.6*unite),y+(14.6*unite), fill="Yellow2")
                self.c4 = self.canvas.create_rectangle(x+(10*unite),y+(25*unite),x+(24.6*unite),y+(29.6*unite), fill="dark green")
                self.carreRouge = self.canvas.create_rectangle(x+(5*unite),y+(10*unite),x+(14.6*unite),y+(14.6*unite), fill="red")

                #Permet de "grouper" nos differents objets
                self.rectH = [self.v1,self.v3,self.c4,self.carreRouge]
                self.rectV = [self.v2,self.c1,self.c2,self.c3]
                self.bloq =  [self.ext1,self.ext2,self.ext3,self.ext4,self.ext5]
                self.rectAll = self.rectH + self.rectV +self.bloq

            if situation == 2:
                self.c1 = self.canvas.create_rectangle(x+(0*unite),y+(15*unite),x+(4.6*unite),y+(29.6*unite), fill="violet")
                self.v1 = self.canvas.create_rectangle(x+(5*unite),y+(0*unite),x+(9.6*unite),y+(9.6*unite), fill="pale green2")
                self.v2 = self.canvas.create_rectangle(x+(10*unite),y+(0*unite),x+(19.6*unite),y+(4.6*unite), fill="orange")
                self.v3 = self.canvas.create_rectangle(x+(20*unite),y+(0*unite),x+(29.6*unite),y+(4.6*unite), fill="sky blue")
                self.v4 = self.canvas.create_rectangle(x+(20*unite),y+(5*unite),x+(29.6*unite),y+(9.6*unite), fill="dark violet")
                self.v5 = self.canvas.create_rectangle(x+(25*unite),y+(10*unite),x+(29.6*unite),y+(19.6*unite), fill="dark green")
                self.v6 = self.canvas.create_rectangle(x+(25*unite),y+(20*unite),x+(29.6*unite),y+(29.6*unite), fill="beige")
                self.v7 = self.canvas.create_rectangle(x+(15*unite),y+(5*unite),x+(19.6*unite),y+(14.6*unite), fill="pink")
                self.v8 = self.canvas.create_rectangle(x+(10*unite),y+(20*unite),x+(14.6*unite),y+(29.6*unite), fill="black")
                self.c2 = self.canvas.create_rectangle(x+(5*unite),y+(15*unite),x+(14.6*unite),y+(19.6*unite), fill="blue")
                self.c3 = self.canvas.create_rectangle(x+(20*unite),y+(10*unite),x+(24.6*unite),y+(24.6*unite), fill="Yellow2")
                self.carreRouge = self.canvas.create_rectangle(x+(0*unite),y+(10*unite),x+(9.6*unite),y+(14.6*unite), fill="red")

                #Permet de "grouper" nos differents objets
                self.rectH = [self.carreRouge,self.v2,self.v3,self.v4,self.c2]
                self.rectV = [self.c1,self.v1,self.v5,self.v6,self.v7,self.v8,self.c3]
                self.bloq =  [self.ext1,self.ext2,self.ext3,self.ext4,self.ext5]
                self.rectAll = self.rectH + self.rectV +self.bloq
            

        
        if self.niveau == 2:
            self.v1 = self.canvas.create_rectangle(x+(0*unite),y+(0*unite),x+(9.6*unite),y+(4.6*unite), fill="pale green2")
            self.v2 = self.canvas.create_rectangle(x+(0*unite),y+(5*unite),x+(9.6*unite),y+(9.6*unite), fill="sky blue")
            self.v3 = self.canvas.create_rectangle(x+(10*unite),y+(0*unite),x+(14.6*unite),y+(9.6*unite), fill="dark orange")
            self.v4 = self.canvas.create_rectangle(x+(5*unite),y+(20*unite),x+(14.6*unite),y+(24.6*unite), fill="pink")
            self.c1 = self.canvas.create_rectangle(x+(0*unite),y+(10*unite),x+(4.6*unite),y+(24.6*unite), fill="pale violet red3")
            self.c2 = self.canvas.create_rectangle(x+(0*unite),y+(25*unite),x+(14.6*unite),y+(29.6*unite), fill="dark green")
            self.c3 = self.canvas.create_rectangle(x+(5*unite),y+(15*unite),x+(19.6*unite),y+(19.6*unite), fill="royal blue4")
            self.c4 = self.canvas.create_rectangle(x+(15*unite),y+(0*unite),x+(19.6*unite),y+(14.6*unite), fill="Yellow2")
            self.carreRouge = self.canvas.create_rectangle(x+(5*unite),y+(10*unite),x+(14.6*unite),y+(14.6*unite), fill="red")
                            
            self.rectH = [self.v1,self.v2,self.c2,self.c3,self.v4,self.carreRouge]
            self.rectV = [self.c1,self.v3,self.c4]
            self.bloq =  [self.ext1,self.ext2,self.ext3,self.ext4,self.ext5]
            self.rectAll = self.rectH + self.rectV +self.bloq

        if self.niveau == 3:
            self.v1 = self.canvas.create_rectangle(x+(10*unite),y+(5*unite),x+(14.6*unite),y+(14.6*unite), fill="pale green2")
            self.v2 = self.canvas.create_rectangle(x+(15*unite),y+(5*unite),x+(24.6*unite),y+(9.6*unite), fill="orange")
            self.v3 = self.canvas.create_rectangle(x+(10*unite),y+(15*unite),x+(14.6*unite),y+(24.6*unite), fill="sky blue")
            self.v4 = self.canvas.create_rectangle(x+(20*unite),y+(15*unite),x+(29.6*unite),y+(19.6*unite), fill="violet")
            self.v5 = self.canvas.create_rectangle(x+(20*unite),y+(20*unite),x+(29.6*unite),y+(24.6*unite), fill="dark green")
            self.v6 = self.canvas.create_rectangle(x+(15*unite),y+(15*unite),x+(19.6*unite),y+(24.6*unite), fill= "pink")
            self.c1 = self.canvas.create_rectangle(x+(25*unite),y+(0*unite),x+(29.6*unite),y+(14.6*unite), fill="pale violet red3")
            self.c2 = self.canvas.create_rectangle(x+(10*unite),y+(25*unite),x+(24.6*unite),y+(29.6*unite), fill="royal blue4")
            self.c3 = self.canvas.create_rectangle(x+(10*unite),y+(0*unite),x+(24.6*unite),y+(4.6*unite), fill="Yellow2")
            self.carreRouge = self.canvas.create_rectangle(x+(15*unite),y+(10*unite),x+(24.6*unite),y+(14.6*unite), fill="red")
                            
            self.rectH = [self.v2,self.c2,self.carreRouge,self.c3,self.v4,self.v5]
            self.rectV = [self.v1,self.c1,self.v3,self.v6]
            self.bloq =  [self.ext1,self.ext2,self.ext3,self.ext4,self.ext5]
            self.rectAll = self.rectH + self.rectV +self.bloq


    
    # def permettant de selectionner et bouger les rectangles objets
    def mouseDown(self, event):
        self.x1, self.y1 = event.x, event.y
        self.selObject = self.canvas.find_closest(self.x1, self.y1) 
    
    #Fonction permettant de faire les sauvegardes
    #TODO /!\ déplacer cette fonction dans la class user quand elle sera crée  
    def DumpSauvegarde(self,pseudo,score):
        print("Voici le score {0} de {1}".format(self.pseudo,self.score))
        with open('sauvegarde.json') as json_data_r:
            data_dict = json.load(json_data_r)
        
        for x in data_dict:
            if x == pseudo:
                for y in data_dict[x]["score"]:
                    if self.niveau == 1:
                        print(data_dict[x]["score"][0])
                        break
                    if self.niveau == 2:
                        print(data_dict[x]["score"][1])
                        break
                    if self.niveau == 3:
                        print(data_dict[x]["score"][2])
                        break

    #Fonction qui nous permet de bloquer les rectangles objets entre eux mais aussi de "gagner" lorsqu'un rectangle particulier atteint une certaine coordonée      
    def FreeToMove(self,X=0,Y=0):
        coord = self.canvas.coords(self.selObject[0])
        cond = True
        if self.varVictoire == 0:
            for rect in self.rectAll:
                coordR = self.canvas.coords(rect)
                if self.selObject[0] == rect and self.varVictoire == 0:
                    if self.canvas.coords(self.carreRouge)[0] >= 650:
                        print ("Gagné !")
                        self.varVictoire = 1
                        self.DumpSauvegarde(self.pseudo,self.score)
                        self.niveausuivant(self.score)
                        break
                elif(coordR[0]<=coord[0]+X<=coordR[2] and coordR[1]<=coord[1]+Y<=coordR[3]) or\
                    (coordR[0]<=coord[2]+X<=coordR[2] and coordR[1]<=coord[3]+Y<=coordR[3]) or\
                    (coordR[0]<=coord[2]+X<=coordR[2] and coordR[1]<=coord[1]+Y<=coordR[3]) or\
                    (coordR[0]<=coord[0]+X<=coordR[2] and coordR[1]<=coord[3]+Y<=coordR[3]):
                    cond = False
                    break
        return cond
        
    # def permettant de selectionner et bouger les rectangles objets
    def mouseMove(self, event):
        x2, y2 = event.x, event.y
        dx, dy = x2 -self.x1, y2 -self.y1
        if self.selObject and self.varVictoire == 0:
            if self.selObject[0] in self.rectV:
                if self.FreeToMove(Y=dy):
                    self.canvas.move(self.selObject, 0, dy)
            elif self.selObject[0] in self.rectH:
                if self.FreeToMove(X=dx):
                    self.canvas.move(self.selObject, dx, 0)
            self.x1, self.y1 = x2, y2
     
    # def permettant de selectionner et bouger les rectangles objets
    def mouseUp(self, event):
        if self.selObject and self.varVictoire == 0:
            self.canvas.itemconfig(self.selObject[0], width = 1)
            self.selObject =None