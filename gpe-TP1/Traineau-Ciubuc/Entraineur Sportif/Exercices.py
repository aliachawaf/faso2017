
from grove.grovepi import *
import time
#-*- coding: utf-8 -*-


ultrasonic_ranger = 4
buzzer = 7 #On met le buzzer sur le port D8

# DistancePompeValide = 150

def Pompe(DistancePompeValideBas,Haut):
    #
    #detecte si une pompe se fait et renvoie True si elle est effectuee
	nbPompe=0
        try:
		dist = ultrasonicRead(ultrasonic_ranger)
		if (dist<DistancePompeValide) :

                        digitalWrite(buzzer,.1) #buzz qd pompe valide en bas 
                        time.sleep(1)
                        while (dist < Haut-40) and (dist > DistancePompeValide): 
                            #Si fait pas bien la pompe et remonte pas suffisemment
                            #alors la pompe ne sera pas comptee.
                            dist = ultrasonicRead(ultrasonic_ranger)
                            if (dist > Haut-40) :
                                return True
                                digitalWrite(buzzer,.1) #buzz qd pompe valide en haut

		else:
			digitalWrite(buzzer,0)
			time.sleep(2)

    #if  BoutonStop():
    #break
        # except KeyboardInterrupt:
        #     digitalWrite(buzzer, 0)
        #     break
    # except DemandeUtil() != True:
    #     digitalWrite(buzzer, 0)

			return False
                        #return dans un try ?
	except:
		pass



def ControleGainage(DistanceValide):
	#Emet un bruit de 1 seconde lorsque l'utillisateur a une mauvaise position ce qui equivaut a etre en dehors de l'intervalle de 10cm autour de la valeur DitanceValide
	#S'arrete lorsque BoutonStop() est vraie
	#Retourne le temps de gainage
	try:
		dist = ultrasonicRead(ultrasonic_ranger)
                if (dist > (DistanceValide + 1) or dist < DistanceValide - 1):
                    #regarder cb vaut 1 d'acard en cm
                    digitalWrite(buzzer,1)
                    time.sleep(2)
                    temps = temps + 2
                        
                else:
                    digitalWrite(buzzer,0)
                    time.sleep(1)
                    temps = temps +1
		Affichage(temps)
          #   except KeyboardInterrupt:
        		# digitalWrite(buzzer, 0)
          #   	break
          #   except DemandeUtil() != True:
          #       digitalWrite(buzzer, 0)
		return temps
	except:
		pass


def PriseDeMesure():
    #Prend une mesure en la renvoie
    # AffichageMesurePompe():
    #while ask != True :
        dist = ultrasonicRead(ultrasonic_ranger)
       
            # ask == BoutonUtil()
	return dist
    




