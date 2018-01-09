import time
import datetime
import grovepi
import sqlite3
from Mail import *
from Wifi import *
database = '/home/pi/Projet/FASO-WEB/db/development.sqlite3'

dhtPin = 3 #digital
luminosityPin = 0 #analogique
moisturePin = 1 #analogique
waterPin = 4  #digital
relayPin = 2

grovepi.pinMode(relayPin, "OUTPUT")

def readTemperatureHumidity():
    data = grovepi.dht(dhtPin,0)
    while data[0] == 0 or data[1] == 0:
	data = grovepi.dht(dhtPin, 0)
    return data
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
    c.execute("select temperature_treshold_min, temperature_treshold_max, luminosity_treshold, moisture_treshold from settings")
    datas = c.fetchall()
    db.close
    return datas[0]

def arroser():
    grovepi.digitalWrite(relayPin, 1)
    time.sleep(3)
    grovepi.digitalWrite(relayPin, 0)

def sendMeasures(temp, hum, lum, moist):
    print(temp, hum, lum, moist)
    db = sqlite3.connect(database)
    c = db.cursor()
    #t = time.strftime("%Y-%m-%d %H:%M:%S")
    t = (datetime.datetime.now() - datetime.timedelta(hours=1)).isoformat()
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
    #t = time.strftime("%Y-%m-%d %H:%M:%S")
    t = (datetime.datetime.now() - datetime.timedelta(hours=1)).isoformat()
    c.execute("insert into waterings (state, created_at, updated_at) values (?, ?, ?)", (state, t, t))
    db.commit()
    db.close()
    return

temperatureTresholdMin, temperatureTresholdMax, luminosityTreshold, moistureTreshold = readTresholds()
#print(temperatureTreshold, luminosityTreshold, moistureTreshold)
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
    if checkConnection():
   	sendMailReservoirVide(destinataire)
if temperature > temperatureTresholdMax or temperature < temperatureTresholdMin:
    if checkConnection():
        sendMailConditionCritique(destinataire)

