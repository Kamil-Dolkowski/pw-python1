#include <iostream>
#include <typeinfo>

template <typename T>
void f(T val) {
    std::cout << typeid(T).name() << ": " << val << std::endl;
}

void f(int val) {}
void f(double val) {}




int main() {
    int i = 0;
    double j = 1.0;
    f<int>(i);
    f<double>(j);

    return 0;
}