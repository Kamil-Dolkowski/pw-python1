# Przeładowanie operatorów. Definiowanie operatorów dla własnych typów.

przeładowanie operatorów -> umożliwia dostosowanie sposobu działania standardowych operatorów (takich jak +,-,*,/, itd.) do własnych typów danych
rozszerza możliwości


aby przeładować operatory -> zdefiniować funkcje
-jako metode klasy
-jako funkcję globalną

#------------------------------------------------

#include <iostream>

class Vector {
public:
    float x, y;

    Vector(float x, float y) : x(x), y(y) {}

    // Przeładowanie operatora + jako metoda klasy
    Vector operator+(const Vector& other) const {
        return Vector(x + other.x, y + other.y);
    }
};

int main() {
    Vector v1(1.0, 2.0), v2(3.0, 4.0);
    Vector v3 = v1 + v2; // Używamy przeładowanego operatora +
    
    std::cout << "v3: (" << v3.x << ", " << v3.y << ")" << std::endl;
    return 0;
}


#------------------------------------------------

#include <numeric> // Dla std::gcd (C++17)
#include <iostream>

class Fraction {
private:
    int numerator, denominator;
    
public:
    Fraction(int numerator, int denominator) : numerator(numerator), denominator(denominator) {
        // Normalizacja ułamka
        int gcd = std::gcd(numerator, denominator);
        this->numerator /= gcd;
        this->denominator /= gcd;
    }
    
    // Przeładowanie operatora *
    Fraction operator*(const Fraction& other) const {
        return Fraction(numerator * other.numerator, denominator * other.denominator);
    }
    
    // Przeładowanie operatora ==
    bool operator==(const Fraction& other) const {
        return numerator == other.numerator && denominator == other.denominator;
    }
};

int main() {
    Fraction f1(1,2), f2(2,3);
    Fraction result = f1 * f2;
    std::cout << "Result: " << result.numerator << "/" << result.denominator << std::endl;
    
    Fraction f3(2,4);
    if (f1 == f3) {
        std::cout << "f1 and f3 are equal." << std::endl;
    } else {
        std::cout << "f1 and f3 are not equal." << std::endl;
    }
    
    return 0;
}

#------------------------------------------TECHNIKA RAII, STL-----------------------------------------------

#-------------------

Technika RAII - zarządzanie zasobami przez obiekty



// Przykład zarządzania pamięcią
int* ptr = new int(10);

delete ptr; // Pamięć zwalniana ręcznie


#-------------------

RAII:
-Inicjalizacja
-Użycie
-Dealokacja
-Przykład

std::unique_ptr<int> ptr = std::make_unique<int>(10);

#-------------------

std::vector<int> vec = {1,2,3}



std::unique_ptr<int> ptr = std::make_unique<int>(10);



std::mutex mtx;
{
    std::lock_guard::mutex ..... ??
}

#-------------------

Menedżer zasobów plików
Klasa: FileResourceManager - zarządza zasobami plików


Pułapka połączeń do bazy danych
klasa: DatabaseConnectionPool - zarządza połączeniami do bazy danych, zapewniając ich właściwe zwolnienie

#-------------------

RAII:
-zapobiega wyciekom zasobów, zapewnia bezpieczeństwo wyjątków, czytelniejszy kod
-używane w stl

#-----------------------------------------DZIEDZICZENIE, POLIMORFIZM-----------------------------------------------

#----------------DZIEDZICZENIE----------------

dziedziczenie - tworzenie nowych klas na podst. istniejących klas

#---------------------

class Animal {
public:
    void eat() {
        cout << "Animal is eating ..." << endl;
    }
};

class Dog : public Animal {
public:
    void bark() {
        cout << "Dog is barking ..." << endl;
    }
};

int main() {
    Dog myDog;
    myDog.eat(); // Dziedziczenie metody eat() z klasy Animal
    myDog.bark();
    
    return 0;
}



#-----------------POLIMORFIZM-----------------

polimorfizm - zdolnośc obiektu do przyjmowania wielu form lub postaci

metody wirtualne - przesłonięte (nadpisane) w klasach pochodnych

#--------------------

#include <iostream>

class Shape {
public:
    virtual void draw() {
        std::cout << "Drawing shape ..." << std::endl;
    }
};

class Circle : public Shape {
public:
    void draw() override {
        std::cout << "Drawing circle ..." << std::endl;
    }
};

int main() {
    Shape* shapePtr = new Circle();
    shapePtr->draw(); // Wywołanie polimorficznej metody draw()
    delete shapePtr;
    
    return 0;
}


#-----------------

** 
using namespace std;  -> by nie pisać 'std::cout' , tylko 'cout'


#-----------------

Best Practise:
-virtual przy definiowaniu metody, które mają być przesłonięte w klasach pochodnych
-override przy przesyłaniu metod


#--------------------------------------WSKAŹNIKI---------------------------------------------

-dynamiczne alokowanie pamięci
-tradycyjne wskaźniki wymagają ręcznego zwalniania pamięci


int* ptr = new int(5);

*ptr = 10;


#--------WSKAŹNIK UNIQUE_PTR---------

unique_ptr
-gdy wychodzi poza zakres zostaje automatycznie zwolniony


#include <memory>
std::unique_ptr
...
??


#--------WSKAŹNIK SHARED_PTR---------

-współdzielenie zasobów
-automatyczne zwalnianie pamięci
-bezpieczeństwo


std::shared_ptr<int> ptr1 = std::make_shared<int>(5);

std::shared_ptr ... ??

#--------WSKAŹNIK WEAK_PTR---------

-do obserwowania shared_ptr 
-zapobiega cyklicznym zależnościom między obiektami


std::share_ptr<int> ptr1 = std::make_shared<int>(5);

std::weak_ptr<int> ptr2 = ptr1;


#----------------------------------

Wady:
-unique_ptr - brak możliwości współdzielenia
-shared_ptr - związany z licznikiem referencji
-weak_ptr - konieczność konwersji shared_ptr przed uzyciem


Zalety:
-unique_ptr - własność wyłącznie jednego wskaźnika
-shared_ptr - współdzielenie zasobów między wieloma wskaźnikami
-weak_ptr - ??
