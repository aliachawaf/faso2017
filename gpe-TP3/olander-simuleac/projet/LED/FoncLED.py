from grove.grovepi import *
from time import sleep


def turnon(l):
	pinMode(l, "OUTPUT")
	digitalWrite(l,1)

def turnoff(l):
        pinMode(l, "OUTPUT")
        digitalWrite(l,0)

def changer(l):
        for i in range(3):
                digitalWrite(l,1)
                sleep(0.1)
                digitalWrite(l,0)
                sleep(0.1)
       # sleep(2)
#end
