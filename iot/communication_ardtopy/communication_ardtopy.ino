#include <SoftwareSerial.h>

// Pin Definitions
const int frontLeftDoorPin = 13;
const int frontRightDoorPin = 12;
const int backLeftDoorPin = 11;
const int backRightDoorPin = 10;
const int frontBonnetPin = 9;
const int backTrunkPin = 8;

// Temperature sensor pin (LM35) - Now at A5
const int tempPin = A5;  

// Gas sensor pin (analog input)
const int gasPin = A4;  // Gas sensor connected to A4 pin

// PIR sensor pin
const int pirPin = 7;   // PIR sensor to detect motion

// Debounce-related variables
unsigned long debounceDelay = 50;  // 50ms debounce delay
unsigned long lastDebounceTime[6]; // Store debounce time for 6 switches
int lastButtonState[6] = {HIGH, HIGH, HIGH, HIGH, HIGH, HIGH};  // Last state of switches
int buttonState[6] = {HIGH, HIGH, HIGH, HIGH, HIGH, HIGH};      // Current state of switches

void setup() {
  // Initialize serial communication
  Serial.begin(9600);    // Serial to PC
  
  // Initialize limit switch pins as inputs with internal pull-ups
  pinMode(frontLeftDoorPin, INPUT_PULLUP);
  pinMode(frontRightDoorPin, INPUT_PULLUP);
  pinMode(backLeftDoorPin, INPUT_PULLUP);
  pinMode(backRightDoorPin, INPUT_PULLUP);
  pinMode(frontBonnetPin, INPUT_PULLUP);
  pinMode(backTrunkPin, INPUT_PULLUP);
  
  // Initialize sensor pins
  pinMode(tempPin, INPUT);  // Temperature sensor pin
  pinMode(gasPin, INPUT);   // Gas sensor pin
  pinMode(pirPin, INPUT);   // PIR sensor pin
}

void loop() {
  // Read the temperature sensor (LM35 at A5)
  int tempValue = analogRead(tempPin);
  float temperatureC = (tempValue * 5.0 * 100.0) / 1024.0; // LM35 in Celsius
  
  // Read the gas sensor (analog reading from A4)
  int gasValue = analogRead( gasPin);
  bool gasDetected = (gasValue > 100);  // Threshold for detecting harmful gas, adjust as needed
  
  // Read the PIR sensor (detect motion)
  bool motionDetected = digitalRead(pirPin); // HIGH means motion detected

  // Limit switch reading with debounce logic
  unsigned long currentMillis = millis();
  
  // Read each limit switch and debounce
  buttonState[0] = digitalRead(frontLeftDoorPin);
  if (buttonState[0] != lastButtonState[0] && (currentMillis - lastDebounceTime[0]) > debounceDelay) {
    lastDebounceTime[0] = currentMillis;
    lastButtonState[0] = buttonState[0];
  }
  
  buttonState[1] = digitalRead(frontRightDoorPin);
  if (buttonState[1] != lastButtonState[1] && (currentMillis - lastDebounceTime[1]) > debounceDelay) {
    lastDebounceTime[1] = currentMillis;
    lastButtonState[1] = buttonState[1];
  }
  
  buttonState[2] = digitalRead(backLeftDoorPin);
  if (buttonState[2] != lastButtonState[2] && (currentMillis - lastDebounceTime[2]) > debounceDelay) {
    lastDebounceTime[2] = currentMillis;
    lastButtonState[2] = buttonState[2];
  }
  
  buttonState[3] = digitalRead(backRightDoorPin);
  if (buttonState[3] != lastButtonState[3] && (currentMillis - lastDebounceTime[3]) > debounceDelay) {
    lastDebounceTime[3] = currentMillis;
    lastButtonState[3] = buttonState[3];
  }
  
  buttonState[4] = digitalRead(frontBonnetPin);
  if (buttonState[4] != lastButtonState[4] && (currentMillis - lastDebounceTime[4]) > debounceDelay) {
    lastDebounceTime[4] = currentMillis;
    lastButtonState[4] = buttonState[4];
  }
  
  buttonState[5] = digitalRead(backTrunkPin);
  if (buttonState[5] != lastButtonState[5] && (currentMillis - lastDebounceTime[5]) > debounceDelay) {
    lastDebounceTime[5] = currentMillis;
    lastButtonState[5] = buttonState[5];
  }

  // Wait for a request from Python
  if (Serial.available() > 0) {
    char request = Serial.read();  // Read the incoming request

    if (request == 'R') {  // If 'R' is received, send status of all data
      // Read limit switch states (debounced)
      int frontLeftDoor = !buttonState[0];
      int frontRightDoor = !buttonState[1];
      int backLeftDoor = !buttonState[2];
      int backRightDoor = !buttonState[3];
      int frontBonnet = !buttonState[4];
      int backBonnet = !buttonState[5];
      
      // Send the states back to Python (limit switches, temp, gas, motion)
      Serial.print(frontLeftDoor);
      Serial.print(",");
      Serial.print(frontRightDoor);
      Serial.print(",");
      Serial.print(backLeftDoor);
      Serial.print(",");
      Serial.print(backRightDoor);
      Serial.print(",");
      Serial.print(frontBonnet);
      Serial.print(",");
      Serial.print(backBonnet);
      Serial.print(",");
      Serial.print(temperatureC);  // Send temperature
      Serial.print(",");
      Serial.print(gasDetected);  // Send gas detection status (true/false)
      Serial.print(",");
      Serial.println(motionDetected);  // Send PIR motion detection status (true/false)
      
      // If gas is detected, send a warning
      if (gasDetected) {
        Serial.println("WARNING: Harmful gas detected! Please check.");
      }
      
      // If motion is detected, send an alert
      if (motionDetected) {
        Serial.println("ALERT: Motion detected near the car.");
      }
    }
    else if (request == 'O') {  // If 'O' is received, perform some operation based on Python's command
      // Perform a sample operation like turning on/off an LED (example: you could control other actuators based on Python's command)
      digitalWrite(LED_BUILTIN, HIGH);  // Turn on the onboard LED (just an example)
      delay(1000);                      // Keep it on for 1 second
      digitalWrite(LED_BUILTIN, LOW);   // Turn off the LED
      Serial.println("Commmand received ");
    }
  }
}
