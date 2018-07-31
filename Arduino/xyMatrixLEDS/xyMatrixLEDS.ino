#include <FastLED.h>
//#include <Adafruit_NeoPixel.h>

#define LED_PIN 3

#define COLOR_ORDER GRB
#define CHIPSET     WS2812B

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


// Params for width and height
const uint8_t kMatrixWidth = 10;
const uint8_t kMatrixHeight = 10;

int xInt = 0;
int yInt = 0;
CRGB color = off;

#define NUM_LEDS (kMatrixWidth * kMatrixHeight)
CRGB leds_plus_safety_pixel[ NUM_LEDS + 1];
CRGB* leds( leds_plus_safety_pixel + 1);

//Adafruit_NeoPixel strip = Adafruit_NeoPixel(60, LED_PIN, NEO_GRB + NEO_KHZ800);


union {
  byte data_len[4];
  int data_len_int;
} read_data;

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
  //pinMode(LED_PIN, OUTPUT);
  //digitalWrite (LED_PIN, HIGH);
  Serial.print("ready!");

  int i = 0;
  while (i < 100) {
    leds[i]  = CRGB::Blue;
    i = i+1;
  }


//  strip.begin();
//  strip.show();
  
}

void loop() {
  // put your main code here, to run repeatedly:
  
  //uint32_t ms = millis();
  //byte pixelHue = ((int32_t)cos16( ms * (27/1) ) * (350 / kMatrixWidth))/32763;
  
  leds[ XY(0, 0)]  = CRGB::Yellow;
  FastLED.show();
  //color = orange;

//  if (Serial.available() < 4) {
//    for (i = 0; i < 4; i++) {
//      read_data.data_len[i] = (byte)Serial.read();
//    }
//  }
//  Serial.write(read_data.data_len_int);

//  int valX = 0;
//  int valY = 0;
//  int hms = 0;

  Serial.write("x");

  if (Serial.available()) {
    char ch = Serial.read();
    //if (ch == '0') {
    leds[ XY(0, 0)] = CRGB::Red;
    FastLED.show();
    //delay(1000);
    //}
  }
  
  //FastLED.show();

    
    //char valX = Serial.read();
    //char valY = Serial.read();
    //char hms = Serial.read();
    //int x = 0;
    //int y = 0;
//    if (valX >= '0' && valX <= '9' ) {
//      x = valX - '0';
//    }
//    if (valY >= '0' && valY <= '9' ) {
//      y = valY - '0';
//    }
//    if (hms == 'h') {
//      color = red;
//    }
//    else if (hms == 'm') {
//      color = white;
//    }
//    else if (hms == 's') {
//      color = yellow;
//    }

    //Serial.write(hms);

    //leds[ XY(x, y)] = color;
    //FastLED.show();
    //delay(100000000);
    

    //leds[ XY(0, 0)] = purple;
    //delay(10000000);
    //FastLED.show();
    //delay(10000000);
  //}


  //leds[ XY(0, 1)] = color;
  //FastLED.show();
   
//  if (Serial.available()) {
////    Serial.print("hi");
//    char x = Serial.read();
//    if (x == 'b') {
////      color = green;
////      yInt = 1;
////    }
////    else if (x == 'b') {
////      color = red;
////      yInt = 2;
////    }
//      color = red;
//    }
//    //char y = Serial.read();
//    //char hms = Serial.read(); // hit/miss/ship
//    //if (x == 'z') {
//      //color = red;
//    //}
//    //if (y == '1') {
//      //color = orange;
//    //}
//    //if (hms == 'l') {
//      //color = green;
//    //}
//    //x = Serial.parseInt();
//    //Serial.print(x);
//    //color = green;
//  }
}
