  #include <Adafruit_NeoPixel.h>
  #include<LiquidCrystal.h>

  LiquidCrystal lcd(7, 6, 5, 4, 3, 2);

  // ====== Buzzer for Sound Effects ======
  // Variables for controlling buzzer timing
  unsigned long previousToneMillis = 0;  // Timer to avoid blocking delays for tone.
  unsigned long previousPauseMillis = 0; // Timer to avoid blocking delays for pause.
  bool isTonePlaying = false;            // Flag to indicate if tone is playing.
  bool isPauseActive = false;            // Flag to indicate if pause is active.


  #define PINBUZZ A1	 // input pin Buzz is attached to

  #define PIN A0	 // input pin Neopixel is attached to

  #define NUMPIXELS     4  // number of neopixels in Ring


  Adafruit_NeoPixel pixels = Adafruit_NeoPixel(NUMPIXELS, PIN, NEO_GRB + NEO_KHZ800);

  int delayval = 100; // timing delay
  int redColor = 0;
  int greenColor = 0;
  int blueColor = 0;

  void setup() {
    pixels.begin(); // Initializes the NeoPixel library.
    lcd.begin(16, 2);
  Serial.begin(9600);
    
    // BOT started !!!! NOW READY TO BALANCE 
    tone(PINBUZZ, 300);   // BEEP AGAIN FOR SUCCESS 
    delay(100);
    noTone(PINBUZZ);
    delay(100);
    tone(PINBUZZ, 300);
    delay(100);
    noTone(PINBUZZ);
    delay(100);
  }

  void loop() {
    showled();
    lcd.setCursor(0,0);          
    lcd.print("   Subscribe!"); 
    lcd.setCursor(2,1);           
    lcd.print("RaspberryUser"); 
  }

  // setColor()
  // picks random values to set for RGB
  void showled(){
  setColor();
  

    for(int i=0;i<NUMPIXELS;i++){

      // pixels.Color takes RGB values, from 0,0,0 up to 255,255,255
      pixels.setPixelColor(i, pixels.Color(redColor, greenColor, blueColor)); // Moderately bright green color.

      pixels.show(); // This sends the updated pixel color to the hardware.
    beep();
      delay(delayval); // Delay for a period of time (in milliseconds).
      
      // Serial.println(i);
      
      if (i == NUMPIXELS){
        i = 0; // start all over again!
          setColor();
      }

    }
  }
  void setColor(){
    redColor =255;
    greenColor = 0;
    blueColor = 0;
    Serial.print("red: ");
    Serial.println(redColor);
    Serial.print("green: ");
    Serial.println(greenColor);
    Serial.print("blue: ");
    Serial.println(blueColor);
    
  }


  void beep(){
    Serial.println("sd");
    unsigned long currentMillis = millis();
    if (true ){
      // Tone ON for 100 ms
      if (!isTonePlaying && !isPauseActive && currentMillis - previousToneMillis >= 300) {
        tone(PINBUZZ, 800);
        isTonePlaying = true;
        previousToneMillis = currentMillis;
      }
      // Tone OFF after 100 ms
      if (isTonePlaying && currentMillis - previousToneMillis >= 100) {
        noTone(PINBUZZ);
        isTonePlaying = false;
        isPauseActive = true;
        previousPauseMillis = currentMillis;
      }

      // Pause for 300 ms after the tone
      if (isPauseActive && currentMillis - previousPauseMillis >= 300) {
        isPauseActive = false;  // Reset for the next tone
      }
  }
    else noTone(PINBUZZ);
  }