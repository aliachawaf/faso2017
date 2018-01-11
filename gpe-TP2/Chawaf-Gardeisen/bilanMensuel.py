#coding: utf-8

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import datetime
import time

fig = plt.figure()

axes = plt.gca()

#on recupere les dates pour l'axe des abscisses
jour = np.loadtxt("HistoriqueTemps.txt")

#on recupere les etats de la boite pour l'axe des ordonnées
etat = np.loadtxt("HistoriqueEtat.txt")

#on recupère le mois pour lequel on fait le bilan afin de le mettre dans le titre
date = datetime.datetime.now()
mois = date.month



#comme on envoie le bilan le 1er du mois, alors il correspond à l'historique du mois precedent.

#si on est le 1er janvier, il faut renvoyer le mois de décembre (donc 12)
if mois==1:
        mois_precedent = 12
else:
        mois_precedent = mois-1


mois_titre = time.strftime('%b', time.struct_time((0, mois_precedent, 0,)+(0,)*6)) 



#titre du graphique
plt.title("Bilan du mois de " + str(mois_titre) + "\n", color='firebrick', fontsize=15, fontweight='bold')

#creation du graphique
plt.plot(jour, etat, color='mediumslateblue', linewidth=2)

#nom des axes
plt.xlabel("Jour du mois de  " + str(mois_titre), color='royalblue', fontsize=12, fontweight='bold')
plt.ylabel('Etat de bali', color='royalblue', fontsize=12, fontweight='bold')
axes.yaxis.set_ticklabels([' ','VIDE',' ',' ',' ',' ', 'PLEINE'])

#parametrage des axes
axes.xaxis.set_ticks(range(0,60,2))
axes.xaxis.set_tick_params(labelsize=8)

#enregistrement du graphique
fig.savefig('graphique.png')
