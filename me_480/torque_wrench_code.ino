#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>


// load cell libs
#include "Adafruit_HX711.h"
// load cell parameters
const uint8_t DATA_PIN = 4;  // Can use any pins!
const uint8_t CLOCK_PIN = 16; // Can use any pins!

Adafruit_HX711 hx711(DATA_PIN, CLOCK_PIN);

// display load cell text
static String disp_text;

// Set LCD screen parameters
#define SCREEN_WIDTH 128 // OLED display width, in pixels
#define SCREEN_HEIGHT 32 // OLED display height, in pixels
#define OLED_RESET     -1 // Reset pin # (or -1 if sharing Arduino reset pin)
#define SCREEN_ADDRESS 0x3C ///< See datasheet for Address; 0x3D for 128x64, 0x3C for 128x32
Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

// Rotary Encoder Inputs
#define CLK 18
#define DT 17
#define SW 15

// set rotary encoder variables
int counter = 0;                    // Counter for encoder position
int currentStateCLK;                // Current state of CLK
int lastStateCLK;                   // Last state of CLK
String currentDir = "";             // Current direction of rotation
unsigned long lastButtonPress = 0;  // Time of last button press

// set state pins 
int torque_set = 0;
int last_set = 0;

// define power pins
#define PWR_PIN_1 5 

// define motor direction switch
#define MOT_DIR 12

#define IN1 25
#define IN2 32
#define ENA 27

// blink when power buttons are pressed
#define LED_BUILTIN 2

int pwr_1_val = 0;
int mot_dir_val = 0;
int torque_meas = 0;
bool reached_torque = false;

void setup() {
  // Set encoder pins as inputs
  pinMode(CLK, INPUT);
  pinMode(DT, INPUT);
  pinMode(SW, INPUT_PULLUP);
  pinMode(PWR_PIN_1, INPUT_PULLUP);
  pinMode(MOT_DIR, INPUT_PULLUP);
  pinMode(LED_BUILTIN, OUTPUT);
  pinMode(IN1, OUTPUT);
  pinMode(IN2, OUTPUT);
  pinMode(ENA, OUTPUT);
  // Setup Serial Monitor
  Serial.begin(115200);

  // wait for serial port to connect. Needed for native USB port only
  while (!Serial) {
    delay(10);
  }
  // Read the initial state of CLK
  lastStateCLK = digitalRead(CLK);
  // SSD1306_SWITCHCAPVCC = generate display voltage from 3.3V internally
  if(!display.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS)) {
    Serial.println(F("SSD1306 allocation failed"));
    for(;;); // Don't proceed, loop forever
  }

  display.clearDisplay();
  display.setCursor(0,0);             // Start at top-left corner
  display.setTextSize(2);             // Draw 2X-scale text
  display.setTextColor(SSD1306_WHITE);
  display.println("Turn to");
  display.println("Assign Torque");
  display.display();

  // Initialize the HX711
  hx711.begin();
  // tare sensor
  Serial.println("Tareing....");
  for (uint8_t t=0; t<3; t++) {
    hx711.tareA(hx711.readChannelRaw(CHAN_A_GAIN_128));
    hx711.tareA(hx711.readChannelRaw(CHAN_A_GAIN_128));
    hx711.tareB(hx711.readChannelRaw(CHAN_B_GAIN_32));
    hx711.tareB(hx711.readChannelRaw(CHAN_B_GAIN_32));
  }

}

