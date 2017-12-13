# coding: utf-8


import os

os.system("sudo chmod a+rw /dev/i2c-*")


from driverLCD import *
from driverDigital import *
from driverMail import *
import datetime

#TUTO capteur mvt : http://deusyss.developpez.com/tutoriels/RaspberryPi/PythonEtLeGpio/


#initialisation des caracteristiques de la boite aux lettres
#_init_lcd() 

lcd_commande(0x01)
lcd_commande(0x0F)
lcd_commande(0x38)

lcd_message("Bali est VIDE ! ")
lcd_couleur(130,0,5)  #rouge

with open('historiqueEtat.txt', 'a') as f:
	f.write(str(1) + '\n')




while True:
	#quand le capteur de mouvement s'active
	if Detection_Courrier():

		#lcd_commande(0x01)
		#lcd_commande(0x0F)
		#lcd_commande(0x0F)

		lcd_message(" Bali est PLEINE!")
		lcd_couleur(0,130,5) #affichage de l'écren devient vert

		send_email() #envoie de mail à l'utilisateur

		maintenant = datetime.datetime.now() #on stock la date du moment 

		jour = maintenant.day

		with open('historiqueTemps.txt', 'a') as f:

        		f.write(str(jour) + '\n')    #on inscrit la valeur dans le fichier txt pour pouvoir l'utiliser plus tard  (bilanHebdomadaire)

		with open('historiqueEtat.txt', 'a') as f:

			f.write(str(2) + '\n')



		time.sleep(1)





#if "fin de la semaine"
		#historique


	if Etat_Bouton()==1 :
		lcd_commande(0x01)
		lcd_commande(0x0F)
		lcd_commande(0x38)
		lcd_message(" Bali est VIDE !")
		lcd_couleur(130,0,5)  #l'affichage de l'écran devient rouge

		time.sleep(15) #on arrete le fonctionnement du capteur de mouvement le temps que l'utilisateur referme la porte de bali


		send_email2()
		maintenant = datetime.datetime.now()
		jour = maintenant.day

		with open('historiqueTemps.txt', 'a') as f:

                        f.write(str(jour) + '\n')    #on inscrit la valeur dans le fichier t

		with open('historiqueEtat.txt', 'a') as f:

			f.write(str(1) + '\n')


time.sleep(1)










	# envoi un mail je crois que c'est juste une commande (faire une fonction?)
	#si on utilise notre raspberry comme un serveur ?
	#
	#
	#
	#stocker dans la base de données.



#a la fin de la semaine historique 


