#coding: utf-8

import pygame
from pygame.locals import*

pygame.init()

def init() :
	pygame.mixer.init(44100, -16, 2, 2048) # initialisation des parametres
	return None

def play(n) :
	pygame.mixer.music.play(n)
	return None

def pause() :
	pygame.mixer.music.pause()
	return None
 
def unpause() :
	pygame.mixer.music.unpause()
	return None

def load(music) :
	pygame.mixer.music.load(music)
	return None

def stop() :
	pygame.mixer.music.stop()
	return None

def queue(music) :
	pygame.mixer.music.queue(music)
	return None

def busy():
	return pygame.mixer.music.get_busy() 

def suivant(playlist,indice):
	if indice == len(playlist)-1 :
		indice = 0
	else :
		indice += 1
	load("/home/walines/home/scripts/grovepi/Musique/"+playlist[indice])
        play(1)
	return indice

def precedent(playlist,indice):
	if indice == 0 :
		indice = len(playlist)-1
	else :
		indice -= 1
	load("/home/walines/home/scripts/grovepi/Musique/"+playlist[indice])
	play(1)
	return indice
