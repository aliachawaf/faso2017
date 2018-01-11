Tout les scripts sont dans le même répertoire pour faciliter les from machin import * qui ont tendances 
à créer beaucoup de problèmes entre plusieurs dossiers.
Il y a un main dit "graphique" (InterfaceGraphique) qui gère l'application tkinter et importe entrainement et lance les fonctions de ce script
, Entrainement est le main de la partie "raspberry" il va appeler les packages Bouton, Affichage et Exercices pour faire tourner 
l'entrainement. Ces packages appelent la bibliothèque grovepi ou lcd_rgb.
L'application tkinter ouvre également des fichiers texte "manuel d'utilisation" et " Descriptifs des entraînements"
et import statistiques.py qui trace des graphiques avec matplotlib.

Code compatible avec la version GrovePi Python library v1.2.2, matplotlib 2.1.1 et Python 3/2.7

SportTrainer 1.0, 12/01/2018
