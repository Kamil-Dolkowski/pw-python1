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
        
        this->name = new char[strlen(_name)+1];
        sprintf(this->name, "%s", _name);
        this->id = count;
        
        std::cout << "Konstruktor: Alokujemy pamięć dla obiektu " << this->name << " " << count << "\n";
    }

    ~Product()
    {
        std::cout << "Destruktor: Zwalniamy pamięc dla obiektu " << this->name << " " << count << "\n";
        delete [] name;
    }

    const char* getName()
    {
        return this->name;
    }
    
    private:
        char *name;
        static size_t count;
        size_t id;
};

size_t Product::count = 0;

Product *laptop0 = new Product("DellStatyczny", 1234);

int main()
{
    Product laptop1("DellMain", 1234);    
    {
        Product laptop2("DellMainInternal1", 1234);  
        Product laptop3("DellMainInternal2", 1234);
    } 

    Product *laptop4 = new Product("DellDynamiczny", 1234);
    return 0;
}