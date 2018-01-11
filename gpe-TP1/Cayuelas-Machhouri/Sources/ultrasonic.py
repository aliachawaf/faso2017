#-*- encoding: utf-8 -*-

from grovepi import *
import time

def getDistance(pin):
	d =ultrasonicRead(pin)
	return d

