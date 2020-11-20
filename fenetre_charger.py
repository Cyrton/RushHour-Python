# -*- coding: utf-8 -*-
"""
Created on Sun May 07 11:11:12 2017

@author: marti
"""
from tkinter import *
from PIL import Image

#Fonction de la fenêtre Charger
def Fenetre_Charger(fenetre_P, Fenetre_Principale,canvas_general):
    
    canvas_general.destroy()
    print("Fenetre_Classement")

    
    #Mise en page (Fenêtre, Titre, Texte, Boutons)
    canvas_classement = Canvas(fenetre_P,width=900, height=800,bg='sky blue')
    canvas_classement.pack(side=TOP, fill=BOTH, expand=YES)
    fenetre_P['bg']='sky blue'
    fenetre_P.geometry("900x800")
    fenetre_P.title('UNBLOCK THE BLOCK')

    label = Label(canvas_classement, text="Classement",bg = 'sky blue',font="Arial 16 underline ")
    label.pack(padx=0,pady=50)

    """
    #Tentative de recupération de liste du fichier sauvegardes.txt
    try:
        f = open('sauvegardes.txt','r')
        li = []
        for i in range(nombreSauvegarde):
            li.append(load(f))
            print (li)
        f.close()
        varY = 200
        a = 0
        for j in li:
            loadS = [LoadSauvegarde1,LoadSauvegarde2,LoadSauvegarde3]
            deleteS = [DeleteSauvegarde1,DeleteSauvegarde2,DeleteSauvegarde3]           
            sauvegardeJ=j[0]+" / "+" Niv: "+str(j[1])+" / "+str(j[2])+" points"
            bSave = Button(fenetre_C, text=sauvegardeJ,command=loadS[a],fg ='black',bg = '#FEA347',activebackground='grey',font="Arial 11 bold ",width =35, height = 2)
            bDelete = Button(fenetre_C, text="Supprimer \nla Sauvegarde",command=deleteS[a],fg ='red',bg = '#FEA347',activebackground='grey',font="Arial 11 bold ",width =35, height = 2)
            bSave.place(anchor=CENTER, x=250, y=varY)
            bDelete.place(anchor=CENTER, x=650, y=varY)
            varY += 100
            a += 1
    except:
        pass
    """
    bRetour = Button(canvas_classement, text="RETOUR AU MENU", command=lambda :Fenetre_Principale(fenetre_P,NONE,canvas_classement),fg ='black',bg = '#FD4141',activebackground='#F96E6E',font="Arial 11 bold ",width =35, height = 1)
    bRetour.place(anchor=CENTER, x=450, y=600)
    #bRetour.pack(padx=0,pady=15)
    fenetre_P.mainloop()