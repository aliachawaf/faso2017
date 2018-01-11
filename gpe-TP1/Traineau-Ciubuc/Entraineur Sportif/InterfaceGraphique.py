#!/usr/bin/env python
# -*- coding: utf-8 -*-

from Entrainements import *
from tkinter import *
from Statistiques import *


#Exemple de code tkinter : 
class Interface(Frame):
    
    """Notre fenêtre principale.
    Tous les widgets sont stockés comme attributs de cette fenêtre."""
    
    def __init__(self, fenetre, **kwargs):
        Frame.__init__(self, fenetre, width=768, height=576, **kwargs)
        self.pack(fill=BOTH)
        
        canvas = Canvas(fenetre, width=550, height=620, background='grey')
        # Création de nos widgets
        label = Label(fenetre, text="Bienvenue sur votre entraineur sportif !")
        label.pack()
        self.message = Label(self, text="Il est l'heure de se reprendre en main !")
        self.message.pack()
        
        #self.bouton_quitter = Button(self, text="Quitter", command=self.quit)
        #elf.bouton_quitter.pack(side="left")
        
        self.bouton_manuel = Button(self, text="Manuel D'utilisation", fg="green",
                command=self.Manuel)
        self.bouton_manuel.pack(padx=10, pady = 10)

        self.bouton_descriptif = Button(self, text="Descriptif des entrainements", fg="green",
                command=self.Descriptif)
        self.bouton_descriptif.pack(padx=10, pady = 10)

        self.bouton_entrainement1 = Button(self, text="Demo", fg="green",
                command=self.entrainement1)
        self.bouton_entrainement1.pack(padx=10, pady = 10)

        self.bouton_entrainement2 = Button(self, text="Brindille ", fg="green",
                command=self.entrainement2)
        self.bouton_entrainement2.pack(padx=10, pady = 10)

        self.bouton_entrainement3 = Button(self, text="Road to Spartan", fg="red",
                command=self.entrainement3)
        self.bouton_entrainement3.pack(padx=15, pady = 10)

    
    def Manuel(self):
        
        fen = Toplevel(fenetre, width = "200")
        with open('manuel.txt','r') as f:
             txt=f.read()
        texte=Label(fen, text=txt)
        texte.pack()
        return 0
    
    def Descriptif(self):
        fen = Toplevel(fenetre, width = "200")
        with open('DescriptifEntrainement.txt','r') as f:
             txt=f.read()
        texte=Label(fen, text=txt)
        texte.pack()
        return 0
        
    def entrainement1(self):
        
        
        en = entrainement1()
        AffStatistiques(en)
        return 0

    def entrainement2(self):
        
        
        en = entrainement2()
        AffStatistiques(en)
        return 0

    def entrainement3(self):
        
        
        en = entrainement3()
        AffStatistiques(en)
        return 0
        


fenetre = Tk()
interface = Interface(fenetre)

interface.mainloop()
interface.destroy()







