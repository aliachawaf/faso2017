import sys
sys.path.insert(0, r'/home/igwall/FallDetect/driver/buzzer')
sys.path.insert(0, r'/home/igwall/FallDetect/driver/led')
#sys.path.insert(0, r'/home/igwall/FallDetect/driver/lsm303d')
sys.path.insert(0, r'/home/igwall/FallDetect/driver/')
sys.path.insert(0, r'home/igwall/FallDetect/package')
from buzzer.buzzer import *
from lsm303d import lsm303d
from led.led import *
import time
from datetime import datetime
from threading import Timer


def speedCalculX():
    acc_mag=lsm303d.lsm303d()
    acc=acc_mag.getRealAccel()
    heading= acc_mag.getHeading()
    accInit = acc[0]
    time.sleep(0.1)
    acc=acc_mag.getRealAccel()
    heading= acc_mag.getHeading()
    accFin = acc[0]
    vitesseX = (accFin - accInit)*0.1
    return vitesseX



def speedCalculY():
    acc_mag=lsm303d.lsm303d()
    acc=acc_mag.getRealAccel()
    heading= acc_mag.getHeading()
    accInit = acc[0]
    time.sleep(0.1)
    acc=acc_mag.getRealAccel()
    heading= acc_mag.getHeading()
    accFin = acc[0]
    vitesseY = (accFin - accInit)*0.1
    return vitesseY



def speedCalculZ():
    acc_mag=lsm303d.lsm303d()
    acc=acc_mag.getRealAccel()
    heading= acc_mag.getHeading()
    accInit = acc[0]
    time.sleep(0.1)
    acc=acc_mag.getRealAccel()
    heading= acc_mag.getHeading()
    accFin = acc[0]
    vitesseZ = (accFin - accInit)* 0.1 #Vitesse = acc Fin moins acc Init * delais
    return vitesseZ    
    

# === PLUS UTILISE === #       
def minDegree(): #On fait un calcul de minDegree pendant 10 secondes
	minDegree = 1000
	fin = time.time() + 10 # l'heure actuelle + 10 (en secondes depuis epoch)
	while time.time()<fin:
		# fin attente des 10 secondes
		degree = acc_mag.getHeading()
		print(minDegree, degree)
		if minDegree >= degree : 
			minDegree = degree 
	return minDegree


# === PLUS UTILISE === #
def maxDegree(): 
	maxDegree = 10
	fin = time.time() + 10 # l'heure actuelle + 10 (en secondes depuis epoch)
	while time.time()<fin:
	# fin attente des 10 secondes
		degree = acc_mag.getHeading()
		print(minDegree, degree)
		if maxDegree <= degree : 
			maxDegree = degree 
	return maxDegree



def getSpeedChute():

    speedX = speedCalculX()
    speedY = speedCalculY()
    speedZ = speedCalculZ()

    print("X vitesse: ",speedX," Y vitesse : ",speedY," Z speed : " ,speedZ)
    #Conditions liées a une chute
    if speedX > 0.1  or speedX < -0.1  or speedY < -0.08  or speedY>0.08  or speedZ < -0.08  or speedZ > 0.08  and speedX < 9 and speedY < 9 and speedZ < 9 and speedZ >-9 and speedX > -9 and speedY > -9 : 
            buzz(7)
            chute = True
    else:
            stop(7)
            chute = False
    return speedX, speedY, speedZ, chute


# === ==== ==== Programme principal ==== ==== ==== ==== #

#Ouverture des fichiers d'enregistrement: 
#     Un fichier est prévu pour chacun des axes
#     Ils 'enregistrent en même temps mais permettent d'avoir un enregistrement assuré 
#     en cas de défaillance d'un des axes.


open('~/FallDetect/package/dataX.csv', 'w').close() #On efface le fichier de saveTemporaitre de la session precedente pour ecrire par dessus 
sessionX = open("~/FallDetect/package/dataX.csv","w") 

open('~/FallDetect/package/dataY.csv', 'w').close() #On efface le fichier de saveTemporaitre de la session precedente pour ecrire par dessus 
sessionY = open("~/FallDetect/package/dataY.csv","w") 

