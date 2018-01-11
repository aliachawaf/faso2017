from grove.grovepi import *
from time import sleep
from LED.FoncLED import *
from buzzer.Foncbuzzer import *
from light.Fonclight import *
from move.FoncMove import *
from music.Foncmusic import *
import random
import pygame


musique = "etoile.mp3" #la chanson qui va jouer

#les Leds sont trouves a D4, D3, D2
#buzzer sur D7
#motion sensor sur D8
#light sensor sur A1
led1 = 4
led2 = 3
led3 = 2 
leds = [led1,led2, led3]
buzzer = 7
pir = 8
light = 1

fileLight = "/home/pi/Lampe/light.txt"
fileMove = "/home/pi/Lampe/move.txt"

variable = 200 #le seuil qui decide si on allume les leds 
music = False #pour savoir si la musique joue ou non
mlist = [] #la liste avec les donnees du mouvement
lightlist =[] #la liste avec les donnes de la lumiere
nb =0 #un compteur pour le mouvement

#La lampe commence a fonctionner
turnon(buzzer)
sleep(0.2)
turnoff(buzzer)
print "La lampe commence a fonctioner" 
while True:
        i = random.randint(0,2)
        l = leds[i]
        try:
		sensor = startLight(light) #appel la fonction startLight qui renvoie la donnee d'environnement
		print "valeur de capteur =" + str(sensor)
                with open(fileLight, 'r') as f: #ouvrir le fichier pour la lumiere
                	for line in f:
                        	line = line.strip()
                                lightlist.append(line)
 
                lightlist.append(str(sensor)) #ajout la nouvelle donnee a la liste

                with open(fileLight,'w') as fhandler: #ouvrir le fichier pour ecrire la liste dans le fichier
                	for item in lightlist:
                		fhandler.write("{}\n".format(item)) #ecrire la liste dans le fichier

		if (int(lightlist[len(lightlist)-1]) < variable): #verifier si la lumiere est plus ou moins que le seuil
			turnon(l) 
			changer(l)
			print ("led est: " + str(l))
			move = startMove(pir) #appel la fonction startMove qui renvoie la donnee d'environnement 
			if move==1:
				print "motion"
				if not(music): #commencer la musique 
					startMusic(musique)
					setVolume()
					music=True
			else:
				print "pas motion"

			with open(fileMove, 'r') as file: #ouvrir le fichier pour le mouvement
				for line in file:
					line = line.strip()
					mlist.append(line)
			mlist.append(str(move)) #ajout la nouvelle donnee a la liste

			if len(mlist)>5: #calculer si il n'y a pas du mouvement
				for i in range(len(mlist)-5,len(mlist)-1):
					if mlist[i]==str(0):
						nb=nb+1
			if nb == 4: #s'il n'y a pas du mouvement on arrete la musique
				stopMusic()
				music=False
				print "music stop"

			nb=0
			with open(fileMove, 'w') as file_handler: #ouvrir le fichier pour ecrire la liste dans le fichier
    				for item in mlist:
        				file_handler.write("{}\n".format(item))
		else:
			print "pas led" #sinon on n'allume pas les leds
			turnoff(l)
			stopMusic()
			music=False

		sleep(1) #on attend jusqu'a on commence de nouveau
		turnoff(l)
		mlist = []
		lightlist = []

        except KeyboardInterrupt:
		turnoff(l)
		stopMusic()
		turnon(buzzer)
		print "buzzer on"
		sleep(0.2)
		turnoff(buzzer)
		print "buzzer off"
		break

        except IOError as e:
                print "Erreur capteur"
		print e
		break

