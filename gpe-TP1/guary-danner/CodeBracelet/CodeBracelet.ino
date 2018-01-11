//Besoin d'inclure les bibliothèque LCD et RTC avant de Téléverser el programme

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
int r=0;
int g=0;
int b=0;
bool bon;
bool alerte;
bool debranche=false;
String salerte;

//// Variables des boutons et Buzzer/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
unsigned long tok = -10000; //on init au début de la pression du bouton OK
int sosPin = 3;   // pin du bouton SOS
int inOk = 4;   // pin du bouton OK
int buzPin = 6; // pin du buzzer

// int buzz = LOW;  // état actuel du Buzzer
int inSOS;  // état actuel du bouton SOS
int ok; //etat actuel du bouton OK
int okprev = LOW; // etat passé du bouton OK
int prevSOS = LOW;  // état passé du bouton SOS

/// Variables qui servent à débug les rebonds du bouton ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

long time = 0;
long debounce = 200;

//Initialisation variable freq cardiaque//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
unsigned char cpt;
unsigned long temp[11];
unsigned long sub;
bool recuDonnee = true;
volatile unsigned int bpm = 0; //résultat du calcul du BPM
char sbpm[10];
const int erreurBPM = 1000; /// Si 1000ms sans mesure == erreur

//Variables pour l'heure////////////////////////////////////////////////////////////////////////////////////////////////////

char hh[10];
char mm[10];
char ss[10];

//////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

void setup() {
    
  //Initialisation des deux boutons
  pinMode(inOk, INPUT);
  pinMode(sosPin, INPUT);
  // Ini du buzzer
  pinMode(buzPin, OUTPUT);

  // Ini du moniteur
  Serial.begin(9600);
  //Serial.println("Initialisation du bracelet...");

  arrayInit(); //Initialise le tableau qui compte le temps

  //Serial.println("Calibrage du BPM en cours....");
  attachInterrupt(digitalPinToInterrupt(2), interrupt, RISING); //met interrupt à 0 sur le port digital 2


  //Initialise l'écran LCD
  lcd.begin(16, 2);
  lcd.setCursor(0, 0);


  //Place le curseur de l'écran sur 2ème colonne
  lcd.setCursor(0, 1);
  lcd.write("BPM:");

  // Initialise l'horloge (fonctions de la librairie RTC)
  clock.begin();
  clock.fillByYMD(2017, 12, 13); //Date
  clock.fillByHMS(13, 39, 55); //HEURE A INITIALISER A LA MAIN
  clock.fillDayOfWeek(WED);//Jour
  clock.setTime();//write time to the RTC chip

}


void loop() {
   
  calcTime(); // Recupere l'heure du rtc
  lcdHeure(); // Affiche l'heure sur l'écran
  couleurLCD(); //Met l'écran en rouge ou vert selon l'état de l'utilisateur

  lcdBPM(); //Affiche la valeur du BPM sur l'écran

  //Serial.write("F");
  //Serial.write("B");
  //Serial.write(alerte); //On affiche le bool qui donne l'alerte sur le port série pour Processing
  
  inSOS = digitalRead(sosPin); // Regarde si le bouton sos est enclenché
  ok = digitalRead(inOk);      // Regarde si le bouton ok est enclenché


  // si enclenché et buzzer allumé on garde en mémoire depuis combien de temps
  if (ok && digitalRead(buzPin)) {
    tok = millis();             
  }

  // si le buzzer est éteint et qu'on doit l'allumer, on l'allume
  if (not digitalRead(buzPin) && doitAllumer()) {
    digitalWrite(buzPin, HIGH);
    alerte = true;
    
    Serial.println("1"); 
    Serial.print("");
    bon=false;
    // Ajouter Signal processing pour SMS
  }

  if (doitEteindre()) {
    digitalWrite(buzPin, LOW);
    alerte = false;
    bon=true;
  }

  prevSOS = inSOS;        // Garde en mémoire l'état précédent du bouton alerte
}

////Fonction: calcul du BPM de la fréquence cardiaque
void bpmCalc()  {
  if (recuDonnee) {
    bpm = 600000 / (temp[10] - temp[0]); //60*10*1000/20_temps_total
    //Serial.println("bpm:\t");
    //Serial.println(bpm);
    Serial.write(sbpm); //On affiche le BPM sur le port série pour Processing
    
    Serial.println(" ");
  }
  recuDonnee = 1; //bit signe
}

//Fonction de la bibliothèque du capteur de fréquence permet d'afficher une alterte si le capteur ne reçoit pas de valeur et sinon calcule bpm
void interrupt() {
  temp[cpt] = millis();
  //Serial.println(cpt, DEC);
  //Serial.println(temp[cpt]);
  switch (cpt) {
    case 0:
      sub = temp[cpt] - temp[10];
      //Serial.println(sub);
      break;
    default:
      sub = temp[cpt] - temp[cpt - 1];
      //Serial.println(sub);
      break;
  }
  if (sub > erreurBPM) //1 secondes sans mesure == erreur
  {
    recuDonnee = 0; //bit signe
    cpt = 0;
    //Serial.println("Erreur de mesure! Veuillez vérifier l'appareil" );
    debranche=true;
    arrayInit();
  }
  if (cpt == 10 && recuDonnee)
  {
    cpt = 0;
    bpmCalc();
    debranche = false;
  }
  else if (cpt != 10 && recuDonnee){
    cpt++;
    debranche = false;
  }
  else
  {
    cpt = 0;
    recuDonnee = 1;
  }
}

