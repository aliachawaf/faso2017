// LUMINOSITE
#include "LedControl.h"
LedControl lc=LedControl(12,10,11,4);
float lum;

// BLUETOOTH
#include <SoftwareSerial.h>   //Software Serial Port
#define RxD 6
#define TxD 7 
SoftwareSerial blueToothSerial(RxD,TxD);

// ACCELEROMETRE
#include <Wire.h>
#include <ADXL345.h>
ADXL345 adxl; // Instance de la librairie

// VARIABLE D ETAT
double tempsAffichage = 10000;
double tmpDroite = -tempsAffichage;
double tmpGauche = -tempsAffichage;
double tmpStop = -tempsAffichage;
double majMatrice = -2000;
int timeCligno = 1000;
void setup() {
  /// Vitesse pour moniteur
  Serial.begin (9600);
  
  
  // Reglage de la lum
  pinMode (A0, INPUT);
  lum = (analogRead (A0)/750) *15;

  // Reglage de la matrice
  int devices=lc.getDeviceCount();
  // initialisation de tout les carrés de la matrice
  for(int address=0;address<devices;address++) {
    /*The MAX72XX is in power-saving mode on startup*/
    lc.shutdown(address,false);
    lc.setIntensity(address,(int) lum);
    lc.clearDisplay(address);
  }


  // Reglage du bluetooth
  pinMode(RxD, INPUT);
  pinMode(TxD, OUTPUT);
  setupBlueToothConnection();

  // Initialisation pour l'accéléromètre
  adxl.powerOn();

  //set activity/ inactivity thresholds (0-255)
  adxl.setActivityThreshold(75); //62.5mg per increment
  adxl.setInactivityThreshold(75); //62.5mg per increment
  adxl.setTimeInactivity(10); // how many seconds of no activity is inactive?
 
  //look of activity movement on this axes - 1 == on; 0 == off 
  adxl.setActivityX(1);
  adxl.setActivityY(1);
  adxl.setActivityZ(1);
 
  //look of inactivity movement on this axes - 1 == on; 0 == off
  adxl.setInactivityX(1);
  adxl.setInactivityY(1);
  adxl.setInactivityZ(1);
 
  //look of tap movement on this axes - 1 == on; 0 == off
  adxl.setTapDetectionOnX(0);
  adxl.setTapDetectionOnY(0);
  adxl.setTapDetectionOnZ(1);
 
  //set values for what is a tap, and what is a double tap (0-255)
  adxl.setTapThreshold(50); //62.5mg per increment
  adxl.setTapDuration(15); //625us per increment
  adxl.setDoubleTapLatency(80); //1.25ms per increment
  adxl.setDoubleTapWindow(200); //1.25ms per increment
 
  //set values for what is considered freefall (0-255)
  adxl.setFreeFallThreshold(7); //(5 - 9) recommended - 62.5mg per increment
  adxl.setFreeFallDuration(45); //(20 - 70) recommended - 5ms per increment
 
  //setting all interrupts to take place on int pin 1
  //I had issues with int pin 2, was unable to reset it
  adxl.setInterruptMapping( ADXL345_INT_SINGLE_TAP_BIT,   ADXL345_INT1_PIN );
  adxl.setInterruptMapping( ADXL345_INT_DOUBLE_TAP_BIT,   ADXL345_INT1_PIN );
  adxl.setInterruptMapping( ADXL345_INT_FREE_FALL_BIT,    ADXL345_INT1_PIN );
  adxl.setInterruptMapping( ADXL345_INT_ACTIVITY_BIT,     ADXL345_INT1_PIN );
  adxl.setInterruptMapping( ADXL345_INT_INACTIVITY_BIT,   ADXL345_INT1_PIN );
 
  //register interrupt actions - 1 == on; 0 == off  
  adxl.setInterrupt( ADXL345_INT_SINGLE_TAP_BIT, 1);
  adxl.setInterrupt( ADXL345_INT_DOUBLE_TAP_BIT, 1);
  adxl.setInterrupt( ADXL345_INT_FREE_FALL_BIT,  1);
  adxl.setInterrupt( ADXL345_INT_ACTIVITY_BIT,   1);
  adxl.setInterrupt( ADXL345_INT_INACTIVITY_BIT, 1);
  // Fin de l'init pour l'accelerometre
}

