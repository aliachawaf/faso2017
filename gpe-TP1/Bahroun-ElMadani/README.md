# Aquarium Intelligent Autonomne
## Hiérarchie du code

Le projet repose sur un site internet constitué d'un fichier HTMl (index.html) et de deux fichiers PHP (traitement.php et delete_dbb.php). Egalement, l'ajout des données capturées se fait à l'aide d'un script python (script.py)

Fichier | Description
------------ | -------------
index.html | Page où l'on arrive en tapant l'adresse du site. Redirige automatiquement vers "traitement.php".
traitement.php | Page principale du site. Permet le suivi des données enregistrées sur un tableau. 
delete_bdd.php | Permet de vider le tableau des données enregistrées en vidant la base de données.
script.py | Permet l'enregistrement des données captées par les capteurs chaque 10 secondes.

Les fichiers index.html, traitement.php et delete_bdd.php doivent être dans le même dossier sur le raspberry. Le fichier script.py peut être dans un dossier à part. 

## Guide d'utilisation

Pour utiliser le dispositif, branchez le raspberry en réseau (ou vous pouvez également y accéder en branchant un écran et un clavier au raspberry directement), lancez votre navigateur Internet et tapez dans la barre de recherche "162.38.111.124". Vous accéderez au site qui vous affiche les données captées par le dispositif chaque 10 secondes. 

## Dispositifs utilisés
* Raspberry Pi 3, Model B, 1 GB RAM<addr>
* Arduino Uno REV3 <addr>
* Base Shield V2 <addr>

## Versions logicielles

* Python 2.7.13<addr>
* Bibliothèques : <addr>
	* Pour Arduino : OneWire, RGB_LCD <addr>
	* Pour Raspberry : Serial, MySQLdb, time <addr>

## Informations

* Version : 1.0.0
* Mise à Jour : 11/01/2017
