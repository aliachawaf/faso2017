// Guide NTP : https://tttapa.github.io/ESP8266/Chap15%20-%20NTP.html

#include <ESP8266WiFi.h>
#include <ESP8266WiFiMulti.h>
#include <WiFiUdp.h>
#include <SPI.h>
#include <SD.h>
#include <I2Cdev.h>

//___
//PARTIE NTP
  // Créer une instance de la classe ESP8266WiFiMulti appelée 'wifiMulti'
  ESP8266WiFiMulti wifiMulti;
  // Créer une instance de la classe WiFiUDP pour envoyer et recevoir des paquets
  WiFiUDP UDP;
  // adresse du serveur NTP
  IPAddress timeServerIP;
  // Adresse du pool NTP Francais
  const char* NTPServerName = "0.fr.pool.ntp.org";
  // Créer une variable contenant la taille d'un paquet NTP
  const int NTP_PACKET_SIZE = 48;
  // Créer un buffer pour acceuillir les paquet à envoyer ou ceux reçus
  byte NTPBuffer[NTP_PACKET_SIZE];

  // Si HeureHiver = 1, appliquer l'heure d'hiver
  bool HeureHiver = 1;

  // Variables pour le temp
  unsigned long intervalNTP1 = 60000;     // 1 minute en temps UNIX
  unsigned long intervalNTP2 = 1*60000;   // 5 minute en temps UNIX (Ici 1 pour l'exemple)
  unsigned long prevNTP1 = 0;             
  unsigned long prevNTP2 = 0;
  unsigned long lastNTPResponse = millis();
  uint32_t timeUNIX = 0;
  
  unsigned long prevActualTime = 0;
  unsigned int compteur = 0;
  
//___
// PARTIE SD
  const int chipSelect = 4;



//__________________________________________________________________________________________________________________________________________________________________________
// Partie Setup
void setup() {
  
  // ___
  // Setup communication Serie
  // Initialisation de la communication par port serie. 
  Serial.begin(38400);
  delay(10);

  
  // ___
  // Setup Carte Sd
  // Detection de la carte Micro SD
  Serial.print("Initialisation de la carte SD ...");

  // Regarde si la carte SD est bien accessible
  if (!SD.begin(chipSelect)) {  // Si elle n'est pas accessible
    Serial.println("La carte est inaccessible ou débranchée");
    // Redémarrer
    Serial.flush();
    ESP.reset();
  }
  Serial.println("card initialized.");


  // ___ 
  // Setup Wifi
  // Connection au reseau Wifi
  startWiFi();                   // Connexion au réseau Wifi
  startUDP();                    // Initialisation du protocole NTP

  if(!WiFi.hostByName(NTPServerName, timeServerIP)) { // Récupère l'adresse IP du serveur NTP
    Serial.println("La requete NTP a échoué, redémarrage.");  // Si cela échoue, redemarrer
    Serial.flush();
    ESP.reset();
  }

  Serial.print("Time server IP:\t");  // Affiche l'ip du serveur NTP
  Serial.println(timeServerIP);
  
  Serial.println("\r\nEnvoie d'une requete NTP ...");
  sendNTPpacket(timeServerIP);  
  
}

