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
}

void loop() {
  // put your main code here, to run repeatedly:
  uint32_t ms = millis();
  byte pixelHue = ((int32_t)cos16( ms * (27/1) ) * (350 / kMatrixWidth))/32763;
  leds[ XY(0, 0)]  = CHSV( pixelHue, 255, 255);

  FastLED.show();
}
