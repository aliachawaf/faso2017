#!/usr/bin/env python
#-*- coding: utf-8 -*-

from Affichage import *
#from chrono.Chronometre import *
from Exercices import *

from Bouton import *
sensor = 1
from grovepi import *
#if __name__== '__main__'

#Fonction utiles pour les entrainements :


Fin = False
mesures=[]

def PrisesDesMesures():
    global Fin    
    #Prend les mesures 
    AffichageMesurePompe()
    ValidationMesures = True #veut dire qu'il passe
    #On met aussi la possibilité qu'il appuie plus de 5 sec auquel cas ca n'arrête pas tout.
    while ValidationMesures == True and Fin == False:
        mesuresPompe = PriseDeMesure()
        while mesuresPompe< 3 or mesuresPompe >40:
            digitalWrite(buzzer,1)
            Affichage("La prise n'est pas bonne ")
            time.sleep(3)
            digitalWrite(buzzer,0)
            Affichage("Recommencez")
            time.sleep(3)
            AffichageMesurePompe()
            mesuresPompe = PriseDeMesure()
        AffichageMesureFin()
        ValidationMesures = DemandeUtil(False)
        
    
    ValidationMesures = True
    
    while ValidationMesures == True and Fin == False:
        AffichageMesureGainage()
        mesuresGainage = PriseDeMesure()
        while mesuresGainage< 3 or mesuresGainage >40:
            digitalWrite(buzzer,1)
            Affichage("La prise n'est pas bonne ")
            time.sleep(3)
            digitalWrite(buzzer,0)
            Affichage("Recommencez")
            time.sleep(3)
            AffichageMesureGainage()
            mesuresGainage = PriseDeMesure()
            
        Affichage("Garder les mesures ? ")
        ValidationMesures = DemandeUtil(False)
    print([mesuresPompe,mesuresGainage])
    
    
    time.sleep(3)
    return [mesuresPompe,mesuresGainage]

#test
#PrisesdesMesures()

def DemandeUtil(continu):
    #Interprète BoutonInteract
    #renvoie False si l'util veut arrêter l'exo 
    #instantannément renv si util appui
    #Pour 3 
    global Fin
    global mesures #ca cherche dans les autres fonction ?
    appuie = BoutonInteract(continu)
    if appuie == 1 :
        mesures = PrisesDesMesures() #Reprendre ses mesures ca n'arrête pas la série
        return True
        #la prise de mesure renvoie
    if appuie == 0 :
        return False
    if appuie == 2 :
        Fin = True
        return False
    else :
        return True #sert pour quand on est en sondage permanent et qu'il y a des fois où le bouton n'est pas appuyé

def ComptePompe():
    #Je pense que ca va boucler sans discontinue avec les pompes
    #Sauf quand va rentrer dans boucle while car descendu assez bas
    #alors devra sortir boucle pour intéragir avec bouton
    #Donc il faut qu'au moment d'arrêter l'exercice il s'éloigne du capteur
    #
    global Fin
    global mesures #On cherche mesure car peut changer en cours de série
    PompesValideBas = 5
    pompes = 0
    compteur = -1
    Affichage("On passe aux pompes")
    time.sleep(3)
    while DemandeUtil(True) == True and (PriseDeMesure()> mesures[0] + 4) or (PriseDeMesure()< mesures[0] - 4):
        Affichage("Mettez-vous en position")
        time.sleep(1)
    Affichage("C'est partit !!")
    time.sleep(2)
    while DemandeUtil(True) == True and Fin ==False: 
            #tant que pompe rentre pas dans boucle va sonder valeur bouton
            #Aucun try tout se fait en direct
            #est ce que dès que va en bas ca detecte et rentre dans boucle ?
            if pompes > compteur :
                Affichage("Nombre de pompe =" + str(pompes))
                compteur = pompes
                #Pour afficher que quand une pompe supplémentaire
            if Pompe(PompesValideBas,mesures[0]):

                #si la pompe est validée
                pompes = pompes + 1
                
                
    return pompes