//__________________________________________________________________________________________________________________________________________________________________________
// Partie Loop
void loop() {
  // Creation d'une variable pour le timer
  
  unsigned long currentMillis = millis();

  if (currentMillis - prevNTP1 > intervalNTP1) { // Si une minute est passé depuis le dernier paquet NTP envoyé
    prevNTP1 = currentMillis;
    Serial.println("\r\nSending NTP request ...");
    sendNTPpacket(timeServerIP);               // Envoie une requete NTP
  } // endIf

  uint32_t time = getTime();                   // Vérifie si un paquet NTP est arrivé

  if (time) {                                  // Si un paquet d'horodatage est disponible (https://fr.wikipedia.org/wiki/Horodatage)
    timeUNIX = time;
    Serial.print("Réponse NTP : \t");
    Serial.println(timeUNIX);
    lastNTPResponse = currentMillis;
  } else if ((currentMillis - lastNTPResponse) > 3600000) {
    Serial.println("1 heure écoulé depuis la dernière réponse du serveur, redémarrage.");
    Serial.flush();
    ESP.reset();
  } // endIf

  uint32_t actualTime = timeUNIX + (currentMillis - lastNTPResponse)/1000;
  
  if (actualTime != prevActualTime && timeUNIX != 0) { // Si une seconde s'est écoulé depuis le dernier affichage de l'heure : Afficher l'heure
    prevActualTime = actualTime;
    Serial.printf("\rUTC time:\t%d:%d:%d Compteur : %d   \n", getHours(actualTime), getMinutes(actualTime), getSeconds(actualTime), compteur);
  } // endIf

  if (currentMillis - prevNTP2 > intervalNTP2) { // Si cinq minutes se sont écoulés depuis le dernier paquet NTP envoyé
    prevNTP2 = currentMillis;
    // Creer une chaine de caractère afin d'acc les données dans le fichier log
    String dataString = "";
    dataString += (getHours(actualTime));
    dataString += (":");
    dataString += (getMinutes(actualTime));
    dataString += (":");
    dataString += String(compteur);

    // Ouvre le fichier "releve.txt
    File dataFile = SD.open("releve.txt", FILE_WRITE);

    // Si le fichier est bien disponible : 
    if (dataFile) {
      // Ecrire dans le fichier txt la chaine de caractère dataString
      dataFile.println(dataString);
      // Ferme le fichier log.txt
      dataFile.close();
      // Ecrit dans le Serial ce qui a été ajouté dans le fichier texte
      Serial.println(dataString);
    }
    // Si le fichier ne peut pas être ouvert
    else {
      // Ecrire qu'il y a une erreur dans le Serial
      Serial.println("Erreur lors de l'ouverture de log.txt");
    }
    // Remet le compteur à 0
    compteur = 0;
  } // endIf
  delay(50);
} // EndLoop





//__________________________________________________________________________________________________________________________________________________________________________
// Partie Fonctions

void startWiFi() { // Connexion au réseau Wifi
 
  wifiMulti.addAP("Livebox-AE9C", "WDTrCPy5MoSwnE7NmW");   // Ajoute les informations de connexion (ID/MDP)
  Serial.println("Connexion ... ");
  while (wifiMulti.run() != WL_CONNECTED) {  // Attend que la wifi se connecte
    delay(250);
    Serial.print('.');
  }
  Serial.println("\r\n");
  Serial.print("Connected to ");
  Serial.println(WiFi.SSID());             // Ecrit dans le Serial l'ID du réseau 
  Serial.print("IP address:\t");
  Serial.print(WiFi.localIP());            // Ecrit dans la Serial l'adresse IP de l'ESP
  Serial.println("\r\n");
}

void startUDP() {
  Serial.println("Démarrage de l' UDP");
  UDP.begin(123);                          // Ecoute le port 123
  Serial.print("Port local :\t");
  Serial.println(UDP.localPort());
  Serial.println();
}

uint32_t getTime() {
  if (UDP.parsePacket() == 0) { // S'il n'y a pas encore de réponse
    return 0;
  }
  UDP.read(NTPBuffer, NTP_PACKET_SIZE); // Lire le paquet UDP reçu
  // Combine les 4 paquets d'horodatage en une variable de 32 bit contenant le temps actuel
  uint32_t NTPTime = (NTPBuffer[40] << 24) | (NTPBuffer[41] << 16) | (NTPBuffer[42] << 8) | NTPBuffer[43];
  // Converti le temps NTP en temps UNIX
  const uint32_t seventyYears = 2208988800UL;
  // Soustrait 70 années
  uint32_t UNIXTime = NTPTime - seventyYears;
  return UNIXTime;
}

void sendNTPpacket(IPAddress& address) {
  memset(NTPBuffer, 0, NTP_PACKET_SIZE);  // Remet tout les bits du buffer à 0
  // Initialisation de la requête NTP
  NTPBuffer[0] = 0b11100011;   // Requête de base NTP
  // Envoie le paquet
  UDP.beginPacket(address, 123); // Les requêtes NTP se font sur le port 123
  UDP.write(NTPBuffer, NTP_PACKET_SIZE);
  UDP.endPacket();
}

// Transforme le temps UNIX en secondes
inline int getSeconds(uint32_t UNIXTime) {
  return UNIXTime % 60;
}

// Transforme le temps UNIX en minutes
inline int getMinutes(uint32_t UNIXTime) {
  return UNIXTime / 60 % 60;
}

// Transforme le temps UNIX en heures
inline int getHours(uint32_t UNIXTime) {
  if (HeureHiver == true)
    return (UNIXTime + 3600) / 3600 % 24;
  else
    return (UNIXTime) / 3600 % 24;
}
