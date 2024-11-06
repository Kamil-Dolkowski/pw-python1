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
protected:
    unsigned int id;
    unsigned int salary;
};




int main()
{
    Employee e(1234567890, "Adam", "Kowalski", 123, 6666);

    return 0;
}