def Test_Capteur_Distance():
        while True :
            Affichage(str(PriseDeMesure()))
            time.sleep(0.2)
        return 0

def ChronoGainage():
    #renvoie le temps de gainage effectué jusqu'à ce que l'utilisateur
    #appuie sur le bouton pour passer
    global Fin
    global mesures #On cherche mesure car peut changer en cours de série
    BonnePosition = mesures[1]
    temps = 0
    Affichage("On passe au gainage")
    time.sleep(4)
    while DemandeUtil(True) == True and (PriseDeMesure()> BonnePosition + 4) or (PriseDeMesure()< BonnePosition - 4):
        Affichage("Mettez-vous en position")
        time.sleep(1)
    
    Affichage("C'est partit !!")
    time.sleep(2)
    while DemandeUtil(True) == True and Fin == False: 
           #Sonde toutes les secondes si y a une faute
           #si pas de faute avance de 1 sec
           #si faute attend 2 secondes et bip
                temps = temps + ControleGainage(BonnePosition)
                Affichage("Temps de gainage = " + str(temps))
    return temps




def ComptePompeSecours(Bas):
    #Compte les pompes mais s'arrête pas avec le bouton
    #renvoie la distance
    nbPompe=0
    a=temp(sensor, '1.1')
    Affichage(str(a)) 
    while True :
            try :
                dist = ultrasonicRead(ultrasonic_ranger)
                if (dist< Bas):
                        digitalWrite(buzzer,1)
                        time.sleep(2)
                        nbPompe = nbPompe + 1
                        Affichage(str(nbPompe))
                        digitalWrite(buzzer,0) 
            
        
                        digitalWrite(buzzer,0)
                        time.sleep(2)
            except :
                return 0



    #return nbPompe
#Entrainements
#

def pause():
    #Arrête l'entrainement et chronomètre la pause
    temps = 0
    i=0
    global Fin
    while DemandeUtil(True) == True and Fin ==False:
                #Sondage en continu
        #il faut appuyer plus de 1 seconde car sinon peut que demandeUtil ne soit pas scruté 
        #car timesleep fait des pauses de 1 secondes
        #autre solution le threading (progra parallèle mais trop compliqué)
        time.sleep(0.1)
        i=i+1
        if i == 10 :
            #Pour ne pas afficher trop de temps ca clignote
            temps = temps + 1
            Affichage("Temps de pause = " + str(temps))
            i=0
    return temps

def AffichageDebut():
   #Affiche le tutoriel à l'écran lcd
   time.sleep(1)
   Affichage("Bienvenue sur votre Sport Trainer")
   time.sleep(8)
   Affichage("Pour passer le tutoriel appuyez ")
   time.sleep(3)
   Affichage("sur le bouton plus de 3 secondes")
   if BoutonInteract(False) !=1  and Fin ==False : 
                time.sleep(3)
                Affichage("Vous allez dialoguer avec ")
                time.sleep(3)
                Affichage("votre entraineur")
                time.sleep(3)
                Affichage("au moyens d'un bouton")
                time.sleep(3)
                Affichage(" entre 0 et 3 sec vous passez")
                time.sleep(3)
                Affichage("a l'etape suivante")
                time.sleep(2)
                Affichage("entre 3 et 7 sec vous ")
                time.sleep(3)
                Affichage("reprenez vos mesures")
                time.sleep(3)
                Affichage("plus de 7 sec vous ")
                time.sleep(3)
                Affichage("arretez l'entraînement")
                time.sleep(3)
                Affichage("Essayez ! appuyez entre 0 et ")
                time.sleep(3)
                Affichage("3 secondes sur le bouton")
                time.sleep(3)
                while BoutonInteract(False) != 0   :
                          Affichage("Non reessayez ! ")
                Affichage("Bravo ! ")
                time.sleep(3)
   Affichage("Commencons l'entrainement")
   time.sleep(3)
   return 0

