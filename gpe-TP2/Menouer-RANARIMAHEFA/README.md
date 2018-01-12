
=======================
###### README.md ######
=======================

Le fichier ci dessous est écrit en 'Markdown'
Il donnera des indications sur le projet, notamment sur les codes écrits pendant la période de développement

Voici le plan de ce fichier :
- Hierarchie du projet
- Description des fichiers de l'architecture

1. # Hierarchie du projet #

A la racine:

  1. ## Fichier ##
          - main.py
          - DweetPost.py
          - DHT.py

  2. ## Dossier ##
          - dust_sensor

  3. ## contenu du dossier : dust_sensor: ##
          - dust_sensor.ino

2. # Description des fichiers de l'architecture #
    Point d'entree : main.py

    Procedure d'installation du code: televerser ce script sur l'Arduino ensuite débrancher le cable USB-AB de l'ordinateur
    et le brancher sur l'un des ports USB du raspberry.


  1. ## Sur raspberry ##
  Implementation sous python 2.7.9
  Raspberry 3

    1. ### main.py ###
    Programme principal
    Version 4 - 11/01/2018

    2. ### DweetPost.py ###
    Thread qui poste les données sur les service dweet.io tout les 2 secondes
    Le temps d'envoie est a définir selon les besoins de l'utilisateur.
    Version 2 - 11/01/2018

    3. ### DHT.py ###
    Thread qui collecte données du capteur de température/humidité toute les 5 secondes.
    Le temps de relevé est a définir selon les besoins de l'utilisateur.
    Version 2 - 11/01/2018

    4. ## Librairies ##
    grovepi : firmware 1.2.7
    requests : version 2.18.4

  2. ## Arduino ##
  type de Carte : Arduino/Genuino Uno

  Version logiciel :1.8.5

    1. ### dust_sensor.ino ###
      relève les données du capteur de poussiere et l'envoie sur le port Série.
      Version 1 - 11/01/2018
