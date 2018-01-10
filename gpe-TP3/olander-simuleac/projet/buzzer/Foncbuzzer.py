from grove.grovepi import *


def turnon(b):
        pinMode(b, "OUTPUT")
        digitalWrite(b,1)

def turnoff(b):
        pinMode(b, "OUTPUT")
        digitalWrite(b,0)

