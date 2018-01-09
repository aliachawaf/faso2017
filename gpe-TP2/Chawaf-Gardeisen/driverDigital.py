#coding: utf-8

import time
from grovepi import*
import datetime


def Detection_Courrier():
#renvoie True si le capteur de mouvement détecte un mouvement (depot de courrier), False sinon

	motion_sensor = 3	#capteur relié sur le port digital 3

	pinMode(motion_sensor,"INPUT")	#le capteur de mouvement est une entrée

	if digitalRead(motion_sensor)==1 :
		return True

	else:
		return False


def Etat_Bouton():
#renvoie l'état actuel du bouton (1 si on appuie, 0 sinon)

	bouton = 2 #le bouton relié au port digital 2 (D2)

	etat_bouton = digitalRead(bouton) #pour lire l'état actuel du bouton

	pinMode(bouton,"INPUT") #on déclare le bouton comme entrée

	return etat_bouton #on retourne l'état actuel du bouton (0 ou 1)


