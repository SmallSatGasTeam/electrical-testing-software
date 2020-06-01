#include <Wire.h>
#define SLAVE_ADDRESS 0x08

void receiveData(int byteCount){
  while(1 < Wire.available()) {
    char c = Wire.read();
    //Serial.print(c);
  }
  int x = Wire.read();
  Serial.println(x);
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600);
  Wire.begin(SLAVE_ADDRESS);
  //Wire.onReceive(receiveData);
  Serial.println("I2C Ready.");
}

void loop() {
  // put your main code here, to run repeatedly:
  delay(100);
}
