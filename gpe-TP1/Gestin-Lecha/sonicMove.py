#coding: utf-8
import time
from grovepi import *
from pynput.keyboard import Key, Controller

gauche = 4
droite = 7
haut   = 8
bas    = 3

k = Controller()

while True:
	try:	
		distanceG = ultrasonicRead(gauche)
		distanceD = ultrasonicRead(droite)
		distanceH = ultrasonicRead(haut)
		distanceB = ultrasonicRead(bas)
				
		if distanceG < 30:
			tmp = 0
			while tmp < 10:
				try:
					distanceD = ultrasonicRead(droite)
					
					if distanceD < 30:
						print("mouvement gauche droite")
						k.press("d")
						k.release('d')
						tmp = 10
						time.sleep(1)
				except TypeError:
					print("TypeError")
				except IOError:
					print("IOError")	
				tmp +=1
				time.sleep(0.1)
		elif distanceD < 30:
			tmp = 0
			while tmp < 10:
				try:
					distanceG = ultrasonicRead(gauche)
					
					if distanceG < 30:
						print("mouvement droite gauche")
						k.press('g')
						k.release('g')
						tmp = 10
						time.sleep(1)
				except TypeError:
					print("TypeError")
				except IOError:
					print("IOError")
				tmp +=1
				time.sleep(0.1)
		elif distanceH < 30:
			tmp = 0
			while tmp < 20:
				try:
					distanceB = ultrasonicRead(bas)
					
					if distanceB < 30:
						print("mouvement haut bas")
						k.press(Key.page_down)
						k.release(Key.page_down)
						tmp = 10
						time.sleep(1)
				except TypeError:
					print("TypeError")
				except IOError:
					print("IOError")
				tmp +=1
				time.sleep(0.1)

		elif distanceB < 30:
			tmp = 0
			while tmp < 20:
				try:
					distanceH = ultrasonicRead(haut)
					
					if distanceH < 30:
						print("mouvement bas haut")
						k.press(Key.page_up)
						k.release(Key.page_up)
						tmp = 10
						time.sleep(1)
				except TypeError:
					print("TypeError")
				except IOError:
					print("IOError")
				tmp +=1
				time.sleep(0.1)
	except TypeError:
		print("error Error ")
	except IOError:
		print("error io")
	time.sleep(0.05)
