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
import threading
import time


#Class comprenant toutes les fonctiosn necessaire au bon déroulement du jeu
class ApplicationNv1(ApplicationBase):
    def __init__(self,unite, x, y,score,fenetre_P,canvas_profil):
        self.fenetre_P = fenetre_P
        self.canvas_profil = canvas_profil
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
        self.Niveau1(10, 300,  125)
        self.root.mainloop()
    
    #Fonction reprenant la creation de tout les rectangles necessaire au niveau
    def Niveau1(self,unite, x, y):
        
        #Rectangles du "jeu" a proprement parlé
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

        #Rectangles (invisible) se trouvant sur le cote de la grille afin de bloquer les rectangles a l'interieur de celle ci
        self.ext1 = self.canvas.create_rectangle(x+(-0.3*unite),y+(-100.4*unite),x+(29.9*unite),y+(-0.01*unite), outline="")
        self.ext2 = self.canvas.create_rectangle(x+(-100.4*unite),y+(-0.3*unite),x+(-0.01*unite),y+(29.9*unite), outline="")
        self.ext3 = self.canvas.create_rectangle(x+(-0.3*unite),y+(29.61*unite),x+(29.9*unite),y+(130*unite), outline="")
        self.ext4 = self.canvas.create_rectangle(x+(29.61*unite),y+(14.7*unite),x+(130*unite),y+(29.9*unite), outline="")
        self.ext5 = self.canvas.create_rectangle(x+(29.61*unite),y+(-0.3*unite),x+(130*unite),y+(9.9*unite), outline="")
        
        #Permet de "grouper" nos differents objets
        self.rectH = [self.v1,self.v2,self.v3,self.carreRouge,self.c2,self.v6,self.v7,self.v8]
        self.rectV = [self.c1,self.v4,self.v5,self.c3]
        self.bloq =  [self.ext1,self.ext2,self.ext3,self.ext4,self.ext5]
        self.rectAll = self.rectH + self.rectV +self.bloq
            
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
        ApplicationNv2(10, 300,  125,score,self.fenetre_P,self.canvas_profil)   
    