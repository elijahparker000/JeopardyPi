#include <Arduino.h>

/**************************************************************************
 This is an example for our Monochrome OLEDs based on SSD1306 drivers

 Pick one up today in the adafruit shop!
 ------> http://www.adafruit.com/category/63_98

 This example is for a 128x32 pixel display using I2C to communicate
 3 pins are required to interface (two I2C and one reset).

 Adafruit invests time and resources providing this open
 source code, please support Adafruit and open-source
 hardware by purchasing products from Adafruit!

 Written by Limor Fried/Ladyada for Adafruit Industries,
 with contributions from the open source community.
 BSD license, check license.txt for more information
 All text above, and the splash screen below must be
 included in any redistribution.
 **************************************************************************/

#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>
#include <nRF24L01.h>
#include <RF24.h>

#define SCREEN_WIDTH 128 // OLED display width, in pixels
#define SCREEN_HEIGHT 32 // OLED display height, in pixels

// Declaration for an SSD1306 display connected to I2C (SDA, SCL pins)
#define OLED_RESET     4 // Reset pin # (or -1 if sharing Arduino reset pin)
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

#define NUMFLAKES     10 // Number of snowflakes in the animation example

#define LOGO_HEIGHT   16
#define LOGO_WIDTH    16
static const unsigned char PROGMEM logo_bmp[] =
{ B00000000, B11000000,
  B00000001, B11000000,
  B00000001, B11000000,
  B00000011, B11100000,
  B11110011, B11100000,
  B11111110, B11111000,
  B01111110, B11111111,
  B00110011, B10011111,
  B00011111, B11111100,
  B00001101, B01110000,
  B00011011, B10100000,
  B00111111, B11100000,
  B00111111, B11110000,
  B01111100, B11110000,
  B01110000, B01110000,
  B00000000, B00110000 };


const int buttonPin = 5;    // The number of the button pin
int buttonState = 0;        // Variable to store the button state
String response = "";

RF24 radio(4, 6); // CE, CSN
const byte address[6] = "00001";


void testdrawline() {
  int16_t i;

  display.clearDisplay(); // Clear display buffer

  for(i=0; i<display.width(); i+=4) {
    display.drawLine(0, 0, i, display.height()-1, SSD1306_WHITE);
    display.display(); // Update screen with each newly-drawn line
    delay(1);
  }
  for(i=0; i<display.height(); i+=4) {
    display.drawLine(0, 0, display.width()-1, i, SSD1306_WHITE);
    display.display();
    delay(1);
  }
  delay(250);

  display.clearDisplay();

  for(i=0; i<display.width(); i+=4) {
    display.drawLine(0, display.height()-1, i, 0, SSD1306_WHITE);
    display.display();
    delay(1);
  }
  for(i=display.height()-1; i>=0; i-=4) {
    display.drawLine(0, display.height()-1, display.width()-1, i, SSD1306_WHITE);
    display.display();
    delay(1);
  }
  delay(250);

  display.clearDisplay();

  for(i=display.width()-1; i>=0; i-=4) {
    display.drawLine(display.width()-1, display.height()-1, i, 0, SSD1306_WHITE);
    display.display();
    delay(1);
  }
  for(i=display.height()-1; i>=0; i-=4) {
    display.drawLine(display.width()-1, display.height()-1, 0, i, SSD1306_WHITE);
    display.display();
    delay(1);
  }
  delay(250);

  display.clearDisplay();

  for(i=0; i<display.height(); i+=4) {
    display.drawLine(display.width()-1, 0, 0, i, SSD1306_WHITE);
    display.display();
    delay(1);
  }
  for(i=0; i<display.width(); i+=4) {
    display.drawLine(display.width()-1, 0, i, display.height()-1, SSD1306_WHITE);
    display.display();
    delay(1);
  }

  delay(2000); // Pause for 2 seconds
}

void testdrawrect(void) {
  display.clearDisplay();

  for(int16_t i=0; i<display.height()/2; i+=2) {
    display.drawRect(i, i, display.width()-2*i, display.height()-2*i, SSD1306_WHITE);
    display.display(); // Update screen with each newly-drawn rectangle
    delay(1);
  }

  delay(2000);
}

