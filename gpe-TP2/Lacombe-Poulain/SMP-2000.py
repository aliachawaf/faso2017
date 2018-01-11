# coding: utf-8

import datetime
import time
import grovepi
import grove_rgb_lcd
from math import isnan
import os
import requests
import numpy as np
import math
import sys
import serial
import subprocess
import serial



#Initialisation des ports
button=2
button2=3
dht_sensor_port=7
dht_sensor_type=0
grovepi.pinMode(button,"INPUT")
grovepi.pinMode(button2,"INPUT")
ser=serial.Serial('/dev/ttyACM1', 9600)
#time.sleep(4)



def traitement_parle(donnees):
	#donnees=(date,temperature,pluie,humidite,nebulosite,neige,vent)
	#Cas de la nébulosité
	n=donnees[4]
	if n<10:
		ajout2="Le ciel sera entièrement dégagé . "
		code=1
	elif n<40:
		ajout2="Le ciel sera majoritairement dégagé . "
		code=1
	elif n<65:
		ajout2="Le ciel sera assez nuageux . "
		code=4
	elif n<90:
		ajout2="Le ciel sera très nuageux . "
		code=2
	else:
		ajout2="Le ciel sera complèrement occulté . "
		code=2
        #Cas de la pluie
        p=donnees[2]
        if p<1:
                ajout="On ne prévoit pas de pluie . "
        elif p<3:
                ajout="On prévoit une pluie faible . "
		code=3
        elif p<7:
                ajout="On prévoit une pluie modérée . "
		code=3
        else:
                ajout="On prévoit une forte pluie . "
		code=3
	#Cas de la neige
	ne=donnees[5]
	if ne==1:
		ajout3="Il y a un risque de neige . "
		code=5
	else:
		ajout3="Il ny a aucun risque de neige . "
	#Ecriture de la phrase
	phrase="'On prevoit pour cette journée du "+donnees[0]+" une temperature extérieure de "+str(donnees[1])+" degré celsiuss le matin '"
	phrase2="'et de"+str(donnees[7])+" degré celsiuss l après midi . '"
	phrase3="'"+ajout+"Lumidité extérieure sera de "+str(donnees[3])+" pourçant . "+ajout2+"Le vent soufflera en moyenne à "+str(donnees[6])+" kilomètre par heure . "+ajout3+"'"
	return phrase, phrase2, phrase3, code

def recherche_meteo(date):
	r=requests.get('http://www.infoclimat.fr/public-api/gfs/csv?_ll=43.63333,3.9&_auth=Bx1XQAB%2BASNecwA3BXNXflc%2FBjNcKggvVytWNVg2XyIJbFE2VTVWN1M%2FAH0GKQE2Ay4AaVl5BSJXNwtsD2BROgdnVzAAZAF8Xi4AfwU0V3xXewZnXGUIMlcqVjJYPV8iCWtRNFU3VipTOgBgBikBKgMxAGVZZwU%2FVzQLbw9hUTEHYFcxAHwBfF40ADMFNFc1VzcGNVxgCGVXZ1YyWDNfPAluUTJVKFY1UzkAYAYyATcDNQBjWWMFIlcrCxUPEVEvByRXcQA2ASVeLAA3BWtXNw%3D%3D&_c=4a7491219487c12fd8fac3adca7e62ec')
	txt=r.text
	#Recherche de la date
	deb=txt.find("date/heure")
	fin=txt.find("temperature:2m",deb)
	dates=txt[deb:fin]
	dates=dates.split(',')
	dates=dates[1:]
	i=0
	while date not in str(dates[i]):
		i=i+1
	date=str(dates[i])
	date=date[:10]
	#Recherche de la température de la matinée
	deb=fin
	fin=txt.find("temperature:sol",deb)
	temps=txt[deb:fin]
	temps=temps.split(',')
	temps=temps[1:]
	temperaturemat=int(float(temps[i+2]))-273
	#Recherche de la température de l'après-midi
	temperatureapm=int(float(temps[i+5]))-273
	#Recherche de la pluie
	deb=txt.find("pluie,",fin)
	fin=txt.find("pluie_convective",deb)
	pluies=txt[deb:fin]
	pluies=pluies.split(',')
	pluies=pluies[1:]
	pluie=float(pluies[i])
	#Recherche de l'humidité
	deb=txt.find("humidite:2m",fin)
	fin=txt.find("nebulosite:totale",deb)
	humidites=txt[deb:fin]
	humidites=humidites.split(',')
	humidites=humidites[1:]
	humidite=int(float(humidites[i]))
	#Recherche de la nébulosité
	deb=fin
	fin=txt.find("nebulosite:haute",deb)
	nebulosites=txt[deb:fin]
	nebulosites=nebulosites.split(',')
	nebulosites=nebulosites[1:]
	nebulosite=int(nebulosites[i])
	#Recherche du risque de neige
	deb=txt.find("risque_neige",fin)
	fin=txt.find("vent_moyen",deb)
	neiges=txt[deb:fin]
	neiges=neiges.split(',')
	neiges=neiges[1:]
	neige=int(neiges[i])
	#Recherche du vent moyen
	deb=fin
	fin=txt.find("vent_rafales",deb)
	vents=txt[deb:fin]
	vents=vents.split(',')
	vents=vents[1:]
	vent=int(float(vents[i]))
	#Regroupement
	prev=(date,temperaturemat,pluie,humidite,nebulosite,neige,vent,temperatureapm)
	traitement_stockage(prev)
	return prev

