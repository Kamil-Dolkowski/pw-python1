#include <iostream>

class Car {
public:
    Car(const std::string &_man, const std::string  &_mod, const std::string &_vin)
        : manufacturer(_man), model(_mod), vin(_vin) {}
    void drive() { std::cout << "Drive " << vin << std::endl; }
    void setVin(const std::string &_vin) { this->vin = _vin; }
protected:
    Car() {};
private:
    std::string manufacturer;
    std::string model;
    std::string vin;
};

class PetrolCar : virtual public Car {
public:
    PetrolCar(const std::string &_man, const std::string  &_mod, const std::string &_vin, int &_cap)
        : Car(_man, _mod, _vin), fuelCapasity(_cap) {}
protected:
    PetrolCar() {};
private:
    int fuelCapasity;
};

class ElectricCar : virtual public Car {
public:
    ElectricCar(const std::string &_man, const std::string  &_mod, const std::string &_vin, int _cap)
        : Car(_man, _mod, _vin), batteryCapasity(_cap) {}
protected:
    ElectricCar() {};
private:
    int batteryCapasity;
};

class HybridCar : public PetrolCar, public ElectricCar {
public:
    HybridCar(const std::string &_man, const std::string  &_mod, const std::string &_vin, int _fuelCapasity, int _batteryCapasity)
        : PetrolCar("to","jest","nadpisywane", _fuelCapasity), ElectricCar("przez","Car","(_man, _mod, _vin)", _batteryCapasity), Car(_man, _mod, _vin) {}
};




int main() {
    HybridCar hc("manufacture","model","12345", 60, 100);

    hc.drive();
    
    return 0;
}