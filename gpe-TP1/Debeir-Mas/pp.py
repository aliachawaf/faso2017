#!/usr/bin/env python
# coding: utf-8
import RPi.GPIO as GPIO
import time
import cwiid
import nunchuk
import servo
from grovepi import *
from grove_rgb_lcd import *
import luminosite
import manipfile

#Initialisation de l'écran

setText("WiiLabyrinthe")
setRGB(64,16,15)

def main() :
	setText("Appuyez sur les boutons 1 et 2")
	time.sleep(1.5)
	setText("de votre Wiimote")
	wm = connexionWii()
	setText("Wiimote         connectee !")
	wm.rumble=1
	time.sleep(3)
	wm.rumble=0
	setText("Arret partie :  appuyez sur + ")
	wm.rpt_mode = cwiid.RPT_NUNCHUK|cwiid.RPT_BTN
	moteurs = servo.init()
	moteur_x = moteurs[0]
	moteur_y = moteurs[1]
	partie(wm,moteur_x,moteur_y)	



def connexionWii():
    #setText("Appuyez sur les boutons 1 et 2")
    #time.sleep(6)
    #setText("de votre Wiimote")
    wm=cwiid.Wiimote()
    return wm
	

def end():
	return setText("Partie          abandonnee !")



def partie(wm,moteur_x,moteur_y):
	setText("Placez la bille en bas a gauche")
	time.sleep(1)
	setText("Appuyez sur A   pour valider !")
	while wm.state['buttons']!=8:
		i=0
	setText("Pret ?")
	time.sleep(1)
	setText("Pour lancer la  partie :")
	time.sleep(1)
	setText("Appuyez sur le  bouton A !")
	while wm.state['buttons']!=8: #on presse le bouton A
		i=0
	t0=time.time()
	setText("Partie en cours !")
	lumiere=luminosite.getLuminosite()
	while wm.state['buttons']!=4 and lumiere>150: #condition d'arrêt du capteur de luminosité :
		x = float(nunchuk.get_x(wm))
		y = float(nunchuk.get_y(wm))
		servo.coordonne_to_position_moteur_x(moteur_x,x)
		servo.coordonne_to_position_moteur_y(moteur_y,y)	
		#time.sleep(0.1)
		lumiere=luminosite.getLuminosite()
		if wm.state['buttons']==4096:
			return end()
	servo.stop(moteur_x,moteur_y)
	t=time.time()-t0
        manipfile.writeScore(t)
	setText("Temps"+str(t))
	time.sleep(2)
	if t<25:
		setText("GAGNE !")
		time.sleep(2)
	else:
		setText("PERDU !")
		time.sleep(2)
	moteurs = servo.init()
	setText("Nouvelle partie ?")
	time.sleep(2)
	setText("Si oui, appuyez longtemps sur A")
	time.sleep(2)
	setText("Sinon, appuyez  sur +")
	time.sleep(2)
	if wm.state['buttons']==8:
		partie(wm,moteur_x,moteur_y)
	else:
		setText("Fin de partie")
		time.sleep(2)
		setText("WiiLabyrinthe")



main()





