#coding: utf-8

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import datetime

fig = plt.figure()

axes = plt.gca()

etat = np.loadtxt("pb2.txt")

print etat

jour = np.loadtxt("pb1.txt")

print jour


plt.title("Bilan du mois ", color='black')
plt.plot(jour, etat, color='purple', linewidth=1)

#axes.set_ylim(1,2)

plt.xlabel("Jour du mois", color='purple')
plt.ylabel('Etat de bali', color='purple')

axes.yaxis.set_ticklabels([' ','VIDE',' ',' ',' ',' ', 'PLEINE'])
#axes.xaxis.set_ticklabels(np.loadtxt("pb1.txt", dtype=np.str))
#j = np.loadtxt("testjour.txt, dtype=np.str")
#axes.xaxis.set_ticklabels(j)

fig.savefig('graphique.png')
