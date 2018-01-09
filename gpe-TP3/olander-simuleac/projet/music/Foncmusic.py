import pygame
pygame.mixer.init() 

def startMusic(l):
	#pygame.mixer.init()
	pygame.mixer.music.load(l)
	pygame.mixer.music.play()

def stopMusic():
	#pygame.mixer.init()
	pygame.mixer.music.stop()


def setVolume():
	pygame.mixer.music.set_volume(1)
