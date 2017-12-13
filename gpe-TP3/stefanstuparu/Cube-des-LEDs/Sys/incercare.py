import serial


def arduinoString(x):
  # code for reading the string from the arduino..
	ser = serial.Serial('/dev/ttyACM0',9600)
	s = [0]
	files = open("sensor_data", 'w')
	for i in range(0,x):
		read_serial=ser.readline()
		s[0] = str(int (ser.readline(),16))
		files.write(str(read_serial))
		#files.write(s[0])
		#files.write("\n")
		print "read_serial: " + str(read_serial)
		#print "s[0]: " + s[0]
	files.close()
	return s[0]
		#print read_serial
