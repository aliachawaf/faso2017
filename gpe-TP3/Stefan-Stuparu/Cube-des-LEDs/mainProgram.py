from Sys.incercare import *
from Button.button import *
from Lumiere.LEDbyFR import * 
from Sound.sunet import *
import pygame
import time

def main():
	try:
		Music(5)
		arduinoString(5)
		lumiere()
	except KeyboardInterrupt:
		print("FIN inregistrare")

main()
