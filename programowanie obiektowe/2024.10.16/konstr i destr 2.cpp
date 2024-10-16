#include <iostream>

class Bazowa
{
public:
    Bazowa() {
        std::cout << "Konstruktor klasy bazowej" << std::endl;
    };
    ~Bazowa() {
        std::cout << "Destruktor klasy bazowej" << std::endl;
    };
};

class Pochodna : Bazowa
{
public:
    Pochodna() {
        std::cout << "Konstruktor klasy pochodnej" << std::endl;
    };
    ~Pochodna() {
        std::cout << "Destruktor klasy pochodnej" << std::endl;
    };
};

class Pochodna2 : Pochodna
{
public:
    Pochodna2() {
        std::cout << "Konstruktor klasy pochodnej2" << std::endl;
    };
    ~Pochodna2() {
        std::cout << "Destruktor klasy pochodnej2" << std::endl;
    };
};

int main()
{
    Pochodna2 p;

    return 0;
}




/*
Konstruktor klasy bazowej
Konstruktor klasy pochodnej
Konstruktor klasy pochodnej2
Destruktor klasy pochodnej2
Destruktor klasy pochodnej
Destruktor klasy bazowej
*/