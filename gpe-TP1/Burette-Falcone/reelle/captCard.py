from grovepi import *
import time

def readHeartRate(sens,timeInt):
	pinMode(sens,"INPUT")
	current = time.time()
	prec = 0
	count = 0
	sec = current
	while sec < current + timeInt  :
		lec = digitalRead(sens)
		if not prec and lec :
			count += 1
		prec = lec

		sec = time.time()

	btm = count * (60/timeInt)

	return btm