#ComptePompe(150)
def entrainement1():
    #Procédure de l'entrainement 1
    AffichageDebut()
    global mesures
    Affichage("Pour commencer")
    time.sleep(3)
    mesures = PrisesDesMesures()
    Affichage("On va commencer l'entrainement")
    time.sleep(4)
    global Fin
    ResultatsEntrainement = []
    while True  :
           if Fin :
                   
                   break
           pompes1 = ComptePompe()
           if Fin :
                   
                   break
           ResultatsEntrainement = ResultatsEntrainement +[(1,pompes1,0)]
           
           tempsPause = pause()
          
        #Vérif si l'util veut arrêter ou pas
        #Global Fin marche t'elle ?
           if Fin :
                   break
           pompes2 = ComptePompe()
           if Fin :
                   
                   break
           ResultatsEntrainement = ResultatsEntrainement +[(1,pompes2,tempsPause)]
           
           tempsPause = pause()
           print(ResultatsEntrainement)
           #Si la pause n'est pas fini quand on arrête l'entrainement alors elle ne sera pas comptabilisée dans les stats
        #Vérif si l'util veut arrêter ou pas
        #Global Fin marche t'elle ?
           if Fin :
                   break
        # Fin Vérif
        
           gainage1 = ChronoGainage()
           ResultatsEntrainement = ResultatsEntrainement + [(2,gainage1,tempsPause)]
           print(ResultatsEntrainement)
        #pause()
        #Vérif si l'util veut arrêter ou pas
           if Fin :
                   break
           tempsPause = pause()
           if Fin :
                   break 
           gainag1 = ChronoGainage()
           ResultatsEntrainement = ResultatsEntrainement + [(2,gainage2,tempsPause)]
        #pause()
        #Vérif si l'util veut arrêter ou pas
           if Fin :
                   break 
        #pompes2 = ComptePompe( mesures[0])
        #ResultatsEntrainement = ResultatsEntrainement +[(1,pompes2,tempsPause)]
        #tempsPause = pause()
        #Vérif si l'util veut arrêter ou pas
        #Global Fin marche t'elle ?
           
        # Fin Vérif
           Affichage("Fin d'entrainement au revoir")
           time.sleep(5)
           Affichage("Regardez vos stats à l'ecran")
           print(ResultatsEntrainement)
           return ResultatsEntrainement
    Affichage("Vous vous en allez ? au revoir")
    time.sleep(5)
    Affichage("Regardez vos stats à l'ecran")
    
    return ResultatsEntrainement
        


def entrainement2():
    #Procédure de l'entrainement 1
    #AffichageDebut()
    global mesures
    mesures = PrisesDesMesures()
    Affichage("On va commencer l'entrainement")
    time.sleep(4)
    global Fin
    ResultatsEntrainement = []
    while True  :
           if Fin :
                   
                   break
           pompes1 = ComptePompe()
           if Fin :
                   
                   break
           ResultatsEntrainement = ResultatsEntrainement +[(1,pompes1,0)]
           
           tempsPause = pause()
          
        #Vérif si l'util veut arrêter ou pas
        #Global Fin marche t'elle ?
           if Fin :
                   break
           tempsPause = pause()
           if Fin :
                   break 
           gainage1 = ChronoGainage()
           ResultatsEntrainement = ResultatsEntrainement +[(2,gainage1,tempsPause)]
        #pause()
        #Vérif si l'util veut arrêter ou pas
           if Fin :
                   break  
           pompes2 = ComptePompe()
           if Fin :
                   
                   break
           ResultatsEntrainement = ResultatsEntrainement +[(1,pompes2,0)]
           
           tempsPause = pause()
          
        #Vérif si l'util veut arrêter ou pas
        #Global Fin marche t'elle ?
           if Fin :
                   break
        # Fin Vérif
        
           gainage1 = ChronoGainage()
           ResultatsEntrainement = ResultatsEntrainement +[(2,gainage1,tempsPause)]
        #pause()
        #Vérif si l'util veut arrêter ou pas
           if Fin :
                   break
           tempsPause = pause()
           if Fin :
                   break 
           gainage1 = ChronoGainage()
           ResultatsEntrainement = ResultatsEntrainement +[(2,gainage1,tempsPause)]
        #pause()
        #Vérif si l'util veut arrêter ou pas
           if Fin :
                   break 
        #pompes2 = ComptePompe( mesures[0])
        #ResultatsEntrainement = ResultatsEntrainement +[(1,pompes2,tempsPause)]
        #tempsPause = pause()
        #Vérif si l'util veut arrêter ou pas
        #Global Fin marche t'elle ?
           
        # Fin Vérif

           return ResultatsEntrainement
    Affichage("Fin d'entrainement au revoir")
    time.sleep(5)
    Affichage("Regardez vos stats à l'ecran")
    
    return ResultatsEntrainement




