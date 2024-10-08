const uint8_t gpioNum = 2;

void setup()
{
    // Ustawiamy GPIO 2 jako wejście podciągnięte do plusa
    Serial.begin(9600);
    pinMode(gpioNum, INPUT_PULLUP);
}

void loop () 
{
    static bool lastValue = 1;
    /* Polling */
    bool currentValue = digitalRead(gpioNum);
    if (currentValue == 0 && lastValue == 1)
    {
        /* Wystąpił warunek przerwania */
        Serial.println("Warunek spełniony");
    }
    lastValue = currentValue;
}