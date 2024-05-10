tinkercad <- strona z symulacją mikrokontrolera


Arduino:

#------------------------------------WPROWADZENIE--------------------------------------

#define LED_GREEN 6		//nie zajmuje miejsca w pamięci

const int ledRed = 5;	//zajmuje miejsce w pamięci

void setup() {
  pinMode(7, OUTPUT);
  pinMode(LED_GREEN, OUTPUT);
  pinMode(ledRed, OUTPUT);
}

void loop() {
  digitalWrite(LED_GREEN, HIGH);
  delay(1000);
  digitalWrite(LED_GREEN, LOW);
  delay(500);
}

#-------------------------------------ZADANIE------------------------------------------

const int ledRed = 5;
const int ledGreen = 6;
const int ledYellow = 7;

const int ledNumber = 3;
int leds[] = {ledRed, ledGreen, ledYellow};

void setup() {
  for (int i=0; i<ledNumber; i++) {
    pinMode(leds[i], OUTPUT);
  }
}

void loop() {

  digitalWrite(ledGreen, HIGH);
  delay(1000);
  digitalWrite(ledGreen, LOW);
  delay(500);
}

#---------------------------- [mój]

#include <iostream>
#include <cstdlib>

const int ledRed = 5;
const int ledGreen = 6;
const int ledYellow = 7;

class LedController {
  private:
    int ledNumber;
    int leds[10];
  public:
    LedController();
    void addPin(int x);
    void printLeds() {
        for(int i=0; i<ledNumber; i++) {
            printf("leds[%d]=%d\n", i, leds[i]);
        }
    }
};


LedController::LedController() {
    ledNumber = 0;
}

void LedController::addPin(int x) {
  leds[ledNumber] = x;
  ledNumber++;
  printf("leds[%d]=%d ledNumber=%d\n", ledNumber-1, leds[ledNumber-1], ledNumber);
}



int main() {
    LedController lc;
    lc.addPin(1);
    lc.addPin(6);
    lc.addPin(7);
    lc.printLeds();
    return 0;
}


#-------------------------------------------

const int ledRed = 5;
const int ledGreen = 6;
const int ledYellow = 7;

class LedController {
  private:
    const int capacity = 2;
    int ledNumber;
    int leds[2];
  public:
    LedController() {;
      ledNumber = 0;
    }
    bool addPin(int x);
};

bool LedController::addPin(int x) {
  int index = ledNumber;
  if (index < capacity) {
    leds[index] = x;
    ledNumber += 1;
    return true;
  }
  return false;
}


void setup() {
  Serial.begin(9600);	  //komunikacja przez konsolę szeregową
  LedController ledContr;
  bool result = ledContr.addPin(ledRed);
  if (!result){
    Serial.println("No space for red LED");
  }
  
  result = ledContr.addPin(ledGreen);
  if (!result){
    Serial.println("No space for green LED");
  }
  
  result = ledContr.addPin(ledYellow);
  if (!result){
    Serial.println("No space for yellow LED");
  }
}

void loop() {

  digitalWrite(ledGreen, HIGH);
  delay(1000);
  digitalWrite(ledGreen, LOW);
  delay(500);
}


#- - - - - - - - - - - 

OUTPUT:
No space for yellow LED


#------------------------------------------

const int ledRed = 5;
const int ledGreen = 6;
const int ledYellow = 7;

class LedController {
  private:
    const int capacity = 2;
    int ledNumber;
    int leds[2];
  public:
    LedController() {;
      ledNumber = 0;
    }
    bool addPin(int x);
    void turnAllLEDs(int state = 1); 
};

bool LedController::addPin(int x) {
  int index = ledNumber;
  if (index < capacity) {
    pinMode(x, OUTPUT);
    leds[index] = x;
    ledNumber += 1;
    return true;
  }
  return false;
}

void LedController::turnAllLEDs(int state) {
  for (int i=0; i<ledNumber; i++) {
    if (state == 1) {
      digitalWrite(leds[i], HIGH);
    } else {
      digitalWrite(leds[i], LOW);
    }
  }  
}


LedController ledContr;

void setup() {
  Serial.begin(9600);	//komunikacja przez konsolę szeregową
  bool result = ledContr.addPin(ledRed);
  if (!result){
    Serial.println("No space for red LED");
  }
  
  result = ledContr.addPin(ledGreen);
  if (!result){
    Serial.println("No space for green LED");
  }
  
  result = ledContr.addPin(ledYellow);
  if (!result){
    Serial.println("No space for yellow LED");
  }
}

