#!/usr/bin/env python
#-*- coding: utf-8 -*-
import RPi.GPIO as GPIO         # Importation des librairies qui gerent les ports
# Importation de la librairie temps
from grovepi import *
from grove_rgb_lcd import *
import os
from enregistrement import *
import time

print("Mise à jour de la date...")
os.system('sh maj.sh') #MAJ de la date

bouton = 2   #Port du bouton
test = True

#print("Etat du bouton au début : " + str(digitalRead(bouton)))

while test:        #boucle infinie
	button_status= digitalRead(bouton)    #On lit l'état du bouton (appuyé ou non)
#	print("Ca doit être toujours 0 avant appui : " + str(button_status))
	if button_status:    #Si le bouton a été appuyé
		repertoire=time.strftime("%Y-%m-%d-%H-%M") #Récupération du nom du dossier
		nom = "photo-"+time.strftime("%Y-%m-%d-%H-%M")+".jpg" #Récupération du nom de la photo
#		print(nom)

		setText("Prise de la\nphoto") #Affichage d'un message à l'écran
		setRGB(150,150,150) #Fond d'écran blanc

		#Prendre la photo, l'enregistrer et afficher un message su l'écran
        	os.system('sh photo.sh '+ nom + ' ' + repertoire)    #Récupération du script correspondant

		setText("Appuyer pour\nlaisser message") #Affichage d'un message à l'écran
		time.sleep(1) # Delai de 1 seconde pour prevenir plusieurs appuis rapides et pour que la valeur de button_status repasse à 0
	
        	timeout = time.time() + 5    #on créé une valeur de temps avant la fin de la boucle

        	while test and time.time() < timeout:        #boucle infinie pendant 5s
           		button_status= digitalRead(bouton)    #On lit l'état du bouton
#			print("etat du bouto au milieu : " + str(button_status))

            		if button_status:    #Si le bouton a été appuyé
#				print("Etat du bouton à la fin : " + str(button_status))
				#Enregistrement du message audio et afficher un message sur l'écran
				nom_enregistrement = "message-"+time.strftime("%Y-%m-%d-%H-%M")+".wav" #Récupération du nom de l'enregistrement
                        	#os.system('sh message.sh')    #Récupération du script correspondant
				setText("Enregistrement\nen cours") #Affichage d'un message à l'écran
				enregistrement(nom_enregistrement) #Appel de la fonction d'enregistrement du message vocal

#				setText("Appuyer pour\nfinir message") #Affichage d'un message à l'écran
#				time.sleep(1) # Delai de 1 seconde pour prevenir plusieurs appuis rapides et pour que la valeur de button_status repasse à 0
			
#				timeout = time.time() + 5    #on créé une valeur de temps avant la fin de la boucle

#				while test and time.time() < timeout:        #boucle infinie pendant 5s
#                			button_status= digitalRead(bouton)    #On lit l'état du bouton
#               			print("etat du bouto au milieu : " + str(button_status))

#               			if button_status:    #Si le bouton a été appuyé
#						setText("Photo et message\nenvoyes") #Affichage d'un message à l'écran
#						time.sleep(3) # On laisse le message affiché pendant 3 secondes avant d'éteindre l'écran et de fermer le programme
#						setText("") # Extinction de l'écran
#						setRGB(0,0,0)
#						os.system('sh uploadphotomessage.sh '+ nom) #Upload la photo et le message sur le drive
#						test = False # Le programme se termine
				if not test:
					break
				# Cas où le visiteur n'a pas rappuyé pour finir son message
#				setText("Limite du\nmessage depassee") #Affichage d'un message à l'écran
#				time.sleep(3) # On laisse le message affiché pendant 3 secondes avant de modifier le message		
				setText("Photo et message\nenvoyes") #Affichage d'un message à l'écran
				time.sleep(3) # On laisse le message affiché pendant 3 secondes avant d'éteindre l'écran et de fermer le programme
                        	setText("") # Extinction de l'écran
				setRGB(0,0,0)
				os.system('sh uploadphotomessage.sh '+ nom + ' ' + nom_enregistrement + ' ' + repertoire) #Upload la photo et le message sur le drive
				test = False # Le programme se termine
		if not test:
			break
	
		# Cas où le visiteur n'a pas rappuyé pour enregistrer un message       
		setText("Photo envoyee\nsans message") #Affichage d'un message à l'écran
		time.sleep(3) # On laisse le message affiché pendant 3 secondes avant d'éteindre l'écran et de fermer le programme
		setText("") # Extinction de l'écran
		setRGB(0,0,0)
		os.system('sh uploadphoto.sh '+ nom + ' ' + repertoire) #Upload uniquement la photo sur le drive
		test = False # Le programme se termine
