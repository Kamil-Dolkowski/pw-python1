#include <iostream>

class Bazowa {
public:
    virtual void wirtualna() {
        std::cout << "Metoda wirtualna w klasie bazowej" << std::endl;
    };
    void normalna() {
        std::cout << "Metoda normalna w klasie bazowej" << std::endl;
    };
};

class Pochodna : public Bazowa {
public:
    void wirtualna() {
        std::cout << "Metoda wirtualna w klasie pochodnej" << std::endl;
    };
    void normalna() {
        std::cout << "Metoda normalna w klasie pochodnej" << std::endl;
    };
};



int main()
{
    Pochodna p;
    Bazowa &ref = p;

    p.wirtualna();
    p.normalna();

    ref.wirtualna();
    ref.normalna();

    return 0;
}