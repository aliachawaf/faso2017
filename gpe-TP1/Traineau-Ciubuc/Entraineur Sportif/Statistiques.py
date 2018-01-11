#!/usr/bin/env python
# -*- coding: utf-8 -*-


import matplotlib.pyplot as plt
import random


Resultats = [(1,3.67,45),(2,45.6,50),(1,45.4,23),(1,23.4,23),(2,12.5,12),(2,32.5,50),(2,48.5,50),(2,20.5,50)]

def AffStatistiques(Resultats):
	 #Prend en paramètre une liste de tuple de résultats tel que chaque tuple
	 #soit composés d'un chiffre, une liste et un temps de pause en secondes
	 #1 pour pompe et 2 pour gainage
	 # le chiffre est un type d'exercice et donc selon le type la liste sera des répétitions en fonction d'un
	 # temps
	 #ou un nombre de fautes  en fonction temps tout court 
	 
	 #Cette fonction a pour but d'afficher le nombre de répétitions de pompe en fonction du temps
	 #
        
        # 1000 tirages entre 0 et 150
        seriesPompe=[]
        for i in Resultats :
            if i[0]==1:
                seriesPompe.append(i)
        seriesGainage=[]
        for i in Resultats :
            if i[0]==2:
                seriesGainage.append(i)
                
        AffichagePompes(seriesPompe)
        AffichageGainage(seriesGainage)
        return 0



def AffichagePompes(seriesPompes):
        l = seriesPompes
        NbPompes = []
        for pompes in l :
                NbPompes=NbPompes + [pompes[1]]
        m= max(NbPompes)
        
        TempsPause= []
        for pauses in l :
                TempsPause=TempsPause + [pauses[2]]
        
        series = [i for i in range(len(l))]
        
        #plt.subplot(221)
        #plt.hist(NbPompes, series, normed=1, facecolor='b', alpha=1)
        plt.figure(1)
        plt.title("Résumé des séries Pompes de l'entrainement")
        plt.bar (series,NbPompes)
        plt.xlabel('Séries')
        plt.ylabel('Nombre de Pompes')
        plt.axis([0, len(l), 0, m+5])
        for i in range(len(series)) :
                plt.text(i+0.45,m*0.3, "pause : "+ str(TempsPause[i]),rotation ='vertical')
        #plt.grid(True)
        plt.show()
        return 0
                
def AffichageGainage(seriesGainage):
        l = seriesGainage
        TempsGainage = []
        for i in l :
                TempsGainage = TempsGainage + [i[1]]
        m= max(TempsGainage)
        series = [i for i in range(len(l))]

        TempsPause= []
        for pauses in l :
                TempsPause=TempsPause + [pauses[2]]
        
        plt.figure(2)
        plt.title("Résumé des séries Gainage de l'entrainement")
        plt.bar (series,TempsGainage)
        plt.xlabel('Série')
        plt.ylabel('Temps Gainage')
        plt.axis([0, len(l), 0, m+5])
        for i in range(len(series)) :
                plt.text(i+0.45,m*0.3, "pause : "+ str(TempsPause[i]),rotation ='vertical')
        
        plt.show()
        return 0

#AffStatistiques(Resultats)

                

