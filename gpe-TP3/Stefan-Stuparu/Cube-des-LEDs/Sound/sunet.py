from Sys.incercare import *
import pygame
from pygame.locals import *
import time
def Music(x):
	
	pygame.mixer.init(48000, -16, 2, 2048)
	pygame.mixer.music.load(b"aze.mp3")
	pygame.mixer.music.queue("aze.mp3")
	pygame.mixer.music.play()
	i=0
	while i!= x:
		i=i+1


#Music()
