 import processing.serial.*;

 Serial myPort;        // Variable Port Série
 int xPos = 1;         // variable abscisse  - x
 int xPos0=1;       // variable mémorisation xPos n-1

float yPos=1;  // variable yPos - ordonnée
float yPos0=1; // variable yPos n-1

 void setup () {

 // initialise la fenêtre 
 size(400,220);  


 // Liste tous les ports disponible et affiche le résultat 
 println(Serial.list());

 // Le port COM3 est listé avec l'indice 1
 // donc j'ouvre le port Serial.list()[1].
 // A adapter si votre port est différent - cf liste qui s'affiche à l'exécution
 myPort = new Serial(this, Serial.list()[1], 9600);
 // ne génère aucun évènement Série tant qu'aucun caractère saut de ligne n'est reçu
 myPort.bufferUntil('\n');
 // initialise le fond de la fenêtre
 background(255);// 0 = noir - 255 = blanc
 }
 void draw () {
  int valeur = myPort.read();
  delay(3000);
  println(valeur);
  
   if (valeur != 0) {

 yPos=valeur; // l'ordonnée est la valeur reçue par le port série

 // trace la ligne
 stroke(255,0,0); // fixe la couleur utilisée pour le tracé en RVB 

 line (xPos0,height-yPos0,xPos,height-yPos); // trace une ligne en tenant compte valeur reçue

 xPos0=xPos; // mémorisation xPos n-1
 yPos0=yPos; // mémorisation xPos n-1

 // à la fin de l'écran revient au début
 if (xPos >= width) {
 xPos = 0;
 xPos0=0; // pour retour de la trace sans ligne

 background(255); // 0 pour noir - 255 pour blanc...  
 } 
 else {
 // incrémente la position horizontale (abscisse)
 xPos++;
 }
 }
 }