def entrainement3():
    #Procédure de l'entrainement 1
    #AffichageDebut()
    global mesures
    mesures = PrisesDesMesures()
    Affichage("On va commencer l'entrainement")
    time.sleep(4)
    global Fin
    ResultatsEntrainement = []
    while True  :
           if Fin :
                   
                   break
           pompes1 = ComptePompe()
           if Fin :
                   
                   break
           ResultatsEntrainement = ResultatsEntrainement +[(1,pompes1,0)]
           
           tempsPause = pause()
          
        #Vérif si l'util veut arrêter ou pas
        #Global Fin marche t'elle ?
           if Fin :
                   break
           pompes2 = ComptePompe()
           if Fin :
                   
                   break
           ResultatsEntrainement = ResultatsEntrainement +[(1,pompes2,0)]
           
           tempsPause = pause()
          
        #Vérif si l'util veut arrêter ou pas
        #Global Fin marche t'elle ?
           if Fin :
                   break
        # Fin Vérif
        
           gainage1 = ChronoGainage()
           ResultatsEntrainement = ResultatsEntrainement +[(2,gainage1,tempsPause)]
        #pause()
        #Vérif si l'util veut arrêter ou pas
           if Fin :
                   break
           tempsPause = pause()
           if Fin :
                   break 
           gainage1 = ChronoGainage()
           ResultatsEntrainement = ResultatsEntrainement +[(2,gainage1,tempsPause)]
        #pause()
        #Vérif si l'util veut arrêter ou pas
           if Fin :
                   break 
        #pompes2 = ComptePompe( mesures[0])
        #ResultatsEntrainement = ResultatsEntrainement +[(1,pompes2,tempsPause)]
        #tempsPause = pause()
        #Vérif si l'util veut arrêter ou pas
        #Global Fin marche t'elle ?
           
        # Fin Vérif
           return ResultatsEntrainement
           
    Affichage("Fin d'entrainement au revoir")
    time.sleep(5)
    Affichage("Regardez vos stats à l'ecran")
    
    return ResultatsEntrainement
#Main  

def mainDeSecours():
    fin = "n"
    while fin !="o":
        #Invariant de boucle : fin différent de o
        ask1 = 7
        while ask1 != 1 and ask1 != 0 :
            ask1 = input("Voulez vous découvrir les entraînements (1/0) ou en choisir directement un ? ")
        if ask1 == 1 :
            print("Quand vous aurez fini de consulter le guide pressez entrer")
            #AfficherGuide()
            
        
        ask2=input("Quel entrainement voulez-vous faire ? 1-3  ")
        print("Lisez attentivement le manuel d'utilisation pour savoir comment se déroule un entraînement")
        if ask2 == 1:
            entrainement1 = entrainement1()
            AffichageValeurs(entrainement1)
        elif ask2 == 2 :
            entrainement2 = entrainement2()
            AffichageValeurs(entrainement2)
        elif ask2 == 3 :
            entrainement3 = entrainement3()
            AffichageValeurs(entrainement3)
        #ask4=input("Voir vos statistiques ? o/n")
        #if ask4 == "o":
        #   AffichageStat()


        fin= input ("voulez vous arrêter o/n")
        return 0

