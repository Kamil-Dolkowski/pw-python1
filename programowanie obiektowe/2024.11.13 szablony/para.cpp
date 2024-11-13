#include <iostream>
#include <string>
#include <cstdlib>
#include <ctime>

template <typename T1, typename T2>
class Pair {
public:
    Pair(const T1 &_x, const T2 &_y) : x(_x), y(_y) {}
    T1 first() const { return x; }
    T2 second() const { return y; }

    void first(const T1 &_x) { x = _x; }
    void second(const T2 &_y) { y = _y; }

private:
    T1 x;
    T2 y;
};

Pair<int, std::string> doSomething() {
    int v = rand() % 3;

    switch (v)
    {
        case 0:
            return Pair<int, std::string>(v, "no error");
        case 1:
            return Pair<int, std::string>(v, "invalid read");
        case 2: 
            return Pair<int, std::string>(v, "invalid write");
        default:
            return Pair<int, std::string>(v, "unknown error");
    }
}





int main() {
    srand(time(NULL));

    for (int i=0; i<10; i++) {
        const Pair<int, std::string> error = doSomething();
        std::cout << error.second() << " (" << error.first() << ")" << std::endl;
    }

    std::cout << "===================" << std::endl;

    Pair<int, std::string> example(123, "changeme");

    std::cout << example.second() << " (" << example.first() << ")" << std::endl;

    example.first(321);
    example.second("changed");

    std::cout << example.second() << " (" << example.first() << ")" << std::endl;

    return 0;
}