#!/usr/bin/python

import serial
import MySQLdb
import time
from time import sleep

while True:
        db = MySQLdb.connect(host="localhost",
                     user="root",
                     passwd="projetfaso",
                     db="Donnees")

        cur = db.cursor()


        port = serial.Serial("/dev/ttyACM0", baudrate = 9600,timeout=None)
        port.flushInput()

        tempVal = 0;
        phVal = 0;

        vals = []

        while (port.inWaiting()==0): 
                port.write("*")
                time.sleep(1)

        vals = (port.readline()).split(',')
        print vals
        tempVal = vals[0]
        phVal    =  vals[1]
        cur.execute("insert into donnees(Temperature,PH) values(" + tempVal + "," + phVal + ")" ) 
        db.commit()

        cur.execute("SELECT * from donnees")


        db.close()
        sleep(10)