open('~/FallDetect/package/dataZ.csv', 'w').close() #On efface le fichier de saveTemporaitre de la session precedente pour ecrire par dessus 
sessionZ = open("~/FallDetect/package/dataZ.csv","w") 

datetime = datetime.now()

# === On lance une première lecture "dans le vide" afin d'éviter les problème d'analyse sur la premiere valeur
speedX = speedCalculX()
speedY = speedCalculY()
speedZ = speedCalculZ()


while True:
    turnOn(4)
 
    # Tableaux qui servent à faire un calcul de données moyennes
    #Le tableau est de taille 10 car moyenne sur 10 minutes avec récupération toute les minutes
    TableauMoyenneX = [] # De longueur 10
    TableauMoyenneY = [] # De longueur 10
    TableauMoyenneZ = [] # De longueur 10
    
    # Variables qui permettent de stocker une donnée moyenne
    sommeValeursX = 0
    sommeValeursY = 0
    sommeValeursZ = 0
    
    
    
    i = 0
    # Calcul de l'intervalle de durée d'enregistrement : Pour être sûr d'enregistrer 5 min après captation
    intervalle = datetime.now()
    intervalle = intervalle = intervalle.minute

    if intervalle+1 > 60 :
        intervalle = 60 - intervalle+1
    else :
        intervalle = intervalle

    while (i < 10): #Nombre d'enregistrements dans un intervalle de 10 minutes de données "moyennes"
        timer = datetime.now()
        timer = timer.minute
        #on récupère les données de mouvement et la fonction de detection de chute
        speedX, speedY, speedZ, chute = getSpeedChute()
        speedX *= 300
        speedY *= 300
        speedZ *= 300
        

        if not(chute) and intervalle+1 == timer :
            if speedX < 0 :
                speedX *= -1

            if speedY < 0 : 
                speedY *= -1

            if speedZ < 0 : 
                speedZ *= -1

            TableauMoyenneX.append(speedX)
            TableauMoyenneY.append(speedY)
            TableauMoyenneZ.append(speedZ)

            i +=1
            
        elif chute : 
            print("La donnée reçue est une donnée de chute !")
            #On enregistre les valeurs précédentes (celles de la moyenne)
            
            for data in range (0,i):
                sommeValeursX += TableauMoyenneX[i]
                sommeValeursY += TableauMoyenneY[i]
                sommeValeursZ += TableauMoyenneZ[i]
                
            if len(TableauMoyenneX) == 0:
                valeurMoyenneX = sommeValeursX
                valeurMoyenneY = sommeValeursY
                valeurMoyenneZ = sommeValeursZ
            else : 
                valeurMoyenneX = sommeValeursX // len(TableauMoyenneX)
                valeurMoyenneY = sommeValeursY // len(TableauMoyenneY)
                valeurMoyenneZ = sommeValeursZ // len(TableauMoyenneZ)
                
            print("On a sauvegardé les valeurs normales entre temps")

            #On récupère l'heure moyenne des valeurs enregistrées (moins i/2 x 30 secondes)
            heureActuelle = datetime.now()
            heure = heureActuelle.hour

            minute = heureActuelle.minute
            minute -= i
            if minute <=0 :
                temp = minute
                minute = 60 -temp
                heure = heure -1
            if heure < 0 :
                heure = 23
            
            minute = str(minute)
            minute = minute+"\n"
            print("Mise sous forme str de minute : ",minute)

            #On récupère la valeur moyenne de l'intervalle avant detection de la chute : 
            donnee_moyenneX = str(valeurMoyenneX)+";"+str(heure)+"H"+str(minute)
            donnee_moyenneY = str(valeurMoyenneY)+";"+str(heure)+"H"+str(minute)
            donnee_moyenneZ = str(valeurMoyenneZ)+";"+str(heure)+"H"+str(minute)

            #On enregistre les sauts de ligne 
            sessionX.write("\n")
            sessionY.write("\n")
            sessionZ.write("\n")

            #On enregistre les valeurs moyennes de detection dans le fichier de session : 
            sessionX.write(donnee_moyenneX)
            sessionY.write(donnee_moyenneY)
            sessionZ.write(donnee_moyenneZ)
            
            #On enregistre les sauts de ligne 
            #sessionX.write("\n")
            #sessionY.write("\n")
            #sessionZ.write("\n")
            print("On a stocké la donnée moyenne dans le fichier")
            

            #On multiplie els valeurs par 100 pour que les données soient plus "prononcées et lisibles" lors de la création du tableau 
            speedX *= 100
            speedY *= 100
            speedZ *= 100
            
            #On enregistre la valeur "exeptionnelle, on la converti d'abord en nombre positif"
            
            
            if speedX < 0 :
                speedX *= -1

            if speedY < 0 : 
                speedY *= -1

            if speedZ < 0 : 
                speedZ *= -1

            heureActuelle = datetime.now()
            heure = heureActuelle.hour
            minute = heureActuelle.minute
            donneeExeptionnelleX = str(speedX)+";"+str(heure)+"H"+str(minute)
            donneeExeptionnelleY = str(speedY)+";"+str(heure)+"H"+str(minute)
            donneeExeptionnelleZ = str(speedZ)+";"+str(heure)+"H"+str(minute)

            #On enregistre la donnée exeptionnelle sur les trois axes
            sessionX.write(donneeExeptionnelleX)
            sessionY.write(donneeExeptionnelleY)
            sessionZ.write(donneeExeptionnelleZ)

            sessionX.write("\n")
            sessionY.write("\n")
            sessionZ.write("\n")
            print("On a stocké les valeurs exceptionnelles dans le fichier")

            time.sleep(8.0) #On annule l'enregistrement temps que la personne se releve ou qu'on l'aide ou autre.
            print("le programme fait une pause de 8 secondes, on se relève")

            #On reinitialise pour relancer un nouveau tableau d'enregistrement des valeurs moyennes
            i = 0
            
            TableauMoyenneX = [] # De longueur 10
            TableauMoyenneY = [] # De longueur 10
            TableauMoyenneZ = [] # De longueur 10

        else: #Dans le cas ou on ne fait pas face à une chute:

            print("Pas d'enregistrement de valeurs")

