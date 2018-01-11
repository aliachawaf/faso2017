HIERARCHIE DU CODE - PROJET SMP-2000

V2.0 - 10/01/2018

LACOMBE Hugo - POULAIN Mathias

Les bibliothèques sont celles à jour le 10/01/2018

Le projet contient trois fichiers de code: un qui se trouve sur l'arduino et deux autres sur la raspberry.

Le fichier code_arduino contient le de l'arduino. Il fonctionne avec l'IDE arduino et les bibliothèques Wire, SeeedGrayOLED.

Le fichier SMP-2000.py contient le code présent sur la raspberry. Il utilise les bibliothèques suivantes : time, datatime, grovepi, grove_rgb_lcd, math, os, requests, numpy, sys, serial, subprocess.

Le code python fait appel à un script shell nommé ScriptParole.sh. C'est le troisième fichier.

LA procèdure d'installation est la suivante. Il faut téléverser le code arduino sur l'arduino, puis copier le code python depuis la raspberry.