 // Include the Wire library for I2C
#include <Wire.h>
#include <Servo.h>

Servo servo;
Servo servo2;


void setup() {
  // Join I2C bus as slave with address 8
  Wire.begin(0x8);
  
  // Call receiveEvent when data received                
  Wire.onReceive(receiveEvent);
  
  Serial.begin(9600);
  servo.attach(8);
  servo.write(0);
  servo2.attach(9);
  servo2.write(0);
  delay(2000);
}
 
// Function that executes whenever data is received from master
void receiveEvent(int howMany) {
  while (Wire.available()) { // loop through all but the last
    char c = Wire.read(); // receive byte as a character
    if (c == 0) {
      Serial.print("nsw\n");
      servo.write(90);
      delay(3000);
    }
    else if (c == 1) {
      Serial.print("vic\n");
      servo.write(0);
      delay(3000);
    }
  }
}
void loop() {
  delay(100);
  servo2.write(360);

}
