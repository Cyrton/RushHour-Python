# -*- coding: utf-8 -*-
"""
Created on Sun May 07 11:11:12 2017

@author: marti
"""
from tkinter import *
from PIL import Image
from pickle import dump, load
import threading
import time

score = 2000
#Class comprenant toutes les fonctiosn necessaire au bon déroulement du jeu
class ApplicationBase(object):
    #Def qui permet de crée les boutons communs à tous les niveaux
    def __init__(self):
        self.score = score
        self.b = Button(self.root,text="COMMENCER",command = self.Commencer,bg="#66EC62",width=25,height=1)
        self.b.place(anchor=CENTER, x=450,y=585)
        self.boutton2 = Button(self.root,text="Sauvergarde",state = DISABLED,bg="#86DED2",width =25,height=1 )
        self.boutton2.place(anchor=CENTER, x=450,y=635)
        self.b2 = Button(self.root,text="RETOURNER AU MENU",command=self.RetourPrincipale,bg="#FD4141",width=25,height=1)
        self.b2.place(anchor=CENTER, x=450,y=685)

    #Def qui Permet de lancer la partie et donc le compte a rebour
    def Commencer(self):
        self.b.destroy()
        self.varVictoire = 0
        self.ScoreJoueur()
        self.canvas.bind("<Button-1>", self.mouseDown)
        self.canvas.bind("<Button1-Motion>", self.mouseMove)
        self.canvas.bind("<Button1-ButtonRelease>", self.mouseUp)
    
    #Def permettant d'ajuster l'enlevement des points par niveau et par secondes
    def ScoreJoueur(self):        
        if self.niveau == 1:
            if self.score > 0 and self.varVictoire == 0:
                self.score -= 5
            self.fenetre_P.after(1000,self.ScoreJoueur)
        if self.niveau == 2:
            if self.score > 0 and self.varVictoire == 0:
                self.score -= 10
            self.fenetre_P.after(1000,self.ScoreJoueur)
        if self.niveau == 3:
            if self.score > 0 and self.varVictoire == 0:
                self.score -= 15
            self.fenetre_P.after(1000,self.ScoreJoueur)

    # def permettant de selectionner et bouger les rectangles objets
    def mouseDown(self, event):
        self.x1, self.y1 = event.x, event.y
        self.selObject = self.canvas.find_closest(self.x1, self.y1) 
    
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
    
    #Def qui permet de revenir au menu principal 
    def RetourPrincipale(self):
        self.root.destroy()
        #Fenetre_Principale()