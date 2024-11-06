#include <iostream>
#include <string>

class Entity {
public:
    // virtual void attack() = 0;
    virtual void damage(unsigned int receivedDamage) = 0;
protected:
    Entity(const std::string &_type) : type(_type) {
        counter++;
    }
private:
    std::string type;
    static unsigned int counter;
};

unsigned int Entity::counter = 0;

class Player : public Entity {
public:
    Player(std::string _name) : Entity("player") {
        name = new std::string(_name);
    }
    Player(const Player &source) : Entity("player") {
        // name = new std::string(source.name);
        currentHp = source.currentHp;
        damageValue = source.damageValue;
    }
    Player& operator=(const Player &source) {
        delete name;
        // name = new std::string(source.name);
        currentHp = source.currentHp;
        damageValue = source.damageValue;
        return *this;
    }
    virtual ~Player() {
        delete name;
    }
    // virtual void attack() override {

    // }
    virtual void damage(unsigned int receivedDamage) {
        currentHp -= receivedDamage;
    }
    bool isDead() const {
        if (currentHp <= 0) {
            return true;
        }
        return false;
    }
private:
    std::string *name;
    const unsigned int maxHp = 100;
    unsigned int currentHp = maxHp;
    unsigned int damageValue = 10;
};

/*
class Zombie : public Entity {
public:
    Zombie() : Entity("zombie") {

    }
    ~Zombie() {}
    virtual void attack() {

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
private:
    const unsigned int maxHp = 100;
    unsigned int currentHp = maxHp;
    unsigned int damageValue = 5;
};
*/


int main() {
    Player p("Kamil");
    Player p1("Kuba");

    p=p1;


    return 0;
}