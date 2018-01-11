#Miroir connecté et interactif 1.0 (11/01/2018)

Tous le code python (python3) se trouve dans ~/projet/GrovePi/Software/Python
-**sonicMove.py :**
ce fichier est le driver des capteurs ultrasons, il s'occupe d'analyser les mouvements effectués et d'émuler les pressions de touches correspondantes à ces actions (pression de 'd' pour un mouvement gauche->droite, pression de 'g' pour un mouvement droite->gauche, "page_up" pour un mouvement bas->haut et 'page_down' pour un mouvement haut->bas. 
compatibilité : pynput 1.3.8.1 | GrovePi

-**temp.py :**
ce fichier est le driver du capteur de température, il récupère de régulièrement la tempèrature ambiante et l'ajoute à un fichier qui stocke ces dernières
compatibilité : GrovePi

Tous les fichiers d'interface se trouvent dans /var/www/html/miroir, ils sont composés de fichier html, css et js
-**graph.html :**
affichage d'un graph contenant les données envoyées par temp.py
 
-**heure.html :** 
affichage de l'heure en temps réel

-**index.html :**
 appelle les autres fichiers html sous forme d'iframe

-**interface.js :** 
programme js qui récupère les pressions de touche émulées et qui les interprête pour intéragir avec les interfaces contenus dans index.html

-**refreshTemp.js :** 
rafraichit de manière asynchrone le graphique de température pour faire apparaître les nouvelles données en temps réel

-**tabMeteo.js :** 
fichier js contenant des tableaux servant à l'affichage de graph.html

Comment lancer les programmes : 
il suffit de lancer tous les fichiers situé dans le dossier bash de la manière suivante : bash programme.sh

