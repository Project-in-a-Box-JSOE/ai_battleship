#include <Adafruit_NeoPixel.h>
#ifdef __AVR__
  #include <avr/power.h>
#endif

#define PIN 6

const int lettersPin = A0;     // the number of the pushbutton pin for letters(rows)
const int numbersPin = A1;     // the number of the pushbutton pin for numbers(columns)

// Params for width and height
const uint8_t kMatrixWidth = 10;
const uint8_t kMatrixHeight = 20;

const int BUTTON_A_LOW = 950;
const int BUTTON_A_HIGH = 1024;
const int BUTTON_B_LOW = 850;
const int BUTTON_B_HIGH = 900;
const int BUTTON_C_LOW = 740;
const int BUTTON_C_HIGH = 800;
const int BUTTON_D_LOW = 680;
const int BUTTON_D_HIGH = 705;
const int BUTTON_E_LOW = 598;
const int BUTTON_E_HIGH = 620;
const int BUTTON_F_LOW = 560;
const int BUTTON_F_HIGH = 571;
const int BUTTON_G_LOW = 475;
const int BUTTON_G_HIGH = 500;
const int BUTTON_H_LOW = 290;
const int BUTTON_H_HIGH = 310;
const int BUTTON_I_LOW = 170;
const int BUTTON_I_HIGH = 195;
const int BUTTON_J_LOW = 100;
const int BUTTON_J_HIGH = 115;

const int BUTTON_1_LOW = 950;
const int BUTTON_1_HIGH = 1024;
const int BUTTON_2_LOW = 850;
const int BUTTON_2_HIGH = 900;
const int BUTTON_3_LOW = 740;
const int BUTTON_3_HIGH = 800;
const int BUTTON_4_LOW = 680;
const int BUTTON_4_HIGH = 705;
const int BUTTON_5_LOW = 598;
const int BUTTON_5_HIGH = 620;
const int BUTTON_6_LOW = 560;
const int BUTTON_6_HIGH = 571;
const int BUTTON_7_LOW = 475;
const int BUTTON_7_HIGH = 500;
const int BUTTON_8_LOW = 290;
const int BUTTON_8_HIGH = 310;
const int BUTTON_9_LOW = 170;
const int BUTTON_9_HIGH = 195;
const int BUTTON_10_LOW = 100;
const int BUTTON_10_HIGH = 115;

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

  pinMode(lettersPin, INPUT);
  pinMode(numbersPin, INPUT);

  Serial.begin(9600);
}

