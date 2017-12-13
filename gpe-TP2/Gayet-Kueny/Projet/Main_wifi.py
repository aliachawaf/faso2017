import sqlite3
from Wifi import *

database = '/home/pi/Projet/FASO-WEB/db/development.sqlite3'

def readWifiSettings():
	db = sqlite3.connect(database)
	c = db.cursor()
	c.execute("select wifi_name, wifi_password from settings")
	datas = c.fetchall()
	db.close()
	return datas[0]

wifi_name, wifi_password = readWifiSettings()
print(wifi_name, wifi_password)

if not isAvailable(wifi_name):
	startHotspot()
	print("not available")
else:
	stopHotspot()
	configConnection(wifi_name, wifi_password)
	print("available")
