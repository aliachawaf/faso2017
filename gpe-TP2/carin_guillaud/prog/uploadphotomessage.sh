
#!/bin/bash
./gdrive mkdir "$3"
id=`./gdrive list -q "name contains '$3'" | sed '1d' | cut -d " " -f 1`

./gdrive upload -p "$id" "$1"
./gdrive upload -p "$id" "$2"

sudo echo "Bonjour, un individu a sonné à votre porte, voici la photo et l'enregistrement vidéo en pièces jointes." | mutt -s "Sonnette" -a "$1" "$2" -- sonnette.interactive@gmail.com

sudo rm "$1" "$2"
