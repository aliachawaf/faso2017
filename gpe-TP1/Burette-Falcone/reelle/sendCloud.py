#!/usr/bin/env python3

import http.client, urllib
import sys
import time

key = 'Y0D6SD5C247DXZIW'  # Clé de la chaine Thingspeak

def send(toSendTemp,bpm,temp=0,hum=0):
	try :
		if toSendTemp :
			print("Envoi sur le cloud de bpm:"+str(bpm)+" temp:"+str(temp)+" hum:"+str(hum))
			params = urllib.parse.urlencode({'field1':float(bpm),'field2': float(temp), 'field3': float(hum),'key':key }) 
		else :
			print("Envoi sur le cloud de bpm:"+str(bpm)+" uniquement")
			params = urllib.parse.urlencode({'field1':float(bpm),'key':key})
		headers = {"Content-typZZe": "application/x-www-form-urlencoded","Accept": "text/plain"}
		conn = http.client.HTTPConnection("api.thingspeak.com:80")
		conn.request("POST", "/update", params, headers)
		#On effectue la requete HTTP aupres de ThingSpeak 
		response = conn.getresponse()
		print(response.status)
		print(response.reason)
		#Reason et Status permettront de savoir comment l'envoi s'est passé.
		data = response.read()
		conn.close()
	except ValueError :
		print("Attention le ième argument n'est pas un entier")
	except :
		print("Erreur lors de l'envoi:"+ str(sys.exc_info()[0]))