void loop() {

  int reading = analogRead(lettersPin);
//  Serial.println(reading);

  //Input for rows (A-J)
  if(reading>BUTTON_A_LOW && reading<BUTTON_A_HIGH){ //if button A
    //strip.setPixelColor( XY(0, 0), strip.Color(127, 127, 0)); //Yellow
    //strip.show();
    Serial.println("A");
    Serial.flush();  
  }
  if(reading>BUTTON_B_LOW && reading<BUTTON_B_HIGH){ //if button B
    //strip.setPixelColor( XY(0, 1), strip.Color(127, 0, 0)); //Red
    //strip.show();
    Serial.println("B");
    Serial.flush();
  }
  if(reading>BUTTON_C_LOW && reading<BUTTON_C_HIGH){ //if button C
    //strip.setPixelColor( XY(0, 2), strip.Color(0, 127, 0)); //Green
    //strip.show();
    Serial.println("C");
    Serial.flush();
  }
  if(reading>BUTTON_D_LOW && reading<BUTTON_D_HIGH){ //if button D
//    strip.setPixelColor( XY(0, 3), strip.Color(127, 127, 127)); //White
//    strip.show();
    Serial.println("D");
    Serial.flush();
  }
  if(reading>BUTTON_E_LOW && reading<BUTTON_E_HIGH){ //if button E
//    strip.setPixelColor( XY(0, 4), strip.Color(127, 127, 0)); //Yellow
//    strip.show();
    Serial.println("E");
    Serial.flush();
  }
  if(reading>BUTTON_F_LOW && reading<BUTTON_F_HIGH){ //if button F
//    strip.setPixelColor( XY(0, 5), strip.Color(127, 0, 0)); //Red
//    strip.show();
    Serial.println("F");
    Serial.flush();
  }
  if(reading>BUTTON_G_LOW && reading<BUTTON_G_HIGH){ //if button G
//    strip.setPixelColor( XY(0, 6), strip.Color(0, 127, 0)); //Green
//    strip.show();
    Serial.println("G");
    Serial.flush();
  }
  if(reading>BUTTON_H_LOW && reading<BUTTON_H_HIGH){ //if button H
//    strip.setPixelColor( XY(0, 7), strip.Color(127, 127, 127)); //White
//    strip.show();
    Serial.println("H");
    Serial.flush();
  }
  if(reading>BUTTON_I_LOW && reading<BUTTON_I_HIGH){ //if button I
//    strip.setPixelColor( XY(0, 8), strip.Color(127, 127, 0)); //Yellow
//    strip.show();
    Serial.println("I");
    Serial.flush();
  }
  if(reading>BUTTON_J_LOW && reading<BUTTON_J_HIGH){ //if button J
//    strip.setPixelColor( XY(0, 9), strip.Color(127, 0, 0)); //Red
//    strip.show();
    Serial.println("J");
    Serial.flush();
  }

  int reading2 = analogRead(numbersPin);
//  Serial.println(reading2);
  
  //Input for columns (1-10 or 0-9)
  if(reading2>BUTTON_1_LOW && reading2<BUTTON_1_HIGH){ //if button 1
    //strip.setPixelColor( XY(0, 0), strip.Color(127, 127, 0)); //Yellow
    //strip.show();
    Serial.println("0");
    Serial.flush();   
  }
  if(reading2>BUTTON_2_LOW && reading2<BUTTON_2_HIGH){ //if button 2
    //strip.setPixelColor( XY(0, 1), strip.Color(127, 0, 0)); //Red
    //strip.show();
    Serial.println("1");
    Serial.flush();
  }
  if(reading2>BUTTON_3_LOW && reading2<BUTTON_3_HIGH){ //if button 3
    //strip.setPixelColor( XY(0, 2), strip.Color(0, 127, 0)); //Green
    //strip.show();
    Serial.println("2");
    Serial.flush();
  }
  if(reading2>BUTTON_4_LOW && reading2<BUTTON_4_HIGH){ //if button 4
//    strip.setPixelColor( XY(0, 3), strip.Color(127, 127, 127)); //White
//    strip.show();
    Serial.println("3");
    Serial.flush();
  }
  if(reading2>BUTTON_5_LOW && reading2<BUTTON_5_HIGH){ //if button 5
//    strip.setPixelColor( XY(0, 4), strip.Color(127, 127, 0)); //Yellow
//    strip.show();
    Serial.println("4");
    Serial.flush();
  }
  if(reading2>BUTTON_6_LOW && reading2<BUTTON_6_HIGH){ //if button 6
//    strip.setPixelColor( XY(0, 5), strip.Color(127, 0, 0)); //Red
//    strip.show();
    Serial.println("5");
    Serial.flush();
  }
  if(reading2>BUTTON_7_LOW && reading2<BUTTON_7_HIGH){ //if button 7
//    strip.setPixelColor( XY(0, 6), strip.Color(0, 127, 0)); //Green
//    strip.show();
    Serial.println("6");
    Serial.flush();
  }
  if(reading2>BUTTON_8_LOW && reading2<BUTTON_8_HIGH){ //if button 8
//    strip.setPixelColor( XY(0, 7), strip.Color(127, 127, 127)); //White
//    strip.show();
    Serial.println("7");
    Serial.flush();
  }
  if(reading2>BUTTON_9_LOW && reading2<BUTTON_9_HIGH){ //if button 9
//    strip.setPixelColor( XY(0, 8), strip.Color(127, 127, 0)); //Yellow
//    strip.show();
    Serial.println("8");
    Serial.flush();
  }
  if(reading2>BUTTON_10_LOW && reading2<BUTTON_10_HIGH){ //if button 10
//    strip.setPixelColor( XY(0, 9), strip.Color(127, 0, 0)); //Red
//    strip.show();
    Serial.println("9");
    Serial.flush();
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
      strip.setPixelColor( XY(x, y), strip.Color(0, 0, 0)); //off
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