void loop() {

  // Read the current state of CLK if torque isn't set
  // Serial.println("Torque Set: "+ String(counter)); 
  if (torque_set == 0){
    // delay(1);
    currentStateCLK = digitalRead(CLK);
    // delay(1);
    // If last and current state of CLK are different, then pulse occurred
    // React to only 1 state change to avoid double count
    // Serial.println("Clock: " + String(currentStateCLK));
    if (currentStateCLK != lastStateCLK && currentStateCLK == 1) {
      // If the DT state is different than the CLK state then
      // the encoder is rotating CCW so decrement
      if (digitalRead(DT) != currentStateCLK) {
        counter = counter + 25;
        currentDir = "CW";
        Serial.println("Tick Detected +");
      } else {
        // Encoder is rotating CW so increment
        counter = counter - 25;
        currentDir = "CCW";
        Serial.println("Tick Detected -");
      }
      display.clearDisplay();
      display.setCursor(0,0);             // Start at top-left corner
      display.setTextSize(2);             // Draw 2X-scale text
      display.setTextColor(SSD1306_WHITE);
      display.println("Set T: ");
      String message = String(counter) + " Nmm";
      display.println(message);
      display.display();
    }

    // Remember last CLK state
    lastStateCLK = currentStateCLK;
  }
  else{
    pwr_1_val = digitalRead(PWR_PIN_1);
    mot_dir_val = digitalRead(MOT_DIR);
    // if power button is pressed, value will be low
    Serial.println("Mot Dir: " + String(mot_dir_val));
    if (mot_dir_val == 0){
      digitalWrite(IN1, 0);
      digitalWrite(IN2, 1);
    }
    else{
      digitalWrite(IN1, 1);
      digitalWrite(IN2, 0);
    }

    if (reached_torque == false){
      if (pwr_1_val == LOW){
        digitalWrite(LED_BUILTIN, HIGH); // turn on LED
        digitalWrite(ENA, HIGH);
      }
      else{
        digitalWrite(LED_BUILTIN, LOW); // turn off LED
        digitalWrite(ENA, LOW);
      }
    }
    else if (reached_torque == true){
      digitalWrite(LED_BUILTIN, LOW); // turn off LED
      digitalWrite(ENA, LOW);
      display.clearDisplay();
      display.setCursor(0,0);             // Start at top-left corner
      display.setTextSize(2);             // Draw 2X-scale text
      display.setTextColor(SSD1306_WHITE);
      disp_text = String(counter) + " Nmm";
      display.println(disp_text);
      display.println("Torque Reached!");
      display.display();
      delay(800);
      torque_set = 0;
      // counter = 0;
      reached_torque = false;
      display.clearDisplay();
      display.setCursor(0,0);             // Start at top-left corner
      display.setTextSize(2);             // Draw 2X-scale text
      display.setTextColor(SSD1306_WHITE);
      display.println("Turn to");
      display.println("Assign Torque");
      display.display();
    }
    // display load cell weight
    int32_t weightA128 = hx711.readChannelBlocking(CHAN_A_GAIN_128);
    weightA128 = int(weightA128/100);
    torque_meas = int(weightA128*0.1831);
    disp_text = String(torque_meas) + " Nmm";
    display.clearDisplay();
    display.setCursor(0,0);             // Start at top-left corner
    display.setTextSize(2);             // Draw 2X-scale text
    display.setTextColor(SSD1306_WHITE);
    display.println("Load Cell:" );
    display.println(disp_text);
    display.display();
    delay(20);
    
    if(abs(torque_meas) > abs(counter)){
      reached_torque = true;
    }
    else{
      reached_torque = false;
    }

  }

  // Read the button state
  int btnState = digitalRead(SW);

  //If we detect LOW signal, button is pressed
  if (btnState == LOW) {
    // Remember last button press event
    lastButtonPress = millis();
    
    if (last_set == 0){
      torque_set = 1;
      last_set = 1;
      // display fixed value of torque drill
      display.clearDisplay();
      display.setCursor(0,0);             // Start at top-left corner
      display.setTextSize(2);             // Draw 2X-scale text
      display.setTextColor(SSD1306_WHITE);
      display.println("Fixed T: ");
      String message = String(counter) + " Nmm";
      display.println(message);
      display.display();
      delay(250);
    }
    else{
      torque_set = 0;
      last_set = 0;
      display.clearDisplay();
      display.setCursor(0,0);             // Start at top-left corner
      display.setTextSize(2);             // Draw 2X-scale text
      display.setTextColor(SSD1306_WHITE);
      display.println("Set T: ");
      String message = String(counter) + " Nmm";
      display.println(message);
      display.display();
    }

    // wait for button press to end
    while (millis() - lastButtonPress < 100) {
      delay(5);
    }

    // Remember last button press event
    lastButtonPress = millis();
  }

  delay(1);
}
