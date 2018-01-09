from grove.grovepi import *
from time import sleep
from LED.FoncLED import *
from buzzer.Foncbuzzer import *
from light.Fonclight import *
from move.FoncMove import *
from music.Foncmusic import *
import random
import pygame

#rc.local pour commencer quand on branche le raspberry a l'electricite

#pygame.mixer.init()
#pygame.mixer.music.load("song.mp3")
musique = "song.mp3"

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


variable = 200
#f = open ("light.txt", 'w')
music = False
mlist = []
lightlist =[]
nb =0
while True:
        i = random.randint(0,2)
        l = leds[i]
        try:
		sensor = startLight(light)
		print(sensor)
                with open("light.txt") as f:
                	for line in f:
                        	line = line.strip()
                                lightlist.append(line)
                lightlist.append(str(sensor))
                with open("light.txt", 'w') as fhandler:
                	for item in lightlist:
                		fhandler.write("{}\n".format(item))
		if (int(lightlist[len(lightlist)-1]) < variable):
			turnon(l)
			changer(l)
			print ("led est: " + str(l))
			move = startMove(pir)
			if move==1:
				print "motion"
				#commencer la musique
				if not(music):
					startMusic(musique)
					setVolume()
					music=True
			
			#else:
			#	print "pas de motion"
			#	pygame.mixer.music.stop()
			#	music=False
				#arreter la musique, mais quand? une liste pour sauvegarder les donnees et les comparer
			with open("move.txt") as file:
				for line in file:
					line = line.strip()
					mlist.append(line)
			mlist.append(str(move))
#			print mlist
			if len(mlist)>5:
				for i in range(len(mlist)-5,len(mlist)-1):
					print "in loop"
					if mlist[i]==str(0):
						print "0"
						nb=nb+1
			if nb == 4:
				#pygame.mixer.music.stop()
				stopMusic()
				music=False
				print "music stop"
			nb=0
			with open("move.txt", 'w') as file_handler:
    				for item in mlist:
        				file_handler.write("{}\n".format(item))
		else:
			print "pas led"
			turnoff(l)
			pygame.mixer.music.stop()
                        music=False
                        print "music stop quand pas de led"
		sleep(3)
		turnoff(l)
		mlist = []
		lightlist = []
        except KeyboardInterrupt:
		turnoff(l)
		#turnon(buzzer)
		print "buzzer on"
		sleep(0.2)
		#turnoff(buzzer)
		print "buzzer off"
		break
        except IOError:
                print "Erreur capteur"

