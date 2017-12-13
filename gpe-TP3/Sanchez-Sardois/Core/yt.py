import os
import pafy
import urllib.request
import urllib.parse
import re

def searchYoutube(keyword):
	query_string = urllib.parse.urlencode({ "search_query" : keyword })
	html_content = urllib.request.urlopen("http://www.youtube.com/results?" + query_string)
	search_results = re.findall(r'href=\"\/watch\?v=(.{11})', html_content.read().decode())
	video = pafy.new(search_results[0])
	print(search_results[0])
	best = video.getbestaudio()
	
	# Sur la raspberry
	cmd = "omxplayer \"" + best.url + "\""
	# Sur mon pc
	#cmd = "cvlc \"" + best.url + "\""

	print(best.url)
	os.system(cmd)
