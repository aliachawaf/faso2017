#!/usr/bin/env python3
# coding: utf8

import speech_recognition as sr
import re
from threading import Thread
try:
	# Pour python 3
	from queue import Queue
except ImportError:
	# Pour python 2
	from Queue import Queue

from yt import *

# Thread en background
def recognize_task():
	while True:
		audio = audio_queue.get()
		if audio is None: break		# On ne fait rien si il n'y a pas d'audio

		# Sinon on essaye de l'interpréter
		try:
			text = r.recognize_google(audio, None, "fr-FR")
			text = text.lower()
			print("Vous avez dit: " + text)

			match = re.search('(?<=joue.).*', text)
			if match is not None:
				searchYoutube(match.group(0))
				

		except sr.UnknownValueError:
		    print("Nous n'avons pas comprit")
		except sr.RequestError as e:
		    print("Les services de reconnaissances sont indisponnible; {0}".format(e))

		audio_queue.task_done()

# Initialisation
r = sr.Recognizer()
audio_queue = Queue()
recognize_thread = Thread(target=recognize_task)
recognize_thread.daemon = True
recognize_thread.start()

print("On écoute !")

# On récupère l'audio du microphone
#r.energy_treshold = 10000
with sr.Microphone() as source:
    try:
    	while True:
    		#r.adjust_for_ambient_noise(source, 1)
    		audio_queue.put(r.listen(source))
    except KeyboardInterrupt:
    	pass

audio_queue.join()		# On attend la fin de toutes les tâches de reconaissance vocale
audio_queue.put(None)	# On demande aux tâches de stopper
recognize_thread.join()	# On attend la fin des threads
