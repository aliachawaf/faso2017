import grovepi

def tempHumidity(pin):
	try:
		[temp,humidity] = grovepi.dht(pin,0)

		if humidity <= 0 or temp <= 0 :
			print("Erreur de lecture")
			temp = -1
			humidity = -1
	except IOError:
		print ("Error")
		temp = -1
		humidity = -1

	return [temp,humidity]
