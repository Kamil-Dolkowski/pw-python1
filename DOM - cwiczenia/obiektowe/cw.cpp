#include <iostream>
#include <string>

class Computer {
public:
    Computer(int _ram, int _id) : ram(_ram), id(_id) {}
    ~Computer() {}
    
    Computer(const Computer &source) {
        ram = source.ram;
        id = source.id;
    }
    
    Computer& operator=(Computer &source) {
        ram = source.ram;
        id = source.id;
        return *this;
    }
    
    int getRam() { return ram; }
private:
    int ram;
    int id;
};

class Employee {
public:
    virtual void print() = 0;
    void printT() {
        std::cout << "type: "<< type << ", id: "<< personId << std::endl;
    };
protected:
    Employee(std::string _type) : type(_type) {
        personId = counter;
        counter++;
    }
private:
    std::string type;
    int personId;
    static int counter;
};

int Employee::counter = 1;

class Programmer : public Employee {
public:
    Programmer(std::string _name, Computer &_c) : Employee("programmer"), name(_name), c(_c) {}
    ~Programmer() {}
    
    Programmer(const Programmer &source) : Employee("programmer"), name(source.name), c(source.c) {}
    
    void print() {
        std::cout << name << ", " << c.getRam() << "GB" << std::endl;
    }
    friend std::ostream& operator<<(std::ostream &os, Programmer &p);
    
private:
    Computer &c;
    std::string name;
};

std::ostream& operator<<(std::ostream &os, Programmer &p) {
    os << p.name << ", " << p.c.getRam() << "GB" << std::endl;
    return os;
}


int main()
{
    Computer c(8, 1), c1(10,1);
    Programmer p("Kamil",c), p1("Wera",c1);
    
    std::cout << p << std::endl;
    std::cout << p1 << std::endl;
    
    Programmer p2(p);
    
    std::cout << p2 << std::endl;
    
    p2.printT();
    
    
    //p.print();
    //std::cout << p << std::endl;

    //c = c1;
    //std::cout << c.getRam();

    return 0;
}