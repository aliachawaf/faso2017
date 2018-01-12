import time
import grovepi
# Connecter le capteur de luminosite sur le port analogique A0 
def getLuminosite():

	light_sensor = 0


	grovepi.pinMode(light_sensor,"INPUT")

        sensor_value = grovepi.analogRead(light_sensor)

        return sensor_value
