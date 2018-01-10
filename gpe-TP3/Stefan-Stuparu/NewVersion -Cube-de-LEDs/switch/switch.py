import time
import grovepi
def getAngle():
# Connect the Grove Rotary Angle Sensor to analog port A2
	potentiometer =2

	grovepi.pinMode(potentiometer,"INPUT")

	time.sleep(1)

# Reference voltage of ADC is 5v
	adc_ref = 5

# Vcc of the grove interface is normally 5v
	grove_vcc = 5

# Full value of the rotary angle is 300 degrees, as per it's specs (0 to 300)
	full_angle = 300

        # Read sensor value from potentiometer
        sensor_value = grovepi.analogRead(potentiometer)

        # Calculate rotation in degrees (0 to 300)
        degrees = round((round((float)(sensor_value)*adc_ref/1023,2) * full_angle) / grove_vcc, 2)
	time.sleep(1)
	return  degrees
