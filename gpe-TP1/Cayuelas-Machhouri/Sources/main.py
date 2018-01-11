import grovepi
import led
import ultrasonic
import lightSensor
import loudnessSensor
import time 
import os
from grove_rgb_lcd import *
import datetime

pir_sensor = 8
motion=0
grovepi.pinMode(pir_sensor,"INPUT")

#Variables
light_sensor = 0
pinLed = 6
pinUltraSon = 4
loudness_sensor = 1 
button = 3


bool = True

#initialisation
led.init(pinLed)
led.offLED(pinLed)

#Init Ecran + affichage
setText("Luminosite 0")	
setRGB(20,20,20)


date = datetime.date.today()
compteur = 0
cout = 1 #a definir prix pour 1 seconde

mois = date.month
compteurMois = 0
cMois = 0

while True:	
	timeTotal1=0
	timeTotal2=0
	pression = grovepi.digitalRead(button)
	time.sleep(0.5)
	if pression == 1:
		if bool:
			setText("Consommation jour : " +str(compteur))
			bool = False
		else:
			setText("Consommation mois : " +str(compteurMois))
			bool = True





	mon_fichier = open("Clap.txt", "r") 
	contenu = mon_fichier.read()
	mon_fichier2 = open("Passage.txt", "r") 
	contenu2 = mon_fichier2.read()

	
	
	if date != datetime.date.today():
		jour = open("consommationJour.txt", "a")
		jour.write(str(date))
		jour.write("\n")
		jour.write(str(compteur)) #compteur du temps d'allumage en secondes par jour
		jour.write("\n")
		c = compteur * cout
		jour.write(str(c)) #consommation en euro par jour
		jour.write("\n")
		jour.write("\n")
		
		date = datetime.date.today()

		cMois += c 

		compteur = 0 
		c = 0
		
		
		if mois != date.month:
			mois = open("consommationMois.txt", "a")
			mois.write(str(mois))
			mois.write("\n")
			mois.write(str(compteurMois)) #compteur du temps d'allumage en secondes par mois
			mois.write("\n")
			mois.write(str(cMois))   #consommation en euro par mois
			mois.write("\n")
			mois.write("\n")
			
			mois = date.month
			compteurMois = 0
			cMois = 0	 
			

