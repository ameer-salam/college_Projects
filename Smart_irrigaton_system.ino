/*
This program was written on 1st June, 2023
Author - Ameer Salam
Program Description - This program takes Analog value of Soil moisture level and accordingly controls motor to pump the water to the pot
Functionality -
The Program takes in Analog values form the Soil Moisture sensor connected to ANalog pin 0
The Pin number 2 is connected to Relay module which controls the motor pump
The value varies from 1000 to 200
  * value > 700-                 Moisture is Low
  * value < 700 && value > 500-  Moisture is Mid 
  * value < 500 && value > 300-  Moisture is High

the motor is activated in the if statement where the value ranges from (value < 700 && value > 500) and also in statement (value < 500 && value > 300)
*/
 
void setup() {
  Serial.begin(9600);
  pinMode(2, OUTPUT);
  digitalWrite(2, HIGH);
  delay(3000);
  Serial.println();
  Serial.println("IRRIGATION Start");
  delay(3000);
  Serial.println("SYSTEM IS ON ");
  delay(3000);
}
 
void loop() {
  int value = analogRead(A0);
  Serial.print("The Value obtained from the sensor is : ");
  Serial.println(value);
  if (value > 700) {
    Serial.println("Moisture level:\tLOW");
    digitalWrite(2, HIGH);
    Serial.println("Water Pump is ON ");
    Serial.println("Water level is low\n");
    delay(3000);
  } else if (value > 500 && value < 700) {
    Serial.println("Moisture level:\tMID");
    digitalWrite(2, HIGH);
    Serial.println("Water Pump is ON ");
    Serial.println("Water level is at medium\n");
    delay(3000);
  } else if (value <500 && value >300) {
    Serial.println("Moisture level:\tHIGH");
    digitalWrite(2, LOW);
    Serial.println("Water Pump is OFF ");
    Serial.println("Water level is HIGH\n");
    delay(3000);
  }
}
