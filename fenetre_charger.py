# -*- coding: utf-8 -*-
"""
Created on Sun May 07 11:11:12 2017

@author: marti
"""
from tkinter import *
from PIL import Image
import pandas as pd
import json

#Fonction de la fenêtre Charger
def Fenetre_Charger(fenetre_P, Fenetre_Principale,canvas_general):
    
    canvas_general.destroy()
    print("Fenetre_Classement")

     #Partie pour récuperer les données du fichier json sauvegarde
    #dict_pandas = {joueur, score, niveau}
    data = pd.read_json ('sauvegarde.json')
    for Joueurs in data:
        
    data.sort_values("Niveau1")
    data["Rank"] = data["Niveau1"].rank() 
    print (data)
    with open('sauvegarde.json') as json_data_r:
        data_dict = json.load(json_data_r)


    #Mise en page (Fenêtre, Titre, Texte, Boutons)
    canvas_classement = Canvas(fenetre_P,width=900, height=800,bg='sky blue')
    canvas_classement.pack(side=TOP, fill=BOTH, expand=YES)
    fenetre_P['bg']='sky blue'
    fenetre_P.geometry("900x800")
    fenetre_P.title('UNBLOCK THE BLOCK')

    label = Label(canvas_classement, text="Classement",bg = 'sky blue',font="Arial 16 underline ")
    label.pack(padx=0,pady=50)

    #mise en page des colonnes pour les classements
    labelNiveau1 = Label(canvas_classement, text=data, bg='sky blue', font = "Arial 13 underline")
    labelNiveau2 = Label(canvas_classement, text="Niveau 2", bg='sky blue', font = "Arial 13 underline")
    labelNiveau3 = Label(canvas_classement, text="Niveau 3", bg='sky blue', font = "Arial 13 underline")
    
    labelNiveau1.place(anchor=CENTER, x=150, y=150)
    labelNiveau2.place(anchor=CENTER, x=450, y=150)
    labelNiveau3.place(anchor=CENTER, x=750, y=150)

    bRetour = Button(canvas_classement, text="RETOUR AU MENU", command=lambda :Fenetre_Principale(fenetre_P,NONE,canvas_classement),fg ='black',bg = '#FD4141',activebackground='#F96E6E',font="Arial 11 bold ",width =35, height = 1)
    bRetour.place(anchor=CENTER, x=450, y=600)
    fenetre_P.mainloop()