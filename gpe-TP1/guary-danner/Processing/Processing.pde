
//Importation des differentes librairies (SMS, Fichier txt)
import processing.serial.*;
import java.io.FileWriter;
import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.net.HttpURLConnection;
import java.net.URL;
import java.net.URLEncoder;


Serial monPort; // Objet responsable de la lecture de valeurs sur le port serie


//VARIABLES
//Affichage graphique
 int xPos = 1;         // variable abscisse  - x
 int xPos0=1;       // variable mémorisation xPos n-1

float yPos=1;  // variable yPos - ordonnée
float yPos0=1; // variable yPos n-1

//Ecriture fichier texte

String nomDossier = "Desktop/"; //dossier de sauvegarde du fichier texte (a partir de ~

String nomFichier = "Frequence.txt" ; //fichier créé

int lf = 10; //saut de ligne en ascii

int valeur;
int valeurintermediaire=-1;

FileWriter output = null;

//Envoi SMS
String myString =null;
String myStringintermediaire=null;

String results=null;
boolean valeurbool=false;



// FONCTION UTILISEE UNIQUEMENT AU DEPART DU PROGRAMME
//
void setup() {
  size(400,220);  //Initialisation de la fenetre pour le graphique

  println("Ports serie disponibles :");
  String [] lesPorts =Serial.list(); //Affichage des ports disponibles
  for (int i=0; i<lesPorts.length;i++) { println("port ",i," : ",lesPorts[i]);} 
 
  
  String nomPort = lesPorts[9] ; //Valeur du port correspondant au arduino à mettre dans les crochets
  monPort = new Serial(this, nomPort, 9600); //Connection avec Arduino sur la meme fréquence (ici 9600)
  monPort.clear();
  background(255);// 0 = noir - 255 = blanc
  
//Creation et Ouverture du fichier Texte
 try {
    output = new FileWriter(nomDossier + nomFichier, true); 
    println("fichier ouvert"); //Cas ou l'on reussit
  }
  catch (IOException e) {
    println("Ouverture de fichier ne marche pas"); e.printStackTrace();
    exit(); //Cas d'erreur
  }



}



//FONCTIONS
void draw() {
  
  
  //Partie document texte
   myString = monPort.readStringUntil(lf); //Lire les données recues jusqu'au saut de ligne
   if (myString!=null) {
   myString = trim(myString); //Séparer le texte recu en ascii
   println(myString);
   println(valeurbool);
   if (myString=="True") { //fonction qui determine si il y a une alerte
     valeurbool=true;
     
   }
     
   else {
   valeur=int(myString);
   }
  
  
  if (valeur != 0) { // 0 = pas de nouvelle valeur à lire 
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
  
  
    println(valeurbool);
    println(valeur); // AFFICHE a l'ecran la valeur lue
    //delay(1000);
    // TO DO : 
    try {
    output.write("valeur :");
    output.write(nf(valeur)); // number format -> String pour affichage
                              // attention, s'utilise avec plus de param si c'est un nb réel à écrire
    output.write("\n");
    println("valeur ecrite dans fichier");
    output.flush(); // vide le buffer sur disque (si fichier utilisé tout de suite par quelqu'un) 
  }
  catch (IOException e) {
    println("Ecriture dans fichier ne marche pas"); e.printStackTrace();
    exit();
    
  }
    
  }
  else {
      
    delay(10000); // s'arrête 10000ms le temps que de nouvelles données arrivent sur le port série
  }
   }
   
   //Partie SMS
   try
   {
     if (((valeur<30 || valeur>110) && valeur!=0 && results==null)  || (valeurbool==true && results==null)){ //Cas de connections http
     String myUrl = "https://api.allmysms.com/http/9.0/?login=marcantoine&apiKey=dd089a2d5014721&message=Alerte,%20j%27ai%20besoin%20d%27aide%20au%20plus%20vite%20.%20STOP%20au%2036180&mobile=0630141930&tpoa=Proche";
     String results = doHttpUrlConnectionAction(myUrl);
     System.out.println(results);
     results="envoyé";
     
     }
   }
   catch (Exception e)
   {
     // deal with the exception in your "controller"
   }
   
 }
//Cas d'exceptions pour la requete
 private String doHttpUrlConnectionAction(String desiredUrl)
 throws Exception
 {
   URL url = null;
   BufferedReader reader = null;
   StringBuilder stringBuilder;

   try
   {
     // create the HttpURLConnection
     url = new URL(desiredUrl);
     HttpURLConnection connection = (HttpURLConnection) url.openConnection();
     
     // just want to do an HTTP GET here
     connection.setRequestMethod("GET");
     
     // uncomment this if you want to write output to this url
     //connection.setDoOutput(true);
     
     // give it 15 seconds to respond
     connection.setReadTimeout(5*1000);
     connection.connect();

     // read the output from the server
     reader = new BufferedReader(new InputStreamReader(connection.getInputStream()));
     stringBuilder = new StringBuilder();

     String line = null;
     while ((line = reader.readLine()) != null)
     {
       stringBuilder.append(line + "\n");
     }
     return stringBuilder.toString();
   }
   catch (Exception e)
   {
     //e.printStackTrace();
           println("url not found");
     throw e;

   }
   finally
   {
     // close the reader; this can throw an exception too, so
     // wrap it in another try/catch block.
     if (reader != null)
     {
       try
       {
         reader.close();
       }
       catch (IOException ioe)
       {
         ioe.printStackTrace();
         
       }
     }
   }
}


// FONCTION QUI S'EXECUTE AU MOMENT OU ON TAPE SUR UNE TOUCHE CLAVIER
//
void keyPressed() { 
  exit(); // MET FIN A L'EXECUTION DU PROGRAMME
  

}