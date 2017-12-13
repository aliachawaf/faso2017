#!/usr/bin/env python
#-*- coding: utf-8 -*-

from affichage.Affichage import *
#from chrono.Chronometre import *
from exercices.Exercices import *
from TestUnit.TestUnit import *
from Bouton.Bouton import *
sensor = 1
from grove.grovepi import *
#if __name__== '__main__'

#Fonction utiles pour les entrainements :
Fin = False
def PrisesDesMesures():
	#Prend les mesures 
	AffichageMesurePompe()
	ValidationMesures = True
	while ValidationMesures == True :
		mesuresPompe = PriseDeMesure()
		AffichageMesureFin()
		ValidationMesures = DemandeUtil()
	AffichageMesureGainage()
	ValidationMesures = True
	while ValidationMesures == True :
		mesuresGainage = PriseDeMesure()
		AffichageMesureFin()
		ValidationMesures = DemandeUtil()
	return [mesuresPompe,mesuresGainage]

#test
#PrisesdesMesures()

def DemandeUtil():
	#Interprète BoutonInteract
	#renvoie False si l'util veut arrêter l'exo 
	global Fin
	appuie = BoutonInteract()
	if appuie == 1 :
		mesures = PrisesDesMesures()
		return False
	if appuie == 0 :
		return False
	if appuie == 2 :
		Fin == True
		return False
	else :
		return True

def omptePompe(maxi):
	pompes = 0
	while DemandeUtil() == True : 
			if Pompe(160,maxi):
				#si la pompe est validée
				pompes = pompes + 1
	return pompes

def ChronoGainage(BonnePosition):
	#renvoie le temps de gainage effectué jusqu'à ce que l'utilisateur
	#appuie sur le bouton pour passer
	temps = 0
	while DemandeUtil() == True : 
		temps = temps + Gainage(BonnePosition)
	return temps

def ComptePompe(DistancePompeValide):
    #renvoie la distance
    nbPompe=0
    a=temp(sensor, '1.1')
    Affichage(str(a)) 
    while True :
        try:
           	dist = ultrasonicRead(ultrasonic_ranger)
                if (dist<DistancePompeValide):
                   	digitalWrite(buzzer,1)
                        time.sleep(2)
                        nbPompe = nbPompe + 1
                        Affichage(str(nbPompe))
			digitalWrite(buzzer,0)
		else:
                    digitalWrite(buzzer,0)
                    time.sleep(2)
	except nbPompes > 10:
		digitalWrite(buzzer, 0)
		pass
	#return nbPompe
#Entrainements
#

#ComptePompe(150)
def entrainement1():
	#Procédure de l'entrainement 1
	AffichageDebut()
	mesures = PrisesDesMesures()
	global Fin
	while True  :
		AffichagePompe()
		time.sleep(1)
		pompes1 = ComptePompe(mesures[0])
		#pause()
		#Vérif si l'util veut arrêter ou pas
		if Fin :
			break
		# Fin Vérif
		gainage1 = ChronoGainage
		#pause()
		#Vérif si l'util veut arrêter ou pas
		if Fin :
			break
		# Fin Vérif

	return [pompes1, gainage1]
entrainement1()

#Main  

def main():
	fin = "n"
	while fin !="o":
		#Invariant de boucle : fin différent de o
		ask1 = 7
		while ask1 != 1 and ask1 != 0 :
			ask1 = input("Voulez vous découvrir les entraînement (1/0) ou en choisir directement un ? ")
		if ask1 == 1 :
			print("Quand vous aurez fini de consulter le guide pressez entrer")
			#AfficherGuide()
			
		
		ask2=input("Quel entrainement voulez-vous faire ? 1-3 Voir stats de cette connexion : 's' ")
		print("Lisez attentivement le manuel d'utilisation pour savoir comment se déroule un entraînement")
		if ask2 == 1:
			entrainement1()
		elif ask2 == 2 :
			entrainement2()
		elif ask2 == 3 :
			entrainement3()
		ask4=input("Voir vos statistiques ? o/n")
		if ask4 == "o":
			AffichageStat()


		fin= input ("voulez vous arrêter o/n")
		return 0

