#-*- encoding: utf-8 -*-

from grovepi import *

def getSeuil(pin):
	s = analogRead(pin)
	return s

