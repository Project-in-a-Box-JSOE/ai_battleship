#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
  #include <avr/power.h>
#endif

#define PIN 6

// Params for width and height
const uint8_t kMatrixWidth = 10;
const uint8_t kMatrixHeight = 20;

#define NUM_LEDS (kMatrixWidth * kMatrixHeight)

// Parameter 1 = number of pixels in strip
// Parameter 2 = Arduino pin number (most are valid)
// Parameter 3 = pixel type flags, add together as needed:
//   NEO_KHZ800  800 KHz bitstream (most NeoPixel products w/WS2812 LEDs)
//   NEO_KHZ400  400 KHz (classic 'v1' (not v2) FLORA pixels, WS2811 drivers)
//   NEO_GRB     Pixels are wired for GRB bitstream (most NeoPixel products)
//   NEO_RGB     Pixels are wired for RGB bitstream (v1 FLORA pixels, not v2)
//   NEO_RGBW    Pixels are wired for RGBW bitstream (NeoPixel RGBW products)
Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUM_LEDS, PIN, NEO_GRB + NEO_KHZ800);

String theInfo = "";
int x = 0;
int y = 0;

// IMPORTANT: To reduce NeoPixel burnout risk, add 1000 uF capacitor across
// pixel power leads, add 300 - 500 Ohm resistor on first pixel's data input
// and minimize distance between Arduino and first pixel.  Avoid connecting
// on a live circuit...if you must, connect GND first.

int16_t XY( uint8_t x, uint8_t y) {
  uint16_t i;
  i = (x * kMatrixWidth) + y;
  return i;
}

void setup() {
  strip.begin();
  int i = 0;
  while (i < 200) {
    strip.setPixelColor(i, strip.Color(0, 0, 127)); //Blue
    //leds[i]  = CRGB::Blue;
    i = i+1;
  }
  strip.show(); // Initialize all pixels to 'off'

  Serial.begin(9600);
}

void loop() {
  //strip.setPixelColor( XY(0,0), strip.Color(127, 0, 0)); //Red
  //strip.show();

  if (Serial.available() >= 4) { //4 bytes of info x/y/board/hms
//    theInfo = Serial.readString();
//    theInfo.trim();
//
//    x = theInfo[0] - 48; //to get correct int number (ascii)
//    y = theInfo[1] - 48;
//    int board = theInfo[2] - 48;
//    char hms = theInfo[3];

      Serial.println(Serial.available());

      x = Serial.read();
      x = x - 48;
      y = Serial.read();
      y = y - 48;
      int board = Serial.read();
      board = board - 48;
      char hms = Serial.read();
  
    if (board == 1) { //human side
      x = x + 10;
    }

    if (hms == 'h') { //if hit
      strip.setPixelColor( XY(x, y), strip.Color(127, 0, 0)); //Red
    }
    else if (hms == 'm') { //if miss
      strip.setPixelColor( XY(x, y), strip.Color(127, 127, 127)); //White
    }
    else if (hms == 's') { //if ship
      strip.setPixelColor( XY(x, y), strip.Color(127, 127, 0)); //Yellow
    }

    strip.show();
    
//    Serial.print("You wrote: ");
//    Serial.println(theInfo);
//    Serial.println(x);
//    Serial.println(y);
//    Serial.println(board);
//    Serial.println(hms);

  }

}

