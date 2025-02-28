#include <iostream>

class ICommand {
public:
    ICommand() {
        std::cout << "Konstruktor ICommand" << std::endl;
    }
    virtual ~ICommand() {
        std::cout << "Destruktor ICommand" << std::endl;
    }

    virtual char getCommand() const = 0;
};

class SystemUptime : public ICommand {
public:
    SystemUptime() {
        std::cout << "Konstruktor SystemUptime" << std::endl;
    }
    ~SystemUptime() {
        std::cout << "Destruktor SystemUptime" << std::endl;
    }

    virtual char getCommand() const override { return 'U'; }
};

class SystemMemory : public ICommand {
public:
    SystemMemory() {
        std::cout << "Konstruktor SystemMemory" << std::endl;
    }
    ~SystemMemory() {
        std::cout << "Destruktor SystemMemory" << std::endl;
    }

    virtual char getCommand() const override { return 'M'; }
};


void printCommand(const ICommand *c) {
        std::cout << c->getCommand() << std::endl;
}





int main() {
    ICommand *su = new SystemUptime;
    ICommand *sm = new SystemMemory;

    printCommand(su);
    printCommand(sm);

    delete su;
    delete sm;

    return 0;
}