#------------------------3 DIODY-------------------------

#define LED_RED 12
#define LED_YELLOW 11
#define LED_GREEN 10


void setup() {
  pinMode(LED_RED, OUTPUT);
  pinMode(LED_YELLOW, OUTPUT);
  pinMode(LED_GREEN, OUTPUT);

  digitalWrite(LED_RED, LOW);
  digitalWrite(LED_YELLOW, LOW);
  digitalWrite(LED_GREEN, LOW);
}

void loop() {
  digitalWrite(LED_RED, HIGH);
  delay(1000);
  digitalWrite(LED_RED, LOW);

  digitalWrite(LED_YELLOW, HIGH);
  delay(1000);
  digitalWrite(LED_YELLOW, LOW);

  digitalWrite(LED_GREEN, HIGH);
  delay(1000);
  digitalWrite(LED_GREEN, LOW);
}

#----------------------POTENCJOMETR-----------------------

#define LED_RED 12
#define LED_YELLOW 11
#define LED_GREEN 10

#define POTENCJOMETR A0

void turnAllLedsOff() {
  digitalWrite(LED_RED, LOW);
  digitalWrite(LED_YELLOW, LOW);
  digitalWrite(LED_GREEN, LOW);
}

int val;


void setup() {
  Serial.begin(9600);

  pinMode(LED_RED, OUTPUT);
  pinMode(LED_YELLOW, OUTPUT);
  pinMode(LED_GREEN, OUTPUT);

  digitalWrite(LED_RED, LOW);
  digitalWrite(LED_YELLOW, LOW);
  digitalWrite(LED_GREEN, LOW);
}

void loop() {
  val = analogRead(POTENCJOMETR);
  Serial.println(val);
  turnAllLedsOff();

  if (val < 330) {
    digitalWrite(LED_RED, HIGH);
  } else if (val > 660) {
    digitalWrite(LED_GREEN, HIGH);
  } else {
    digitalWrite(LED_YELLOW, HIGH);
  }

}

#----------------------KLASA SELECTOR----------------------

                0                     val       1023
intervals = 2   |               |      X         |            ->  1
                        0                1

                0                               1023
intervals = 4   |       |       |      X |       |            ->  2
                    0       1       2       3

#----------------------------------------------------------

#define LED_RED 12
#define LED_YELLOW 11
#define LED_GREEN 10

#define POTENCJOMETR A0

void turnAllLedsOff() {
  digitalWrite(LED_RED, LOW);
  digitalWrite(LED_YELLOW, LOW);
  digitalWrite(LED_GREEN, LOW);
}

class Selector {
private:
  const int intervals;
  int currentState;
  int pin;
public:
  Selector(int pin, const int intervals):intervals(intervals) {
    this->pin = pin;
  }
  int getValue() {
    int intervalLength = 1023/intervals+1;
    int valA = analogRead(pin);
    int val = valA / intervalLength;
    return val;
  }
};


Selector s1(A0, 3);

void setup() {
  Serial.begin(9600);

  pinMode(LED_RED, OUTPUT);
  pinMode(LED_YELLOW, OUTPUT);
  pinMode(LED_GREEN, OUTPUT);

  digitalWrite(LED_RED, LOW);
  digitalWrite(LED_YELLOW, LOW);
  digitalWrite(LED_GREEN, LOW);
}

void loop() {
  turnAllLedsOff();

  switch(s1.getValue()) {
    case 0:
      digitalWrite(LED_RED, HIGH);
      break;
    case 1:
      digitalWrite(LED_YELLOW, HIGH);
      break;
    case 2:
    digitalWrite(LED_GREEN, HIGH);
      break;
  }

  delay(100);
}

#----------------------------------------------------------

#define LED_RED 12
#define LED_YELLOW 11
#define LED_GREEN 10

#define POTENCJOMETR A0

void turnAllLedsOff() {
  digitalWrite(LED_RED, LOW);
  digitalWrite(LED_YELLOW, LOW);
  digitalWrite(LED_GREEN, LOW);
}

class Selector {
private:
  const int intervals;
  int intervalLength;
  int previousState;
  int currentState;
  int pin;
  bool isNewF;
public:
  Selector(int pin, const int intervals):intervals(intervals) {
    this->pin = pin;
    previousState = -1;
    intervalLength = 1023/intervals+1;
  }
  
  int getValue() {
    return currentState;
  }

  void update() {
    int valA = analogRead(pin);
    currentState = valA / intervalLength;

    if (currentState != previousState) {
      previousState = currentState;
      isNewF = true;
    } else {
      isNewF = false;
    }
  }

  bool isNew() {
    return isNewF;
  }

};


Selector s1(A0, 3);

void setup() {
  Serial.begin(9600);

  pinMode(LED_RED, OUTPUT);
  pinMode(LED_YELLOW, OUTPUT);
  pinMode(LED_GREEN, OUTPUT);

  digitalWrite(LED_RED, LOW);
  digitalWrite(LED_YELLOW, LOW);
  digitalWrite(LED_GREEN, LOW);
}

