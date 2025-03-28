#include <iostream>

class Foo {
public:
    Foo(int x) : x(x){
        std::cout << "Foo" << std::endl;
    }

    ~Foo(){
        std::cout << "~Foo" << std::endl;
    }
    int x;
};

int main() {
    Foo f = Foo(123);

    int x=2, y=0;
    int z=x/y;

    std::cout << x/y << std::endl;
    return 0;
}