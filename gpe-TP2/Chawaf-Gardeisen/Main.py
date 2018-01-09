#coding: utf-8

import os

os.system("sudo chmod a+rw /dev/i2c-*")

from driverLCD import *
from driverDigital import *
from driverMail import *
import datetime


#envoie du bilan de demonstration
send_BilanDemo()
v=0


#initialisation des caracteristiques de la boite aux lettres
lcd_commande(0x01)
lcd_commande(0x0F)
lcd_commande(0x38)
lcd_message("Bali est VIDE ! ")
lcd_couleur(130,0,5)  #rouge


#on enregistre une premiere fois l'etat de la boite dans un fichier texte
with open('HistoriqueEtat.txt', 'a') as f:
	f.write(str('1') + '\n') #1 represente l'etat Vide


#on enregistre une premiere fois le temps actuel dans un autre fichier texte
maintenant = datetime.datetime.now()


#pour la demonstration lors de la soutenance, on decide d'enregistrer les secondes au lieu du jour.
with open('HistoriqueTemps.txt', 'a') as f:
	f.write(str(maintenant.second) + '\n')

#with open('HistoriqueTemps.txt', 'a') as f:
 #       f.write(str(maintenant.second) + '\n')


n=0	#variable utilisée pour empecher le capteur de mvt d'etre en marche lorsque la boite est deja pleine



#boucle infinie
while True:

	#si le capteur de mouvement s'active et que la boite est vide (n==0)
	if (Detection_Courrier() and n==0):
		
		#changement de l'affichage de l'écran
		lcd_message(" Bali est PLEINE!")
		lcd_couleur(0,130,5) #vert

		send_email() #envoie de mail de reception de courrier à l'utilisateur

		maintenant = datetime.datetime.now() #on stock la date du moment

		#on enregistre la seconde à laquelle le courrier a été déposé. (on enregistre 2 la donnée pour une question d'esthetique du graphique historique)
		with open('HistoriqueTemps.txt', 'a') as f:
                        f.write(str(maintenant.second) + '\n')

		with open('HistoriqueTemps.txt', 'a') as f:
                        f.write(str(maintenant.second) + '\n')


		#on enregistre l'etat initial de la boite pour une question d'esthetique du graphique
                with open('HistoriqueEtat.txt', 'a') as f:
                        f.write(str('1') + '\n') #etat Vide

		#on enregistre le nouvel état de la boite
		with open('HistoriqueEtat.txt', 'a') as f:
			f.write(str('2') + '\n')  #etat Plein

		n=1

		time.sleep(3)




	#Quand l'utilisateur récupère le courrier, il appuie sur le bouton pour l'initialiser.
	if Etat_Bouton()==1 :

		#initialisation de l'affichage écran
		lcd_commande(0x01)
		lcd_commande(0x0F)
		lcd_commande(0x38)
		lcd_message(" Bali est VIDE !")
		lcd_couleur(130,0,5)  #l'affichage de l'écran devient rouge

		v=v+1

		time.sleep(3) #on arrete le fonctionnement du capteur de mouvement le temps que l'utilisateur referme la porte de bali

		#envoi de releve de courrier
		send_email2()

		maintenant = datetime.datetime.now()

		with open('HistoriqueTemps.txt', 'a') as f:
		        f.write(str(maintenant.second) + '\n')

		with open('HistoriqueTemps.txt', 'a') as f:

                        f.write(str(maintenant.second) + '\n')



                with open('HistoriqueEtat.txt', 'a') as f:
                        f.write(str('2') + '\n')

   		with open('HistoriqueEtat.txt', 'a') as f:
			f.write(str('1') + '\n')

		n=0


	#Envoi de l'historique bilan à la fin du mois :

	maintenant = datetime.datetime.now()
	jour = maintenant.day
	heure = maintenant.hour
	minute = maintenant.minute
	seconde = maintenant.second

	#le 1er jour du mois, on envoie un mail avec le graphique historique du mois precedent.
	if jour==9 and heure==10 and minute == 30 and seconde ==0 :
		#on crée le graphique
		os.system("python bilanMensuel.py")

		#on envoie le grapahique en piece jointe par mail
		send_Bilan()

		#on efface les donnees enregistrées dans les fichiers txt pour le mois suivant
		os.system("rm HistoriqueTemps.txt")
		os.system("rm HistoriqueEtat.txt")


	#pour la soutenance, on envoie un mail avec un graphique historique à la fin de la minute
	if v == 4:
		os.system("python bilanMensuel.py")
		send_Bilan()
		v=0




