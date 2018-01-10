import serial
import time
import math

def arduinoString(x):
  # code for reading the string from the arduino..
	ser = serial.Serial('/dev/ttyACM0',9600)
	s = [0]
	files = open("sensor_data", 'w')
	for i in range(0,x):
		time.sleep(1)
		read_serial=ser.readline()
		if (not(read_serial.strip()))or (read_serial.split()[0][0]=="/"):
			read_serial='0'
		s[0] = str(int (ser.readline(),16))
		files.write(str(read_serial))
		#files.write(s[0])
		#files.write("\n")
		print "Frequance: " + str(read_serial)
		#print "s[0]: " + s[0]
	files.close()
	return s[0]
		#print read_serial
