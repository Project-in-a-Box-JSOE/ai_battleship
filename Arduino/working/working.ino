#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
  #include <avr/power.h>
#endif

#define PIN 6

const int buttonPin = A0;     // the number of the pushbutton pin

// Params for width and height
const uint8_t kMatrixWidth = 10;
const uint8_t kMatrixHeight = 20;

const int BUTTON1 = 1;
const int BUTTON2 = 2;
const int BUTTON3 = 3;
const int BUTTON4 = 4;
const int BUTTON5 = 5;
const int BUTTON6 = 6;
const int BUTTON7 = 7;
const int BUTTON8 = 8;
const int BUTTON9 = 9;
const int BUTTON10 = 10;

//const int BUTTON1LOW = 960;
//const int BUTTON1HIGH = 1024;
//const int BUTTON2LOW = 900;
//const int BUTTON2HIGH = 950;
//const int BUTTON3LOW = 760;
//const int BUTTON3HIGH = 820;
//const int BUTTON4LOW = 683;
//const int BUTTON4HIGH = 740;
//const int BUTTON5LOW = 628;
//const int BUTTON5HIGH = 680;
//const int BUTTON6LOW = 574;
//const int BUTTON6HIGH = 627;
//const int BUTTON7LOW = 490;
//const int BUTTON7HIGH = 570;
//const int BUTTON8LOW = 315;
//const int BUTTON8HIGH = 400;
//const int BUTTON9LOW = 150;
//const int BUTTON9HIGH = 250;
//const int BUTTON10LOW = 60;
//const int BUTTON10HIGH = 130;

const int BUTTON1LOW = 950;
const int BUTTON1HIGH = 1024;
const int BUTTON2LOW = 850;
const int BUTTON2HIGH = 900;
const int BUTTON3LOW = 740;
const int BUTTON3HIGH = 800;
const int BUTTON4LOW = 680;
const int BUTTON4HIGH = 705;
const int BUTTON5LOW = 598;
const int BUTTON5HIGH = 620;
const int BUTTON6LOW = 544;
const int BUTTON6HIGH = 617;
const int BUTTON7LOW = 506;
const int BUTTON7HIGH = 520;
const int BUTTON8LOW = 290;
const int BUTTON8HIGH = 310;
const int BUTTON9LOW = 170;
const int BUTTON9HIGH = 195;
const int BUTTON10LOW = 83;
const int BUTTON10HIGH = 130;

#define NUM_LEDS (kMatrixWidth * kMatrixHeight)

Adafruit_NeoPixel strip = Adafruit_NeoPixel(NUM_LEDS, PIN, NEO_GRB + NEO_KHZ800);

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

  pinMode(buttonPin, INPUT);

  Serial.begin(9600);
}

void loop() {

  int reading = analogRead(buttonPin);
  Serial.println(reading);
  if(reading>BUTTON1LOW && reading<BUTTON1HIGH){
      strip.setPixelColor( XY(0, 0), strip.Color(127, 127, 0)); //Yellow
      strip.show();
   }
   if(reading>BUTTON2LOW && reading<BUTTON2HIGH){
      strip.setPixelColor( XY(0, 1), strip.Color(127, 0, 0)); //Red
      strip.show();
   }
   if(reading>BUTTON3LOW && reading<BUTTON3HIGH){
      strip.setPixelColor( XY(0, 2), strip.Color(0, 127, 0)); //Green
      strip.show();
   }
   if(reading>BUTTON4LOW && reading<BUTTON4HIGH){
      strip.setPixelColor( XY(0, 3), strip.Color(127, 127, 127)); //White
      strip.show();
   }
     if(reading>BUTTON5LOW && reading<BUTTON5HIGH){
      strip.setPixelColor( XY(0, 4), strip.Color(127, 127, 0)); //Yellow
      strip.show();
   }
   if(reading>BUTTON6LOW && reading<BUTTON6HIGH){
      strip.setPixelColor( XY(0, 5), strip.Color(127, 0, 0)); //Red
      strip.show();
   }
   if(reading>BUTTON7LOW && reading<BUTTON7HIGH){
      strip.setPixelColor( XY(0, 6), strip.Color(0, 127, 0)); //Green
      strip.show();
   }
   if(reading>BUTTON8LOW && reading<BUTTON8HIGH){
      strip.setPixelColor( XY(0, 7), strip.Color(127, 127, 127)); //White
      strip.show();
   }
   if(reading>BUTTON9LOW && reading<BUTTON9HIGH){
      strip.setPixelColor( XY(0, 8), strip.Color(127, 127, 0)); //Yellow
      strip.show();
   }
   if(reading>BUTTON10LOW && reading<BUTTON10HIGH){
      strip.setPixelColor( XY(0, 9), strip.Color(127, 0, 0)); //Red
      strip.show();
   }

  if (Serial.available() >= 4) { //4 bytes of info x/y/board/hms
      
      //Serial.println(Serial.available());
      int x = Serial.read();
      x = x - 48;
      int y = Serial.read();
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

