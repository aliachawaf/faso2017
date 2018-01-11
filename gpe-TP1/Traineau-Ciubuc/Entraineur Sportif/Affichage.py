#!/usr/bin/env python
#-*- coding: utf-8 -*-

from grove_rgb_lcd import *
import time

#if __name__== '__main__'

def Affichage(phrase):
	#Affiche la phrase passée en paramètre
        
	setText(phrase)
	return 0

def AffichagePompe():
	#Affiche pompe à l'écran
	Affichage("pompe")
	return 0

def AffichageGainage():
	#Affiche Gainage à l'écran
	Affichage("Gainage")
	return 0

def AffichageDebut():
	#Affiche Debut entraînement à l'écran
	Affichage("Debut entraînement")
	return 0

def AffichagePause():
	#Affiche pause à l'écran
	Affichage("pause")
	return 0



def AffichageFinPause():
	#Affiche un text pour la fin de pause
	setText_norefresh("Il est temps de faire une nouvelle serie")
	return 0


def AffichageMesurePompe():
    Affichage("Vous allez prendre vos mesures ")
    time.sleep(3)
    Affichage("Placez-vous en position pompes ")
    time.sleep(3)
    Affichage("bras tendus au dessus du capteur de distance")
    time.sleep(4)
    Affichage("prise de mesure dans 5 secondes")
    time.sleep(5)
    return 0

def AffichageMesureGainage():
	Affichage(" Mettez vous en position gainage ")
	time.sleep(3)
	Affichage("Coudes au sol bras tendues")
	time.sleep(3)
	Affichage("prise de mesure ")
	time.sleep(3)
	Affichage("dans 5 secondes ")
	time.sleep(5)
	return 0

def AffichageMesureFin():
	Affichage("Garder les mesures ? ")
	time.sleep(3)
	Affichage("Appuyer sur le bouton ")
	time.sleep(3)
	Affichage("moins de 3 sec")
	time.sleep(3)
	Affichage("Plus si vous voulez refaire ")
	return 0
