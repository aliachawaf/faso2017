#!/usr/bin/env python
#-*- coding: utf-8 -*-

from lcd.grove_rgb_lcd import *
import time

#if __name__== '__main__'

def Affichage(phrase):
	#Affiche la phrase passée en paramètre
	setText(phrase)
	return 0

def AffichagePompe():
	#Affiche pompe à l'écran
	setText("pompe")
	return 0

def AffichageGainage():
	#Affiche Gainage à l'écran
	setText("Gainage")
	return 0

def AffichageDebut():
	#Affiche Debut entraînement à l'écran
	setText("Debut entraînement")
	return 0

def AffichagePause():
	#Affiche pause à l'écran
	setText("pause")
	return 0

def AffichageBienvenue():
	#Affiche "Bienvenue sur votre Sport Trainer" à l'écran
	setText("Bienvenue sur votre Sport Trainer")
	return 0

def AffichageFinPause():
	#Affiche un text pour la fin de pause
	setText_norefresh("Il est temps de faire une nouvelle serie")
	return 0


def AffichageMesurePompe():
	setText("Placez-vous en position pompes ")
	time.sleep(3)
	setText("bras tendus au dessus du capteur de distance")
	time.sleep(4)
	setText("prise de mesure dans 5 secondes")
	time.sleep(5)
	return 0

def AffichageMesureGainage():
	setText(" Mettez vous en position gainage ")
	time.sleep(3)
	setText("Coudes au sol bras tendues")
	time.sleep(3)
	setText("prise de mesure dans 5 secondes")
	return 0

def AffichageMesureFin():
	setText("Garder les mesures ? ")
	time.sleep(3)
	setText("Appuyer sur le bouton moins de 5 sec")
	time.sleep(3)
	setText("Plus si vous voulez refaire ")
	return 0
