import sys
import os
sys.path.insert(0, r'/home/ScriptChute/Scripts/Demo')
from grove.grovepi import *
import time

def init(pin):
        pinMode(pin,"OUTPUT")

def turnOn(pin):
	digitalWrite(pin,1)


def turnOff(pin):
	digitalWrite(pin,0)

turnOn(3)
time.sleep(2.0)
turnOff(3)
