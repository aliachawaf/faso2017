# -*- coding: utf-8 -*-
# programme principal - Alarme incendie connectée - V4
# Réalisé par:
# - MENOUER Amjad
# - RANARIMAHEFA Mitantsoa Michel
#
# Les données peuvent être consulté a l'adresse suivante: https://dweet.io/follow/projet_faso_menouer_ranari

import time
import grovepi
from grove_rgb_lcd import *
import math
from DHT import DHT
from DweetPost import DweetPost
from threading import Thread
import serial

# Connecter le bouton au port digital D3 du shield du raspberry
# Connecer le buzzer au port digital D4 du shield du raspberry
# Connecter le capteur de température/humidité au port digital D7 du shield du raspberry
# Connecter le capteur de poussière au port D8 du shield de l'Arduino
# Televerser le fichier dust_sensor.ino sur l'Arduino ensuite débrancher le cable USB-AB
# de l'ordinateur et le brancher sur l'un des ports USB du raspberry

#setup
button = 3
buzzer = 4
grovepi.pinMode(button,"INPUT")
grovepi.pinMode(buzzer,"OUTPUT")
ser = serial.Serial('/dev/ttyACM0',9600)

#variable globale
appuie = 0
y = 0
temps = 0
seconde = 0
dust = 0
buzer_on = False
long_press = 0

if __name__ == '__main__':

    dht_thread = DHT()
    envoi_thread = DweetPost()
    dht_thread.start()
    envoi_thread.start()

    while True:
        y=time.time()-temps
        seconde = time.localtime(y)[5]
        print time.strftime(str(seconde))
        try:

            # recuperation donne des capteurs
            [temp,humidite] = dht_thread.getValueDHT()
            # donnees du capteur de poussiere sur le port serie
            print("Densite air:\n" + str(dust) + " pcs\\0.01cf")
            dust = ser.readline()

            # si on detecte de la fumee
            if dust > 80000:
                 grovepi.digitalWrite(buzzer,1)
                 buzer_on = True
                 setText("Fumee detectee !")

            # si on apres avoir consulter les donnees on appuie pas au bout de 30s
            if seconde > 30 and appuie > 0:
                # eteindre l'ecran lcd
                setText("")
                setRGB(0, 0, 0)
                appuie = 0

            # Gestion de l'appuie sur le bouton
            if grovepi.digitalRead(button) == 1:
                # si on reste appuyé 3s sur le bouton: on desactive l'alarme
                if (long_press == grovepi.digitalRead(button)):
                    if seconde > 3 and buzer_on:
                        grovepi.digitalWrite(buzzer,0)
                        setText("")
                        setRGB(0, 0, 0)
                # sinon on affiche les donnees sur lecran lcd
                else:
                    setRGB(193, 254, 240)
                    if (appuie%3) == 0:
                        setText("Temperature:\n" + str(temp) + " C")
                    if (appuie%3)== 1:
                        setText("Humidite:\n" + str(humidite) + " %")
                    if (appuie%3) == 2:
                        setText("Densite air:\n" + str(dust) + " pcs/0.01cf")

                    # raz du chrono et on incremente le nb d'appuie
                    temps = time.time()
                    appuie = appuie + 1

                long_press = grovepi.digitalRead(button)

            long_press = grovepi.digitalRead(button)
	    envoi_thread.setValueDweet(temp,humidite,dust)

        except KeyboardInterrupt:
    		# On arrete tout
                grovepi.digitalWrite(buzzer,0)
    		setText("")
            	setRGB(0, 0, 0)
                dht_thread.stop()
                envoi_thread.stop()
    		break

        except IOError:
            print ("Error")

        time.sleep(0.25)
