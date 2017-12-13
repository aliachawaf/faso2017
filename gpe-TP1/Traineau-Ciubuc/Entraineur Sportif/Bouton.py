
#!/usr/bin/env python
#-*- coding: utf-8 -*-

#import grove.grovepi *

import time 
from grove.grovepi import *

button =3 #Bouton sur le port D3
pinMode(button, "INPUT")

def Bouton():
	#Fonction chronometrant le nombre de secondes pendant 
	#lesquelles le bouton a ete appuye
	while True:
		temps = 0
		if digitalRead(button) == 1 :
			while digitalRead(button) == 1 :
				time.sleep(1)
				temps = temps + 1
		 	return temps
	

#print(Bouton())

def Intervalle(entier,min,max) :
	#renvoie true si le nombre donne en parametre est 
	#compris entre min et max 
	return (entier>=min and entier<=max)

def BoutonInteract():
	#retourne 0 si l'utilisateur appui moins de 2 secondes
	# 1 si entre 3 et 5 et 2 si au dessus de 5
	temps = Bouton()
	if Intervalle(temps,0.1,2):
		#Avance dans l'entrainement
		return 0
	elif Intervalle(temps,3,5):
		#Reprend les mesures
		return 1
	elif Intervalle(temps,5,10):
		#Fin entrainement
		return 2
	else :
		return 3



def Reboot():
	#Renvoie True si le bouton a ete appuye plus de 3 secondes 
	return Bouton(3,5)

def StopEntrainement():
	#Fin de l'entrainement
	#Renvoie true lorsque l'utilisateur 
	#a appue plus de 5 secondes sur le bouton
	return Bouton(5,10)
