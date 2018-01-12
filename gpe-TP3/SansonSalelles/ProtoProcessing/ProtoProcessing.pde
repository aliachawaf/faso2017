import cc.arduino.*;
import org.firmata.*;
import processing.serial.*;
import java.io.*;

int[] positions = new int[96];
int j = 0;

String fichier ="fichierpositions.txt";

String i = "";
String libelle = "";
int val;
int position;
int temperature;
int tension;
int posLh; //ligne en fonction de l'heure
// The serial port:
Serial arduino;

FileWriter output= null;

void setup(){
  read();
  //lire les positions envoyé par l'arduino sur le port série
  printArray(Serial.list());
  arduino = new Serial(this, Serial.list()[1], 9600);
  val = 0;
  position = 0;
  temperature = 0;
  tension = 0;
  delay(50);
  size(200, 200);
  arduino.clear();
}

void draw(){
  
 if(arduino.available()>0)//le port contient des infos
  { 
    delay(50);
    recupDataArduino(); 
  }
 
  if(temperature >= 35){
    String envoi = "ALERT;";
    arduino.write(envoi);
  }
  
  
  if(minute()==00 && second()==0) //Toutes les heures
  {
    write(); // Ecrase et recrée le fichier de positions avec des nouvelles valeurs
    delay(300);
  }
  
  if (minute()%15 == 0)
  {
    recupH();
    println("Position dans le tableau : " + posLh);
    String envoi = "BOUGE;";
    envoi += positions[posLh];
    delay(1000);
    arduino.write(envoi);
  }
  
   clear();
   textSize(15);
   textAlign(LEFT);
   text("Position : "+position, 10, 15);
   text("Temperature : "+temperature, 10, 30);
   
   //text("Tension : "+tension, 10, 30);
 
}

void read(){
    //lecture du fichier texte  
    String[] line= loadStrings(fichier);
    println("Il y a " + line.length + " positions");
    try{
       FileReader fr = new FileReader(fichier);
       BufferedReader br = new BufferedReader(fr);
       int var = 0;
       println("Le fichier est trouve");
       for(int i=0;i<96; i++)
       {
         var = parseInt(line[i]);
         positions[i] = var;
       }
       br.close();
    }
    catch(IOException e){
      e.printStackTrace();
      for(int i=0; i<96; i++){ //on initialise a 0
        positions[i]=0;
      }
      
    }
    
    
}
  
void write(){
    try {
      FileWriter fw = new FileWriter (fichier);
      BufferedWriter bw = new BufferedWriter (fw);
      String[] ecrire = str(positions) ;// nouveau tableau de String dans lequel on met les positions du panneau
      PrintWriter fichierSortie = new PrintWriter (bw); 
      fichierSortie.println(ecrire);
      fichierSortie.close();
      //println(positions);
      saveStrings("fichierpositions.txt", ecrire);// permet de sauvegarder le fichier texte 
      System.out.println("Le fichier " + fichier + " a été créé!"); 
    }
    catch (Exception e){
      System.out.println(e.toString());
    }    
}


void recupH(){//recupere la ligne où est stocké la position du panneau pour l'heure voulue 
  int h=hour();
  int m= minute();
  posLh=(h*4)-1;
  if (m==15){
    posLh=posLh+1;
  }
  else if (m==30){
    posLh=posLh+2;
  }
  else if (m==45){
    posLh=posLh+3;
  } 
  delay(10000);
}

void recupDataArduino()
{
    try{
      i = arduino.readString(); //on lit les infos
      i = trim(i);
      println(i);
      libelle = split(i, ";")[0];
      delay(50);
      String valeur = split(i, ";")[1];
      val = parseInt(valeur);
      arduino.clear(); 
      
      switch(libelle){
         case "POS":
            //recupH();
              position = val;
              positions[posLh] = val;
              delay(50);  
              break;
      
          case "TEMP":
            temperature = val;
            break;
      
          case "TENSION":
            tension = val;
            break;
      
          default:
            break;
          
        }
    }
    catch (Exception e){
    } 
}