// Define the button pins (change these to the pins you want to use)
const int buttonPins[6] = {9, 8, 7, 5, 3, 10}; // Pins where buttons are connected

// Variables to keep track of button states
bool buttonStates[6] = {HIGH, HIGH, HIGH, HIGH, HIGH, HIGH};        // Current state of the buttons
bool lastButtonStates[6] = {HIGH, HIGH, HIGH, HIGH, HIGH, HIGH};    // Previous state of the buttons
unsigned long lastDebounceTime[6] = {0, 0, 0, 0, 0, 0};             // Timestamp of the last state change
const unsigned long debounceDelay = 50;                             // Debounce delay in milliseconds

void setup() {
  // Initialize serial communication
  Serial.begin(9600);

  // Initialize the button pins as inputs with internal pull-up resistors
  for (int i = 0; i < 6; i++) {
    pinMode(buttonPins[i], INPUT_PULLUP);
  }
}

void loop() {
  // Iterate over each button
  for (int i = 0; i < 6; i++) {
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

        if (i < 5) {
          // For buttons 1-5
          if (buttonStates[i] == LOW) {
            Serial.println(i + 1); // Send 1-5 for buttons 1-5
          }
        } else if (i == 5) {
          // For button 6 (special behavior)
          if (buttonStates[i] == LOW) {
            Serial.println("6_press"); // When button 6 is pressed
          } else {
            Serial.println("6_release"); // When button 6 is released
          }
        }
      }
    }

    // Save the current reading as the last state for the next loop iteration
    lastButtonStates[i] = reading;
  }
}
