#include <iostream>
#include <string>

class Entity {
public:
    virtual void attack(Entity &t) = 0;
    virtual void damage(unsigned int receivedDamage) = 0;
    virtual ~Entity() {}

protected:
    Entity(const std::string &_type) : type(_type) {
        id = counter;
        counter++;
    }

    std::string type;
    unsigned int id;
    static unsigned int counter;
};

unsigned int Entity::counter = 0;

class Player : public Entity {
public:
    Player(std::string _name) : Entity("player") {
        name = new std::string(_name);
    }
    Player(const Player &source) : Entity("player") {
        name = new std::string(*source.name);
        currentHp = source.currentHp;
        damageValue = source.damageValue;
    }
    Player& operator=(const Player &source) {
        delete name;
        name = new std::string(*source.name);
        currentHp = source.currentHp;
        damageValue = source.damageValue;
        return *this;
    }
    ~Player() {
        delete name;
    }

    virtual void attack(Entity &t) override {
        t.damage(damageValue);
    }
    virtual void damage(unsigned int receivedDamage) {
        currentHp -= receivedDamage;
    }
    bool isDead() const {
        if (currentHp <= 0) {
            return true;
        }
        return false;
    }

    friend std::ostream& operator<<(std::ostream &os, const Player &p);

    Player& operator+(int hpValue) {
        if (currentHp+hpValue <= maxHp) {
            currentHp+=hpValue;
        } 
        return *this;
    }
    Player& operator-(int hpValue) {
        if (currentHp-hpValue >= 0) {
            currentHp-=hpValue;
        } else {
            currentHp = 0;
        }
        return *this;
    }

private:
    std::string *name;
    const unsigned int maxHp = 100;
    int currentHp = maxHp;
    unsigned int damageValue = 10;
};

std::ostream& operator<<(std::ostream &os, const Player &p) {
    os << "type: " << p.type << std::endl; 
    os << "id: " << p.id << std::endl; 
    os << "------------------------" << std::endl;
    os << "name: " << *p.name << std::endl; 
    os << "max hp: " << p.maxHp << std::endl;
    os << "hp: " << p.currentHp << std::endl; 
    os << "damage value: " << p.damageValue << std::endl; 
    return os;
};


class Zombie : public Entity {
public:
    Zombie() : Entity("zombie") {

    }
    ~Zombie() {
        // std::cout << "Dekonstruktor" << std::endl;
    }

    virtual void attack(Entity &t) {
        t.damage(damageValue);
    }
    virtual void damage(unsigned int receivedDamage) {
        currentHp -= receivedDamage;
    }
    bool isDead() {
        if (currentHp <= 0) {
            return true;
        }
        return false;
    }

    friend std::ostream& operator<<(std::ostream &os, const Zombie &z);

private:
    const unsigned int maxHp = 100;
    unsigned int currentHp = maxHp;
    unsigned int damageValue = 5;
};

std::ostream& operator<<(std::ostream &os, const Zombie &z) {
    os << "type: " << z.type << std::endl; 
    os << "id: " << z.id << std::endl; 
    os << "------------------------" << std::endl;
    os << "max hp: " << z.maxHp << std::endl;
    os << "hp: " << z.currentHp << std::endl; 
    os << "damage value: " << z.damageValue << std::endl; 
    return os;
};


int main() {
    Player p("Kamil");
    Player p1("Kuba");
    Player p2(p1);

    Zombie z;

    // ==Konstruktor kopiujący:==
    // p1.print();
    // p2.print();

    // ==Operator przypisania (=):==
    // std::cout << p << std::endl;
    // p=p1;
    // std::cout << p1 << std::endl;
    
    // ==Przeciążenie operatora (-):==
    // std::cout << p << std::endl;
    // p-110;
    // std::cout << p << std::endl;

    // ==Atakowanie:==
    // std::cout << z << std::endl;
    // p.attack(z);
    // std::cout << z << std::endl;


    // Zombie *e[2] = {new Zombie, new Zombie};
    // std::cout << *e[1] << std::endl;
    // delete e[1];

    return 0;
}