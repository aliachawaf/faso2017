# Bracelet de santé connecté pour personnes âgées

- Hardware: Arduino 
- Arduino IDE: Développé sous Arduino IDE v1.8.5 et Processing	3.3.6
- Date:  11 Janvier 2017
- Version: v1.0
- par Nicolas GUARY et Marc-Antoine DANNER

Voici le code mis en place dans le cadre de notre projet FASO: un bracelet de santé connecté pour personnes âgées muni d'un capteur de fréquence cardiaque.

### Pre-requis

Avant de commencer, veuillez à bien disposer de:
La librarie LCD disponible ici: https://github.com/Seeed-Studio/Grove_LCD_RGB_Backlight/archive/master.zip
La librarie du module RTC disponible ici: https://raw.githubusercontent.com/SeeedDocument/Grove-RTC/master/res/RTC_Library.zip
Le bracelet connecté comme suit:
  - Bouton SOS sur la pin D3
  - Bouton I'm Fine sur la pin D4
  - Buzzer sur la pin D6
  - Capteur de fréquence cardiaque sur la pin D2
  - Ecran LCD sur une pin i2c
  - Module RTC sur une pin i2c

## Hiérarchie et contenu

Ce projet fonctionne grâce à deux fichiers:
  - CodeBracelet.ino pour Arduino IDE
  - Processing.pde pour Processing
  
La partie Arduino contient l'ensemble des fonctions necessaires au fonctionnement du bracelet (bpmCalc(), calcTime(), lcdHeure(), couleurLCD(), lcdBPM(), doitAllumer(), doitEteindre()...)
La partie processing gère l'envoi des SMS, et traite les données (affichage d'une courbe + stockage des valeurs dans un docuement .txt)

### Installation

Téléversez dans un premier temps le code Arduino IDE sur l'Arduino, mettez ensuite le capteur de fréquence cardiaque à votre oreille: l'écran LCD s'allume en bleu et un message "INIT" s'affiche pour vous confirmer que le bracelet est en marche et que le setup est en cours.
Une fois fini (environs 6-7 secondes) l'écran s'allume en vert et indique votre fréquence cardiaque et l'heure actuelle.
Vous pouvez maintenant exectuer le code Processing, un graphique représentant votre fréquence cardiaque s'affiche alors à l'écran, de plus un fichier .txt est crée sur votre bureau, il contient les valeurs relevées par le capteur pour votre fréquence cardiaque.
De plus, en cas de problème, un SMS est envoyé par une requete http.

## Développé avec

* [Arduino IDE](https://www.arduino.cc/en/main/software)
* [Processing](https://processing.org/) 

## Auteurs

* **Nicolas GUARY** 
élève en IG3 à Polytech Montpellier
* **Marc-Antoine DANNER** 
élève en IG3 à Polytech Montpellier