void loop() {
  ledContr.turnAllLEDs();
  delay(1000);
  ledContr.turnAllLEDs(0);
  delay(500);
}

#------------------------------------------

void digitalWrite(uint8_t pin, uint8_t val)

uint8_t - unsign int 8-bitowy 

#-----------------uint8_t------------------

const int ledRed = 5;
const int ledGreen = 6;
const int ledYellow = 7;


class LedController {
  private:
    const int capacity = 2;
    int ledNumber;
    int leds[2];
  public:
    LedController() {;
      ledNumber = 0;
    }
    bool addPin(int x);
    void turnAllLEDs(uint8_t state = HIGH); 
};

bool LedController::addPin(int x) {
  int index = ledNumber;
  if (index < capacity) {
    pinMode(x, OUTPUT);
    leds[index] = x;
    ledNumber += 1;
    return true;
  }
  return false;
}

void LedController::turnAllLEDs(uint8_t state) {
  for (int i=0; i<ledNumber; i++) {
    digitalWrite(leds[i], state);
  }  
}





LedController ledContr;

void setup() {
  Serial.begin(9600);	//komunikacja przez konsolę szeregową
  bool result = ledContr.addPin(ledRed);
  if (!result){
    Serial.println("No space for red LED");
  }
  
  result = ledContr.addPin(ledGreen);
  if (!result){
    Serial.println("No space for green LED");
  }
  
  result = ledContr.addPin(ledYellow);
  if (!result){
    Serial.println("No space for yellow LED");
  }
}

void loop() {
  ledContr.turnAllLEDs();
  delay(1000);
  ledContr.turnAllLEDs(LOW);
  delay(500);
}

#--------------DYNAM. TABLICA---------------

const int ledRed = 5;
const int ledGreen = 6;
const int ledYellow = 7;


class LedController {
  private:
    int capacity;
    int ledNumber;
    int *leds;
  public:
    LedController(int capacity) {
      this->capacity = capacity;                           
      ledNumber = 0;
      leds = new int[capacity];
    }
    bool addPin(int x);
    void turnAllLEDs(uint8_t state = HIGH); 
};

bool LedController::addPin(int x) {
  int index = ledNumber;
  if (index < capacity) {
    pinMode(x, OUTPUT);
    leds[index] = x;
    ledNumber += 1;
    return true;
  }
  return false;
}

void LedController::turnAllLEDs(uint8_t state) {
  for (int i=0; i<ledNumber; i++) {
    digitalWrite(leds[i], state);
  }  
}





LedController ledContr(5);

void setup() {
  Serial.begin(9600);	//komunikacja przez konsolę szeregową
  bool result = ledContr.addPin(ledRed);
  if (!result){
    Serial.println("No space for red LED");
  }
  
  result = ledContr.addPin(ledGreen);
  if (!result){
    Serial.println("No space for green LED");
  }
  
  result = ledContr.addPin(ledYellow);
  if (!result){
    Serial.println("No space for yellow LED");
  }
}

void loop() {
  ledContr.turnAllLEDs();
  delay(1000);
  ledContr.turnAllLEDs(LOW);
  delay(500);
}

#----------------DESTRUKTOR-----------------

const int ledRed = 5;
const int ledGreen = 6;
const int ledYellow = 7;


class LedController {
  private:
    int capacity;
    int ledNumber;
    int *leds;
  public:
    LedController(int capacity) {
      this->capacity = capacity;                           
      ledNumber = 0;
      leds = new int[capacity];
    }
    ~LedController() {		//destruktor
      delete [] leds; 		//free() z języka C
    }
    bool addPin(int x);
    void turnAllLEDs(uint8_t state = HIGH); 
};

bool LedController::addPin(int x) {
  int index = ledNumber;
  if (index < capacity) {
    pinMode(x, OUTPUT);
    leds[index] = x;
    ledNumber += 1;
    return true;
  }
  return false;
}

void LedController::turnAllLEDs(uint8_t state) {
  for (int i=0; i<ledNumber; i++) {
    digitalWrite(leds[i], state);
  }  
}





LedController ledContr(5);

void setup() {
  Serial.begin(9600);	//komunikacja przez konsolę szeregową
  bool result = ledContr.addPin(ledRed);
  if (!result){
    Serial.println("No space for red LED");
  }
  
  result = ledContr.addPin(ledGreen);
  if (!result){
    Serial.println("No space for green LED");
  }
  
  result = ledContr.addPin(ledYellow);
  if (!result){
    Serial.println("No space for yellow LED");
  }
}

