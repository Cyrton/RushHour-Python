# -*- coding: utf-8 -*-
"""
Created on Sun May 07 11:11:12 2017

@author: marti
"""
from tkinter import *
from PIL import Image
from niveau_1 import *
from niveau_2 import *
from niveau_3 import *
import json

def supprimer_sauvegarde(li_sauvegarde,pseudo,data_dict):
    b = 0
    for y in li_sauvegarde:
        print(b)
        del li_sauvegarde[b]
        b += 1
    data_dict[pseudo]["historique"] = li_sauvegarde

    with open('sauvegarde.json','w') as json_data_w:
        json.dump(data_dict,json_data_w)



def chargement(pseudo,canvas_profil,fenetre_P,score):
    #Partie pour récuperer les données du fichier json sauvegarde
    with open('sauvegarde.json') as json_data_r:
        data_dict = json.load(json_data_r)

    Frame1 = Frame(canvas_profil,width=900, height=550, bg="sky blue")
    Frame1.pack(padx=0,pady=0) #mettre une scroobar

    a = 0
    varY = 100

    for x in data_dict:
        if x == pseudo:
            for y in data_dict[x]["historique"]:
                
                li_sauvegarde = data_dict[x]["historique"]

                if data_dict[x]["historique"][a] == 1:
                    niveau = lambda: ApplicationNv1(10, 300,  125,score,fenetre_P,canvas_profil,pseudo)
                elif data_dict[x]["historique"][a] == 2:
                    niveau = lambda: ApplicationNv2(10, 300,  125,score,fenetre_P,canvas_profil,pseudo)
                else:
                    niveau = lambda: ApplicationNv3(10, 300,  125,score,fenetre_P,canvas_profil,pseudo)

                sauvegardeJ= "Niveau: "+str(data_dict[x]["historique"][a])
                bSave = Button(Frame1, text=sauvegardeJ,command=  niveau,fg ='black',bg = '#FEA347',activebackground='grey',font="Arial 11 bold ",width =35, height = 2)
                bDelete = Button(Frame1, text="Supprimer \nla Sauvegarde",command= lambda: supprimer_sauvegarde(li_sauvegarde,pseudo,data_dict),fg ='red',bg = '#FEA347',activebackground='grey',font="Arial 11 bold ",width =35, height = 2)

                bSave.place(anchor=CENTER, x=250, y=varY)
                bDelete.place(anchor=CENTER, x=650, y=varY)
                varY += 100
                a += 1

#Fonction de la fenêtre Jouer
def Fenetre_profil(canvas_jouer,fenetre_P,Fenetre_Jouer,pseudo):
    print("Fenetre_profil")
    
    canvas_jouer.destroy()
    canvas_profil = Canvas(fenetre_P,width=900, height=800,bg='sky blue')
    canvas_profil.pack(side=TOP, fill=BOTH, expand=YES)
    
    #Mise en page (Fenêtre, Titre, Texte, Entrée Texte, Boutons)
    fenetre_P['bg']='sky blue'
    fenetre_P.geometry("900x800")
    fenetre_P.title('UNBLOCK THE BLOCK')

    label1 = Label(canvas_profil, text="Profil de {0}".format(pseudo),bg = 'sky blue',font="Arial 16 underline ")
    label1.pack(padx=0,pady=35)

    boutonGO = Button(canvas_profil, text="Jouer", command= lambda: ApplicationNv1(10, 300,  125,score,fenetre_P,canvas_profil,pseudo),fg ='black',bg = '#66EC62',activebackground='light green',font="Arial 11 bold",width =35, height = 1)
    boutonGO.pack(padx=0,pady=15)

    bRetour = Button(canvas_profil, text="RETOUR AU MENU", command=lambda :Fenetre_Jouer(fenetre_P,Fenetre_Jouer,NONE),fg ='black',bg = '#FD4141',activebackground='#F96E6E',font="Arial 11 bold ",width =35, height = 1)
    bRetour.pack(padx=0,pady=15)

    label2 = Label(canvas_profil, text="Sauvegarde",bg = 'sky blue',font="Arial 16 underline ")
    label2.pack(padx=0,pady=0)

    chargement(pseudo,canvas_profil,fenetre_P,score)
    fenetre_P.mainloop()

