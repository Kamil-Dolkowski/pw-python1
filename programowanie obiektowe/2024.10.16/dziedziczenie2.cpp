#include <iostream>
#include <string>

class Person {
public:
    Person(unsigned int _pesel,
           const std::string &_name,
           const std::string &_surname)
        : pesel(_pesel), name(_name), surname(_surname) {};  
protected:
    unsigned int pesel;
    std::string name;
    std::string surname;
};


class Employee : public Person {
public:
    Employee(unsigned int _pesel,
             const std::string &_name,
             const std::string &_surname,
             unsigned int _id,
             unsigned int _salary) 
        : Person(_pesel, _name, _surname),
        id(_id), salary(_salary) {};
        
    Employee(const Person &_p,
             unsigned int _id,
             unsigned int _salary) 
        : Person(_p),
        id(_id), salary(_salary) {};
protected:
    unsigned int id;
    unsigned int salary;
};


/*
class Programmer : public Employee {
public:
    Programmer(const Employee &_e)
        : Employee(_e) {};
    void program();
    void debug();
    void writeDocumentation();
};

class Tester : public Employee {
 public:
    Tester(const Employee &_e)
        : Employee(_e) {};
    void test();
    void sleep();
    void writeReport(); 
};

class Manager : public Employee {
    
};
*/

int main()
{
    Employee e(1234567890, "Adam", "Kowalski", 123, 6666);
    
    Person p(1234567890, "Adam", "Kowalski");
    Employee e2(p, 123, 6666);

    return 0;
}