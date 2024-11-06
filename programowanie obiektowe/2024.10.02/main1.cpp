#include <iostream>
#include <stdio.h>
#include <string.h>

class Product
{
    public:
    Product(const char *_name,
            unsigned int price)
    {
        count++;
        //Product::count++;
        
        std::cout << "Konstruktor: Alokujemy pamięć dla obiektu " << count << "\n";
        this->name = new char[strlen(_name)+1];
        sprintf(this->name, "%s", _name);
    }

    ~Product()
    {
        std::cout << "Destruktor: Zwalniamy pamięc dla obiektu " << count << "\n";
        delete [] name;
    }

    const char* getName()
    {
        return this->name;
    }
    
    private:
        char *name;
        static size_t count;
};

size_t Product::count = 0;

int main()
{
    for(int i=0; i < 10; i++) 
    {
        Product laptop("Dell", 1234);    
    }
    while(1);
    std::cout << "Test" << std::endl;

    return 0;
}