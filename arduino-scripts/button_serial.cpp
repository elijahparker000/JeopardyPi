// Arduino script to read 5 buttons and send numbers 1-5 to the serial port
// Uses internal pull-up resistors
// Buttons are connected between the digital pins and ground

// Define the button pins (change these to the pins you want to use)
const int buttonPins[5] = {9, 8, 7, 5, 3}; // Pins where buttons are connected

// Variables to keep track of button states
bool buttonStates[5] = {HIGH, HIGH, HIGH, HIGH, HIGH};        // Current state of the buttons
bool lastButtonStates[5] = {HIGH, HIGH, HIGH, HIGH, HIGH};    // Previous state of the buttons
unsigned long lastDebounceTime[5] = {0, 0, 0, 0, 0};          // Timestamp of the last state change
const unsigned long debounceDelay = 50;                       // Debounce delay in milliseconds

void setup() {
  // Initialize serial communication
  Serial.begin(9600);

  // Initialize the button pins as inputs with internal pull-up resistors
  for (int i = 0; i < 5; i++) {
    pinMode(buttonPins[i], INPUT_PULLUP);
  }
}

void loop() {
  // Iterate over each button
  for (int i = 0; i < 5; i++) {
    // Read the current state of the button
    int reading = digitalRead(buttonPins[i]);

    // If the button state has changed due to noise or pressing
    if (reading != lastButtonStates[i]) {
      // Reset the debouncing timer
      lastDebounceTime[i] = millis();
    }

    // If enough time has passed (debounce delay)
    if ((millis() - lastDebounceTime[i]) > debounceDelay) {
      // If the button state has changed
      if (reading != buttonStates[i]) {
        buttonStates[i] = reading;

        // If the button is pressed (since we're using INPUT_PULLUP, LOW means pressed)
        if (buttonStates[i] == LOW) {
          // Send the corresponding number to the serial port
          Serial.println(i + 1); // i ranges from 0-4, so add 1 to get 1-5
        }
      }
    }

    // Save the current reading as the last state for the next loop iteration
    lastButtonStates[i] = reading;
  }
}