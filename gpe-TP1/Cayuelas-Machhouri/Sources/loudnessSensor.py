#-*- encoding: utf-8 -*-

from grovepi import *

def getClap(pin):
	c = analogRead(pin)
	return c

