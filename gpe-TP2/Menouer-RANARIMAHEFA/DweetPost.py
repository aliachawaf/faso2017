# -*- coding: utf-8 -*-
# DweetPost V2
# Réalisé par:
# - MENOUER Amjad
# - RANARIMAHEFA Mitantsoa Michel
# Thread qui poste les données sur les service dweet.io tout les 2 secondes
# Le temps d'envoie est a définir selon les besoins de l'utilisateur.
# Les données peuvent être consulté a l'adresse suivante: https://dweet.io/follow/projet_faso_menouer_ranari

import requests
import time
from threading import Thread
import sys

class DweetPost(Thread):

    def __init__(self):
        Thread.__init__(self)
        self.dweetIO = "https://dweet.io/dweet/for/projet_faso_menouer_ranari"
    	self.running = False
	self.temperature = 0
	self.humidite = 0
	self.dust = 0

    def run(self):
        self.running = True
        while (self.running):
    		parametre = {'temp': str(self.temperature), 'hum': str(self.humidite),'dust': str(self.dust)}
    		r = requests.post(self.dweetIO, data=parametre)
    		time.sleep(0.25)

	# modifie la valeurs des attribus de la classe
	# val1 : temperature
	# val2 : humidite
	# val3 : dust
    def setValueDweet(self,val1,val2,val3):
	self.temperature = val1
	self.humidite = val2
	self.dust = val3

    def stop(self):
        self.running = False
