//Bibliothèque RTC//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#include <Wire.h>
#include "DS1307.h"
int h;
int m;
int s;
DS1307 clock; //defini un objet de la classe DS1307 necessaire pour le RTC

//Bibliothèque Ecran LCD///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

#include <Wire.h>
#include "rgb_lcd.h"
rgb_lcd lcd;

//// Variables des boutons et Buzzer/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
unsigned long tok = millis(); //on init au début de la pression du bouton OK
int sosPin = 3;   // pin du bouton SOS
int inOk = 4;   // pin du bouton OK
int buzPin = 6; // pin du buzzer

int buzz = LOW;  // état actuel du Buzzer
int inSOS;  // état actuel du bouton SOS
int ok; //etat actuel du bouton OK
int okprev=LOW;  // etat passé du bouton OK
int prevSOS = LOW;  // état passé du bouton SOS

/// Variables qui servent à débug les rebonds du bouton ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

long time = 0;         
long debounce = 200;  
 
//Initialisation variable freq cardiaque//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
unsigned char cpt;
unsigned long temp[11];
unsigned long sub;
bool recuDonnee=true;
unsigned int bpm=0;//résultat du calcul du BPM
char sbpm[10];
const int erreurBPM = 1000; /// Si 1000ms sans mesure == erreur

//Variables pour l'heure////////////////////////////////////////////////////////////////////////////////////////////////////

char hh[10];
char mm[10];
char ss[10];

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    void setup()
    {
        pinMode(inOk,INPUT); //Met la pin du boutton OK en mode INPUT
        pinMode(sosPin, INPUT);  //Met la pin du boutton SOS en mode INPUT
        pinMode(buzPin, OUTPUT); //Met la pin du boutton OK en mode INPUT
        
        Serial.begin(9600);
        Serial.println("Initialisation du bracelet...");
        delay(5000);
        
        arrayInit(); //Initialise le tableau qui compte le temps
        
        Serial.println("Calibrage du BPM en cours....");
        attachInterrupt(0, interrupt, RISING);//met interrupt à 0 sur le port digital 2
        
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
        
        lcd.begin(16, 2); //Initialise l'écran LCD
        lcd.setCursor(0, 0);
        
////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

        pinMode(6, OUTPUT); // Initialise le Buzzer sur le port D6
        pinMode(3, INPUT); //Initialise le Bouton SOS sur le port D3
        pinMode(4, INPUT); //Initialise le Bouton I'm Fine sur le port D4
        lcd.setCursor(0, 1); //Place le curseur de l'écran sur 2ème colonne
        lcd.write("BPM:");

// Initialise l'horloge (fonctions de la librarie RTC)/////////////////////////////////////////////////////////////
    clock.begin();
    clock.fillByYMD(2017,12,13);//Date
    clock.fillByHMS(13,39,55);//HEURE A INITIALISER A LA MAIN
    clock.fillDayOfWeek(WED);//Jour
    clock.setTime();//write time to the RTC chip

    }
    
    void loop()
    {
       
     calcTime(); //envoi heure au RTC 
     Serial.write(bpm); //On affiche le BPM sur le port série pour Processing
   
     inSOS = digitalRead(sosPin); 
     ok = digitalRead(inOk);
     
     if (ok){
      tok=millis();
     }
     analogRead(bpm);

     lcdBPM(); //Affiche la valeur du BPM sur l'écran
     lcdHeure(); //Affiche l'heure sur l'écran
    
//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

//bpm=51;
if (not digitalRead(buzPin) && doitAllumer()){
    digitalWrite(buzPin,HIGH);
    //Signal processing pour SMS
  }

if (doitEteindre()){
    digitalWrite(buzPin,LOW);
  }
  prevSOS = inSOS;
}
    
////Fonction: calcul du BPM de la fréquence cardiaque///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
void bpmCalc()  {
     if(recuDonnee)
        { 
          bpm=600000/(temp[10]-temp[0]);//60*10*1000/20_temps_total
          //Serial.print("bpm:\t");
          Serial.println(bpm);

        
        }
       recuDonnee=1;//bit signe
}
   
//Fonction de la bibliothèque RTC permet d'afficher une alterte si le capteur ne reçoit pas de valeur//////////////////////////////////////////////////////////////////////////////////////////////
    void interrupt()
    {
        temp[cpt]=millis();
        Serial.println(cpt,DEC);
        Serial.println(temp[cpt]);
        switch(cpt)
        {
            case 0:
                sub=temp[cpt]-temp[10];
                Serial.println(sub);
                break;
            default:
                sub=temp[cpt]-temp[cpt-1];
                Serial.println(sub);
                break;
        }
        if(sub>erreurBPM)//1 secondes sans mesure == erreur
        {
            recuDonnee=0;//sign bit
            cpt=0;
            Serial.println("Erreur de mesure! Veuillez vérifier l'appareil" );
            arrayInit();
        }
        if (cpt==10&&recuDonnee)
        {
            cpt=0;
          //  bpmCalc();
        }
        else if(cpt!=10&&recuDonnee)
        cpt++;
        else 
        {
            cpt=0;
            recuDonnee=1;
        }
    }
    
