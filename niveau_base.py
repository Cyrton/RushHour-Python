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
from vehicule import *


score = 2000
#Class comprenant toutes les fonctiosn necessaire au bon déroulement du jeu
class ApplicationBase(vehicule):
    #Def qui permet de crée les boutons communs à tous les niveaux
    def __init__(self):
        self.score = score
        self.labelInfo = Label(self.root, text="Pour lancer ler niveau, cliquer sur le bouton 'COMMENCER'",font="Arial 11",bg='sky blue')
        self.labelInfo.place(anchor=CENTER,x=450,y=585)
        self.b = Button(self.root,text="COMMENCER",command = self.Commencer,bg="#66EC62",width=25,height=1)
        self.b.place(anchor=CENTER, x=450,y=635)
        self.b2 = Button(self.root,text="RETOURNER AU MENU",command=self.RetourPrincipale,bg="#FD4141",width=25,height=1)
        self.b2.place(anchor=CENTER, x=450,y=685)

    #Def qui Permet de lancer la partie et donc le compte a rebour
    def Commencer(self):
        self.b.destroy()
        self.labelInfo.destroy()
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
             
    #Def qui permet de revenir à la page profil 
    def RetourPrincipale(self):
        self.Fenetre_profil(NONE,self.fenetre_P,self.Fenetre_Jouer,self.pseudo,self.Fenetre_Principale,1,self.root)

