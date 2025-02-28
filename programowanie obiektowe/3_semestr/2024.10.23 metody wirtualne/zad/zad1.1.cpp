#include <iostream>
#include <string>


class Computer {
private:
    std::string manufacturer;
    std::string model;
    std::string cpu;
    unsigned int ramMemory; // [GB]
    unsigned int diskMemory; // [GB]
public:
    Computer(std::string _manufacturer, 
            std::string _model, 
            std::string _cpu, 
            unsigned int _ramMemory, 
            unsigned int _diskMemory) 
            : manufacturer(_manufacturer), 
            model(_model), cpu(_cpu), 
            ramMemory(_ramMemory), 
            diskMemory(_diskMemory) {};
    void print() const {
        std::cout << manufacturer << " " << model << " / " << cpu << " / " << ramMemory << " GB RAM / " << diskMemory << " GB DISK" << std::endl;
    };
    void setManufacturer(std::string new_manufacturer) { manufacturer = new_manufacturer; };
    void setModel(std::string new_model) { model = new_model; };
    void setCpu(std::string new_cpu) { cpu = new_cpu;};
    void setRamMemory(unsigned int new_ramMemory) { ramMemory = new_ramMemory; };
    void setDiskMemory(unsigned int new_diskMemory) { diskMemory = new_diskMemory; };
};

class Laptop : public Computer {
private:
    unsigned int screen; // [inches]
    unsigned int battery; // [Wh]
public:
    Laptop(std::string _manufacturer, 
            std::string _model, 
            std::string _cpu, 
            unsigned int _ramMemory, 
            unsigned int _diskMemory, 
            unsigned int _screen, 
            unsigned int _battery) 
            : Computer(_manufacturer, _model, _cpu, _ramMemory, _diskMemory), 
            screen(_screen), battery(_battery) {} ;
    Laptop(const Computer &c, 
            unsigned int _screen, 
            unsigned int _battery) 
            : Computer(c), 
            screen(_screen), battery(_battery) {} ;
    void print() const {
        Computer::print();
        std::cout << screen << "\" / " << battery << " Wh" << std::endl;
    };
    void setScreen(unsigned int new_screen) { screen = new_screen; };
    void setBattery(unsigned int new_battery) { battery = new_battery; };
};

class Desktop : public Computer {
protected:
    std::string formFactor;
    std::string psu;
public:
    Desktop(std::string _manufacturer, 
            std::string _model, 
            std::string _cpu, 
            unsigned int _ramMemory, 
            unsigned int _diskMemory, 
            std::string _formFactor, 
            std::string _psu) 
            : Computer(_manufacturer, _model, _cpu, _ramMemory, _diskMemory), 
            formFactor(_formFactor), psu(_psu) {};
    Desktop(const Computer &c, 
            std::string _formFactor, 
            std::string _psu) 
            : Computer(c), 
            formFactor(_formFactor), psu(_psu) {};
    void print() const {
        Computer::print();
        std::cout << formFactor << " / " << psu << std::endl;
    };
    void setFormFactor(std::string new_formFactor) { formFactor = new_formFactor; };
    void setPsu(std::string new_psu) { psu = new_psu; };
};

void show(const Computer &computer) {
    computer.print();
}



int main() {
    Computer c("SNSV", "Longitude 555", "i11-1234X", 16, 512);
    Laptop l(c, 15, 50);
    Desktop d("Optimus", "PW-000", "i13-4321X", 96, 4096, "SFF", "550W 80 Plus Gold");

    std::cout << "Specyfikacja komputera:" << std::endl;
    c.print();

    std::cout << "Specyfikacja laptopa:" << std::endl;
    l.print();

    std::cout << "Specyfikacja desktopa:" << std::endl;
    d.print();
    
    std::cout << "===============================================" << std::endl;

    std::cout << "Specyfikacja komputera:" << std::endl;
    show(c);

    std::cout << "Specyfikacja laptopa:" << std::endl;
    show(l);

    std::cout << "Specyfikacja desktopa:" << std::endl;
    show(d);


    return 0;
}


//polimorfizm