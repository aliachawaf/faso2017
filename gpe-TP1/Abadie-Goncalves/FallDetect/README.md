Fall Detect

Dispositif d'aide aux personnes agées ayant pour but la détection d'une chute afin de pouvoir alerter les personnes alentours par le biais d'un bip sonore. Ce dispositif permet également la collecte de données liées aux mouvements des personnes et celles-ci sont retransmisent par le biais d'un graphique.

Pour commencer :
    Utiliser la commande "sudo python3 launcher_v1.2.0.py" pour lancer le code du dispositif. Tout se fait automatiquement par la suite.

Prérequis :
    Se rendre sur 
        https://github.com/DexterInd/GrovePi/tree/master/Software/Python/grove_6axis_acc_compass 
    et récupérer le fichier "lsm303d.py" qui est le driver du capteur accéléromètre/gyroscope. Il suffit de le placer dans le dossier "drive/lsm303d/". Ajouter le code dans le raspeberry et celui-ci sera fonctionnel.
    
Structure des répertoires :
    - FallDetect est le répertoire principal du projet. Celui-ci contient :
        - le fichier "launcher_v1.2.0.py" : programme principal
        - le sous répertoire "driver" : contient tous les drivers utiles au fonctionnement du projet
            - "grove" : intéractions avec le shield Grove
            - "led" : driver de la led
            - "buzzer" : driver du buzzer
            - "lsm303d" : driver du capteur accéléromètre/gyroscope
        - le sous répertoire "package" : contient les fichiers de données et le script de génération du graphique
            - "data?.csv" : fichiers de stockage des valeurs et heures pour les axes X, Y et Z
            - "graphe" : contient le script de génération du graphe

Compatibilité :
    - Python 3.4

Auteurs :
    Aubin ABADIE, IG3
    Lucas GONCALVES, IG3