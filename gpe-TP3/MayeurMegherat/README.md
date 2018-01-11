# Projet RaspSecuriPi

date: 11/01/2018
version du projet: 1.0

## Hiérachie du code

Le dossier `FASlocalisation` contient le projet Android Studio de l'application android
Le dossier `raspberry` contient les fichiers à mettre sur le Raspberry Pi
Le dossier `serveur-projet-fas-ig3` contient le serveur python, il est à installer sur le Google App Engine.

## Installation du code

Prérequis :
* python 2.7

Il n'est possible de récuperer l'application sur son smartphone qu'à l'aide
de Android Studio pour le moment.

Il faut récuperer le code du projet sur la raspberry à l'aide de la commande:
`scp raspberry/ pi@<ip-du-raspberry>:~`
Il n'y a pas besoin de compilation pour le code python.
Le code du projet se lance à l'aide de la commande `python projet.py`.
