# Signalisation et sécurité cycliste 

- *Hardware*: Arduino
- *Arduino IDE*: Développé sous Arduino IDE v1.8.5 et Processing	3.3.6
- *Date*: 11 Janvier 2017
- par theo PONTHIEU et julien ROUMAGNAC
- Dans le cadre du projet FASO nous avons décider de créer un sac à dos connecté pour cycliste, permettant de mieux se faire voir et comprendre par les usagers de la route.



### Pre-requis
- Pour que l'objet soit opérationnel, vous aurez besoin de : 
- La librarie LEDControl disponible [ici:](http://wayoda.github.io/LedControl/)
- La librairie ADXL pour l'accelerometre [ici:](https://github.com/Seeed-Studio/Accelerometer_ADXL345)
- La librairie SoftwareSerail pour le module bluetooth disponible [ici:](https://github.com/PaulStoffregen/SoftwareSerial)
- Le sac à dos connecté et les branchements suivant réalisés :
  - module bluetooth sur Pin D6
  - accélerometre sur port I2C 
  - capteur de luminosité sur port A0
  - matrice sur les branchement 10,11,12,5V,GND
- un smartphone Android et l'application AI2 companion installé
- et le fichier principal present sur ce git chargé sur l'arduino.


### démarrage et utilisation 

televersez le programme principal sur l'arduino démarrer le sac en mettant la batterie sur ON. Lancez votre application sur smartphone et dans les bluetoth connécté vous a "HMSOFT". vous pouvez mainteant roulez , en cas de freinage un message de stop saffichra si vous désirez affichez dautres informations il vous suffit de cliquez sur l'application selon vos besoins .

**Développé en IG3 à polytech Montpellier avec
Arduino IDE
MIT App Inventor 2**

