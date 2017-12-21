#!/usr/bin/python3
#-*- coding: utf-8 -*-

from grovepi import *
import time

HIGH = 1
LOW = 0
def init(pin):
	pinMode(pin,"OUTPUT")

def onLED(pin):
	digitalWrite(pin,HIGH)
	return 1

def offLED(pin):
	digitalWrite(pin,LOW)
	return 1

def blink(pin,tps):
	time.sleep(tps)
	digitalWrite(pin,1)
 	time.sleep(tps);
	digitalWrite(pin,0)


