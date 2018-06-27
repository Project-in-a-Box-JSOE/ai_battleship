//c++ code for aduino


// this funtion ony runs once when the arduino turns on
void setup () {
	Serial.begin(9600);
}

//this method runs continuously afterwards
void loop() {

	//we will be using output for the LED lights
	//we will be using input for the buttons
	pinMode(pin, INPUT/OUTPUT); //this is an example of setting a pin to input or output
	digitalWrite(pin, HIGH/LOW); //example of setting pin voltage to high(5V) or low(ground) if output
								//in input, set high(enable) or low(disable)

}