# coding: utf8
#=== === === Abadie - Gonçalves 
#=== === === === = PROJET CHUTE 
#=== === === === === === == IG3
    

#=== === Importation des modules à ajouter
import sys
sys.path.insert(0, r'/home/ScriptChute/Scripts/Demo')
sys.path.insert(0, r'/home/ScriptChute/Scripts/Demo/led')
from graphe.constructor import *
from led import *
from buzzer.buzzer import *
from datetime import datetime
import time
time.sleep(3.0) #On prévoit 10 secondes pour être sur que la personne ai le temps d'accrocher le dispositif 
print('launching')

#Au lancement, on Allume la led générale pour indiquer le fonctionnement du dispositif
turnOn(3)# Car la led se trouve sur le port 3


#On commence la captation des valeurs du gyroscope (dans une fonction dès lors que ce dernier fonctionnera)
valeur = open("donnee_simulee.txt","r")
print("ouverture de valeur correcte")
#turnOn(3)# Car la led se trouve sur le port 3
open('data.csv', 'w').close() #On efface le fichier de saveTemporaitre de la session precedente pour ecrire par dessus 
session = open("data.csv","w") #On ouvre le fichier à nouveau pour y mentionner les nouvelles données. 

#On se connecte au système de captation du gyroscope


#On récupère la valeur d'angle et d'acceleration (pour analyse du déclanchement)
donnee = valeur.readline()

#On enregistre la valeur et l'heure dans le fichier de save
now = datetime.now()

#On récupère l'heure et on la stocke dans une variable 

#On enregistre la valeur "d'acceleration globale" (post traitement des infos) dans un tableau de données 
j=0
while j<5: #Dans la version finale, on s'arrête lorsque le signal d'extinction est enregistré. 
    TableauMoyenne = [] # De longueur 10
   
    #Le tableau est de taille 10 car moyenne sur 5 minutes avec récupération toute les 30 secondes (5x(1/2) = 10)
    i = 0
    while (i < 10): #Nombre d'enregistrements dans un intervalle de 5 minutes
        print("On est au tour",i)
        #On récupère la valeur envoyée par le fichier de calcul (valeur qui indique vitesse ou gyroscopie ou autre)
        donnee = valeur.readline()
        print("On lit correctement la donnée")
        donnee = int(donnee)
        #Si on est dans un cas de chute : 
        if (donnee > 100): #Dans notre cas, il s'agit du seuil de detection
            print("La donnée reçue est une donnée de chute !")
            #On enregistre les valeurs précédentes (celles de la moyenne)
            sommeValeurs = 0
            for data in range (0,i):
                sommeValeurs += TableauMoyenne[i]
            if len(TableauMoyenne) == 0:
                valeurMoyenne = sommeValeurs
            else : 
                valeurMoyenne = sommeValeurs // len(TableauMoyenne)
            print("On a sauvegardé les valeurs normales entre temps")
            
            #On récupère l'heure moyenne des valeurs enregistrées (moins i/2 x 30 secondes)
            heure = now.hour
            minute = now.minute
            minute -= 0.5 * i
            minute = str(minute)
            minute = minute+"\n"
            print("Mise sous forme str de minute : ",minute)
            #On récupère la valeur moyenne de l'intervalle avant detection de la chute : 
            donnee_moyenne = str(valeurMoyenne)+";"+str(heure)+"H"+str(minute)
            session.write("\n")
            #On enregistre la valeur moyenne de detection dans le fichier de session : 
            session.write(donnee_moyenne+"\n")
            print("On a stocké la donnée moyenne dans le fichier")
            #On enregistre la valeur "exeptionnelle" 
            minute = now.minute
            donneeExeptionnelle = str(donnee)+";"+str(heure)+"H"+str(minute)
            session.write(donneeExeptionnelle)
            session.write("\n")
            print("On a stocké la valeur exceptionnelle dans le fichier")
            #On déclanche la sonnerie
            #buzz(7) #Faites sonner les cors d'isengard !
            print("Tu tombes JAMY")
            #stop(7) # Ne faites plus sonner les cors d'isengard !
            time.sleep(5.0) #On annule l'enregistrement temps que la personne se releve ou qu'on l'aide ou autre.
            print("le programme fait une pause de 5 secondes")
            #On reinitialise pour relancer un nouveau tableau moyen d'enregistrement
            i = 0
            
        else: #Dans le cas ou on ne fait pas face à une chute:
            
            #On stocke cette valeur dans un tableau (de taille 10)
            TableauMoyenne.append(donnee)
            i +=1
    moyenne = 0
    for i in range (0, len(TableauMoyenne)-1):
        moyenne += TableauMoyenne[i]
    heure = now.hour
    heure = str(heure)
    print(heure)	
    minuteMoy = now.minute
    print(minuteMoy)
    minuteMoy -= 2
    minuteMoy = str(minuteMoy)
    print(minuteMoy)
    moyenne = moyenne // len(TableauMoyenne)-1
    moyenne = str(moyenne)
    print("valeur moyenne du tableau")
    if isinstance(moyenne, str) :
        print("Conversion faite avec succès")
    else:
        print("Erreur dans le traitement")
    donnee_moyenne = moyenne+";"+str(heure)+"H"+minuteMoy
    session.write(donnee_moyenne)
    session.write("\n")
    print("Le tableau des données moyenne est plein, la moyenne a été faite et enregistrée dans le fichier")
    donnee = 0
    j+=1
    time.sleep(3.0)
        
# === Une fois le signal d'extinction reçue : 


#On ferme le fichier de save temporaire
session.close()
valeur.close() #pour la démo
print("Fin de session, les fichiers ont été fermés")
print("Creation de votre graphe en cours")
#On lance la fonction de création de graphe 
constructeur("data.csv")

#On etteind la led pour indiquer la fin de captation et d'enregistrement
turnOff(3)     
    
