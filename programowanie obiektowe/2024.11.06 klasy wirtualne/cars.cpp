#include <iostream>

class Car {
public:
    void drive() { std::cout << "Drive" << vin << std::endl; }
    void setVin(const std::string &_vin) { this->vin = _vin; }
private:
    std::string manufacturer;
    std::string model;
    std::string vin;
};

class PetrolCar : public Car {

};

class ElectricCar : public Car {

};

class HybridCar : public PetrolCar, public ElectricCar {

};




int main() {
    HybridCar hc;
    PetrolCar &pc = static_cast<PetrolCar&>(hc);
    ElectricCar &ec = static_cast<ElectricCar&>(hc);

    // hc.drive(); // nie działa
    pc.drive();
    ec.drive();

    pc.setVin("12345");
    ec.setVin("123456778899");

    pc.drive();
    ec.drive();
    
    return 0;
}