void loop() {
  ledContr.turnAllLEDs();
  delay(1000);
  ledContr.turnAllLEDs(LOW);
  delay(500);
}

#---------WYŁ/WŁ OPCJI ZMIANY STANU LEDa----------

const int ledRed = 5;
const int ledGreen = 6;
const int ledYellow = 7;


class LedController {
  private:
    int capacity;
    int ledNumber;
    int *leds;
    bool *active;
  public:
    LedController(int capacity) {
      this->capacity = capacity;                           
      ledNumber = 0;
      leds = new int[capacity];
      active = new bool[capacity];
    }
    ~LedController() {		//destruktor
      delete [] leds; 		//free() z języka C
      delete [] active;
    }
    bool addPin(int p);
    void turnAllLEDs(uint8_t state = HIGH); 
    void activateLED(uint8_t p, bool active = true);
};

bool LedController::addPin(int p) {
  int index = ledNumber;
  if (index < capacity) {
    pinMode(p, OUTPUT);
    digitalWrite(p, LOW);
    leds[index] = p;
    active[index] = true;
    ledNumber += 1;
    return true;
  }
  return false;
}

void LedController::turnAllLEDs(uint8_t state) {
  for (int i=0; i<ledNumber; i++) {
    digitalWrite(leds[i], state);
  }  
}

void LedController::activateLED(uint8_t p, bool active) {
  for(int i=0; i<ledNumber; i++) {
    if (leds[i] == p){
      this->active[i] = active;
      break;
    }
  }
  
}




LedController ledContr(5);

void setup() {
  Serial.begin(9600);	//komunikacja przez konsolę szeregową
  bool result = ledContr.addPin(ledRed);
  if (!result){
    Serial.println("No space for red LED");
  }
  
  result = ledContr.addPin(ledGreen);
  if (!result){
    Serial.println("No space for green LED");
  }
  
  result = ledContr.addPin(ledYellow);
  if (!result){
    Serial.println("No space for yellow LED");
  }
  
  ledContr.activateLED(ledGreen, false);
}

void loop() {
  ledContr.turnAllLEDs();
  delay(1000);
  ledContr.turnAllLEDs(LOW);
  delay(500);
}


#---------WYŁ/WŁ OPCJI ZMIANY STANU LEDa C.D.----------

#--------------WYŁĄCZENIE 1 LOSOWEJ DIODY--------------

const int ledRed = 5;
const int ledGreen = 6;
const int ledYellow = 7;


class LedController {
  private:
    int capacity;
    int ledNumber;
    int *leds;
    bool *active;
  public:
    LedController(int capacity) {
      this->capacity = capacity;                           
      ledNumber = 0;
      leds = new int[capacity];
      active = new bool[capacity];
    }
    ~LedController() {		//destruktor
      delete [] leds; 		//free() z języka C
      delete [] active;
    }
    bool addPin(int p);
    void turnAllLEDs(uint8_t state = HIGH); 
    void activateLED(uint8_t p, bool active = true);
};

bool LedController::addPin(int p) {
  int index = ledNumber;
  if (index < capacity) {
    pinMode(p, OUTPUT);
    digitalWrite(p, LOW);
    leds[index] = p;
    active[index] = true;
    ledNumber += 1;
    return true;
  }
  return false;
}

void LedController::turnAllLEDs(uint8_t state) {
  for (int i=0; i<ledNumber; i++) {
    if (active[i]){
      digitalWrite(leds[i], state);
    }
  }  
}

void LedController::activateLED(uint8_t p, bool active) {
  for(int i=0; i<ledNumber; i++) {
    if (leds[i] == p){
      this->active[i] = active;
      break;
    }
  }
}




LedController ledContr(5);

void setup() {
  Serial.begin(9600);	//komunikacja przez konsolę szeregową
  bool result = ledContr.addPin(ledRed);
  if (!result){
    Serial.println("No space for red LED");
  }
  
  result = ledContr.addPin(ledGreen);
  if (!result){
    Serial.println("No space for green LED");
  }
  
  result = ledContr.addPin(ledYellow);
  if (!result){
    Serial.println("No space for yellow LED");
  }
  
  ledContr.activateLED(ledGreen, false);
}

void loop() {
  uint8_t l = rand()% 3+5;
  ledContr.activateLED(l, false);
  ledContr.turnAllLEDs();
  delay(1000);
  ledContr.turnAllLEDs(LOW);
  delay(500);
  ledContr.activateLED(l);
}

#---------------------KLASA LED------------------- [mój] (public)

