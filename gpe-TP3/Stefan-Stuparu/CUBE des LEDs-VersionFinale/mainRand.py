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
		#deg =Angle()
		if etat  == 0:
			print("Le programme n'a pas recu une commande de demarrage!")
		else:
			deg = Angle()
			while deg>=50:
				if deg<100:
					print ("OFF")
					time.sleep(1)
					break
				deg=Angle()
				if deg<200:
					print("Votre mode est MANUEL.")
					Music(5)
                       			arduinoString(20)
                       			lumiere()
					print("Il marche!")
				deg=Angle()
				if deg>=205:
					print("Votre mode est Random")
					Music2(5)
					lumiereRand()
				deg=Angle()
	except KeyboardInterrupt:
        	print("FIN d'enregistrement")

main()


