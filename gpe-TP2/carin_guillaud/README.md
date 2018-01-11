# Sonnette Interactive
**version 3.1 (11/01/2018)**

## Introduction

Notre projet de sonnette interactive a pour objectif d’informer l’utilisateur de la présence d’une personne sonnant à sa porte en son absence. L’utilisateur peut activer le programme lorsqu’il le souhaite. Une fois activé, le programme prend une photo de la personne devant la porte lorsqu’elle sonne. Il propose également à cette personne, via un écran, de laisser un message audio. Pour ce faire, il devra appuyer sur le bouton pour commencer son message, et une nouvelle fois pour le terminer. La photo, ainsi que le message audio éventuel, seront ensuite envoyés à l’utilisateur par mail et stockés sur Google Drive.

## Installation

Pour faire fonctionner la sonnette, voici les différentes étapes :
- Télécharger l’ensemble du répertoire « prog » de Github sur le Raspberry
- Se placer dans le répertoire contenant tous les fichiers et taper la commande « sudo python main.py » qui lance le programme principal


## Architecture

Notre projet est constitué de différents fichiers :

**Fichiers Python (2.7.9) :**

- **main.py :** Contient le programme principal, c’est le programme qui appelle tous les différents fichiers et scripts du projet. Il utilise les librairies suivantes :
	- grovepi (pour utiliser les capteurs comme le bouton)
	- grove_rgb_lcd (pour afficher des messages à l’écran)
	- os (pour effectuer des commandes shell)
	- time (pour gérer le temps).
	
- **enregistrement.py :** Permet d’enregistrer un message audio. Il utilise également les librairies time, grovepi et grove_rgb_lcd. La librairie pyaudio est aussi utilisée pour l’enregistrement vocal.

- **gestionerreur.py :** Permet de rediriger les erreurs dans un fichier, afin de ne pas polluer la console en cas d’erreur.

**Scripts sh :**

- **photo.sh :** prise de la photo.

- **uploadphoto.sh :** envoi d’une photo sur Google Drive et par mail (cas où le visiteur ne souhaite pas laisser de message audio).

- **uploadphotomessage.sh :** envoie d’une photo et d’un message audio sur Google Drive et par mail.

- **maj.sh :** mise à jour de la date et de l’heure sur le Raspberry.


## Matériel

- Raspberry PI
- Grove
- Camera
- Ecran LCD
- Bouton
- Micro USB


## Auteurs

CARIN Maxime et GUILLAUD Nathan - Polytech Montpellier - IG3 - 2017-2018
