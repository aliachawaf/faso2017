import time
import grovepi
import sqlite3
from Mail import *
from Wifi import *
database = '/home/pi/Projet/FASO-WEB/db/development.sqlite3'

dhtPin = 3 #digital
luminosityPin = 0 #analogique
moisturePin = 1 #analogique
waterPin = 4  #digital

def readTemperatureHumidity():
    return grovepi.dht(dhtPin,0)

def readLuminosity():
    lum = 0
    for i in (0,5):
        lum += grovepi.analogRead(luminosityPin)
	time.sleep(1)
    return lum / 5

def readMoisture():
    moist = 0
    for i in (0,5):
        moist += grovepi.analogRead(moisturePin)
	time.sleep(1)
    return moist / 5

def readWaterLevel():
    return grovepi.digitalRead(waterPin)

def readTresholds():
    db = sqlite3.connect(database)
    c = db.cursor()
    c.execute("select temperature_treshold, luminosity_treshold, moisture_treshold from settings")
    datas = c.fetchall()
    db.close
    return datas[0]

def arroser():
    return

def sendMeasures(temp, hum, lum, moist):
    print(temp, hum, lum, moist)
    db = sqlite3.connect(database)
    c = db.cursor()
    t = time.strftime("%Y-%m-%d %H:%M:%S")
    c.execute("insert into temperatures (value, created_at, updated_at) values (?, ?, ?)", (temp, t, t))
    c.execute("insert into humidities (value, created_at, updated_at) values (?, ?, ?)", (hum, t, t))
    c.execute("insert into luminosities (value, created_at, updated_at) values (?, ?, ?)", (lum, t, t))
    c.execute("insert into moistures (value, created_at, updated_at) values (?, ?, ?)", (moist, t, t))
    db.commit()
    db.close()
    return

def sendState(state):
    db = sqlite3.connect(database)
    c = db.cursor()
    t = time.strftime("%Y-%m-%d %H:%M:%S")
    c.execute("insert into waterings (state, created_at, updated_at) values (?, ?, ?)", (state, t, t))
    db.commit()
    db.close()
    return

temperatureTreshold, luminosityTreshold, moistureTreshold = readTresholds()
print(temperatureTreshold, luminosityTreshold, moistureTreshold)
destinataire= 'alexandre.kueny@hotmail.com'

temperature, humidity = readTemperatureHumidity()
luminosity = readLuminosity()
moisture = readMoisture()
waterLevel = readWaterLevel()
print(temperature, humidity, luminosity, moisture, waterLevel)	
sendMeasures(temperature, humidity, luminosity, moisture)

if waterLevel == 0:
    if luminosity < luminosityTreshold and moisture < moistureTreshold:
        sendState(True)
        arroser()
    else:
	sendState(False)
else:
    sendState(False)
#   if checkConnection():
#   	sendMailReservoirVide(destinataire)
#if temperature > temperatureTreshold:
#   if checkConnection():
#       sendMailConditionCritique(destinataire)


