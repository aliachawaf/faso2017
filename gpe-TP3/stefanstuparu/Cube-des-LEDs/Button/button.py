import time
from grovepi import *
def Work(Marche):
	button = 2
	buttonState=0

	pinMode(button,"INPUT");
	buttonState= digitalRead(button)
	if(buttonState==1): # si le bouton est appuye
		if(Marche==0): # si le programme est OFF
			Marche=1
		else:		# le programme est ON 
			Marche=0
	return Marche
