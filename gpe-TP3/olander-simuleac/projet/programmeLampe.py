from grove.grovepi import *
from time import sleep
from LED.FoncLED import *
from buzzer.Foncbuzzer import *
from light.Fonclight import *
from move.FoncMove import *
from music.Foncmusic import *
import random
import pygame

print "is it here?"

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
music = False
mlist = []
lightlist =[]
nb =0
while True:
        i = random.randint(0,2)
        l = leds[i]
	print "you are in while?"
        try:
		sensor = startLight(light)
		print "valeur de capteur =" + str(sensor)
                with open("light.txt") as f:
                	for line in f:
                        	line = line.strip()
                                lightlist.append(line)
		print "how about the file?"
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

			with open("move.txt") as file:
				for line in file:
					line = line.strip()
					mlist.append(line)
			mlist.append(str(move))
			if len(mlist)>5:
				for i in range(len(mlist)-5,len(mlist)-1):
					if mlist[i]==str(0):
						nb=nb+1
			if nb == 4:
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
			stopMusic()
			music=False
                        print "music stop quand pas de led"
		sleep(1)
		turnoff(l)
		mlist = []
		lightlist = []
        except KeyboardInterrupt:
		turnoff(l)
		turnon(buzzer)
		print "buzzer on"
		sleep(0.2)
		turnoff(buzzer)
		print "buzzer off"
		break
        except IOError:
                print "Erreur capteur"
		break

