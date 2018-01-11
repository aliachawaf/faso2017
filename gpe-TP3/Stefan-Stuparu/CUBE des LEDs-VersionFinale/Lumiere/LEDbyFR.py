import time
from Button.button import *
from grovepi import *
import math

def lumiere():

# Connect the Grove LEDs to digital ports type D
	led = 4
	ledb =8
	ledg =7
#Marche=0
#Marche = status ON/OFF de dispositif

	pinMode(led,"OUTPUT")
	pinMode(ledb,"OUTPUT")
	pinMode(ledg,"OUTPUT")
	f= open ("sensor_data","r")
	i='2'
#with f as files:
	with open("sensor_data","r") as files:
                print ("DEBUT")
		for i in files:
        		try:
			
				digitalWrite(led,0)
				digitalWrite(ledb,0)
				digitalWrite(ledg,0)
				#print ("DEBUT")
				if i== None:
					print ("RIP")
					f.close()
			#with open("sensor_data","r") as files:
			#fqr= files.readlines()
				else:
					#if not(i.strip()):
					#	i=0
					if not(i.strip()):
						break
					elif int(i) == 0 or int(i) == 3 :
                                       		digitalWrite(led,1)
                               			print ("STRING")
						time.sleep(1)
						digitalWrite(led,0)

					elif int(i) == 1  or int(i) == 4:
                        			digitalWrite(ledg,1)
                        			print ("REDDDDD")
						time.sleep(1)
						digitalWrite(ledg,0)

					elif int(i)== 2 or int(i) == 5 :
						digitalWrite(ledb,1)
                                       		print ("BLUEEE")
	                       	        	time.sleep(1)
						digitalWrite(ledb,0)

					elif int(i) ==  6 :
                       				digitalWrite(ledg,1)
                        			digitalWrite(ledb,1)
						digitalWrite(led,1)
						print ("ALLL")
						time.sleep(1)
						digitalWrite(ledg,0)
                                       		digitalWrite(ledb,0)
			               	 	digitalWrite(led,0)

			except KeyboardInterrupt:
				digitalWrite(led,0)
              			digitalWrite(ledb,0)
                		digitalWrite(ledg,0)

				print ("FIN!")
				break
       			except IOError:                         # Print "Error" if communication error encountered
               			print ("Error")
