import RPi.GPIO as GPIO
import time
		

#def angleToDutyCycle(a) :
#	return float(a)/10 + 5

def init() :
	GPIO.setmode(GPIO.BCM)
	#On configure les pin GPIO17 et GPIO27 du bloc GPIO de la raspberry comme des 
	#sorties, 
	# la pin 17 pour les donnees du moteur 1
	# la pin 27 pour les donnees du moteur 2
	GPIO.setup(17, GPIO.OUT)
	GPIO.setup(27, GPIO.OUT)

	GPIO.setwarnings(False)

	#Declaration des variables

	#On attribue la fonction PWM du GPIO aux pins 17 et 27
	#La fonction PWM permet de simuler un signal analogique 
	moteur_x = GPIO.PWM(17,100)
	moteur_y = GPIO.PWM(27,100)
	moteur_x.start(14)
	moteur_y.start(14)
	return [moteur_x, moteur_y]
	
def stop(moteur_x,moteur_y) :
	moteur_x.stop()
	moteur_y.stop()
	GPIO.cleanup()

def coordonne_to_position_moteur_x(moteur, coord) :
	dc = coordonnee_x_to_duty_cycle(coord)
	moteur.ChangeDutyCycle(dc)
	return moteur
	
def coordonne_to_position_moteur_y(moteur, coord) :
	dc = coordonnee_y_to_duty_cycle(coord)
	moteur.ChangeDutyCycle(dc)
	return moteur

def coordonnee_x_to_duty_cycle(x) :
	res = (1.0/11.0)*x + 31.0/11.0
	return res

def coordonnee_y_to_duty_cycle(x) :
	res = 9.0/94.0*x + 137.0/94.0
	return res
	
