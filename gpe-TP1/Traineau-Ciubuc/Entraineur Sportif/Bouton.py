
#!/usr/bin/env python
#-*- coding: utf-8 -*-

#import grove.grovepi *

import time 
from grovepi import *
from Affichage import *

button =3 #Bouton sur le port D3
pinMode(button, "INPUT")

def Bouton(continu):
        #
	#Fonction chronometrant le nombre de secondes pendant 
	#lesquelles le bouton a ete appuye
        #Prennd un parametre un bool qui dit continue ou pas
        #True la fonction sortira directement du while
        while True:
                temps = 0
                if digitalRead(button) == 1 :
                        while digitalRead(button) == 1 :
                                time.sleep(1)
                                temps = temps + 1
                                if temps < 3 :
                                        Affichage("Passer, appui : " + str(temps) + "sec")
                                if temps >= 3 and temps < 7 :
                                        Affichage("Reprendre mesures, appui : " + str(temps) + "sec")
                                if temps >= 7 :
                                        Affichage("Fin entrainement appui : " + str(temps) + "sec")
                        return temps #va tourner en continue
                
                if continu :
                        return temps


#print(Bouton())

def Intervalle(entier,min,max) :
	#renvoie true si le nombre donne en parametre est 
	#compris entre min et max 
	return (entier>=min and entier<=max)

def BoutonInteract(continu):
	#retourne 0 si l'utilisateur appui moins de 2 secondes
	# 1 si entre 3 et 5 et 2 si au dessus de 5
	temps = Bouton(continu)
	if Intervalle(temps,0.1,3):
		#Avance dans l'entrainement
		return 0
	elif Intervalle(temps,3,7):
		#Reprend les mesures
		return 1
	elif Intervalle(temps,7,40):
		#Fin entrainement
		return 2
	else :
		return 3


