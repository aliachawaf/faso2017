from Sys.incercare import *
from Button.button import *
from Lumiere.LEDbyFR import *
from Sound.sunet import *
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
		deg = getAngle()
		if deg<150:
			print(deg)
			if etat  == 0:
				print("Le programme n'a pas recu une commande de demarrage!")
			else :
				Music(5)
                        	arduinoString(10)
                        	lumiere()
				print("Il marche!")
		else:
			print("Auto")
	except KeyboardInterrupt:
        	print("FIN d'enregistrement")

main()