#	led.offLED(pinLed)
	a = True 
	b = True
	c = True
	d = True 
       
	f = True
	g = True
	h = True
	i = True
	j = True


	sensor_value = lightSensor.getSeuil(light_sensor)
	distanceUltrason = ultrasonic.getDistance(pinUltraSon)
	loudness_sound = loudnessSensor.getClap(loudness_sensor)
	print(loudness_sound)
		
	if (sensor_value < 450): 

		if(distanceUltrason < 50):
			#Enregistrement Passage#

			mon_fichier2 = open("Passage.txt", "r") 
			contenu2 = mon_fichier2.read()
			mon_fichier2 = open("Passage.txt", "w") 
			nb2 = int(contenu2)
			val2 = nb2 + 1
			mon_fichier2.write(str(val2))
			
			#####
			timeDebut1 = time.clock()
			led.onLED(pinLed)
			print("Luminosite a 100%")
			setText("Luminosite 100%")	
			setRGB(230,0,0)		

			while a == True:	
				pression = grovepi.digitalRead(button)
				time.sleep(0.5)
				if pression == 1 :
					if bool:
						setText("Consommation jour :" +str(compteur))
						bool=False
					else:
						setText("Consommation mois :" +str(compteurMois))
						bool=True
				loudness_sound = loudnessSensor.getClap(loudness_sensor)
				print(loudness_sound)
				if (loudness_sound > 200):
					#Enregistrement Clap#
					mon_fichier = open("Clap.txt", "r") 
					contenu = mon_fichier.read()
					mon_fichier = open("Clap.txt", "w") 
					nb = int(contenu)
					val = nb + 1
					mon_fichier.write(str(val))
					#mon_fichier.close()
					#########
					grovepi.analogWrite(pinLed, 128)
					print("Luminosite a 75%")

					setText("Luminosite 75%")	
					setRGB(230,50,0)
					time.sleep(3)
					while b == True:
						pression = grovepi.digitalRead(button)
						time.sleep(0.5)
						if pression == 1 :
							if bool:
								setText("Consommation jour :" +str(compteur))
								bool=False
							else:
								setText("Consommation mois :" +str(compteurMois))
								bool=True
						loudness_sound = loudnessSensor.getClap(loudness_sensor)	
						if (loudness_sound > 200):
							#Enregistrement Clap#
							mon_fichier = open("Clap.txt", "r") 
							contenu = mon_fichier.read()
							mon_fichier = open("Clap.txt", "w") 
							nb = int(contenu)
							val = nb + 1
							mon_fichier.write(str(val))
							#mon_fichier.close()
							#########
							grovepi.analogWrite(pinLed, 64)
							print("Luminosite a 50%")
							setText("Luminosite 50%")	
							setRGB(230,50,50)
							time.sleep(3)
							while c == True:
								pression = grovepi.digitalRead(button)
								time.sleep(0.5)
								if pression == 1:
									if bool:
										setText("Consommation jour :" +str(compteur))
										bool=False
									else:
										setText("Consommation mois :" +str(compteurMois))
										bool=True
								loudness_sound = loudnessSensor.getClap(loudness_sensor)
								if (loudness_sound > 200):
									#Enregistrement Clap#
									mon_fichier = open("Clap.txt", "r") 
									contenu = mon_fichier.read()
									mon_fichier = open("Clap.txt", "w") 
									nb = int(contenu)
									val = nb + 1
									mon_fichier.write(str(val))
									#mon_fichier.close()
									#########
									grovepi.analogWrite(pinLed, 32)
									print("Luminosite a 25%")
									setText("Luminosite 25%")	
									setRGB(230,100,50)	
									time.sleep(3)							
									while d == True:
										pression = grovepi.digitalRead(button)
										time.sleep(0.5)
										if pression==1:
											if bool:
												setText("Consommation jour :" +str(compteur))
											 	bool=False
											else:
												setText("Consommation mois :" +str(compteurMois))
												bool=True
										loudness_sound = loudnessSensor.getClap(loudness_sensor)	
										if (loudness_sound > 200):
											#Enregistrement Clap#
											mon_fichier = open("Clap.txt", "r") 
											contenu = mon_fichier.read()
											mon_fichier = open("Clap.txt", "w") 
											nb = int(contenu)
											val = nb + 1
											mon_fichier.write(str(val))
											#mon_fichier.close()
											#########
											grovepi.analogWrite(pinLed, 0)
											timeFin1 = time.clock()
											print("Luminosite a 0%")
											setText("Luminosite 0")	
											setRGB(20,20,20)
											time.sleep(3)
											a = False
											b = False
											c = False
											d = False
										
											timeTotal1 = timeFin1 - timeDebut1						

		

		loudness_sound = loudnessSensor.getClap(loudness_sensor)
		print(loudness_sound)
		if (loudness_sound > 100):
			#Enregistrement Clap#
			mon_fichier = open("Clap.txt", "r") 
			contenu = mon_fichier.read()
			mon_fichier = open("Clap.txt", "w") 
			nb = int(contenu)
			val = nb + 1
			mon_fichier.write(str(val))
			#mon_fichier.close()
			#########
			timeDebut2 = time.clock()
			led.onLED(pinLed)
			print("Luminosite a 100%")
			setText("Luminosite 100%")	
			setRGB(230,0,0)
			time.sleep(3)
			while f == True:
                		pression = grovepi.digitalRead(button)
                		time.sleep(0.5)
                		if pression == 1 :
                    			if bool:
                        			setText("Consommation jour :" +str(compteur))
                        			bool=False
                    			else:
                        			setText("Consommation mois :" +str(compteurMois))
                        			bool=True
				loudness_sound = loudnessSensor.getClap(loudness_sensor)
				print(loudness_sound)
				if (loudness_sound > 200):
					#Enregistrement Clap#
					mon_fichier = open("Clap.txt", "r") 
					contenu = mon_fichier.read()
					mon_fichier = open("Clap.txt", "w") 
					nb = int(contenu)
					val = nb + 1
					mon_fichier.write(str(val))
					#mon_fichier.close()
					#########
					led.onLED(pinLed)
					print("Luminosite a 100%")
					setText("Luminosite 100%")	
					setRGB(230,0,0)
					time.sleep(3)
					while g == True:
                        			pression = grovepi.digitalRead(button)
                        			time.sleep(0.5)
                        			if pression == 1 :
                           		 		if bool:
                                				setText("Consommation jour :" +str(compteur))
                                				bool=False
                            				else:
                                				setText("Consommation mois :" +str(compteurMois))
                                				bool=True
						loudness_sound = loudnessSensor.getClap(loudness_sensor)
						if (loudness_sound > 200):
								#Enregistrement Clap#
							mon_fichier = open("Clap.txt", "r") 
							contenu = mon_fichier.read()
							mon_fichier = open("Clap.txt", "w") 
							nb = int(contenu)
							val = nb + 1
							mon_fichier.write(str(val))
							#mon_fichier.close()
							#########
							grovepi.analogWrite(pinLed, 128)
							print("Luminosite a 75%")

							setText("Luminosite 75%")	
							setRGB(230,50,0)
							time.sleep(3)
							while h == True:
                                				pression = grovepi.digitalRead(button)
                                				time.sleep(0.5)
                                				if pression == 1 :
                                    					if bool:
                                        					setText("Consommation jour :" +str(compteur))
                                        					bool=False
                                    					else:
                                        					setText("Consommation mois :" +str(compteurMois))
                                        					bool=True
								loudness_sound = loudnessSensor.getClap(loudness_sensor)
								if (loudness_sound > 200):
										#Enregistrement Clap#
									mon_fichier = open("Clap.txt", "r") 
									contenu = mon_fichier.read()
									mon_fichier = open("Clap.txt", "w") 
									nb = int(contenu)
									val = nb + 1
									mon_fichier.write(str(val))
									#mon_fichier.close()
									#########
									grovepi.analogWrite(pinLed, 64)
									print("Luminosite a 50%")
									setText("Luminosite 50%")	
									setRGB(230,50,50)
									time.sleep(3)							
									while i == True:
                                        					pression = grovepi.digitalRead(button)
                                        					time.sleep(0.5)
                                        					if pression == 1 :
                                            						if bool:
                                                						setText("Consommation jour :" +str(compteur))
                                                						bool=False
                                            						else:
                                                						setText("Consommation mois :" +str(compteurMois))
                                                						bool=True
										loudness_sound = loudnessSensor.getClap(loudness_sensor)	
										if (loudness_sound > 200):
												#Enregistrement Clap#
											mon_fichier = open("Clap.txt", "r") 
											contenu = mon_fichier.read()
											mon_fichier = open("Clap.txt", "w") 
											nb = int(contenu)
											val = nb + 1
											mon_fichier.write(str(val))
											#mon_fichier.close()
											#########
											grovepi.analogWrite(pinLed, 32)
											print("Luminosite a 25%")
											setText("Luminosite 25%")	
											setRGB(230,100,50)	
											time.sleep(3)
											while j == True:
                                                						pression = grovepi.digitalRead(button)
                                                						time.sleep(0.5)
                                                						if pression == 1 :
                                                    							if bool:
                                                        							setText("Consommation jour :" +str(compteur))
                                                        							bool=False
                                                    							else:
                                                        							setText("Consommation mois :" +str(compteurMois))
                                                        							bool=True
												loudness_sound = loudnessSensor.getClap(loudness_sensor)
												if (loudness_sound > 200):
														#Enregistrement Clap#
													mon_fichier = open("Clap.txt", "r") 
													contenu = mon_fichier.read()
													mon_fichier = open("Clap.txt", "w") 
													nb = int(contenu)
													val = nb + 1
													mon_fichier.write(str(val))
													#mon_fichier.close()
													#########
													grovepi.analogWrite(pinLed, 0)
													timeFin2 = time.clock()
													print("Luminosite a 0")
													setText("Luminosite 0")	
													setRGB(20,20,20)
													time.sleep(3)
													f = False
													g = False
													h = False
													i = False
													j = False
													timeTotal2 = timeFin2 - timeDebut2

	mon_fichier2.close()
	mon_fichier.close()


	compteur1 = timeTotal1 + timeTotal2
	
	if compteur1 != 0 :
		compteur += compteur1
		compteurMois += compteur1
	 

	print("compteur jour")
	print(compteur)
	print("compteur mois")
	print(compteurMois)