void testfillrect(void) {
  display.clearDisplay();

  for(int16_t i=0; i<display.height()/2; i+=3) {
    // The INVERSE color is used so rectangles alternate white/black
    display.fillRect(i, i, display.width()-i*2, display.height()-i*2, SSD1306_INVERSE);
    display.display(); // Update screen with each newly-drawn rectangle
    delay(1);
  }

  delay(2000);
}

void testdrawcircle(void) {
  display.clearDisplay();

  for(int16_t i=0; i<max(display.width(),display.height())/2; i+=2) {
    display.drawCircle(display.width()/2, display.height()/2, i, SSD1306_WHITE);
    display.display();
    delay(1);
  }

  delay(2000);
}

void testfillcircle(void) {
  display.clearDisplay();

  for(int16_t i=max(display.width(),display.height())/2; i>0; i-=3) {
    // The INVERSE color is used so circles alternate white/black
    display.fillCircle(display.width() / 2, display.height() / 2, i, SSD1306_INVERSE);
    display.display(); // Update screen with each newly-drawn circle
    delay(1);
  }

  delay(2000);
}

void testdrawroundrect(void) {
  display.clearDisplay();

  for(int16_t i=0; i<display.height()/2-2; i+=2) {
    display.drawRoundRect(i, i, display.width()-2*i, display.height()-2*i,
      display.height()/4, SSD1306_WHITE);
    display.display();
    delay(1);
  }

  delay(2000);
}

void testfillroundrect(void) {
  display.clearDisplay();

  for(int16_t i=0; i<display.height()/2-2; i+=2) {
    // The INVERSE color is used so round-rects alternate white/black
    display.fillRoundRect(i, i, display.width()-2*i, display.height()-2*i,
      display.height()/4, SSD1306_INVERSE);
    display.display();
    delay(1);
  }

  delay(2000);
}

void testdrawtriangle(void) {
  display.clearDisplay();

  for(int16_t i=0; i<max(display.width(),display.height())/2; i+=5) {
    display.drawTriangle(
      display.width()/2  , display.height()/2-i,
      display.width()/2-i, display.height()/2+i,
      display.width()/2+i, display.height()/2+i, SSD1306_WHITE);
    display.display();
    delay(1);
  }

  delay(2000);
}

void testfilltriangle(void) {
  display.clearDisplay();

  for(int16_t i=max(display.width(),display.height())/2; i>0; i-=5) {
    // The INVERSE color is used so triangles alternate white/black
    display.fillTriangle(
      display.width()/2  , display.height()/2-i,
      display.width()/2-i, display.height()/2+i,
      display.width()/2+i, display.height()/2+i, SSD1306_INVERSE);
    display.display();
    delay(1);
  }

  delay(2000);
}

void testdrawchar(void) {
  display.clearDisplay();

  display.setTextSize(1);      // Normal 1:1 pixel scale
  display.setTextColor(SSD1306_WHITE); // Draw white text
  display.setCursor(0, 0);     // Start at top-left corner
  display.cp437(true);         // Use full 256 char 'Code Page 437' font

  // Not all the characters will fit on the display. This is normal.
  // Library will draw what it can and the rest will be clipped.
  for(int16_t i=0; i<256; i++) {
    if(i == '\n') display.write(' ');
    else          display.write(i);
  }

  display.display();
  delay(2000);
}

void testdrawstyles(void) {
  display.clearDisplay();

  display.setTextSize(1);             // Normal 1:1 pixel scale
  display.setTextColor(SSD1306_WHITE);        // Draw white text
  display.setCursor(0,0);             // Start at top-left corner
  display.println(F("Hello, world!"));

  display.setTextColor(SSD1306_BLACK, SSD1306_WHITE); // Draw 'inverse' text
  display.println(3.141592);

  display.setTextSize(2);             // Draw 2X-scale text
  display.setTextColor(SSD1306_WHITE);
  display.print(F("0x")); display.println(0xDEADBEEF, HEX);

  display.display();
  delay(2000);
}

