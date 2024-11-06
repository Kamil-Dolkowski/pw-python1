#include <iostream>
#include <cstring>

class Person {
public:
    Person(unsigned int _pesel, const char *_name, const char *_surname) : pesel(_pesel), name(strdup(_name)), surname(strdup(_surname)) {};
    Person(const Person &source) 
    {
        pesel = source.pesel;
        name = strdup(source.name);
        surname = strdup(source.surname);
    };

    ~ Person() 
    {
        //std::cout << "destruktor name: " << name << std::endl;
        free(name);
        free(surname);
    };

    Person& operator=(const Person &source) 
    {
        pesel = source.pesel;

        if (strlen(source.name) > strlen(name)) {
            free(name);
            name = strdup(source.name);
        } else {
            strcpy(name, source.name);
        }

        if (strlen(source.surname) > strlen(surname)) {
            free(surname);
            surname = strdup(source.surname);
        } else {
            strcpy(surname, source.surname);
        }

        return *this;
    };
    
    void showParameters() 
    {
        std::cout << "pesel: " << pesel << std::endl;
        std::cout << "name: " << name << std::endl;
        std::cout << "surname: " << surname << std::endl;
    };

private:
    unsigned int pesel;
    char *name;
    char *surname;
};




int main() {
    Person p(1234567890, "Robert", "Kowalski");
    Person p2(p); /* Konstruktor kopiujący */

    /*
    p.showParameters();
    std::cout << std::endl;
    p2.showParameters();
    std::cout << std::endl;
    */

    Person p3(1234567890, "Adam", "Lewandowski");
    p = p3; /* Operator przypisania */

    //p.showParameters();

    return 0;
}


