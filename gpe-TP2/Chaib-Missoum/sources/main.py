# coding: utf-8

from led import *
import grovepi
from music import *
import time
import random

# Initialisation des ports

pir_sensor = 8
ledr = 5
ledv = 6

# Initialisation de la playlist

playlist = ["un.mp3", "deux.mp3", "trois.mp3", "quatre.mp3", "cinq.mp3"]
indice = 0
init()

# Initialisation des capteurs

grovepi.pinMode(pir_sensor,"INPUT")
grovepi.pinMode(ledv,"OUTPUT")
grovepi.pinMode(ledr,"OUTPUT")

# Initialisation des variables

indice = random.randrange(5)
load("/home/walines/home/scripts/grovepi/Musique/"+playlist[indice])
play(1)
print("Play !")

# Extinction des LED allumés

eteint_led(ledv)
eteint_led(ledr)

# Allumage de la LED correspondante à Play

allume_led(ledv)

# Début de la lecture

while True:
	try :
		UnMvt = False
		DeuxMvt = False
		TroisMvt = False
		Depause = False

		if not(busy()):
			indice = suivant(playlist,indice)
			print("Passage au morceau suivant automatique !")

		time.sleep(1)

		if grovepi.digitalRead(pir_sensor): # Détection d'un mouvement
			UnMvt = True
			time.sleep(1.6)
			print("Faîtes un deuxième mouvement pour passer au morceau suivant !")
			for k in range(1,11) :
				time.sleep(0.1)
				print("Tentative " + str(k) + "/10")
				if grovepi.digitalRead(pir_sensor): # Détection d'un deuxième mouvement
					DeuxMvt = True
					UnMvt = False
					break

			if DeuxMvt :
				time.sleep(2)
				print("Faîtes un troisième mouvement pour passer au morceau suivant !")
				for j in range(1,11) :
					time.sleep(0.1)
					print("Tentative " + str(j) + "/10")
					if grovepi.digitalRead(pir_sensor) : # Détection d'un troisième mouvement
						TroisMvt = True
						DeuxMvt = False
						break
			if TroisMvt :
				indice = precedent(playlist,indice) # je passe au morceau suivant
				print("Passage au morceau précédent par détection de gestes !")
			elif DeuxMvt :
				indice = suivant(playlist,indice)
				print("Passage au morceau suivant par détection de gestes !")
			elif UnMvt :
				allume_led(ledr)
				eteint_led(ledv)
                		pause()
				print("Pause !")
				while not(Depause):
					time.sleep(2)
				#Tant que je n'ai pas "dépausé" le morceau
					if grovepi.digitalRead(pir_sensor):
						eteint_led(ledr)
                				allume_led(ledv)
                				unpause()
						print("Depause !")
						Depause = True
	except KeyboardInterrupt: # Extinction des LED avant la fin du programme
        	eteint_led(ledr)
		eteint_led(ledv)
        	break
