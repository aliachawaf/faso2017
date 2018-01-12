try:
	from queue import Queue
except ImportError:
	print("Utiliser python 3")
	sys.exit()
import os
import sys
import pafy
import urllib.request
import urllib.parse
import re
import speech_recognition as sr
import re
import glob
import time
import random
from bluetooth import *
from enum import Enum
from threading import Thread
from subprocess import Popen
import vlc

class CMD(Enum):
	MUSIC_NEXT = 0,
	MUSIC_PREVIOUS = 1,
	VOLUME_INCREASE = 2,
	VOLUME_DECREASE = 3,
	MUSIC_PAUSE = 4,
	MUSIC_PLAY = 5,
	PLAYLIST_PLAY = 6,
	ERR_MUSIC_NAME = 7,
	ERR_MUSIC_PLAYLIST = 8,
	ERR_INVALID = 9

def command_task():
	pauseState = False
	video_index = 0
	video_list = None
	while True:
		cmd, arg = command_queue.get()
		if cmd is None:
			command_queue.task_done()
			break
		
		if cmd == CMD.MUSIC_PAUSE:
			if not pauseState:
				print("Pause")
				pauseState = True
				player.stop()
			else:
				print("Play")
				pauseState = False
				player.play()
		elif cmd == CMD.MUSIC_NEXT:
			if video_list is not None:
				print("Musique suivante")
				video_index = video_index + 1
				if video_index > len(video_list) - 1:
					video_index = 0
				video = pafy.new(video_list[video_index])
				media = instance.media_new(video.getbestaudio().url)
				media.get_mrl()
				player.set_media(media)
				player.play()
		elif cmd == CMD.MUSIC_PREVIOUS:
			print("Musique précédente")
			if video_list is not None:
				video_index = video_index - 1
				if video_index < 0:
					video_index = len(video_list) - 1
				video = pafy.new(video_list[video_index])
				media = instance.media_new(video.getbestaudio().url)
				media.get_mrl()
				player.set_media(media)
				player.play()
		elif cmd == CMD.VOLUME_INCREASE:
			print("Volume augmenter")
			player.audio_set_volume(player.audio_get_volume() + 25)
		elif cmd == CMD.VOLUME_DECREASE:
			print("Volume baisser")
			player.audio_set_volume(player.audio_get_volume() - 25)
		elif cmd == CMD.MUSIC_PLAY:
			print("Joue musique")
			query_string = urllib.parse.urlencode({ "search_query" : arg })
			html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
			video_list = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
			video_index = 0
			video = pafy.new(video_list[0])
			media = instance.media_new(video.getbestaudio().url)
			media.get_mrl()
			player.set_media(media)
			player.play()

		command_queue.task_done()

def command_parser(str):
		if re.search(".o.|b.b|bo.|.ob", str, re.IGNORECASE) is None:
			return False, False

		if re.search("suivant.?", str, re.IGNORECASE) is not None:
			return CMD.MUSIC_NEXT, False
		if re.search("pr.c.den.?.?", str, re.IGNORECASE) is not None:
			return CMD.MUSIC_PREVIOUS, False
		if re.search("monte|augmente", str, re.IGNORECASE) is not None:
			return CMD.VOLUME_INCREASE, False
		if re.search("baisse|diminue", str, re.IGNORECASE) is not None:
			return CMD.VOLUME_DECREASE, False
		if re.search("pause|.top|arr.te", str, re.IGNORECASE) is not None:
			return CMD.MUSIC_PAUSE, False
		
		found = re.search("(joue|jeu)(.*)", str, re.IGNORECASE)
		if found is not None:
			songName = found.group(2).lstrip()
			if songName == "":
				return CMD.ERR_MUSIC_NAME, False
			else:
				return CMD.MUSIC_PLAY, songName

		found = re.search("playlist(.*)", str, re.IGNORECASE)
		if found is not None:
			playlistName = found.group(1).lstrip()
			if playlistName == "":
				return CMD.ERR_MUSIC_PLAYLIST, False
			else:
				return CMD.PLAYLIST_PLAY, playlistName

		return CMD.ERR_INVALID, False

