# -*- coding: utf-8 -*-
# DHT.py V2
# Réalisé par:
# - MENOUER Amjad
# - RANARIMAHEFA Mitantsoa Michel
# Thread qui collecte données du capteur de température/humidité toute les 5 secondes
# Le temps de relevé est a définir selon les besoins de l'utilisateur.

import grovepi
import math
from threading import Thread
import time
import sys

# Connecter le capteur de température/humidité au port digital D7

class DHT(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.running = False
        self.DHT_Sensor_Port = 7
        self.temp = 0
        self.humidite = 0

    def run(self):
        self.running = True
        while (self.running):
            try:
                [temperature,humidity] = grovepi.dht(self.DHT_Sensor_Port,0)
                if math.isnan(temperature) is True or math.isnan(humidity) is True:
                    raise TypeError('nan error')
                self.temp = temperature
                self.humidite = humidity
                time.sleep(5)
            except IOError:
                print ("Error")


    def getValueDHT(self):
        return self.temp, self.humidite

    def stop(self):
        self.running = False
