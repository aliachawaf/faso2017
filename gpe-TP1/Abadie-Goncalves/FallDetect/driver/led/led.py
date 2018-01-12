import sys
import os
sys.path.insert(0, r'/home/igwall/FallDetect/driver/')
from grove.grovepi import *
import time

def init(pin):
        pinMode(pin,"OUTPUT")

def turnOn(pin):
        digitalWrite(pin,1)
        time.sleep(2)
        digitalWrite(pin,0)
        time.sleep(1)
        digitalWrite(pin,1)     

def turnOff(pin):
	digitalWrite(pin,0)
        
