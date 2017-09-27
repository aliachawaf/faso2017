import driverI2C
import time

setText("Salut Polytech! C'est un test de l'ecran LCD !")
setRGB(0,128,64)
time.sleep(2)

for c in range(0,200):
	setRGB(c,200-c,0)
	time.sleep(0.1)
setRGB(0,255,0)
setText("Bye!")
