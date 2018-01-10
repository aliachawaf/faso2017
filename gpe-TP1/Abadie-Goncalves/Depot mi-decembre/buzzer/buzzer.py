#conding : utf8
import sys
sys.path.insert(0, r'/home/ScriptChute/Scripts/Demo')
from grove.grovepi import *
import time

def init(pin):
        pinMode(pin,"OUTPUT")

def buzz(pin):
    for i in range(0,2):
        digitalWrite(pin, 1) # Turn buzzer ON
        time.sleep(3.0) # Le buzzer reste allume pendant 3 secondes
        digitalWrite(pin, 0) # turn buzzer OFF
        time.sleep(2.0)  #Le buzzer s'etteind 2 secondes
            
def stop(pin):
	digitalWrite(pin, 0) # turn buzzer OFF

