/*
  Blink

  Turns an LED on for one second, then off for one second, repeatedly.

  Most Arduinos have an on-board LED you can control. On the UNO, MEGA and ZERO
  it is attached to digital pin 13, on MKR1000 on pin 6. LED_BUILTIN is set to
  the correct LED pin independent of which board is used.
  If you want to know what pin the on-board LED is connected to on your Arduino
  model, check the Technical Specs of your board at:
  https://www.arduino.cc/en/Main/Products

  modified 8 May 2014
  by Scott Fitzgerald
  modified 2 Sep 2016
  by Arturo Guadalupi
  modified 8 Sep 2016
  by Colby Newman

  This example code is in the public domain.

  http://www.arduino.cc/en/Tutorial/Blink
*/

#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
  #include <avr/power.h>
#endif

#define PIN 3

Adafruit_NeoPixel strip = Adafruit_NeoPixel(200, PIN, NEO_GRB + NEO_KHZ800);

int counter = 0;
int hasRead = false;
String aThing = "";

// the setup function runs once when you press reset or power the board
void setup() {
  // initialize digital pin LED_BUILTIN as an output.
  pinMode(LED_BUILTIN, OUTPUT);

  #if defined (__AVR_ATtiny85__)
    if (F_CPU == 16000000) clock_prescale_set(clock_div_1);
  #endif

  Serial.begin(9600);
  while(!Serial){};
  Serial.println("hello");
  
  strip.begin();
  int i = 0;
  while (i < 200) {
    strip.setPixelColor(i, strip.Color(0, 0, 127)); //Blue
    //leds[i]  = CRGB::Blue;
    i = i+1;
  }
  
}

// the loop function runs over and over again forever
void loop() {
  if (!hasRead) {
    strip.setPixelColor(1, strip.Color(127, 0, 0)); //Red
    strip.show();
    digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
    delay(500);                       // wait for a second
    digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
  //  delay(1000);                       // wait for a second
    Serial.print("Iteration: ");
    Serial.println(counter++);
  }

  if (Serial.available() == 5) {
    aThing = Serial.readString();
    aThing.trim();
    if (aThing.equals("billy"))
      Serial.print("BILLLLLLYYYYYY!!!!!!");
    Serial.print("You wrote: ");
    Serial.println(aThing);
    hasRead = true;
    strip.setPixelColor(3, strip.Color(127, 0, 0)); //Red
    strip.show();
  }
    
}
