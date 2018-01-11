from driverGrove.grovepi import *
import time
import urllib2
import csv

# Limite
limiteUltrason = 50
limiteLuminosite = 10

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

estDedans = True
posMaison = [43.69473119, 1.27020893]
myFile = open('data.csv', 'a')
writer = csv.writer(myFile)


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

def insertBD(type):
    data = [type, time.strftime("%Y-%m-%d %H:%M")]
    writer.writerow(data)

def getPos():
    return urllib2.urlopen("http://serveur-projet-fas-ig3.appspot.com/?cmd=getPosition").read().split(', ')

def estMaison():
    pos = getPos()
    estMaison = True
    if float(pos[0]) > posMaison[0] + 0.0002 or float(pos[0]) < posMaison[0] - 0.002:
        estMaison = False
    elif float(pos[1]) > posMaison[1] + 0.0002 or float(pos[1]) < posMaison[1] - 0.002:
        estMaison = False
    return estMaison


while True:
    if readU() < limiteUltrason:
        if estDedans:
            if readL() < limiteLuminosite and (int(time.strftime('%H')) < 17 or int(time.strftime('%H')) >= 18):
                print("alerte lumiere")
                insertBD("lumiere")
                ring()
            else:
                insertDB("depart")
                print("au revoir")
                estDedans = False
        else:
            position = estMaison()
            if not position: # 0 si maison autre chose si non
                insertBD("intrusion")
                for x in range(0, 10):
                    print("alerte intru")
                    ring()
                    time.sleep(1)
            else:
                estDedans = True
                insertBD("arrive")
                print("bienvenue")
        while readU() < limiteUltrason:
            time.sleep(0.1)
            print("stand by")
    time.sleep(1)
