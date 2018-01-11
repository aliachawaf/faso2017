import time
import grovepi
import ledBuz

def moyenne(liste):
    somme = 0
    for i in liste:
        somme = somme + i
    moyenne = somme/(len(liste))
    return moyenne

def ecartMoyen(liste):
    moy = moyenne(liste)
    sEcart = 0
    for i in liste:
        sEcart = sEcart + abs(moy-i)
    eMoyen = sEcart/(len(liste))
    return eMoyen

def pic(liste):
    ecart = liste[len(liste)-1] - moyenne(liste)
    #print("ecart : "+str(ecart))
    if ecart > ecartMoyen(liste):
        #print("ecartMoy : "+str(ecartMoyen(liste)))
        return True
    else:
        #print("ecartMoy : "+str(ecartMoyen(liste)))
        return False

def decalerListe(x,sliste,nbValeur): #rajoute la nouvelle valeur a la liste et supprime la premiere et decale tout si liste pleine
    if len(sliste) == nbValeur:
        sliste = sliste[1:nbValeur]
    sliste.append(x)
    return sliste
