#include <SoftwareSerial.h>


// Serial connection to the HC-05, RX on pin 5, TX on pin 6
SoftwareSerial bt (6,5); 


// Run once after bootup
void setup() {
  // Serial comm with the HC-05 module
  bt.begin(9600);

  // Led pin
  pinMode(13, OUTPUT);
}


// Loopy code
void loop() {
  while (bt.available()) {
   char inChar = (char)bt.read();
   if (String(inChar)=="?"){

     // Turn on the led and check the sensors
     digitalWrite(13, HIGH);   delay(500);
     int val0 = analogRead(A0);delay(100);
     int val1 = analogRead(A1);delay(100);
     int val2 = analogRead(A2);delay(100);
     int val3 = analogRead(A3);delay(100);
     int val4 = analogRead(A4);delay(100);
     int val5 = analogRead(A5);delay(100);
     digitalWrite(13, LOW);

     // Concatenate into a nice frame
     String Strval0 = String(val0);
     String Strval1 = String(val1);
     String Strval2 = String(val2);
     String Strval3 = String(val3);
     String Strval4 = String(val4);
     String Strval5 = String(val5);
     char buff[50];
     String vals = Strval0+","+Strval1+","+Strval2+","+Strval3+","+Strval4+","+Strval5+";";
     vals.toCharArray(buff, 50);

     // Send the frame to the bluetooth module
     bt.write(buff);
  }
 }
}