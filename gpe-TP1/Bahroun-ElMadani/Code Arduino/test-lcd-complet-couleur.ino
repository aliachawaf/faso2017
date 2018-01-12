#include <OneWire.h>
#include "rgb_lcd.h"

const int pinTempEau = 2;
const int buzzer = 3; //buzzer to arduino pin 3

rgb_lcd lcd;

const int colorR = 0;
const int colorG = 100;
const int colorB = 255;

//Partie temp
#define RELAY1  7                        
const float TMin =25;
const float TMax =28;
//Partie Ph
const float PhMin =5;
const float PhMax = 8;


#define SensorPin A0          
unsigned long int avgValue;  //Store the average value of the sensor feedback
float b;
int buf[10],temp;
//partie Temp
// Initialisation du OneWire
OneWire ds(pinTempEau);

// Récupération de la température eau
boolean getTemperatureEau(float *temp) {
  byte data[9], addr[8];
  
  if (!ds.search(addr)) { // Recherche un module 1-Wire
    ds.reset_search();    // Réinitialise la recherche de module
    return false;         // Retourne une erreur
  }
  if (OneWire::crc8(addr, 7) != addr[7]) // Vérifie que l'adresse a été correctement reçue
    return false;                        // Si le message est corrompu on retourne une erreur
  if (addr[0] != 0x28) // Vérifie qu'il s'agit bien d'un DS18B20
    return false;         // Si ce n'est pas le cas on retourne une erreur
  ds.reset();             // On reset le bus 1-Wire
  ds.select(addr);        // On sélectionne le DS18B20
  ds.write(0x44, 1);      // On lance une prise de mesure de température
  delay(800);             // Et on attend la fin de la mesure
  ds.reset();             // On reset le bus 1-Wire
  ds.select(addr);        // On sélectionne le DS18B20
  ds.write(0xBE);         // On envoie une demande de lecture du scratchpad
 
  for (byte i = 0; i < 9; i++) // On lit le scratchpad
  data[i] = ds.read();       // Et on stock les octets reçus
  // Calcul de la température en degré Celsius
  *temp = ((data[1] << 8) | data[0]) * 0.0625; 
  ds.reset_search();
  // Pas d'erreur
  return true;
}
void setup() {
  pinMode(buzzer, OUTPUT);
  pinMode(13,OUTPUT);  
  pinMode(RELAY1, OUTPUT);
  Serial.begin(9600);  
  //Serial.println("Ready");
  //Test the serial monitor
  //partie lcd
  lcd.begin(16, 2);
  lcd.setRGB(colorR, colorG, colorB);
}
void loop(){

 float tempEau;
 if (getTemperatureEau(&tempEau)){
  
    // Affiche la température
    if (TMin<tempEau && TMax>tempEau){
      lcd.setCursor(0,0);
      lcd.print("Temp Eau : ");
      lcd.print(tempEau);
      lcd.print((char)223);
      lcd.write('C');
      digitalWrite(buzzer, LOW);
      digitalWrite(RELAY1,1);
      }
    else if (TMin>tempEau){
      lcd.setCursor(0,0);
      lcd.print("Temp Eau : ");
      lcd.print(tempEau);
      lcd.print((char)223);
      lcd.write('C');
      digitalWrite(buzzer, LOW);
      digitalWrite(RELAY1,0);  
                                    // ajouter code thermoplongeur

      
    }
     else if (TMax<tempEau){     // temp trop élevéé
      lcd.setCursor(0,0);
      lcd.print("Temp Eau : ");
      lcd.print(tempEau);
      lcd.print((char)223);
      lcd.write('C');
      digitalWrite(buzzer, HIGH);
      digitalWrite(RELAY1,1);
    }
 
    for(int i=0;i<10;i++)       //Get 10 sample value from the sensor for smooth the value
    { 
    buf[i]=analogRead(SensorPin);
    delay(10);
    }
    for(int i=0;i<9;i++)        //sort the analog from small to large
   {
    for(int j=i+1;j<10;j++)
    {
      if(buf[i]>buf[j])
      {
         temp=buf[i];
         buf[i]=buf[j];
         buf[j]=temp;
       }
     }
    }
  avgValue=0;
  for(int i=2;i<8;i++){                      //take the average value of 6 center sample
    avgValue+=buf[i];
  }
  float phValue=(float)avgValue*5.0/1024/6; //conversion analog -> milivolt
  phValue=3.5*phValue;                      //conversion millivolt -> valeur Ph
  
  if (PhMin<phValue && PhMax>phValue){
    const int colorR = 0;
    const int colorG = 100;
    const int colorB = 255;
    lcd.setRGB(colorR, colorG, colorB);
    digitalWrite(buzzer, LOW);// arreter buzzer
    rgb_lcd lcd;
    lcd.setCursor(0,1);
    lcd.print("Ph:");  
    lcd.print(phValue);
    digitalWrite(13, HIGH);
    delay(800);
    digitalWrite(13, LOW); 
    }

  else{
    const int colorR = 255;
    const int colorG = 10;
    const int colorB = 0;
    lcd.setRGB(colorR, colorG, colorB);
    //digitalWrite(buzzer, HIGH);// activer le buzzer
    delay(10);// Attendre 10ms
    rgb_lcd lcd;
    lcd.setCursor(0,1);
    lcd.print("Ph:");  
    lcd.print(phValue);
    digitalWrite(13, HIGH);       
    delay(800);
    digitalWrite(13, LOW);
    }   
    Serial.print(tempEau);  
    Serial.print(",");
    Serial.print(phValue);
    Serial.print("\n");
  delay(100);
  
}
}
