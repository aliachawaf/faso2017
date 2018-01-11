import time
from grovepi import *

def allume_led(led):
        digitalWrite(led,1)             
        return None
 
def eteint_led(led):
        digitalWrite(led,0)             
        return None  