void loop() {
  // Regarde les données en entré
  setCommandeByBluetooth();
  if (isCurbing()) {
    tmpStop = millis();
  }

  // Réglage de la luminosité
  reglerLum();

  affichageMatrice();

}


void affichageMatrice(){
  bool tourneG = millis() - tmpGauche < tempsAffichage;
  bool tourneD = millis() - tmpDroite < tempsAffichage;
  bool freine = millis() - tmpStop < tempsAffichage;
  
  if (millis() - majMatrice > 500){
     if (tourneG and freine) {
        clignotantGauche();
      } else if (tourneD and freine) {
        clignotantDroite();
      }
      else if(tourneD) {
        clearAllMat();
        flecheD();
      }
      else if (tourneG) {
        clearAllMat();
        flecheG();
      }
      else if (freine) {
        clearAllMat();
        STOP();
      }
      else  {
        clearAllMat();
      }
      majMatrice = millis();
  }
}

void clignotantDroite() {
  for (int i =0;i<5;i++){
      flecheG();
      delay(timeCligno);
      clearAllMat();
      STOP();
      delay(timeCligno);
      clearAllMat();
    }
}

void clignotantGauche() {
  for (int i =0;i<5;i++){
    flecheG();
    delay(timeCligno);
    clearAllMat();
    STOP();
    delay(timeCligno);
    clearAllMat();
  }
}

void setCommandeByBluetooth () {
  // Met à jour le temps du dernier clic pou chaque bouton
  if(blueToothSerial.available()){ // Regarde si on envoyé une commande
      int res;
      String ppp;
      while (blueToothSerial.available()) {
        ppp  = blueToothSerial.read();
          if (ppp =="0") {
            tmpStop = millis();
          }
          if (ppp == "120") {
            tmpDroite = millis();
          }
           if (ppp == "248") {
            tmpGauche = millis();
          }
      }
  }
}


void reglerLum () {
  // Regle la luminosite des matrices
  lum = getLuminosite();
  for (int i = 0; i <4; i++){
    lc.setIntensity(i,lum);
  } 
}

int getLuminosite () {
  // Renvoie la luminosité sur une echelle de 0 à 15 avec 15 max
  float res = (analogRead (A0)/750.0)*15.0;
  res = (int)(res);
  return res ;
}

void setupBlueToothConnection()
{
  blueToothSerial.begin(38400); //Set BluetoothBee BaudRate to default baud rate 38400
  blueToothSerial.print("\r\n+STWMOD=0\r\n"); //set the bluetooth work in slave mode
  blueToothSerial.print("\r\n+STNA=SeeedBTSlave\r\n"); //set the bluetooth name as "SeeedBTSlave"
  blueToothSerial.print("\r\n+STPIN=0000\r\n");//Set SLAVE pincode"0000"
  blueToothSerial.print("\r\n+STOAUT=1\r\n"); // Permit Paired device to connect me
  blueToothSerial.print("\r\n+STAUTO=0\r\n"); // Auto-connection should be forbidden here
  delay(2000); // This delay is required.
  blueToothSerial.print("\r\n+INQ=1\r\n"); //make the slave bluetooth inquirable 
  Serial.println("The slave bluetooth is inquirable!");
  delay(2000); // This delay is required.
  blueToothSerial.flush();
}


void flecheG(){
  //read the number cascaded devices
  int devices=lc.getDeviceCount();
  
  //we have to init all devices in a loop
  for(int row=2;row<6;row++) {
    for(int col=0;col<8;col++) {
      for(int address=0;address<devices;address++) {
        
        lc.setLed(address,row,col,true);
        
        
      }
    }
  }
   
  lc.setLed(3,0,3,true); // on allume toute la colonne 5 de la derniere matrice
  lc.setLed(3,1,3,true);
  lc.setLed(3,6,3,true);
  lc.setLed(3,7,3,true);
  
   // on allume toute la colonne 5 de la derniere matrice
  lc.setLed(3,1,2,true);
  lc.setLed(3,6,2,true);
  
  lc.setLed(3,2,0,false);
  lc.setLed(3,5,0,false);
}

