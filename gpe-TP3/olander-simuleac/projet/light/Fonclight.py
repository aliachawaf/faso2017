from grove.grovepi import *

def startLight(light):
	pinMode(light,"INPUT")

	#Recevoir la valeur du capteur
        sensor = analogRead(light)
	if (sensor == 65535) :
		sensor = 250

        # calculer la resistence qui l'on va comparer avec la variable zero
        resistance = (float)(1023 - sensor) * 10 / sensor
        return sensor
