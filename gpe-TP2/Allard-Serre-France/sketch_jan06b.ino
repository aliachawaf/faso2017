#include <Wire.h>
#include "MMA7660.h"
MMA7660 accelemeter;
#define SLAVE_ADDRESS 0x12
int dataReceived = 0;
int8_t x;
int8_t y;
int8_t z;
int8_t envoi = 0;

void setup() {
  Serial.begin(9600);
  accelemeter.init();
  Wire.begin(SLAVE_ADDRESS);
  Wire.onReceive(receiveData);
  Wire.onRequest(sendData);
}

void loop() {
  accelemeter.getXYZ(&x, &y, &z);
  envoi = x+20;
  delay(100);
}

void receiveData(int byteCount) {
  while (Wire.available()) {
    dataReceived = Wire.read();
    Serial.print("Donnee recue : ");
    Serial.println(dataReceived);
  }
}

void sendData() {
  Wire.write(envoi);
}
