import grovepi
import time
from grove_rgb_lcd import *

def configReveil(button, button2, timeMax):

	min = 0
	heure = 0
	timer = 0
	end = True

	while end:
		try:
			time.sleep(0.2)				#si l utilisateur  ne regle pas pendant plus de 10 sec le programme s arrete
			timer = timer + 0.2
			if timer > timeMax:
				end = False

			if grovepi.digitalRead(button) == 1:
				timer = 0
				if heure  == 23:
					heure = -1
				heure = heure + 1

				if min < 10:
					setText("Votre reveil : \n" + str(heure) + ":0" + str(min) )
				else:
					setText("Votre reveil : \n" + str(heure) + ":" + str(min) )

			if grovepi.digitalRead(button2) == 1:
				timer = 0
				if min == 59:
					min = -1
				min = min + 1

				if min < 10:
					setText("Votre reveil : \n" + str(heure) + ":0" + str(min) )
				else:
					setText("Votre reveil : \n" + str(heure) + ":" + str(min) )

		except IOError:
			print( "erreur" )

	if min < 10:
		reveil = str(heure) + ":0" + str(min)
	else:
		reveil = str(heure) + ":" + str(min)
	return [heure,min]
