PROJET FASO 2017 : WIILABYRINTHE

REALISE PAR :

- DEBEIR Luca
- MAS Lucas


INTRODUCTION :

Le WiiLabyrinthe est un jeu, dont le principe est de faire bouger le labyrinthe amovible à
l'aide d'une Nunchuck, connecté à une Wiimote, pour faire tomber une bille au centre du labyrinthe. La partie
est chronométrée, et pour gagner, il faut aller au centre du labyrinthe en moins de 25 secondes.


FICHIERS :

- luminosite.py : permet de récupérer les données du capteur de luminosité installé sur notre labyrinthe.

- servo.py : permet de manipuler les servomteurs en fonction des données qu'on lui envoie.

- nunchuck.py : permet de récupérer les données envoyées depuis la nunchuck.

- pp.py : programme principal. Il permet de faire une partie sur le WiiLabyrinthe.


MATERIEL :

- Raspberry Pi 3, Model B, 1 GB RAM

- Grove

- Ecran LCD

- Capteur de luminosité

- Servomoteurs HS422

- Labyrinthe en bois



PROCEDURE D'INSTALLATION :

- Afin de démarrer une partie sur le WiiLabyrinthe, il faut se connecter depuis un terminal sur le Raspberry du
WiiLabyrinthe.

- Tapez sur le terminal : "ssh pi@192.168.43.35".

- Ensuite tapez "cd WiiLabyrinthe".

- Et pour démarrer la partie, tapez "sudo python pp.py".

- A vous de jouez !


VERSIONS DES LOGICIELS ET DES BIBLIOTHEQUES :

- Python : 2.7.13
- GrovePi : 1.2.2
- Cwiid : 3.0.0


INFORMATIONS :

- Version: 1.0
- Mise à jour : 11/01/2018
