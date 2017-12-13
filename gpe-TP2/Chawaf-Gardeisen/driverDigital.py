#coding: utf-8

#https://github.com/DexterInd/GrovePi lien suuuuper important !!!!

import time
from grovepi import*
import datetime


def Detection_Courrier():
#retourn True s'il détecte un mouvement (courrier), False sinon

	motion_sensor = 3	#relié sur le port digital 3

	pinMode(motion_sensor,"INPUT")	#le capteur de mouvement est une entrée

	if digitalRead(motion_sensor)==1 :
		return True

	else:
		return False




def Etat_Bouton():
	bouton=2 #le bouton se trouve sur le port digital 2 (D2)
	etat_bouton=digitalRead(bouton) #pour lire l'état actuel du bouton (0 ou 1)

	pinMode(bouton,"INPUT") #on déclare le bouton comme entrée

	return etat_bouton #on retourne l'état actuel du bouton (0 ou 1)


