from driverGrove.grovepi import *
import time

# Limite
limiteUltrason = 50
limiteLuminosite = 10
EstMaison = False

# Connect the Grove Ultrasonic Ranger to digital port D4
# SIG,NC,VCC,GND
ultrasonic_ranger = 4

# Connect the Grove Buzzer to digital port D3
# SIG,NC,VCC,GND
buzzer = 3

# Connect the Grove Light Sensor to analog port A0
# SIG,NC,VCC,GND
light_sensor = 0


# PinMode Setup
pinMode(light_sensor,"INPUT")
pinMode(buzzer,"OUTPUT")


def readU():
    valeur = -1
    try:
        # Read distance value from Ultrasonic
        valeur = ultrasonicRead(ultrasonic_ranger)
        print 'ultrason = ' + str(valeur)
    except TypeError:
        print ("Error")
    except IOError:
        print ("Error")
    return valeur


def readL():
    valeur = -1
    try:
        # Get sensor value
        sensor_value = analogRead(light_sensor)

        # Calculate resistance of sensor in K
        resistance = (float)(1023 - sensor_value) * 10 / sensor_value
        valeur = resistance
        print 'light = ' + str(valeur)
    except IOError:
        print ("Error")
    return valeur


def ring():
    try:
        # Buzz for 1 second
        digitalWrite(buzzer,1)
        print ('start')
        time.sleep(1)

        # Stop buzzing
        digitalWrite(buzzer,0)
        print ('stop')

    except IOError:
        print ("Error")
    except KeyboardInterrupt:
        digitalWrite(buzzer,0)

def insertBD():
    pass


while True:
    if readU() < limiteUltrason:
        if EstMaison:
            if readL() < limiteLuminosite and (int(time.strftime('%H')) < 13 or int(time.strftime('%H')) >= 18):
                print 'alarme'
                ring()
            else:
                print 'tout est normal'
        else:
            position = input('Est - tu chez toi? (0 pour oui)\n')
            if position is not 0: # 0 si maison autre chose si non
                for x in range(0, 10):
                    print 'alarme'
                    ring()
                    time.sleep(1)
            else:
                EstMaison = True


    time.sleep(1)
