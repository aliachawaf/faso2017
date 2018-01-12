# Perfect Morning

Notre code se compose de deux parties : une **partie Réelle** pour un code qui fonctionne durant une nuit complète et une **partie Démo** qui permet de montrer que le code nuit fonctionne, mais de manière condensée. 


## Partie Réelle
C'est le *vrai* code du projet. 

La **partie Réelle** comporte les fichiers suivants : 

### analyse.py
Ce fichier contient les fonctions pour analyser le sommeil de l'utilisateur

### captCard.py
Ce fichier contient les fonctions nécessaires pour lire le rythme cardiaque de l'utilisateur

### configReveil.py
Ce fichier contient les fonctions permettant de configurer le réveil avec l'écran

### grovepi.py
Ce fichier correspond au driver permettant de contrôler le Shield Grove Pi et les capteurs branchés dessus

### grovepi_rgb_lcd.py
Ce fichier correspond au driver permettant de contrôler l'écran LCD

### ledBuz.py
Ce fichier contient les fonctions permettant de contrôler le système de réveil, ici le bandeau LEDs

### led.py
Ce fichier contient les fonctions permettant de contrôler les LEDs témoins 

### main.py
C'est **le** fichier du PerfectMorning. Il contient le programme principal permettant le bon fonctionnement du dispositif 

**Le main imprime des informations dans le Terminal. Ceci sert de log si besoin.**

### sendCloud.py
Ce fichier contient les fonctions permettant d'envoyer les informations sur le Cloud

**Pour visualiser les données envoyées par le programme il faut se rendre sur ce lien suivant :** 
https://thingspeak.com/channels/370116 

### sendTemp.py 
Ce fichier contient les fonctions permettant de lire la température et l'humidité sur le capteur DHT

### timeScreen.py
Ce fichier contient les fonctions permettant d'afficher l'heure et l'information concernant le réveil, sur l'écran 

## Partie Demo 

La partie démo contient les mêmes fichiers que la partie Réelle mais ces derniers ont été modifiés pour pouvoir témoigner du bon fonctionnement du dispositif mais sur un temps restreint. Par exemple, dans cette partie, les données du capteur cardiaque sont dans une liste qui sera lue rapidement pour simuler une nuit.  

