import subprocess
import os
import urllib2

def checkConnection():
    try:
        urllib2.urlopen('http://www.google.fr', timeout=1)
        return True
    except urllib2.URLError as err: 
        return False

def isAvailable(ssid):
    res = subprocess.check_output(("iwlist", "wlan0", "scan"))
    pos = res.find(ssid)
    return pos != -1

def configConnection(ssid, password):
    text = "source-directory /etc/network/interfaces.d\nauto lo\niface lo inet loopback\n\niface eth0 inet dhcp\n\nallow-hotplug wlan0\niface wlan0 inet dhcp\n\twpa-ssid \"{}\"\n\twpa-psk \"{}\"".format(ssid, password)
    print(text)

    with open('/etc/network/interfaces', 'w') as f:
        f.write(text)

    os.system("sudo ifdown wlan0")
    os.system("sudo ifup wlan0")

def startHotspot():
    os.system("sudo service hostapd start")

def stopHotspot():
    os.system("sudo service hostapd stop")
