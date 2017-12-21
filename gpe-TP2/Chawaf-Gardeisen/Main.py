# coding: utf-8


import os

os.system("sudo chmod a+rw /dev/i2c-*")


from driverLCD import *
from driverDigital import *
from driverMail import *
import datetime


#initialisation des caracteristiques de la boite aux lettres
#_init_lcd() 

lcd_commande(0x01)
lcd_commande(0x0F)
lcd_commande(0x38)
lcd_message("Bali est VIDE ! ")
lcd_couleur(130,0,5)  #rouge

with open('pb2.txt', 'a') as f:
	f.write(str('1') + '\n')


while True:

		
	#quand le capteur de mouvement s'active
	if Detection_Courrier() :

		lcd_message(" Bali est PLEINE!")
		lcd_couleur(0,130,5) #affichage de l'écren devient vert

		send_email() #envoie de mail à l'utilisateur

		maintenant = datetime.datetime.now() #on stock la date du moment 

#		jour = maintenant.day

		with open('pb1.txt', 'a') as f:

			f.write(str(maintenant) + '\n')    #on inscrit la valeur dans le fichier txt pour pouvoir l'utiliser plus tard  (bilanHebdomadaire)


                with open('pb2.txt', 'a') as f:

                        f.write(str('1') + '\n')


		with open('pb2.txt', 'a') as f:

			f.write(str('2') + '\n')

		n=0

		time.sleep(1)


#if fin du mois
		#historique


	if Etat_Bouton()==1 :
		lcd_commande(0x01)
		lcd_commande(0x0F)
		lcd_commande(0x38)
		lcd_message(" Bali est VIDE !")
		lcd_couleur(130,0,5)  #l'affichage de l'écran devient rouge

		time.sleep(5) #on arrete le fonctionnement du capteur de mouvement le temps que l'utilisateur referme la porte de bali


		send_email2()
		maintenant = datetime.datetime.now()
#		jour = maintenant.day

		with open('pb1.txt', 'a') as f:

                        f.write(str(maintenant) + '\n')    #on inscrit la valeur dans le fichier t


                with open('pb2.txt', 'a') as f:

                        f.write(str('2') + '\n')



		with open('pb2.txt', 'a') as f:

			f.write(str('1') + '\n')


time.sleep(1)


#envoi de l'historique


maintenant = datetime.datetime.now()
jour = maintenant.day
mois = maintenant.month

#pour le mois de janvier
if jour==1 :
	send_Bilan()  #faire attention que l'on envoi bien le bon fichier
	os.system("rm historiqueTemps.txt")
	os.system("rm historiqueEtat.txt")
	