void testscrolltext(void) {
  display.clearDisplay();

  display.setTextSize(2); // Draw 2X-scale text
  display.setTextColor(SSD1306_WHITE);
  display.setCursor(10, 0);
  display.println(F("scroll"));
  display.display();      // Show initial text
  delay(100);

  // Scroll in various directions, pausing in-between:
  display.startscrollright(0x00, 0x0F);
  delay(2000);
  display.stopscroll();
  delay(1000);
  display.startscrollleft(0x00, 0x0F);
  delay(2000);
  display.stopscroll();
  delay(1000);
  display.startscrolldiagright(0x00, 0x07);
  delay(2000);
  display.startscrolldiagleft(0x00, 0x07);
  delay(2000);
  display.stopscroll();
  delay(1000);
}

void testdrawbitmap(void) {
  display.clearDisplay();

  display.drawBitmap(
    (display.width()  - LOGO_WIDTH ) / 2,
    (display.height() - LOGO_HEIGHT) / 2,
    logo_bmp, LOGO_WIDTH, LOGO_HEIGHT, 1);
  display.display();
  delay(1000);
}

#define XPOS   0 // Indexes into the 'icons' array in function below
#define YPOS   1
#define DELTAY 2

void testanimate(const uint8_t *bitmap, uint8_t w, uint8_t h) {
  int8_t f, icons[NUMFLAKES][3];

  // Initialize 'snowflake' positions
  for(f=0; f< NUMFLAKES; f++) {
    icons[f][XPOS]   = random(1 - LOGO_WIDTH, display.width());
    icons[f][YPOS]   = -LOGO_HEIGHT;
    icons[f][DELTAY] = random(1, 6);
    Serial.print(F("x: "));
    Serial.print(icons[f][XPOS], DEC);
    Serial.print(F(" y: "));
    Serial.print(icons[f][YPOS], DEC);
    Serial.print(F(" dy: "));
    Serial.println(icons[f][DELTAY], DEC);
  }

  for(;;) { // Loop forever...
    display.clearDisplay(); // Clear the display buffer

    // Draw each snowflake:
    for(f=0; f< NUMFLAKES; f++) {
      display.drawBitmap(icons[f][XPOS], icons[f][YPOS], bitmap, w, h, SSD1306_WHITE);
    }

    display.display(); // Show the display buffer on the screen
    delay(200);        // Pause for 1/10 second

    // Then update coordinates of each flake...
    for(f=0; f< NUMFLAKES; f++) {
      icons[f][YPOS] += icons[f][DELTAY];
      // If snowflake is off the bottom of the screen...
      if (icons[f][YPOS] >= display.height()) {
        // Reinitialize to a random position, just off the top
        icons[f][XPOS]   = random(1 - LOGO_WIDTH, display.width());
        icons[f][YPOS]   = -LOGO_HEIGHT;
        icons[f][DELTAY] = random(1, 6);
      }
    }
  }
}

float floatMap(float x, float in_min, float in_max, float out_min, float out_max) {
  return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min;
}

void drawKeyboard(){
  //Draw Keyboard
  display.setTextSize(1);      // Normal 1:1 pixel scale
  display.setTextColor(SSD1306_WHITE); // Draw white text
  display.cp437(true);
  display.setCursor(10, 25); 
  display.write("z");
  display.setCursor(20, 25);
  display.write("x");
  display.setCursor(30, 25);
  display.write("c");
  display.setCursor(40, 25);
  display.write("v");
  display.setCursor(50, 25);
  display.write("b");
  display.setCursor(60, 25);
  display.write("n");
  display.setCursor(70, 25);
  display.write("m");
  display.setCursor(95, 25);
  display.write("space");
  display.setCursor(5, 16);
  display.write("a");
  display.setCursor(15, 16);
  display.write("s");
  display.setCursor(25, 16);
  display.write("d");
  display.setCursor(35, 16);
  display.write("f");
  display.setCursor(45, 16);
  display.write("g");
  display.setCursor(55, 16);
  display.write("h");
  display.setCursor(65, 16);
  display.write("j");
  display.setCursor(75, 16);
  display.write("k");
  display.setCursor(85, 16);
  display.write("l");
  display.setCursor(95, 16);
  display.write("enter");
  display.setCursor(0, 7);
  display.write("q");
  display.setCursor(10, 7);
  display.write("w");
  display.setCursor(20, 7);
  display.write("e");
  display.setCursor(30, 7);
  display.write("r");
  display.setCursor(40, 7);
  display.write("t");
  display.setCursor(50, 7);
  display.write("y");
  display.setCursor(60, 7);
  display.write("u");
  display.setCursor(70, 7);
  display.write("i");
  display.setCursor(80, 7);
  display.write("o");
  display.setCursor(90, 7);
  display.write("p");
  display.setCursor(100, 7);
  display.write("back");
}

