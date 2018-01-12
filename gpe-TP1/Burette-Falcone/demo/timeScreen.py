import time
from grove_rgb_lcd import *
setRGB(255,255,255)
from datetime import datetime


def timeScreen(h, m, hReveil, mReveil):

	try:
		now = str(datetime.utcnow().time())
		heure,min,sec = now.split(":")
		heure = int(heure) + 1
		heure = str(heure)
		if not(h == heure) or not(m == min):
			if hReveil == "OFF":
				setText(heure + ":" + min + "\nReveil : " + str(hReveil) )
				h = heure
				m = min

			elif mReveil < 10:
				setText(heure + ":" + min + "\nReveil : " + str(hReveil) + ":0" + str(mReveil) )
				h = heure
				m = min
			else:
				setText(heure + ":" + min + "\nReveil : " + str(hReveil) + ":" + str(mReveil) )
				h = heure
				m = min

	except IOError:
		print( "erreur" )

	return [heure,min]
