
import time
from Button.button import *
from grovepi import *
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
#with f as files:


	while True:
        	try:
			digitalWrite(led,0)
                        digitalWrite(ledb,0)
                        digitalWrite(ledg,0)
                        time.sleep(1)
			print ("DEBUT")
			with open("sensor_data","r") as files:
				for i in files:
					if i== None:
						f.close()
					else:
			 	#fqr= files.readlines()
						if int(i) == 0 or int(i) == 3 :
                                #Blink the LED
	                                   		digitalWrite(led,1)             # Send HIGH to switch on LED
                                       	#print ("LED ON high!")
							print ("STRING")
							time.sleep(1)
							digitalWrite(led,0)
						elif int(i) == 1  or int(i) == 4:
                               				digitalWrite(ledg,1)             # Send HIGH to switch on LED
                               		#print ("LED ON high!")
							print ("REDDDDD")
							time.sleep(1)
							digitalWrite(ledg,0)
						elif int(i)== 2 or int(i) == 5 :
							digitalWrite(ledb,1)             # Send HIGH to switch on LED
                                        #print ("LED ON high!")
							print ("BLUEEE")
	                        	        	time.sleep(1)
							digitalWrite(ledb,0)
						elif int(i) ==  6 :
                       					digitalWrite(ledg,1)
                               				digitalWrite(ledb,1)
							digitalWrite(led,1)
							print ("ALLL")
							time.sleep(2)
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

