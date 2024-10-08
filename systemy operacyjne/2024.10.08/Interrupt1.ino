const uint8_t gpioNum = 2;

void ISRfunc()
{
    Serial.println("Warunek spelniony (INT)");  // <- nie tak; to powinno być w programie głównym, a tu powinna być flaga
}

void setup()
{
    // Ustawiamy GPIO 2 jako wejście podciągnięte do plusa
    Serial.begin(9600);
    pinMode(gpioNum, INPUT_PULLUP);
    attachInterrupt(digitalPinToInterrupt(gpioNum), ISRfunc, FALLING);
}


/*
void loop () 
{
    static bool lastValue = 1;
    //Polling
    bool currentValue = digitalRead(gpioNum);
    if (currentValue == 0 && lastValue == 1)
    {
        // Wystąpił warunek przerwania 
        Serial.println("Warunek spełniony");
    }
    lastValue = currentValue;
}
*/

void loop()
{
    Serial.println("Random print ...");
    delay(100);
}