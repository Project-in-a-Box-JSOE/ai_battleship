#include <Adafruit_NeoPixel.h>
#include <FastLED.h>
#ifdef __AVR__
  #include <avr/power.h>
#endif

#define PIN 3

// Params for width and height
const uint8_t kMatrixWidth = 10;
const uint8_t kMatrixHeight = 10;

#define NUM_LEDS (kMatrixWidth * kMatrixHeight)

Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUM_LEDS, PIN, NEO_GRB + NEO_KHZ800);

int counter = 0;
int hasRead = false;
String aThing = "";
int x = 0;
int y = 0;


int16_t XY( uint8_t x, uint8_t y)
{
  uint16_t i;
  
  i = (x * 10) + y;
  
  return i;
}


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
    strip.setPixelColor(1, CRGB::Green); //Red
    strip.show();
    digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
    delay(500);                       // wait for a second
    digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
  //  delay(1000);                       // wait for a second
    Serial.print("Iteration: ");
    Serial.println(counter++);
  }

  if (Serial.available() == 2) {
    aThing = Serial.readString();
    aThing.trim();
    int x = aThing[0] - 48;
    int y = aThing[1] - 48;
//    if (aThing.equals("billy"))
//      Serial.print("BILLLLLLYYYYYY!!!!!!");
    Serial.print("You wrote: ");
    Serial.println(aThing);
    Serial.println(x);
    Serial.println(y);
    hasRead = true;
    strip.setPixelColor( XY(x, y), CRGB::Red); //Red
    strip.show();
  }
    
}
