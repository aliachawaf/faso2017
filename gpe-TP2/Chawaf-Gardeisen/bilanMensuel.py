#coding: utf-8

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import numpy as np
import datetime

fig = plt.figure()

etat = np.loadtxt("historiqueEtat.txt")
jour = np.loadtxt("historiqueTemps.txt")


plt.title("Bilan du mois ", color='black')
plt.plot(jour, etat, color='purple', linewidth=3)

plt.xlabel("Jour du mois", color='purple')
plt.ylabel('Etat de bali', color='purple')



fig.savefig('graphique.png')


