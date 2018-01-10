#!/usr/bin/env python
#-*- coding: utf-8 -*-
import RPi.GPIO as GPIO         # Importation des librairies qui gerent les ports
from grovepi import *
from grove_rgb_lcd import *
import time

def enregistrement(nom_enregistrement):

		#!/usr/bin/env python3
		import pyaudio
		import wave

		CHUNK = 512
		FORMAT = pyaudio.paInt16 #paInt8
		CHANNELS = 1
		RATE = 44100 #sample rate
		RECORD_SECONDS = 30
		WAVE_OUTPUT_FILENAME = nom_enregistrement
		arret = False

		p = pyaudio.PyAudio()

		stream = p.open(format=FORMAT,
        		        channels=CHANNELS,
                		rate=RATE,
                		input=True,
                		frames_per_buffer=CHUNK) #buffer

		print("Enregistrement")

		frames = []
#		print(digitalRead(2))
		for i in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
			data = stream.read(CHUNK)
			frames.append(data) # 2 bytes(16 bits) per channel
			if(digitalRead(2)):
				arret = True
				break;

		print("Enregistrement terminé")
		if not arret: #Si les 30s sont dépassées
			setText("Limite du \nmessage depassee") #Informer sur l'écran
			time.sleep(2)

		stream.stop_stream()
		stream.close()
		p.terminate()

		wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
		wf.setnchannels(CHANNELS)
		wf.setsampwidth(p.get_sample_size(FORMAT))
		wf.setframerate(RATE)
		wf.writeframes(b''.join(frames))
		wf.close()
