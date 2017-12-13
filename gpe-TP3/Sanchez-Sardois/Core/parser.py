# coding: utf-8

import re

HOTWORD = "bob"

def parser(str):
	if re.search(HOTWORD, str, re.IGNORECASE) is None:
		return None

	if re.search("suivant", str, re.IGNORECASE) is not None:
		print("Jouer la musique suivante")
	if re.search("pr[e|é|è]c[e|é|è]dent", str, re.IGNORECASE) is not None:
		print("Jouer la musique précédente")
	if re.search("monte|augmente", str, re.IGNORECASE) is not None:
		print("Monter le son")
	if re.search("baisse|diminue", str, re.IGNORECASE) is not None:
		print("Baisser le son")
	if re.search("pause|stop", str, re.IGNORECASE) is not None:
		print("Mise en pause de la musique")
	
	
	found = re.search("joue(.*)", str, re.IGNORECASE)
	if found is not None:
		songName = found.group(1).lstrip()
		if songName == "":
			print("Nom de musique incorrect")
		else:
			print("Joue la musique " + songName)

	found = re.search("playlist(.*)", str, re.IGNORECASE)
	if found is not None:
		playlistName = found.group(1).lstrip()
		if playlistName == "":
			print("Nom de playlist incorrect")
		else:
			print("Lecture de la playlist " + playlistName)
		
	


parser("bob musique suivante")
parser("bob precedente")
parser("bob joue nom de musique")
parser("bob playlist star wars")
