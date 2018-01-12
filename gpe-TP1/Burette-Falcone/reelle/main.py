
#!/usr/bin/python3

import ledBuz
import analyse
import led
import configReveil
import timeScreen
import grovepi
import sendTemp
import sendCloud
import captCard
import time
from grove_rgb_lcd import *

def waitingForEnd(bandeau) :
	#Récupération du rythme cardiaque
	card = captCard.readHeartRate(pinCard,intCard)
	while card != 0 :
		print("Attente. L'utilisateur doit enlever le capteur de son oreille")
		time.sleep(0.2)

		##Temporaire
		time.sleep(5)
		card=0
	heure = " "
	min = " "
	hReveil = "OFF"
	mReveil = " "
	ledBuz.off(bandeau)
	return [heure,min,hReveil,mReveil]

def heureMoinsUn(heure):
	if heure == 0 : 
		return 23 
	else : 
		return heure - 1

###### INITIALISATION #######
setText("Demarrage en \ncours")
setRGB(255,255,255)
# ports de branchements
captTemp = 4
boutonD = 6
boutonG = 5
ledAllum = 8
ledReveil = 7
bandLed = 3
pinCard = 2

# reglages des temps
sleepSend = 60
sleepTemp = 600
sleepCard = 60
lastSend = 0
lastReadTemp = 0
lastReadCard= 0
tempReveil = 10
nbValeur = 100
intCard = 10

#Variable pour le reveil
heure = " "
min = " "
hReveil = "OFF"
mReveil = " "
reveilRegle = False

#Initialisation des LEDS
led.init(ledAllum)
led.init(ledReveil)

#On s'assure que les LEDS sont eteintes
led.turnOff(ledAllum)
led.turnOff(ledReveil)
cardNuit = []
precPic = False

#### Fin de l'INITIALISATION ####
time.sleep(5)
setRGB(0,125,255)
led.turnOn(ledAllum)

while True :

	#si l utilisateur n e touche pas aux boutons l ecran affiche l heure actuelle
	if not(grovepi.digitalRead(boutonD) == 1 or grovepi.digitalRead(boutonG) == 1):
		heure, min = timeScreen.timeScreen(heure, min, hReveil, mReveil)
		#On lit la température en vérifiant que la derniere lecture date de plus de ... minutes
		if reveilRegle == True:
			if time.time() - lastReadTemp > sleepTemp :
				temp,humidity = sendTemp.tempHumidity(captTemp)
				if(temp!=-1 and humidity !=-1):
					tempToSend = True
					lastReadTemp = time.time()
				else :
					temp, humidity = [0,0]
					tempToSend = False
			#tempToSend permettra de savoir, lors de l'envoi au cloud, quelles données sont à envoyer

			#On recoit le rythme cardiaque de l'Arduino
			if time.time() - lastReadCard > sleepCard :

				##Réception du rythme cardiaque depuis l'arduino
				card = captCard.readHeartRate(pinCard,intCard)

				lastReadCard = time.time()
				#Ajout à la liste locale :
				cardNuit = analyse.decalerListe(card, cardNuit, nbValeur)
				# si on se trouve dans l intervalle d analyse (1h avant heure de reveil)
				if  (int(heure) == heureMoinsUn(int(hReveil)) and int(min) >= mReveil) :
					print("entre dans la boucle d analyse")
					if precPic and card < cardNuit[ len(cardNuit) -2 ]:
						reveilRegle = False
						led.turnOff(ledReveil)
						ledBuz.on(bandLed)
						#On attend que l'utilisateur enleve le capteur pour éteindre le bandeau
						heure,min,hReveil,mReveil = waitingForEnd(bandLed)

					elif analyse.pic(cardNuit):
						precPic = True
				# si on a depasse l heure de revil max alors on allume
				if  (int(heure) == hReveil and int(min) >= mReveil) :
					print("entre dans la boucle de depassement du temps")
					reveilRegle = False
					led.turnOff(ledReveil)
					ledBuz.on(bandLed)
					heure,min,hReveil,mReveil = waitingForEnd(bandLed)
			#On envoie le tout au cloud :
			if time.time() - lastSend > sleepSend :
				sendCloud.send(tempToSend,card,temp,humidity)
				lastSend = time.time()
				tempToSend = False



	# si l utilisateur appuie sur un des deux boutons on declenche le reglage de l heure de reveil
	else:
		time.sleep(0.5)
		setText("Regler reveil ? \n OUI / NON")
		stop = True
		while stop:
			print("waiting for response 'Regler Reveil Oui Non'")
			# reglage du reveil
			if grovepi.digitalRead(boutonG) == 1:
				stop = False
				setText("Votre reveil : \n" + "0:00")
				hReveil, mReveil = configReveil.configReveil(boutonG, boutonD, tempReveil)
				led.turnOn(ledReveil)
				reveilRegle = True
				print("réveil programmé pour "+ str(hReveil) +":"+str(mReveil))
			# sorti du reglage retour ecran heure
			if grovepi.digitalRead(boutonD) == 1:
				time.sleep(0.2)
				stop = False
				heure, min = timeScreen.timeScreen(" ", " ", hReveil, mReveil)
				print("non")
			time.sleep(0.2)
	time.sleep(0.2)

led.turnOff(ledAllum)

