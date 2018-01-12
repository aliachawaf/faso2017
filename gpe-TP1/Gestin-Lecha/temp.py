#coding: utf-8
import grovepi
import time

capteur = 2

while True:
	time.sleep(30)
	try:
		[temp, humidity] = grovepi.dht(capteur, 0)
		print "temp =", temp
		fichier = open("/var/www/html/miroir/tabMeteo.js","a")
		tabMeteo = "tabMeteo.push("+ str(temp) + ");"
		fichier.write(tabMeteo)
		fichier.write("tabX.push(' ');")
		fichier.close();
	except I0Error:
		print "Error"