///// Fonction: Initialise le tableau temp/////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

void arrayInit()
{
  for (unsigned char i = 0; i < 10; i ++)
  {
    temp[i] = 0;
  }
  temp[10] = millis(); //On stocke dans la cellule 10 le temps écoulé, afin de pouvoir calculer le BPM
}


//// Fonction de la bilbiothèque RTC: permet l'affichage des données sotckées dans le module //////////////////////////////////////////////////////////////////////////////////////////
// Les fonctions d'affichage sont commentées pour simplifier l'affichage du moniteur série ///////////////////////////////////////////////////////////////////////////////////////////
void calcTime()
{
  clock.getTime();
  //Serial.print(clock.hour, DEC);
  h = clock.hour; // Stocke l'heure
  //Serial.print(":");
  //Serial.print(clock.minute, DEC);
  m = clock.minute; //Stocke les minutes
  // Serial.print(":");
  //Serial.print(clock.second, DEC);
  s = clock.second; //Stocke les secondes
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

void lcdBPM() {
  if (bpm == 0 and !debranche and !alerte) {
    int r=0;
    int g=0;
    int b=250;
    lcd.setRGB(r, g, b);
    lcd.setCursor(4 , 1);
    lcd.write("INIT");
    
  }
  else if (debranche and bpm != 0 and !alerte) {
    int r=0;
    int g=0;
    int b=250;
    lcd.setRGB(r, g, b);
    lcd.setCursor(4 , 1);
    lcd.write("STOP");
  }
  else if (bpm < 100) {

    lcd.setCursor(4 , 1);
    itoa(bpm, sbpm, 10);
    lcd.write(sbpm);
    lcd.setCursor(6, 1);
    lcd.print(" ");
    lcd.setCursor(7, 1);
    lcd.print(" ");
    
  }
  else {
    lcd.setCursor(4 , 1);
    itoa(bpm, sbpm, 10);
    lcd.write(sbpm);
    lcd.setCursor(7,1);
    lcd.write(" ");
  }
}


//// AFFICHAGE HEURE ///////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////////

void lcdHeure() {
  if (h < 10) {
    lcd.setCursor(0, 0);
    lcd.write("0");
    lcd.setCursor(1, 0);
    itoa(h, hh, 10);
    lcd.write(hh);
  }
  else {
    lcd.setCursor(0, 0);
    itoa(h, hh, 10);
    lcd.write(hh);
  }

  lcd.setCursor(2, 0);
  lcd.write(":");

  if (m < 10) {
    lcd.setCursor(3, 0);
    lcd.write("0");
    lcd.setCursor(4, 0);
    itoa(m, mm, 10);
    lcd.write(mm);

  }
  else {
    lcd.setCursor(3, 0);
    itoa(m, mm, 10);
    lcd.write(mm);
  }
  lcd.setCursor(5, 0);
  lcd.write(":");
  if (s < 10) {
    lcd.setCursor(6, 0);
    lcd.write("0");
    lcd.setCursor(7, 0);
    itoa(s, ss, 10);
    lcd.write(ss);
  }
  else {
    lcd.setCursor(6, 0);
    itoa(s, ss, 10);
    lcd.write(ss);
  }
}

//Fonction qui teste si l'alerte doit être déclenchée//////////////////////////////////////////////////////////////////////

bool doitAllumer() {

  if (millis() - tok  <= 10000) {
    return false;
  }

   if (inSOS == HIGH  && prevSOS == LOW && millis() - time > debounce) {

    time = millis();
    return true;
 }
 
  else if (bpm > 0) {
    if (bpm < 30 or bpm > 110) {
      //digitalWrite(buzPin, HIGH);

      return true;
    }
  }

  return false;
}


//Fonction qui teste si l'alerte doit être stopée
bool doitEteindre() {
  if (ok == HIGH && okprev == LOW) {
    r=0;
    g=250;
    b=0;
    lcd.setRGB(r, g, b);
    return true;

  }
  return false;
}


//Variation couleur ecran
void couleurLCD() {
 
if(bon && !alerte and not debranche){
  int r=0;
  int g=250;
  int b=0;
  lcd.setRGB(r,g,b);
}

else if (alerte && !bon){
  int r=250;
  int g=0;
  int b=0;
  lcd.setRGB(r,g,b);
}

else if (bpm > 30 or bpm < 110 and !debranche){
    alerte = false;
    bon=true;
}

else if (bpm !=0 && bpm<=30 or bpm >= 110 and !debranche){
    alerte = true;
    bon=false;
}
}

//Changement couleur LCD
void setRGB(int r, int g, int b);