void setup() {
  Serial.begin(9600);

  // SSD1306_SWITCHCAPVCC = generate display voltage from 3.3V internally
  if(!display.begin(SSD1306_SWITCHCAPVCC, 0x3C)) { // Address 0x3C for 128x32
    Serial.println(F("SSD1306 allocation failed"));
    for(;;); // Don't proceed, loop forever
  }

  // Show initial display buffer contents on the screen --
  // the library initializes this with an Adafruit splash screen.
  display.display();
  delay(2000); // Pause for 2 seconds

  // Clear the buffer
  display.clearDisplay();
  display.display();

  // Draw a single pixel in white
//   display.drawPixel(10, 10, SSD1306_WHITE);

//   // Show the display buffer on the screen. You MUST call display() after
//   // drawing commands to make them visible on screen!
//   display.display();
//   delay(2000);
//   // display.display() is NOT necessary after every single drawing command,
//   // unless that's what you want...rather, you can batch up a bunch of
//   // drawing operations and then update the screen all at once by calling
//   // display.display(). These examples demonstrate both approaches...

//   testdrawline();      // Draw many lines

//   testdrawrect();      // Draw rectangles (outlines)

//   testfillrect();      // Draw rectangles (filled)

//   testdrawcircle();    // Draw circles (outlines)

//   testfillcircle();    // Draw circles (filled)

//   testdrawroundrect(); // Draw rounded rectangles (outlines)

//   testfillroundrect(); // Draw rounded rectangles (filled)

//   testdrawtriangle();  // Draw triangles (outlines)

//   testfilltriangle();  // Draw triangles (filled)

//   testdrawchar();      // Draw characters of the default font

//   testdrawstyles();    // Draw 'stylized' characters

//   testscrolltext();    // Draw scrolling text

//   testdrawbitmap();    // Draw a small bitmap image

//   //Invert and restore display, pausing in-between
//   display.invertDisplay(true);
//   delay(1000);
//   display.invertDisplay(false);
//   delay(1000);

//   testanimate(logo_bmp, LOGO_WIDTH, LOGO_HEIGHT); // Animate bitmaps
    //display.drawRoundRect(0, 0, 6, 6, display.height()/4, SSD1306_WHITE);
    //display.drawLine(0, 0, 1, 1, SSD1306_WHITE);
    //display.drawLine(0, 31, 1, 30, SSD1306_WHITE);
    //display.drawLine(127, 0, 126, 1, SSD1306_WHITE);
    //display.drawLine(127, 31, 126, 30, SSD1306_WHITE);
    //display.drawLine(0, 31, 127, 31, SSD1306_WHITE);
    //display.drawLine(0, 25, 127, 25, SSD1306_WHITE);
    //display.drawLine(0, 19, 127, 19, SSD1306_WHITE);
    //display.drawLine(0, 13, 127, 13, SSD1306_WHITE);

    

    //display.setCursor(10, -1);
    //display.write("who is copernicus");
    //display.setCursor(40, 25);     
    //display.cp437(true);
    //display.write("zxcvbnm");
    //display.drawLine(0, 24, 127, 24, SSD1306_WHITE);
    //display.setCursor(36,16);
    //display.write("asdfghjkl");
    //display.drawLine(0, 15, 127, 15, SSD1306_WHITE);
    //display.setCursor(36,7);
    //display.write("qwertyuiop");
    //display.drawLine(0, 6, 127, 6, SSD1306_WHITE);

    //display.setCursor(20,0);
    //display.write("who is copernicus");

    //display.setCursor(-1,-1);
    //display.write("l");
    display.fillRect(25, 25, 10, 10, SSD1306_INVERSE);

    display.display();

    Serial.begin(9600);
    // Initialize the button pin as an input
    pinMode(buttonPin, INPUT_PULLUP);

    radio.begin();
    radio.openWritingPipe(address);
    radio.setPALevel(RF24_PA_MIN);
    radio.stopListening();
}

