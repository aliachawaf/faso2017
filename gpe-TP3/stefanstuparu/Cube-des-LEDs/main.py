from Sys.incercare import *
from Button.button import *
from Lumiere.LEDbyFR import *
from Sound.sunet import *
import pygame
import time
from grovepi import *



def main():
	etat = 0
        try:
		print("Astept apasarea butonului")
		time.sleep(2)
		etat= Work(etat)
		print("Incepeeeeee")
		if etat  == 0:
			print("Nu mergeeeeeee")
		else :
			Music(5)
                        arduinoString(10)
                        lumiere()
			print("mergeeeeeee")
	except KeyboardInterrupt:
        	print("FIN inregistrare")

main()


