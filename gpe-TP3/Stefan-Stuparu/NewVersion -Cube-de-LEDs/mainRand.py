from Sys.incercare import *
from Button.button import *
from Lumiere.LEDbyFR import *
from Sound.sunet import *
from LumRand.LedRand import * 
from switch.switch import *
import pygame
import time
from grovepi import *



def main():
	etat = 0
	try:
		print("Appuyez le bouton!")
		time.sleep(2)
		etat= Work(etat)
		print("Demarrage.")
		time.sleep(2)
		print("Choisi votre mode")
		#deg = getAngle()
		if etat  == 0:
			print("Le programme n'a pas recu une commande de demarrage!")
		else:
			deg = getAngle()
			while deg>=50:
				if deg<100:
					print ("OFF")
					break
				deg=getAngle()
				if deg<200:
					print("Votre mode est MANUEL.")
					Music(5)
                       			arduinoString(20)
                       			lumiere()
					print("Il marche!")
				deg=getAngle()
				if deg>=205:
					print("Votre mode est Random")
					Music2(5)
					lumiereRand()
				deg=getAngle()
	except KeyboardInterrupt:
        	print("FIN d'enregistrement")

main()