const int ledRed = 5;
const int ledGreen = 6;
const int ledYellow = 7;


class Led {
  public:
    int leds;
    bool active;
};


class LedController {
  private:
    int capacity;
    int ledNumber;
    Led *leds;
  public:
    LedController(int capacity) {
      this->capacity = capacity;                           
      ledNumber = 0;
      leds = new Led[capacity];
    }
    ~LedController() {		//destruktor
      delete [] leds; 		//free() z języka C
    }
    bool addPin(int p);
    void turnAllLEDs(uint8_t state = HIGH); 
    void activateLED(uint8_t p, bool active = true);
};

bool LedController::addPin(int p) {
  int index = ledNumber;
  if (index < capacity) {
    pinMode(p, OUTPUT);
    digitalWrite(p, LOW);
    leds[index].leds = p;
    leds[index].active = true;
    ledNumber += 1;
    return true;
  }
  return false;
}

void LedController::turnAllLEDs(uint8_t state) {
  for (int i=0; i<ledNumber; i++) {
    if (leds[i].active){
      digitalWrite(leds[i].leds, state);
    }
  }  
}

void LedController::activateLED(uint8_t p, bool active) {
  for(int i=0; i<ledNumber; i++) {
    if (leds[i].leds == p){
      this->leds[i].active = active;
      break;
    }
  }
}




LedController ledContr(5);

void setup() {
  Serial.begin(9600);	//komunikacja przez konsolę szeregową
  bool result = ledContr.addPin(ledRed);
  if (!result){
    Serial.println("No space for red LED");
  }
  
  result = ledContr.addPin(ledGreen);
  if (!result){
    Serial.println("No space for green LED");
  }
  
  result = ledContr.addPin(ledYellow);
  if (!result){
    Serial.println("No space for yellow LED");
  }
  
  ledContr.activateLED(ledGreen, false);
}

void loop() {
  uint8_t l = rand()% 3+5;
  ledContr.activateLED(l, false);
  ledContr.turnAllLEDs();
  delay(1000);
  ledContr.turnAllLEDs(LOW);
  delay(500);
  ledContr.activateLED(l);
}

#---------------------KLASA LED------------------- [mój] (private)

const int ledRed = 5;
const int ledGreen = 6;
const int ledYellow = 7;


class Led {
  private:
    int leds;
    bool active;
  public:
    int retLeds() {
      return leds;
    }  
    bool retActive() {
      return active;
    }
    void setLeds(int p) {
      leds = p;
    }
    void setActive(bool state) {
      active = state;
    }
};


class LedController {
  private:
    int capacity;
    int ledNumber;
    Led *leds;
  public:
    LedController(int capacity) {
      this->capacity = capacity;                           
      ledNumber = 0;
      leds = new Led[capacity];
    }
    ~LedController() {		//destruktor
      delete [] leds; 		//free() z języka C
    }
    bool addPin(int p);
    void turnAllLEDs(uint8_t state = HIGH); 
    void activateLED(uint8_t p, bool active = true);
};

bool LedController::addPin(int p) {
  int index = ledNumber;
  if (index < capacity) {
    pinMode(p, OUTPUT);
    digitalWrite(p, LOW);
    leds[index].setLeds(p);
    leds[index].setActive(true);
    ledNumber += 1;
    return true;
  }
  return false;
}

void LedController::turnAllLEDs(uint8_t state) {
  for (int i=0; i<ledNumber; i++) {
    if (leds[i].retActive()){
      digitalWrite(leds[i].retLeds(), state);
    }
  }  
}

void LedController::activateLED(uint8_t p, bool active) {
  for(int i=0; i<ledNumber; i++) {
    if (leds[i].retLeds() == p){
      this->leds[i].setActive(active);
      break;
    }
  }
}




LedController ledContr(5);

void setup() {
  Serial.begin(9600);	//komunikacja przez konsolę szeregową
  bool result = ledContr.addPin(ledRed);
  if (!result){
    Serial.println("No space for red LED");
  }
  
  result = ledContr.addPin(ledGreen);
  if (!result){
    Serial.println("No space for green LED");
  }
  
  result = ledContr.addPin(ledYellow);
  if (!result){
    Serial.println("No space for yellow LED");
  }
  
  ledContr.activateLED(ledGreen, false);
}

void loop() {
  uint8_t l = rand()% 3+5;
  ledContr.activateLED(l, false);
  ledContr.turnAllLEDs();
  delay(1000);
  ledContr.turnAllLEDs(LOW);
  delay(500);
  ledContr.activateLED(l);
}


