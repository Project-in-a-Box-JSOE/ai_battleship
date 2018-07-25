#include <FastLED.h>

#define LED_PIN 3
#define COLOR_ORDER GRB
#define CHIPSET     WS2811
#define BRIGHTNESS 64

// Params for width and height
const uint8_t kMatrixWidth = 10;
const uint8_t kMatrixHeight = 10;

#define NUM_LEDS (kMatrixWidth * kMatrixHeight)
CRGB leds_plus_safety_pixel[ NUM_LEDS + 1];
CRGB* const leds( leds_plus_safety_pixel + 1);

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
}

void loop() {
  // put your main code here, to run repeatedly:
  
  uint32_t ms = millis();
  byte pixelHue = ((int32_t)cos16( ms * (27/1) ) * (350 / kMatrixWidth))/32763;
  CRGB red = CRGB( 255, 0, 0);
  CRGB orange = CRGB( 255, 128, 0);
  CRGB yellow = CRGB( 255, 255, 0);
  CRGB green = CRGB( 0, 255, 0);
  CRGB blue = CRGB( 0, 26, 255);
  CRGB purple = CRGB( 102, 0, 204);
  CRGB pink = CRGB( 255, 0, 255);;
  CRGB white = CRGB( 255, 255, 255);
  CRGB off = CRGB( 0, 0, 0);

  
  //leds[ XY(0, 0)]  = CHSV( yellow, 255, 255);
  //leds[ XY(0, 0)]  = CRGB( 255, 0, 0);
  
  //leds[ XY(0, 0)]  = orange;
  int incoming[2];
  if (Serial.available()) {
    for (int i = 0; i < 2; i++){
      //incoming[i] = Serial.read();
      //Serial.print(incoming[i]);
    }
    int place = Serial.read();
    //place = place - 48;
    
    //Serial.println(incoming);
    leds[ XY(place, place)]  = orange;
  }

  leds[ XY(0, 0)]  = blue;

  FastLED.show();
}
