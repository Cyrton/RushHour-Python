# -*- coding: utf-8 -*-
"""
Created on Sun May 07 11:11:12 2017

@author: marti
"""
from tkinter import *
from PIL import Image
from pickle import dump, load
from niveau_base import *
from vehicule import *

#La meme chose que pour le niveau 1                   
class ApplicationNv3(ApplicationBase,vehicule):
    def __init__(self,unite, x, y,score,fenetre_P,canvas_profil,pseudo,Fenetre_profil):

        self.unite = unite
        self.x = x
        self.y = y

        self.Fenetre_profil = Fenetre_profil
        self.canvas_profil = canvas_profil
        self.pseudo = pseudo
        self.canvas_profil.destroy()
        self.fenetre_P = fenetre_P
        self.root= self.fenetre_P
        self.root.title('UNBLOCK THE BLOCK - NIVEAU 3')

        self.canvas = Canvas(self.root, bg="#FE5227", width=0, height=399)
        self.canvas.pack(side=TOP, fill=BOTH, expand=YES)
        ApplicationBase.__init__(self)
    
        photo2 = PhotoImage(file='lave.gif',width=1900,height=1110)
        self.canvas.create_image(0,0,image=photo2)
        self.photo = PhotoImage(file='Image_Grille_Difficile_.gif')
        self.canvas.create_image(448, 274, image=self.photo)

        print ("Niveau 3")            
        self.niveau = 3
        self.Niveau(self.unite, self.x,  self.y)
        self.root.mainloop()
                               
    def niveausuivant(self,score):
        label=Label(self.root,text="VOTRE SCORE !\n\n" + str(score),fg="black",bg="#759EFE",width=25,height=5)
        label.place(anchor=CENTER, x=200,y=635)
        label2=Label(self.root,text="VOTRE SCORE !\n\n" + str(score),fg="black",bg="#759EFE",width=25,height=5)
        label2.place(anchor=CENTER, x=700,y=635)
        label2=Label(self.root,text="FÉLICITATION !\nVous avez fini le jeu !",fg="black",bg="#FE5227", font= "Arial 14",width=25,height=2)
        label2.place(anchor=CENTER, x=450,y=585)