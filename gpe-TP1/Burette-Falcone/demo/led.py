#!/usr/bin/env python3

from grovepi import *
import time
import subprocess
import os

def init(pin):
	pinMode(pin,"OUTPUT")

def turnOn(pin):
	digitalWrite(pin,1)

def turnOff(pin):
	digitalWrite(pin,0)
