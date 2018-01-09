import time
import grovepi

# Connect the Grove Rotary Angle Sensor to analog port A2
potentiometer =2
# Connect the LED to digital port D4
led =4

grovepi.pinMode(potentiometer,"INPUT")
grovepi.pinMode(led,"OUTPUT")
time.sleep(1)

# Reference voltage of ADC is 5v
adc_ref = 5

# Vcc of the grove interface is normally 5v
grove_vcc = 5

# Full value of the rotary angle is 300 degrees, as per it's specs (0 to 300)
full_angle = 300

while True:
    try:
        # Read sensor value from potentiometer
        sensor_value = grovepi.analogRead(potentiometer)

        # Calculate rotation in degrees (0 to 300)
        degrees = round((round((float)(sensor_value)*adc_ref/1023,2) * full_angle) / grove_vcc, 2)
	print("lssssssssssssssss")
	print("sensor_value = %d degrees = %.1f" %(sensor_value, degrees))
	time.sleep(1)
	if (degrees >250):
		grovepi.digitalWrite(led,1)
	else:
		grovepi.digitalWrite(led,0)
    except KeyboardInterrupt:
        grovepi.digitalWrite(led,0)
        break
    except IOError:
        print ("Error")