def recognize_task():
	apiKeyCurrent = 0
	apiKey = [
		"AIzaSyAJE5_0UjWgvh0BudiejspQtXCUvnAGm_s",
		"AIzaSyCNItbshJgYm09_aJLquvfcw0iI96Lzwfs",
		"AIzaSyBZVfAwInpdrt8DAGTcMG3sPWkcix3zexw",
		"AIzaSyB-kuH1EeNtzgXhdiarPVYdNiYzLCLnyfg"
	]
	while True:
		audio = audio_queue.get()
		# On ne fait rien si il n'y a pas d'audio
		if audio is None:
			audio_queue.task_done()
			break
		# Sinon on essaye de l'interpréter
		commands = False
		try:
			print("Reconnaissance...")
			commands = recognizer.recognize_google(audio, apiKey[apiKeyCurrent], "fr-FR", True)
		except sr.UnknownValueError:
			print("Nous n'avons pas comprit")
			commands = False
		except:
			print("Changement de clé d'api")
			apiKeyCurrent = apiKeyCurrent + 1
			if apiKeyCurrent > len(apiKey):
				apiKeyCurrent = 0
			audio_queue.put(audio)
			commands = False

		# Si le tableau n'est pas vide
		if commands:
			print(commands)
			valide = False
			commands = commands['alternative']
			for cmd in commands:
				cmd = cmd['transcript'].lower()
				cmd, arg = command_parser(cmd)
				# Si la commande est valide
				if cmd != False and cmd != CMD.ERR_INVALID and cmd != CMD.ERR_MUSIC_NAME and cmd != CMD.ERR_MUSIC_PLAYLIST:
					valide = True
					break

			# La commande n'a pas était reconnu
			if valide:
				command_queue.put((cmd, arg))

		audio_queue.task_done()

# Serveur Bluetooth, attends une connexion -> créer un fork -> le prog principale attends la fin
# du processus fils puis attends une nouvelle connexion. -> Permet d'éviter que plusieurs appareils
# puissent se connecter en même temps à l'enceinte
def bluetooth_server():
	server_sock = BluetoothSocket(RFCOMM)
	server_sock.bind(("",PORT_ANY))
	server_sock.listen(1)
	port = server_sock.getsockname()[1]
	uuid = "69090025-0c61-4300-8330-7dcab0752d99"
	advertise_service( 
		server_sock, 
		"TestServer",
		service_id = uuid,
		service_classes = [ uuid, SERIAL_PORT_CLASS ],
		profiles = [ SERIAL_PORT_PROFILE ],
		#protocols = [ OBEX_UUID ]
		)
	while True:
		print ("Attente d'une connexion...")
		client_sock, client_info = server_sock.accept()
		#On créer un fork pour le client
		#pid = os.fork()
		pid = 0
		if pid == 0:
			print ("Client connecte: ", client_info)
			while True:
				try:
					req = client_sock.recv(1024).decode("utf-8")
					print("Commande reçu par bluetooth [", req, "]")
					cmd, arg = command_parser(req)
					command_queue.put((cmd, arg))
				except:
					print("client deconnecte")
					client_sock.close()
					sys.exit(0). _exit()
					break
		else:
			os.waitpid(pid, 0)
	server_sock.close()

# Re initalise les ports usb
os.system("./startup/usb /dev/bus/usb/001/004")

recognizer = sr.Recognizer()
recognizer.pause_threshold = 0.7
recognizer.operation_timeout = 10

# Initialization de Vlc
instance = vlc.Instance()
player = instance.media_player_new()
player.audio_set_volume(75)

bluetooth_thread = Thread(target=bluetooth_server)
bluetooth_thread.daemon = True
bluetooth_thread.start()

# 2 Thread pour process l'audio
audio_queue = Queue()
recognize_thread1 = Thread(target=recognize_task)
recognize_thread1.daemon = True
recognize_thread1.start()

recognize_thread2 = Thread(target=recognize_task)
recognize_thread2.daemon = True
recognize_thread2.start()

# 1 Thread pour process les commandes
command_queue = Queue()
command_thread = Thread(target=command_task)
command_thread.daemon = True
command_thread.start()

#with sr.Microphone() as source:
#with sr.Microphone(device_index=2) as source:
# 	os.system('cls' if os.name == 'nt' else 'clear')
# 	print("Bob démarre...")
# 	print("Calibration du microphone...")
# 	recognizer.adjust_for_ambient_noise(source, 15)
# recognizer.energy_threshold = recognizer.energy_threshold * 1.5
# print("Seuil du microphone à " + str(recognizer.energy_threshold))

#command_queue.put((CMD.MUSIC_PLAY, "star wars the force theme"))
#time.sleep(15)
#command_queue.put((CMD.MUSIC_NEXT, False))
#time.sleep(15)

print("Bob est prêt!")
recognizer.energy_threshold = 3000
#recognizer.energy_threshold = 800
with sr.Microphone() as source:
#with sr.Microphone(device_index=2) as source:
	os.system('cls' if os.name == 'nt' else 'clear')
	try:
		while True:
			audio_queue.put(recognizer.listen(source))
	except KeyboardInterrupt:
		os.system('cls' if os.name == 'nt' else 'clear')
		audio_queue.put(None)
		recognize_thread1.join()
		command_queue.put((None, None))
		command_thread.join()

print("Bye !")