void loop() {
  
  // read the input on analog pin A0:
  int analogValue = analogRead(A0);
  // Rescale to potentiometer's voltage (from 0V to 5V):
  //float voltage = floatMap(analogValue, 0, 1023, 0, 5);
  int key = map(analogValue, 0, 1023, 0, 28);

  // print out the value you read:
  //Serial.print("Analog: ");
  //Serial.print(analogValue);
  //Serial.print(", Voltage: ");
  //Serial.print(voltage);
  Serial.print(", Key: ");
  Serial.println(key);

  int square[ 29 ][ 4 ] = { { 0, 7, 7, 8 }, \
                            { 7, 7, 11, 8 }, \
                            { 17, 7, 11, 8 }, \
                            { 27, 7, 11, 8 }, \
                            { 37, 7, 11, 8 }, \
                            { 47, 7, 11, 8 }, \
                            { 57, 7, 11, 8 }, \
                            { 67, 7, 11, 8 }, \
                            { 77, 7, 11, 8 }, \
                            { 87, 7, 11, 8 }, \
                            {97, 7, 31, 8}, \
                            {2, 16, 11, 8}, \
                            {12, 16, 11, 8}, \
                            {22, 16, 11, 8}, \
                            {32, 16, 11, 8}, \
                            {42, 16, 11, 8}, \
                            {52, 16, 11, 8}, \
                            {62, 16, 11, 8}, \
                            {72, 16, 11, 8}, \
                            {82, 16, 11, 8}, \
                            {92, 16, 36, 8}, \
                            {7, 25, 11, 8}, \
                            {17, 25, 11, 8}, \
                            {27, 25, 11, 8}, \
                            {37, 25, 11, 8}, \
                            {47, 25, 11, 8}, \
                            {57, 25, 11, 8}, \
                            {67, 25, 11, 8}, \
                            {92, 25, 36, 8}};

  
  //delay(1000);
  // Read the state of the button
  buttonState = digitalRead(buttonPin);

  // Check if the button is pressed
  // If the button is pressed, the buttonState will be LOW (because of the pull-up)
  if (buttonState == LOW) {
    Serial.println("Button pressed!");
    if (key == 0){
      response += "q";
    }
    if (key == 1){
      response += "w";
    }
    if (key == 2){
      response += "e";
    }
    if (key == 3){
      response += "r";
    }
    if (key == 4){
      response += "t";
    }
    if (key == 5){
      response += "y";
    }
    if (key == 6){
      response += "u";
    }
    if (key == 7){
      response += "i";
    }
    if (key == 8){
      response += "o";
    }
    if (key == 9){
      response += "p";
    }
    if (key == 10){
      response.remove(response.length() - 1);
    }
    if (key == 11){
      response += "a";
    }
    if (key == 12){
      response += "s";
    }
    if (key == 13){
      response += "d";
    }
    if (key == 14){
      response += "f";
    }
    if (key == 15){
      response += "g";
    }
    if (key == 16){
      response += "h";
    }
    if (key == 17){
      response += "j";
    }
    if (key == 18){
      response += "k";
    }
    if (key == 19){
      response += "l";
    }
    if (key == 20) {
        // Convert the response to a C-style string
        const char* responseChar = response.c_str();
        Serial.println(responseChar);

        // Now, responseChar is a C-string (const char*) that can be used with the radio module
        radio.write(responseChar, strlen(responseChar) + 1); // +1 to include the null terminator

        // Clear the response and display a confirmation message
        response = "";
        display.clearDisplay();
        display.setCursor(0, 12);
        display.print("Response sent!");
        display.display();
        delay(3000);
    }
    if (key == 21){
      response += "z";
    }
    if (key == 22){
      response += "x";
    }
    if (key == 23){
      response += "c";
    }
    if (key == 24){
      response += "v";
    }
    if (key == 25){
      response += "b";
    }
    if (key == 26){
      response += "n";
    }
    if (key == 27){
      response += "m";
    }
    if (key == 28){
      response += " ";
    }
    delay(100);
  }


  //display.setCursor(0,0);
  //display.write(voltage);
  display.clearDisplay();
  drawKeyboard();
  display.fillRect(square[key][0], square[key][1], square[key][2], square[key][3], SSD1306_INVERSE);
  display.setCursor(0,0);
  display.print(response);
  display.display();
  
}