def recup_date():
	r=requests.get('http://www.infoclimat.fr/public-api/gfs/csv?_ll=43.63333,3.9&_auth=AxlXQAV7UXMALVBnBnBSewRsATReKAkuUCwKaQ5gAn8DZlQzAmIAYV4yVClUewI1AC1VPF5%2BU3QFZVcwCmUFbgNjVzAFYVEsAHBQLwY3UnkEKAFgXmcJM1AtCm4OawJ%2FA2FUMQJgAHxeOFQyVHsCKQAyVTBeYFNoBWBXOApuBWMDYFc3BXlRLABqUGMGNVJvBDYBYF4wCTFQZwpqDmICZANiVDYCfwBlXjZUNFRgAjQANVU0XmFTdAV5V0kKFAV7AyBXcQUzUXUAclBnBmhSMg%3D%3D&_c=b8bc72b1413d122b6003deb392f2d3c8')
        txt=r.text
        #Recherche de la date du jour
        deb=txt.find("date/heure")
        fin=txt.find("temperature:2m",deb)
        dates=txt[deb:fin]
        dates=dates.split(',')
        dates=dates[1:]
        date=str(dates[0])
        date=date[:10]
	return date

def traitement_stockage(prev):
	with open("Stockage.txt", "a") as fic:
		stock=str(prev)
		stock=stock.replace(",",";")
		stock=stock.replace(" ","")
		stock=stock.replace("'","")
		stock=stock[1:-1]
		fic.write(stock+"\n")
	return

def calcul_moyenne():
	with open("Stockage.txt", "r") as fic:
        	lines=fic.readlines()
        	long=len(lines)
        	lastline=lines[long-1]
        	lastline=lastline.split(";")
        	date=lastline[0]
        	moymat=float(lastline[1])
        	moyapm=float(lastline[7])
        	i=1
        	l=1
        	while i<7:
                	line=lines[long-1-l]
                	line=line.split(";")
                	if line[0]!=date:
                        	date=line[0]
                        	moymat=moymat+float(line[1])
               	        	moyapm=moyapm+float(line[7])
                        	i=i+1
                	l=l+1
		return int(moymat/7),int(moyapm/7)
	        
def decalage_date(date):
	date=date.split('-')
	date[2]=str(int(date[2])+1)
	date="-".join(date)
	return date

def envoi_arduino(date,temp,hum,code,moymat,moyapm):
	date=date.split('-')
        jour=date[2]
        mois=date[1]
        annee=date[0]
	if len(str(temp))==1:
		temp="0"+str(temp)
	if len(str(hum))==1:
		hum="0"+str(hum)
	if len(str(moymat))==1:
		moymat="0"+str(moymat)
	if len(str(moyapm))==1:
		moyapm="0"+str(moyapm)
    	msg=str(code)+str(temp)+str(jour)+str(mois)+str(annee)+str(hum)+str(moymat)+str(moyapm)
	print msg
	for j in range(2):
		ser.write(msg)
		time.sleep(1)
	return


#Main
date=recup_date()
i=1
while True:
	try:
		#Changement de jour
		if grovepi.digitalRead(button2)==1:
			if i!=0:	
				date=decalage_date(date)
			print date
			i=i+1
			if i==8:
				i=0
				date=recup_date()
			time.sleep(0.5)
		#Météo orale
                if grovepi.digitalRead(button)==1:
			prev=recherche_meteo(date)
			[temp,hum]=grovepi.dht(dht_sensor_port,dht_sensor_type)
			while temp==0.0:
				[temp,hum]=grovepi.dht(dht_sensor_port,dht_sensor_type)
			temp=int(temp)
			hum=int(hum)
                        tts2,tts3,tts4,code=traitement_parle(prev)
			moymat,moyapm=calcul_moyenne()
			envoi_arduino(date,temp,hum,code,moymat,moyapm)
			tts1="'Bonjour ! La température actuelle est de "+str(temp)+" degrés celsiuss et le taux dumidité dans lair est de "+str(hum)+" pourçant . '"
			os.system('sh ScriptParole.sh ""'+tts1)
			os.system('sh ScriptParole.sh ""'+tts2)
			os.system('sh ScriptParole.sh ""'+tts3)
			os.system('sh ScriptParole.sh ""'+tts4)
			time.sleep(0.5)
	except IOError:
		print("CA MARCHE PAS")
