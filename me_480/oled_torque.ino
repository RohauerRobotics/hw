// OLED libraries
#include <SPI.h>
#include <Wire.h>
#include <Adafruit_GFX.h>
#include <Adafruit_SSD1306.h>

// load cell libs
#include "Adafruit_HX711.h"

// OLED parameters
#define SCREEN_WIDTH 128 // OLED display width, in pixels
#define SCREEN_HEIGHT 32 // OLED display height, in pixels
#define OLED_RESET     -1 // Reset pin # (or -1 if sharing Arduino reset pin)
#define SCREEN_ADDRESS 0x3C ///< See datasheet for Address; 0x3D for 128x64, 0x3C for 128x32

Adafruit_SSD1306 display(SCREEN_WIDTH, SCREEN_HEIGHT, &Wire, OLED_RESET);

// load cell parameters
const uint8_t DATA_PIN = 4;  // Can use any pins!
const uint8_t CLOCK_PIN = 16; // Can use any pins!

Adafruit_HX711 hx711(DATA_PIN, CLOCK_PIN);

static String disp_text;

void setup() {
  Serial.begin(115200);

  // wait for serial port to connect. Needed for native USB port only
  while (!Serial) {
    delay(10);
  }

  // connect to oled display
  if(!display.begin(SSD1306_SWITCHCAPVCC, SCREEN_ADDRESS)) {
    Serial.println(F("SSD1306 allocation failed"));
    for(;;); // Don't proceed, loop forever
  }

  display.clearDisplay();

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
  // read load cell weight
  int32_t weightA128 = hx711.readChannelBlocking(CHAN_A_GAIN_128);
  weightA128 = int(weightA128/100);
  disp_text = "Tor:"+ String(weightA128) + " Nm";
  display.clearDisplay();
  display.setCursor(0,0);             // Start at top-left corner
  display.setTextSize(2);             // Draw 2X-scale text
  display.setTextColor(SSD1306_WHITE);
  display.println(disp_text);
  display.display();
  delay(100);
}
