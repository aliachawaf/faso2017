#include <HX711.h> // programme poids 
#include <SD.h> // Carte SD
#include <SPI.h> // Carte SD

#include <math.h> // Programme Lumière 
#include <Servo.h> //Servomoteur

#define Grove_Water_Sensor 6 //Attache le capteur d'eau au pin 6
Servo monservo; // création de l'objet pour controler le servo
#define LIGHT_SENSOR A0
const int ledPin=7; // Lumière
//pour la carte SD : 
File monFichier;
HX711 cell(3,2);

void setup() {
  Serial.begin(9600);
  monservo.attach(2); //utilise la broche 2 pour le controle du servo
  pinMode(Grove_Water_Sensor, INPUT); // le capteur d'eau est un input (une entree)
  pinMode(ledPin,OUTPUT);// Programme Lumière

///////////////////////////////////////////////////////
//PROGRAMME CARTE SD ET POIDS 
  Serial.println("Initialisation de la carte SD ..!");
  if (!SD.begin(4)){
     Serial.println("L'initialisation de la carte SD a echoue !");
     return;}
  //quand c'est ok : 
  Serial.println("L'initialisation de la carte SD a réussie !");
  /////on supprime l'ancien fichier :
  if(SD.exists("poids.txt")) {
    SD.remove("poids.txt");}
  //fait une pause de 1 seconde (= 1000ms)
  delay(1000);
  
}





float val = 0;
int count = 0;
float moy = 0;
float a = 0;
int j = 0; //Variable qui compte le nombre de jour depuis la mise en route du système 
int h = 0; //Variable qui compte les heures 
int m = 0;  //Variable qui compte les minutes
int s = 0; //Variable qui compte les secondes








void loop() {
  
  ///////////////////////////////////////////////
  //PROGRAMME CARTE SD ET POIDS 
  count = count + 1;
  s=s+1;
  if(s==60){
    s=0;
    m=m+1;
  if (m==60){
    m=0;
    h = h+1;
  if (h==24){
      h=0;
      j=j+1;}
  }}
/* a = a + cell.read();
  moy = a/count;
  val = moy;*/
  //val = cell.read();
  val=cell.get_value(1);
  //val = (val +73819)/15456.0f *8.5;
  //affiche les valeurs et le temps correspondant : 
  Serial.println(val);
  Serial.print("Jours/Heures/Minutes/Secondes : ");
  Serial.print(j);
  Serial.print("/");
  Serial.print(h);
  Serial.print("/");
  Serial.print(m);
  Serial.print("/");
  Serial.print(s);  
  Serial.print(" Poids = ");
  Serial.print((val +73819)/15456.0f *8.5);
  Serial.println(" g ");
  
  delay (1000);

  // zero = -73819
  // 15456.0f
  //ecrit dans la carte SD : 
  monFichier = SD.open("poids.txt", FILE_WRITE);//ouvre le fichier de la carte SD avec le nom 
  if (monFichier) {
    //si le fichier a bien été ouvert :
    monFichier.print("Jours/Heures/Minutes : ");
    monFichier.print(j);
    monFichier.print("/");
    monFichier.print(h);
    monFichier.print("/");
    monFichier.print(m);
    monFichier.print(" Poids = ");
    monFichier.print((val +73819)/15456.0f *8.5);
    monFichier.println(" g ");
    monFichier.close();}
  
  else {
    Serial.println("Erreur lors de l'ouverture de poids.txt");}



//////////////////////////////////////
//PROGRAMME LUMINOSITE ET LED 
  int sensorValue= analogRead(LIGHT_SENSOR);
  Serial.print("the analog read data is : ");
  Serial.println(sensorValue);
  delay(1000);
  if (((val +73819)/15456.0f *8.5)< 5){
    //Si le poids des graines est inférieur à 5g alors la led doit s'allumer
    digitalWrite(7,HIGH);}
  else {
    if (sensorValue>200){
      //Si le capteur de lumiere capte de la lumiere alors la led doit clignoter 
      digitalWrite(7,HIGH);
      delay(1000);
      digitalWrite(7,LOW);}
    else { 
      // Si le capteur de lumiere ne capte pas de lumiere cela signifie que les graines recouvrent le capteur et donc la led doit etre éteinte
      digitalWrite(7,LOW);
      delay (1000);}}
  Serial.println("jai allumé la led" );

////////////////////////////////////////
//PROGRAMME EAU ET SERVOMOTEUR 
  // Si le capteur detecte l'eau : 
  if (digitalRead(Grove_Water_Sensor)==LOW) {
    monservo.write(120);
    delay(1000);}
  
  //Si le capteur ne detecte pas l'eau :
  if (digitalRead(Grove_Water_Sensor)==HIGH) {
    monservo.write(5);
    delay(100);}    
}

