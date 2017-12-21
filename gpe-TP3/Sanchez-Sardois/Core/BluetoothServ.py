#!/usr/bin/env python

import os
import glob
import time
import random

from bluetooth import *

server_sock = BluetoothSocket( RFCOMM )
server_sock.bind(("",PORT_ANY))
server_sock.listen(1)

port = server_sock.getsockname()[1]

uuid = "69090025-0c61-4300-8330-7dcab0752d99"

advertise_service( server_sock, "SmartSpeakersBlServ",
                   service_id = uuid,
                   service_classes = [ uuid, SERIAL_PORT_CLASS ],
                   profiles = [ SERIAL_PORT_PROFILE ],
                 )

print ("Attente d'une connexion...")
client_sock, client_info = server_sock.accept()
print ("Client connecte: "), client_info

while True:

    try:
        req = client_sock.recv(1024)
        print "Commande recu: %s" % req
        
    except KeyboardInterrupt:

        print ("deconnecte")

        client_sock.close()
        server_sock.close()
        print ("Serveur Ferme")

        break
