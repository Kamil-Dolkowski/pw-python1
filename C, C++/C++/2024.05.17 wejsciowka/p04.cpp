#include <iostream>
#include <cstdlib>
using namespace std;

class A {
private:
  int x;
  int y;
public:
  A();
  int getX() {
    return x;
  }
  int getY() {
    return y;
  }
};

class B {
private:
  int z;
  //A aB;
public:
  int v;
  A aB;

  B();
  void info() {
    cout << "z=" << z << endl;
    cout << "v=" << v << endl;
    cout << "aB.x=" << aB.getX() << endl;
    cout << "aB.y=" << aB.getY() << endl;
  }
};

// Konstruktory

A::A() {
  x = 1;
  y = 2;
}

B::B() {
  z = 3;
  v = 4;
}





int main() {
  A a;
  B b;
  B * pb;

  pb = &b;

  pb -> info();


  return EXIT_SUCCESS;
}
