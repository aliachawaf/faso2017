#include <Adafruit_Sensor.h>

#include <Servo.h>
#include <DHT.h>


#define DHTTYPE DHT11
#define DHTPIN A4
#define CLDROIT A0
#define CLGAUCHE A2
#define DIVTENS A6

/* Capteur lumière droit : A0
 *  Capteur lumière gauche : A1
 *  Capteur température : A2
 *  Diviseur de tension : A3
 */

// Le capteur de lumière DROIT sera en position A0, le capteur de lumière GAUCHE sur A1
int position = 0; // Position du servomoteur
Servo moteur; // le servo
int pinServo = 9; // Le pin du servo (peut changer)
int valDroit = 0; // La valeur du capteur de lumière droit
int valGauche = 0; // La valeur du capteur de lumière gauche

DHT dht(DHTPIN, DHTTYPE); // Le capteur de température

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  moteur.attach(pinServo);
  dht.begin();
}

void ecriturePos() // Il faut vérifier si la position est acceptable pour le servo moteur, sinon on la modifie
{
  if(position >= 180)
  {
    position = 178;
  }
  else if (position < 0)
  {
    position = 2;
  }

   moteur.write(position); // On envoie la bonne position au panneau solaire
   delay(50);
}

bool alignement(){
  
  valDroit = analogRead(CLDROIT);
  valGauche = analogRead(CLGAUCHE);
  bool resultat = false;
  if((valDroit) == (valGauche)) //On peut diminuer la précision ici
  {
     resultat = true;
  }
  return resultat;
}

void bouger(){
    ecriturePos();
    delay(20); // On attend que le panneau tourne
    while(!alignement())
    {
        if(valDroit > valGauche)
        {
          position+=2; // Décaler le servo de 2 degrés sur la droite
          ecriturePos();
        }
        else if (valDroit < valGauche)
        {
          position-=2; // Décaler le servo de 2 degrés sur la gauche
          ecriturePos();
        }
    }
    String ecriturePos = "POS;";
    ecriturePos += position;
    Serial.println(ecriturePos);
    delay(1000);
}

void monitoring() //Fonction qui renvoie les donnnées recues et interprétées des capteurs
{
  float temp = dht.readTemperature();
  double  sensorValue=analogRead(DIVTENS);
  double  sum=0;
  double tension = 0;
  if(!isnan(temp))
  {
    String envoiTemp = "TEMP;";
    envoiTemp += temp;
    Serial.println(envoiTemp); // Envoie la température sur le port série
    delay(1000);
  }

  for(int i=0;i<1000;i++) //Fait une moyenne sur une seconde de toutes les valeurs
  {
      sum +=sensorValue;
      sensorValue=analogRead(DIVTENS);
      delay(2);
  }
  sum=sum/1000;
  tension = 3*sum*4.988/1023.00;
  String envoiTens = "TENSION;";
  envoiTens += tension;
  Serial.println(envoiTens); // Envoie la tension sur le port série
  delay(1000);
  String envoiLum = "LUM1;";
  envoiLum += analogRead(CLDROIT);
  Serial.println(envoiLum);
  delay(1000);
  envoiLum = "LUM2:";
  envoiLum += analogRead(CLGAUCHE);
  Serial.println(envoiLum);
  delay(1000);
}

void emergency()
{
  int posalerte = 180 - position;
  moteur.write(posalerte);
  delay(30000); // On attend que le panneau refroidisse
  moteur.write(position);
}

void loop() 
{
   if(Serial.available() > 0)
    {
        delay(500);
        if(Serial.readStringUntil(';') == "BOUGE") 
        {
            position = Serial.parseInt();
            bouger();
        }
        else if(Serial.readStringUntil(';') == "ALERT")
        {
            emergency();
        }
    }
    monitoring();
}

// Données envoyées par l'ordinateur
// BOUGE;valeur
// ALERT;

// Données envoyées par l'Arduino
// TEMP;valeur
// POS;valeur
// TENSION;valeur
// LUM1;valeur
// LUM2;valeur
