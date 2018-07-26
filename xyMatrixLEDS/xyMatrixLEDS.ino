#include <FastLED.h>

#define LED_PIN 3
#define COLOR_ORDER GRB
#define CHIPSET     WS2811
#define BRIGHTNESS 64

const CRGB red = CRGB( 255, 0, 0);
const CRGB orange = CRGB( 255, 128, 0);
const CRGB yellow = CRGB( 255, 255, 0);
const CRGB green = CRGB( 0, 255, 0);
const CRGB blue = CRGB( 0, 26, 255);
const CRGB purple = CRGB( 102, 0, 204);
const CRGB pink = CRGB( 255, 0, 255);;
const CRGB white = CRGB( 255, 255, 255);
const CRGB off = CRGB( 0, 0, 0);

int xInt = 0;
int yInt = 0;
CRGB color = off;

// Params for width and height
const uint8_t kMatrixWidth = 10;
const uint8_t kMatrixHeight = 10;

#define NUM_LEDS (kMatrixWidth * kMatrixHeight)
CRGB leds_plus_safety_pixel[ NUM_LEDS + 1];
CRGB* leds( leds_plus_safety_pixel + 1);

int16_t XY( uint8_t x, uint8_t y)
{
  uint16_t i;
  
  i = (x * kMatrixWidth) + y;
  
  return i;
}

void setup() {
  // put your setup code here, to run once:
  FastLED.addLeds<CHIPSET, LED_PIN, COLOR_ORDER>(leds, NUM_LEDS).setCorrection(TypicalSMD5050);
  FastLED.setBrightness( BRIGHTNESS );
  Serial.begin(9600);
  pinMode(LED_PIN, OUTPUT);
  digitalWrite (LED_PIN, HIGH);
  Serial.print("ready!");
//  for (int i = 0; i < 10; i++) {
//    for (int j = 0; i < 10; j++) {
//        leds[ XY(i, j)]  = blue; //blue for the ocean
//        //FastLED.show();
//    }
//  }
//  FastLED.show();
}

void loop() {
  // put your main code here, to run repeatedly:
  
  //uint32_t ms = millis();
  //byte pixelHue = ((int32_t)cos16( ms * (27/1) ) * (350 / kMatrixWidth))/32763;

  for (int i = 0; i < 10; i++) {
    for (int j = 0; i < 10; j++) {
        leds[ XY(i, j)]  = blue; //blue for the ocean
        FastLED.show();
    }
  }
  //FastLED.show();

  
  //leds[ XY(0, 0)]  = red;
  //FastLED.show();
  //delay(100000);
  //leds[ XY(0, 1)]  = pink;
  Serial.println("hello");
  //leds[ XY(0, 1)]  = blue;
  //FastLED.show();

  
  //leds[ XY(0, 0)]  = orange;
  //int incoming[2]; 


  color = orange;
   
  if (Serial.available()) {
//    Serial.print("hi");
    char x = Serial.read();
    if (x == 'a') {
      color = green;
      yInt = 1;
    }
    else if (x == 'b') {
      color = red;
      yInt = 2;
    }
    color = red;
    //char y = Serial.read();
    //char hms = Serial.read(); // hit/miss/ship
    //if (x == 'z') {
      //color = red;
    //}
    //if (y == '1') {
      //color = orange;
    //}
    //if (hms == 'l') {
      //color = green;
    //}
    //x = Serial.parseInt();
    //Serial.print(x);
    //color = green;
  }


  //leds[ XY(0, yInt)]  = yellow;
  //leds[ XY(0, 0)] = red;
  //FastLED.show();
  //delay(10000);
  //delay(100);
}