void STOP(){ //on affiche S sur la matrice numero 3
  
  for(int col=0;col<8;col++){lc.setLed(3,0,col,true);}
  for(int col=0;col<8;col++){lc.setLed(3,1,col,true);}
  for(int col=0;col<8;col++){lc.setLed(3,3,col,true);}
  for(int col=0;col<8;col++){lc.setLed(3,4,col,true);}
  for(int col=0;col<8;col++){lc.setLed(3,6,col,true);}
  for(int col=0;col<8;col++){lc.setLed(3,7,col,true);}
  lc.setLed(3,5,7,true);
  lc.setLed(3,5,6,true);
  lc.setLed(3,2,0,true);
  lc.setLed(3,2,1,true);
  
  // on affiche T sur la matrice 2 
  
  for(int col=0;col<8;col++){lc.setLed(2,1,col,true);} // allume toute la premiere ligne 
  for(int col=0;col<8;col++){lc.setLed(2,0,col,true);}
  for(int row=2;row<8;row++){for(int col=3;col<5;col++){lc.setLed(2,row,col,true);}}
  
  // on affiche le 0 sur la mtrice 1
  for(int col=0;col<6;col++){lc.setLed(1,0,col,true);}
  for(int col=0;col<6;col++){lc.setLed(1,1,col,true);}
  for(int col=0;col<6;col++){lc.setLed(1,6,col,true);}
  for(int col=0;col<6;col++){lc.setLed(1,7,col,true);}
  for(int row=2;row<6;row++){lc.setLed(1,row,0,true);
                             lc.setLed(1,row,1,true);
                             lc.setLed(1,row,4,true);
                             lc.setLed(1,row,5,true);}
                         
 // on affiche le P un peu sur la matrice 1 et surtout sur la matrice 0 
 //matrice 1
 for(int row=0;row<8;row++){lc.setLed(1,row,7,true);}
 //matrice 2
 for(int row=0;row<8;row++){lc.setLed(0,row,0,true);}
 for(int col=1;col<5;col++){lc.setLed(0,4,col,true);}
 for(int col=1;col<5;col++){lc.setLed(0,3,col,true);}
 for(int col=1;col<5;col++){lc.setLed(0,1,col,true);}
 for(int col=1;col<5;col++){lc.setLed(0,0,col,true);}
 for(int col=3;col<5;col++){lc.setLed(0,2,col,true);}
 
 // on affiche le point d'exclamation sur la matrice 0
 for(int row=0;row<8;row++){lc.setLed(0,row,7,true);}
 for(int row=0;row<8;row++){lc.setLed(0,row,6,true);}
 lc.setLed(0,5,6,false);
 lc.setLed(0,5,7,false);
 }



void flecheD(){
  int devices=lc.getDeviceCount();
  
  
  for(int row=2;row<6;row++) {
    for(int col=0;col<8;col++) {
      for(int address=0;address<devices;address++) {
        
        lc.setLed(address,row,col,true);
        
        
      }
    }
  }
   
  lc.setLed(0,0,4,true); // on allume toute la colonne 5 de la derniere matrice
  lc.setLed(0,1,4,true);
  lc.setLed(0,6,4,true);
  lc.setLed(0,7,4,true);
  
   // on allume toute la colonne 5 de la derniere matrice
  lc.setLed(0,1,5,true);
  lc.setLed(0,6,5,true);
  
  lc.setLed(0,2,7,false);
  lc.setLed(0,5,7,false);
}

 bool isCurbing (){
  //Boring accelerometer stuff
   int x,y,z;  
   adxl.readXYZ(&x, &y, &z); //read the accelerometer values and store them in variables  x,y,z
   double xyz[3];
   double ax,ay,az;
   double moy = 0.0;

  // On regarde 50 fois la valeur et on fait une moyenne
  for (int i = 0; i < 50; i++) {
    adxl.getAcceleration(xyz);
    az = xyz[2];
    if (az < 0.0 ) {
      moy = moy - az;
    }
    else {
      moy = moy + az;
    }
    
    delay (1);
  }

  moy = moy/50.0;
  // Si ay dépasse une certaine limite veut dire qu'on freine.
  return moy > 0.7;
 }

void clearAllMat() {
  for (int i = 0; i <4; i++){
    lc.clearDisplay(i);
  } 
}


