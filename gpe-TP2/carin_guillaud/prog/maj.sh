# Suppression des erreurs pyaudio
# Enlever ou renommer les fichiers relatifs à pulse sous /usr/share/alsa (par ex oulse.conf.d)...
# Mettre en commentaires les entrées inutiles dans /usr/share/alsa.conf (ex : surrround, ...)
# Erreurs relatives à jack : 
#    sudo apt-get install dbus-x11
#    sudo apt-get install jackd2
#    dbus-launch jack_control start
# Erreur ntp
#   installation apt install ntpdate
#   MAJ /etc/timezone avec Europe/Paris
#   dpkg-reconfigure tzdata
sudo ntpdate -u pool.ntp.org
