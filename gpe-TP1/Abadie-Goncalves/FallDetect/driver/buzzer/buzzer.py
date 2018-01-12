#conding : utf8
import sys
sys.path.insert(0, r'/home/igwall/FallDetect')
from grove.grovepi import *
import time

def init(pin):
        pinMode(pin,"OUTPUT")

def buzz(pin):
    digitalWrite(pin, 1) # Turn buzzer ON
    time.sleep(3)
    digitalWrite(pin, 0)
    time.sleep(2)
    digitalWrite(pin, 1)
    time.sleep(3)
    digitalWrite(pin, 0)        
def stop(pin):
	digitalWrite(pin, 0) # turn buzzer OFF

