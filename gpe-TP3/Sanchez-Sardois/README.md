Enceinte intelligente
======
###### Sanchez Alexis & Sardois Lucas

L'idée est de pouvoir controller une enceinte connecté à l'aide de commande vocale.

Elle pourra rechercher parmis tous les titres présents sur internet et créer des playlists personalisé.

Architecture
======
Le projet est divisé en 2 grandes parties :

* La partie enceinte, qui regroupe tous les programmes liés au fonctionnement de l'enceinte, comme par exemple la reconnaissance vocale, la recherche de musique etc...
* La partie application Android, qui regroupe tout le code permettant de communiqué avec l'enceinte via bluetooth

Materiels
======
* [Microphone](https://www.amazon.fr/SunFounder-Microphone-Raspberry-Recognition-Software/dp/B01KLRBHGM)
* [Haut Parleur](https://www.gotronic.fr/art-haut-parleur-cordon-jack-22392.htm)
* Raspberry Pi 3
* Device Android

Bibliothéques et dépendances
======
Python 3
* [Speech recognition pour Python][1] et toutes ses dépendances
* Les dernières versions de bluetooth et PyBlueEz
* [Python for vlc][2]
* [Pafy][3]

[1]: https://pypi.python.org/pypi/SpeechRecognition/
[2]: https://pypi.python.org/pypi/python-vlc/2.2.6100
[3]: https://pypi.python.org/pypi/pafy
