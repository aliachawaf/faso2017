from  grove.grovepi import *


def startMove(pir):
	pinMode(pir, "INPUT")
	motion = digitalRead(pir) #detecter un mouvement
	if motion == 0 or motion == 1:
		if motion ==1:
			return 1 # s'il y a un mouvement
		else:
			return 0