void loop() {
  s1.update();

  if (s1.isNew()) {
    turnAllLedsOff();

    switch(s1.getValue()) {
      case 0:
        digitalWrite(LED_RED, HIGH);
        break;
      case 1:
        digitalWrite(LED_YELLOW, HIGH);
        break;
      case 2:
      digitalWrite(LED_GREEN, HIGH);
        break;
    }
  }
  
  delay(100);
}

#----------------------------------------------------------

#define LED_RED 12
#define LED_YELLOW 11
#define LED_GREEN 10

#define POTENCJOMETR A0

void turnAllLedsOff() {
  digitalWrite(LED_RED, LOW);
  digitalWrite(LED_YELLOW, LOW);
  digitalWrite(LED_GREEN, LOW);
}

void fLedRed() {
  turnAllLedsOff();
  digitalWrite(LED_RED, HIGH);
}

void fLedYellow() {
  turnAllLedsOff();
  digitalWrite(LED_YELLOW, HIGH);
}

void fLedGreen() {
  turnAllLedsOff();
  digitalWrite(LED_GREEN, HIGH);
}

class Selector {
private:
  const int intervals;
  int intervalLength;
  int previousState;
  int currentState;
  int pin;
  bool isNewF;
  void (*action[3]) (void) = {fLedRed, fLedYellow, fLedGreen};
public:
  Selector(int pin, const int intervals):intervals(intervals) {
    this->pin = pin;
    previousState = -1;
    intervalLength = 1023/intervals+1;
  }
  
  int getValue() {
    return currentState;
  }

  void update() {
    int valA = analogRead(pin);
    currentState = valA / intervalLength;

    if (currentState != previousState) {
      previousState = currentState;
      isNewF = true;
      action[currentState]();
    } else {
      isNewF = false;
    }
  }

  bool isNew() {
    return isNewF;
  }

};


Selector s1(A0, 3);

void setup() {
  Serial.begin(9600);

  pinMode(LED_RED, OUTPUT);
  pinMode(LED_YELLOW, OUTPUT);
  pinMode(LED_GREEN, OUTPUT);

  digitalWrite(LED_RED, LOW);
  digitalWrite(LED_YELLOW, LOW);
  digitalWrite(LED_GREEN, LOW);
}

void loop() {
  s1.update();
  delay(100);
}

#----------------------------------------------------------

#define LED_RED 12
#define LED_YELLOW 11
#define LED_GREEN 10

#define POTENCJOMETR A0

void turnAllLedsOff() {
  digitalWrite(LED_RED, LOW);
  digitalWrite(LED_YELLOW, LOW);
  digitalWrite(LED_GREEN, LOW);
}

void fLedRed() {
  turnAllLedsOff();
  digitalWrite(LED_RED, HIGH);
}

void fLedYellow() {
  turnAllLedsOff();
  digitalWrite(LED_YELLOW, HIGH);
}

void fLedGreen() {
  turnAllLedsOff();
  digitalWrite(LED_GREEN, HIGH);
}

typedef void(*action) (void);

class Selector {
private:
  const int intervals;
  int intervalLength;
  int previousState;
  int currentState;
  int pin;
  bool isNewF;
  action *actions;    //void (**action) (void);    // void (*action[]) (void);
public:
  Selector(int pin, const int intervals):intervals(intervals) {
    this->pin = pin;
    previousState = -1;
    intervalLength = 1023/intervals+1;
    actions = new action[intervals];
  }
  
  ~Selector() {
    delete [] actions;
  }

  int getValue() {
    return currentState;
  }

  void addAction(action act, int idx) {    // takie funkcje nazywane są 'callback'
    actions[idx] = act;
  }

  void update() {
    int valA = analogRead(pin);
    currentState = valA / intervalLength;

    if (currentState != previousState) {
      previousState = currentState;
      isNewF = true;
      actions[currentState]();
    } else {
      isNewF = false;
    }
  }

  bool isNew() {
    return isNewF;
  }

};


Selector s1(A0, 3);

void setup() {
  Serial.begin(9600);

  pinMode(LED_RED, OUTPUT);
  pinMode(LED_YELLOW, OUTPUT);
  pinMode(LED_GREEN, OUTPUT);

  digitalWrite(LED_RED, LOW);
  digitalWrite(LED_YELLOW, LOW);
  digitalWrite(LED_GREEN, LOW);

  turnAllLedsOff();

  s1.addAction(fLedRed, 0);
  s1.addAction(fLedYellow, 1);
  s1.addAction(fLedGreen, 2);
}

void loop() {
  s1.update();

  delay(100);
}

#------------------------------------------------------------------------------------------------------------------------------------------------------

#------------------------PRZYCISK--------------------------

#define PIN_BUTTON 4

void setup() {
  Serial.begin(9600);
  pinMode(PIN_BUTTON, INPUT);
}

void action() {
  Serial.print("Button pressed ");
  Serial.println(millis());
}

void loop() {
  if (digitalRead(PIN_BUTTON) == HIGH) {
    delay(20);
    action();
    while (digitalRead(PIN_BUTTON) == HIGH); 
    delay(20);
  }
}
