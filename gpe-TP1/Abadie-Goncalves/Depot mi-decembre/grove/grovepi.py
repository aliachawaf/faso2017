#!/usr/bin/env python

import sys
import time
import math
import struct
import numpy

debug = 0

if sys.version_info<(3,0):
	p_version=2
else:
	p_version=3

if sys.platform == 'uwp':
	import winrt_smbus as smbus
	bus = smbus.SMBus(1)
else:
	import smbus
	import RPi.GPIO as GPIO
	rev = GPIO.RPI_REVISION
	if rev == 2 or rev == 3:
		bus = smbus.SMBus(1)
	else:
		bus = smbus.SMBus(0)

# I2C Address of Arduino
address = 0x04

# Command Format
# digitalRead() command format header
dRead_cmd = [1]
# digitalWrite() command format header
dWrite_cmd = [2]
# analogRead() command format header
aRead_cmd = [3]
# analogWrite() command format header
aWrite_cmd = [4]
# pinMode() command format header
pMode_cmd = [5]

# This allows us to be more specific about which commands contain unused bytes
unused = 0
retries = 10
# Function declarations of the various functions used for encoding and sending
# data from RPi to Arduino

# Write I2C block
def write_i2c_block(address, block):
	for i in range(retries):
		try:
			return bus.write_i2c_block_data(address, 1, block)
		except IOError:
			if debug:
				print ("IOError")
	return -1

# Read I2C byte
def read_i2c_byte(address):
	for i in range(retries):
		try:
			return bus.read_byte(address)
		except IOError:
			if debug:
				print ("IOError")
	return -1

# Read I2C block
def read_i2c_block(address):
	for i in range(retries):
		try:
			return bus.read_i2c_block_data(address, 1)
		except IOError:
			if debug:
				print ("IOError")
	return -1


# Arduino Digital Read
def digitalRead(pin):
        donnee = dRead_cmd+[pin,unused,unused]
        write_i2c_block(address,donnee)
        return read_i2c_byte(address)

# Arduino Digital Write
def digitalWrite(pin, value):
        donnee = dWrite_cmd+[pin,value,unused]
        write_i2c_block(address,donnee)


# Setting Up Pin mode on Arduino
def pinMode(pin, mode):
        donnee = pMode_cmd+[pin]
        if mode == "INPUT":
                donnee = donnee+[0]
        elif mode == "OUTPUT":
                donnee = donnee+[1]
        donnee=donnee+[unused]
        write_i2c_block(address,donnee)


# Read analog value from Pin
def analogRead(pin):
        donnee = aRead_cmd+[pin,unused,unused]
        time.sleep(0.05)
        read_i2c_byte(address)
        b=read_i2c_block(address)
        return b[1]*256+b[2]

# Write PWM
def analogWrite(pin, value):
        donnee = aWrite_cmd+[pin,value,unused]
        write_i2c_block(address,donnee)