# On est dans le cas ou le tableau est plein mais que l'on a pas de chute, on doit donc enregistrée la donnée moyenne résultante du tableau
    moyenneX = 0
    moyenneY = 0
    moyenneZ = 0
    for i in range (0, len(TableauMoyenneX)-1):
        moyenneX += TableauMoyenneX[i]
        moyenneY += TableauMoyenneY[i]
        moyenneZ += TableauMoyenneZ[i]
    heureActuelle = datetime.now()
    heure = heureActuelle.hour
    print(heure)	
    minuteMoy = heureActuelle.minute


    print(minuteMoy)
    minuteMoy -= i

#On fait attention au cas ou l'erreur peux survenir à 12h03 par exemple ce qui fausse les minutes
    # On fait également attention aux heures
    if minuteMoy <0 :
        temp = minute
        minute = 60 -temp
        heure = heure -1
    if heure < 0 :
        heure = 23

    minuteMoy = str(minuteMoy)
    print(minuteMoy)

    moyenneX = moyenneX // len(TableauMoyenneX)-1
    moyenneY = moyenneY // len(TableauMoyenneY)-1
    moyenneZ = moyenneZ // len(TableauMoyenneZ)-1

    moyenneX = str(moyenneX)
    moyenneY = str(moyenneY)
    moyenneZ = str(moyenneZ)


    print("valeur moyenne du tableau")
    if isinstance(moyenneX, str) and isinstance(moyenneY, str) and isinstance(moyenneZ, str) :
        print("Conversion faite avec succès")
    else:
        print("Erreur dans le traitement")


    donnee_moyenneX = moyenneX+";"+str(heure)+"H"+minuteMoy
    donnee_moyenneY = moyenneY+";"+str(heure)+"H"+minuteMoy
    donnee_moyenneZ = moyenneZ+";"+str(heure)+"H"+minuteMoy

    sessionX.write(donnee_moyenneX)
    sessionY.write(donnee_moyenneY)
    sessionZ.write(donnee_moyenneZ)

    sessionX.write("\n")
    sessionY.write("\n")
    sessionZ.write("\n")

    #On reinitialise le tableau d'enregistrement des données
    TableauMoyenneX = [] # De longueur 10
    TableauMoyenneY = [] # De longueur 10
    TableauMoyenneZ = [] # De longueur 10
    i = 0




