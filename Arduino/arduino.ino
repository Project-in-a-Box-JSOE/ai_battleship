#include <Adafruit_NeoPixel.h>
#include <FastLED.h>
#ifdef __AVR__
  #include <avr/power.h>
#endif

#define PIN 3

// Params for width and height
const uint8_t kMatrixWidth = 10;
const uint8_t kMatrixHeight = 20;

#define NUM_LEDS (kMatrixWidth * kMatrixHeight)

Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUM_LEDS, PIN, NEO_GRB + NEO_KHZ800);

int counter = 0;
//int hasRead = false;
String theInfo = "";
int x = 0;
int y = 0;


int16_t XY( uint8_t x, uint8_t y)
{
  uint16_t i;
  
  i = (x * kMatrixWidth) + y;
  
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
  //if (!hasRead) {
    //strip.setPixelColor(1, CRGB::Green); //Red
    //strip.show();
//    digitalWrite(LED_BUILTIN, HIGH);   // turn the LED on (HIGH is the voltage level)
//    delay(500);                       // wait for a second
//    digitalWrite(LED_BUILTIN, LOW);    // turn the LED off by making the voltage LOW
//  //  delay(1000);                       // wait for a second
//    Serial.print("Iteration: ");
//    Serial.println(counter++);
  //}

  if (Serial.available() == 4) { //4 bytes of info x/y/board/hms
    theInfo = Serial.readString();
    theInfo.trim();
    x = theInfo[0] - 48; //to get correct int number (ascii)
    y = theInfo[1] - 48;
    int board = theInfo[2] -48;
    char hms = theInfo[3];
    
    if (board == 1) { //human side
      x = x + 10;
    }

    if (hms == 'h') { //if hit
      strip.setPixelColor( XY(x, y), CRGB::Red); //Red
    }
    if (hms == 'm') { //if miss
      strip.setPixelColor( XY(x, y), CRGB::White); //White
    }
    if (hms == 's') { //if ship
      strip.setPixelColor( XY(x, y), CRGB::Yellow); //Yellow
    }
    
//    if (aThing.equals("billy"))
//      Serial.print("BILLLLLLYYYYYY!!!!!!");
    Serial.print("You wrote: ");
    Serial.println(theInfo);
    Serial.println(x);
    Serial.println(y);
//    hasRead = true;
    //strip.setPixelColor( XY(x, y), CRGB::Red); //Red
    strip.show();
  }
    
}
