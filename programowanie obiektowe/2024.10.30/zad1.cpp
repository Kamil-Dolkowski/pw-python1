#include <iostream>
#include <cstring>
#include <cstdlib>


class Item
{
public:
    const std::string& getName() { return name; }   // do implementacji
    unsigned int getID() { return id; }           // do implementacji 
    static unsigned int getCount() { return count; } // do implementacji 

protected:
    Item(const std::string &_name) : name(_name) {
        count++;
        id = count;
    };  // do implementacji 

private:
    /* Dodaj odpowiednie trzy zmienne,
       dwie dla danego obiektu i jedną dla całej klasy */
    std::string name;
    unsigned int id;
    static unsigned int count;
};

unsigned int Item::count = 0;


class Weapon : public Item
{
public:
    Weapon(const std::string &name) : Item(name) {};
    virtual ~Weapon() {};
    virtual float getDamage() = 0;
    virtual bool isBroken() = 0;
    virtual void use() = 0;
    virtual void repair() = 0;
    void print() {
        if (isBroken()) {
            std::cout << "Weapon " << getName() << " " << getID() << " cannot be used, as it is broken." << std::endl;
        } else {
            std::cout << "Weapon " << getName() << " " << getID() << " results in " << getDamage() << " of damage points." << std::endl;
        }
    }; // do implementacji 
};


class Sword : public Weapon
{
public:
    Sword() : Weapon("Sword") {};
    ~Sword() { std::cout << "Sword object is being destroyed..." << std::endl; };
    virtual float getDamage() override { return baseDamage * sharpness; }; // do implementacji 
    virtual bool isBroken() override { 
        if (sharpness <= 0) {
            return true;
        } else {
            return false;
        }
    };   // do implementacji 
    virtual void use() override {
        print();
        sharpness-=0.1;
    };    // do implementacji 
    virtual void repair() override {
        if (sharpness*1.1 <= 1.0) {
            sharpness*=1.1;
        } else {
            sharpness=1.0;
        }
    };     // do implementacji 

private:
    const float baseDamage = 8.125;
    float sharpness = 0.5;
};


class Hammer : public Weapon
{
public:
    Hammer() : Weapon("Hammer") {};
    ~Hammer() { std::cout << "Hammer object is being destroyed..." << std::endl; };
    virtual float getDamage() override {
        if (durability > 0) {
            return damage;
        } else {
            return 0;
        }
    } // do implementacji 
    virtual bool isBroken() override {
        if(durability == 0) {
            return true;
        } else {
            return false;
        }
    }   // do implementacji 
    virtual void use() override {
        print();
        durability--;
    }        // do implementacji
    virtual void repair() override {
        durability = defaultDurability;
        // std::cout << "Repair" << std::endl;
    }    // do implementacji

private:
    const unsigned int defaultDurability = 4;
    const float damage = 3.5;
    unsigned int durability = defaultDurability;
};






int main() {
    srand(time(NULL));

    Weapon *equipment[4] = {
        new Sword,
        new Hammer,
        new Sword,
        new Hammer
    };


// for(int i=0; i<)

    while(!equipment[0]->isBroken() || !equipment[1]->isBroken() || !equipment[2]->isBroken() || !equipment[3]->isBroken()) {
        for(int i=0; i<4; i++){
            equipment[i]->use();
            if(!equipment[i]->isBroken()) {
                // equipment[i]->use();
                /* przykład, może trzeba zwiększyć wartość 10 */
                bool shouldRepair = (rand() % 10) == 0; 
                if (shouldRepair)
                {
                equipment[i]->repair();
                }
            }
        }
        std::cout << std::endl;
    }
    
    std::cout << "==========================================\n" << std::endl;
 
    for(int i=0; i<4; i++){
        delete equipment[i];
    }

    return 0;
}






// SHORTHAND IF
// return warunek ? 2 : 3;


// Wychwytuje błąd składni: if(x = 0)   , zamiast if(x == 0)

// $ cd "/home/u334531/Pulpit/Repozytorium/programowanie obiektowe/2024.10.30/" && g++ zad1.cpp -Wall -Wextra -pedantic

// if(durability = 0) {
//    ~~~~~~~~~~~^~~