#import grovepi
import led
import ultrasonic
import lightSensor
import loudnessSensor
#Variables
light_sensor = 0
pinLed = 6
pinUltraSon = 4
loudness_sensor = 1

#initialisation
led.init(pinLed)
led.offLED(pinLed)
while True:	
	# Get sensor value
	sensor_value = lightSensor.getSeuil(light_sensor)
#	print(sensor_value)
	distanceUltrason = ultrasonic.getDistance(pinUltraSon)
	loudness_sound = loudnessSensor.getClap(loudness_sensor)
	print(loudness_sound)
	#print(distanceUltrason)
	#print(sensor_value)
		
	if (sensor_value < 450): 
		#print("L:"+sensor_value)
		#print("DU"+distanceUltrason)
		if(distanceUltrason < 50):
			led.onLED(pinLed)
	#	print("onLED")
		sensor_value = lightSensor.getSeuil(light_sensor)
	

		if (loudness_sound > 150):
			led.onLED(pinLed)
