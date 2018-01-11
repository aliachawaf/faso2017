#!/bin/bash
./gdrive mkdir "$2"
id=`./gdrive list -q "name contains '$2'" | sed '1d' | cut -d " " -f 1`

./gdrive upload -p "$id" "$1"

sudo echo "Bonjour, un individu a sonné à votre porte, voici la photo en pièce jointe." | mutt -s "Sonnette" -a "$1" -- sonnette.interactive@gmail.com

sudo rm "$1"
