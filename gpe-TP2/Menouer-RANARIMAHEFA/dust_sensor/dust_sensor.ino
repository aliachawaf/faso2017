/*
 dust_sensor.ino V1
 Réalisé par:
 - MENOUER Amjad
 - RANARIMAHEFA Mitantsoa Michel
 Script qui relève les données du capteur de poussiere et l'envoie sur le port Série.
 Televerser ce script sur l'Arduino ensuite débrancher le cable USB-AB de l'ordinateur
 et le brancher sur l'un des ports USB du raspberry.
 
 Capteur optique de poussiere : Shinyei Model PPD42NS
 JST Pin 1 (Black Wire)   //Arduino GND
 JST Pin 3 (Red wire)     //Arduino 5VDC
 JST Pin 4 (Yellow wire)  //Broche numérique Arduino 8
 */

int pin = 8; //Broche numérique Arduino 8
unsigned long duration;
unsigned long starttime;
unsigned long sampletime_ms = 150; //sampe 30s
unsigned long lowpulseoccupancy = 0; // correspond au Lo Pulse Occupancy Time (LPO Time) détecté dans un intervalle de 30 s
float ratio = 0;  // indique a quel niveau le temps LPO utilise l'integralite de l'intervalle d'echantillonnage.
float concentration = 0; // densite de l'air en particule/0.01 pieds cube (pieces/0.01 cubic feet) | 0,01 = 0,0002831685 m/3

void setup() {
  Serial.begin(9600);
  pinMode(8,INPUT);
  starttime = millis(); // recuperation temps actuel
}

void loop() {
  duration = pulseIn(pin, LOW);
  lowpulseoccupancy = lowpulseoccupancy+duration;

  if ((millis()-starttime) >= sampletime_ms) //si la durée d'échantillonnage == 30 s
  {
    ratio = lowpulseoccupancy/(sampletime_ms*10.0);  // Integer percentage 0=>100
    concentration = 1.1*pow(ratio,3)-3.8*pow(ratio,2)+520*ratio+0.62; // // en utilisant la courbe de la fiche technique
    Serial.println(concentration);
    //Serial.println(" pcs/0.01cf");

    lowpulseoccupancy = 0;
    starttime = millis();
  }
}
