#include <DHT11.h>

//LED pin definitions based on what they control
#define TEMP_GREEN 3 
#define TEMP_RED   4
#define HUM_GREEN  5
#define HUM_RED    6

DHT11 dht11(2); //created DHT11 object

void temperatureLights(float temperature) { //changing which lights are on based on the measured values
   if (temperature >= 18 && temperature <= 25) { //&& is the equivelant of and in python
    Serial.println("Temperature levels are safe, no need to take any precautions.");
    digitalWrite(TEMP_GREEN, HIGH); //Turns on TEMP_GREEN 
    digitalWrite(TEMP_RED, LOW); //Turns off the TEMP_RED pin to ON
  }
  else if (temperature < 18) {
    Serial.println("Temperature is too cold, turn on a heater or thermostat. If you are outside, please move to controlled indoors or wear some protective warm clothing");
    digitalWrite(TEMP_GREEN, LOW);
    digitalWrite(TEMP_RED, HIGH);
    delay(300); //pauses the code for a couple miliseconds
    digitalWrite(TEMP_RED, LOW);
    delay(300);
  } 
  else {
    Serial.println("Tempreature is too high, turn on a fan or AC. Ensure you drink lots of water.");
    digitalWrite(TEMP_GREEN, LOW);
    digitalWrite(TEMP_RED, HIGH);
  }
}

void humidityLights(float humidity) { //changing which lights are on based on the measured values
  if (humidity >= 40 && humidity <= 55) {
    Serial.println("Humidity levels are safe, no need to take any precautions.");
    digitalWrite(HUM_GREEN, HIGH);
    digitalWrite(HUM_RED, LOW);
  } 
  else if (humidity < 40) {
    Serial.print("Humidity is too low, turn on a humidifier. If you are outside, please move to controlled indoors. Ensure youi drink lots of water");
    digitalWrite(HUM_GREEN, LOW);
    digitalWrite(HUM_RED, HIGH);
    delay(300);
    digitalWrite(HUM_RED, LOW);
    delay(300);
  } 
  else {
    Serial.println("Humidity is too high, turn on a dehumidifier. If you are outside, please move to controlled indoors. Ensure youi drink lots of water as high humidity interferes your cooling systems");
    digitalWrite(HUM_GREEN, LOW);
    digitalWrite(HUM_RED, HIGH);
  }
}

void setup() {
  // put your setup code here, to run once:
  Serial.begin(9600); //establish communication between arduino through computer usb port
  //Set the LED pins to output 
  pinMode(TEMP_GREEN, OUTPUT);
  pinMode(TEMP_RED, OUTPUT);
  pinMode(HUM_GREEN, OUTPUT);
  pinMode(HUM_RED, OUTPUT);
}

void loop() {
  // put your main code here, to run repeatedly:
  float temperature = dht11.readTemperature(); //getting readings from sensor, float for accuracy
  float humidity = dht11.readHumidity();

  Serial.print(temperature); //displaying the measured values so I can see them. No extra words so I can use the serial plotter to graph data
  Serial.print(" ");
  Serial.println(humidity);
  
  temperatureLights(temperature); // calling the functions to control lights
  humidityLights(humidity);

  delay(10000); //delay next loop by 10s because DHT11 is slow at measuring and we don't want to overload it
}