///// Fonction: Initialise le tableau temp/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

    void arrayInit()
    {
        for(unsigned char i=0;i < 10;i ++)
        {
            temp[i]=0;
        }
        temp[10]=millis(); //On stocke dans la cellule 10 le temps écoulé, afin de pouvoir calculer le BPM
    }


//// Fonction de la bilbiothèque RTC: permet l'affichage des données sotckées dans le module //////////////////////////////////////////////////////////////////////////////////////////
// Les fonctions d'affichage sont commentées pour simplifier l'affichage du moniteur série ///////////////////////////////////////////////////////////////////////////////////////////
void calcTime()
{
    clock.getTime();
    //Serial.print(clock.hour, DEC);
    h=clock.hour; // Stocke l'heure
    //Serial.print(":");
    //Serial.print(clock.minute, DEC);
    m=clock.minute; //Stocke les minutes
   // Serial.print(":");
    //Serial.print(clock.second, DEC);
    s=clock.second;  //Stocke les secondes
  //  Serial.print("  ");
  //  Serial.print(clock.month, DEC);
  //  Serial.print("/");
 //   Serial.print(clock.dayOfMonth, DEC);
  //  Serial.print("/");
 //   Serial.print(clock.year+2000, DEC);
 //   Serial.print(" ");
 //   Serial.print(clock.dayOfMonth);
  //  Serial.print("*");
    switch (clock.dayOfWeek)// Friendly printout the weekday
    {
        case MON:
    //    Serial.print("MON");
        break;
        case TUE:
   //     Serial.print("TUE");
        break;
        case WED:
  //      Serial.print("WED");
        break;
        case THU:
 //       Serial.print("THU");
        break;
        case FRI:
    //    Serial.print("FRI");
        break;
        case SAT:
   //     Serial.print("SAT");
        break;
        case SUN:
   //     Serial.print("SUN");
        break;
    }
   // Serial.println(" ");
}


/// Affichage BPM sur ecran LCD ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

void lcdBPM(){
    if (bpm<100){
    lcd.setCursor(4 , 1);
    itoa(bpm,sbpm,10);
    lcd.write(sbpm);
    lcd.setCursor(6,1);
    lcd.print(" ");
    } 
    else {
    lcd.setCursor(4 , 1);
    itoa(bpm,sbpm,10);
    lcd.write(sbpm);
    }
}


//// AFFICHAGE HEURE ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

void lcdHeure(){
if (h<10){
      lcd.setCursor(0,0);
      lcd.write("0");
      lcd.setCursor(1,0);
      itoa(h,hh,10);
      lcd.write(hh);
     }
 else {
      lcd.setCursor(0, 0);
      itoa(h,hh,10);
      lcd.write(hh);
      }
    
    lcd.setCursor(2, 0);
    lcd.write(":");

if (m<10){
   lcd.setCursor(3,0);
   lcd.write("0");
   lcd.setCursor(4,0);
    itoa(m,mm,10);
    lcd.write(mm);

 }
 else {
    lcd.setCursor(3,0);
    itoa(m,mm,10);
    lcd.write(mm);
 }
    lcd.setCursor(5,0);
    lcd.write(":"); 
if (s<10){
    lcd.setCursor(6,0);
    lcd.write("0");
    lcd.setCursor(7,0);
    itoa(s,ss,10);
    lcd.write(ss);
        }
else {lcd.setCursor(6,0);
     itoa(s,ss,10);
     lcd.write(ss);
        }
}

//Fonction qui teste si l'alerte doit être déclenchée//////////////////////////////////////////////////////////////////////

bool doitAllumer(){

  if(millis() - tok  <= 10000){
    return false;
  }
  if(bpm > 0) {
     if (bpm < 40 or bpm > 110) {
        buzz = HIGH; //on allume le buzzer
        return true;
         }
      }
   if (inSOS == HIGH && prevSOS == LOW && millis() - time > debounce){
     time = millis();
     return true;
        
       }
      return false;
}


//Fonction qui teste si l'alerte doit être stopée//////////////////////////////////////////////////////////////////////
bool doitEteindre(){
   if (ok == HIGH && okprev==LOW){
    return true;
   }
   if (bpm>40){
    return true;
   }
  return false;
}



