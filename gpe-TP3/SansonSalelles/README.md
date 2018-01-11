
Projet : Panneau Tournant Rotatif
=========================
Noms : Sanson Yvan, Salelles Marie
---------------------------------------------------

**Hiérarchie du code :**
* /PanneauTournantArduino : on y trouve le fichier de code concernant l'Arduino.
* /ProtoProcessing : on y trouve le fichier de code relatif à la partie Processing sur l'ordinateur. On y trouve aussi le ficher "fichierpositions.txt" qui sert à stocker les positions du panneau solaire en fonction de la journée.

**Procédure d'installation :**

Pour installer le code Arduino, il est nécéssaire de l'avoir l'environnement de développement Arduino, ainsi que les bibliothèques correspondantes (données plus bas dans le document).
Il faudra ensuite téléverser sur la carte Arduino, après avoir branché correctement les modules Grove et le servomoteur sur les ports indiqués en commentaires dans le code.
Pour la partie Processing, il est nécessaire d'avoir l'environnement Processing (téléchargeable sur leur site) ainsi que certaines bibliothèques (données plus bas dans le document).
Il faudra ensuite trouver le bon port série, sur lequel l'Arduino est reliée au PC. Il sera peut être nécessaire de changer certaines parties du code, ou le branchement de l'Arduino.

**Compatibilité avec les bibliothèques :**

Pour ce projet, nous utilisons plusieurs bibliothèques, à la fois pour la partie Arduino et pour la partie Processing.
* Partie Arduino :
	* Biblothèque Servo : Compatible avec toutes les versions.
	* Bibliothèque DHT : Compatible avec toutes les versions. Attention cependant, certaines versions (1.3.0) requièrent l'installation d'une bibliothèque supplémentaire : Adafruit_Sensor
* Partie Processing :
	* Bibliothèque Arduino/Firmata : Compatible avec toutes les versions.
	* Bibloithèque Serial : Compatible avec toutes les versions. 

**Informations supplémentaires à propos du projet :**
* Version du projet : 1.0.0
* Date de dernière mise à jour du projet : 11/01/2018
