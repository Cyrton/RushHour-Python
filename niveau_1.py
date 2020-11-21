# -*- coding: utf-8 -*-
"""
Created on Sun May 07 11:11:12 2017

@author: martin
"""
from tkinter import *
from PIL import Image
from pickle import dump, load
from niveau_base import *
from niveau_2 import *
from vehicule import *
import threading
import time


#Class comprenant toutes les fonctiosn necessaire au bon déroulement du jeu
class ApplicationNv1(ApplicationBase,vehicule):
    def __init__(self,unite, x, y,score,fenetre_P,canvas_profil,pseudo):
        self.fenetre_P = fenetre_P
        self.canvas_profil = canvas_profil
        self.pseudo = pseudo
        self.canvas_profil.destroy()
        self.root= self.fenetre_P
        self.root.geometry("900x800")
        self.root.title('UNBLOCK THE BLOCK - NIVEAU 1')
        
        #Canvas
        self.canvas = Canvas(self.root, bg="light green", width=700, height=500)
        self.canvas.pack(side=TOP, fill=BOTH, expand=YES)
        ApplicationBase.__init__(self)

        #Insertion Image_Grille
        photo2 = PhotoImage(file='herbe.gif',width=1900,height=1105)
        self.canvas.create_image(0,0,image=photo2)
        photo= PhotoImage(file='Image_Grille_Facile_.gif')
        self.canvas.create_image(448, 274, image=photo)

        #Définition du niveau et du score
        print ("Niveau 1")
        self.niveau = 1
        self.Niveau(10, 300,  125)
        self.root.mainloop()

    #Def permetant d'afficher le score et de lancer la commande vers le niveau suivant        
    def niveausuivant(self,score):
        boutton = Button(self.root,text="Niveau Suivant",command=self.nextNiveau,bg="#66EC62",width =25,height=1 )
        boutton.place(anchor=CENTER, x=450,y=585)
        label=Label(self.root,text="VOTRE SCORE !\n\n" + str(score),fg="black",bg="#759EFE",width=25,height=5)
        label.place(anchor=CENTER, x=200,y=635)
        label2=Label(self.root,text="VOTRE SCORE !\n\n" + str(score),fg="black",bg="#759EFE",width=25,height=5)
        label2.place(anchor=CENTER, x=700,y=635)
    
    #Def de lancement du niveau 2
    def nextNiveau(self):
        self.canvas.destroy()
        ApplicationNv2(10, 300,  125,score,self.fenetre_P,self.canvas_profil,self.pseudo)   
    