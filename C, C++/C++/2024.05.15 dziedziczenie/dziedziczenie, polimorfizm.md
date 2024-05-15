polimorfizm (wielopostaciowość) - traktowanie obiektów pewnego rodzaju jako obiekty innego rodzaju

dziedziczenie

#----------------------------------------------------------------

#include <iostream>
using namespace std;

class A {
private:
    int x;
public:
    int y;
    void info() {
        cout << "x=" << x << endl;
        cout << "y=" << y << endl;
    }
};

class B {
private:
    int z;
public:
    int v;
    void info() {
        cout << "z=" << z << endl;
        cout << "v=" << v << endl;
    }
};



int main()
{
    A a;
    B b;
    
    a.info();
    //a.x = 1;
    a.y = 2;
    a.info();
    
    cout << "===========" << endl;
    b.info();
    //b.z = 1;
    b.v = 2;
    b.info();
    
    return 0;
}

#-----------------------class B : public A------------------------

#include <iostream>
using namespace std;

class A {
private:
    int x;
public:
    int y;
    void info() {
        cout << "x=" << x << endl;
        cout << "y=" << y << endl;
    }
    int getX() {
        return x;
    }
};

class B : public A {
private:
    int z;
public:
    int v;
    void info() {
        cout << "z=" << z << endl;
        cout << "v=" << v << endl;
        //cout << "x=" << x << endl;
        cout << "x=" << getX() << endl;
        cout << "y=" << y << endl;
    }
};



int main()
{
    A a;
    B b;
    
    a.info();
    //a.x = 1;
    a.y = 2;
    a.info();
    
    cout << "===========" << endl;
    b.info();
    //b.z = 1;
    b.v = 2;
    b.y = 3;
    b.info();
    
    return 0;
}

#-----------------------class B : private A-----------------------

#include <iostream>
using namespace std;

class A {
private:
    int x;
public:
    int y;
    void info() {
        cout << "x=" << x << endl;
        cout << "y=" << y << endl;
    }
    int getX() {
        return x;
    }
};

class B : private A {
private:
    int z;
public:
    int v;
    void info() {
        cout << "z=" << z << endl;
        cout << "v=" << v << endl;
        //cout << "x=" << x << endl;
        cout << "x=" << getX() << endl;
        cout << "y=" << y << endl;
    }
};



int main()
{
    A a;
    B b;
    
    a.info();
    //a.x = 1;
    a.y = 2;
    a.info();
    
    cout << "===========" << endl;
    b.info();
    //b.z = 1;
    b.v = 2;
    b.y = 3;
    b.info();
    
    return 0;
}

#----------------------------------------------------------------

class B : public A     ->   y jest public w B; public A idzie do public B

class B : private A    ->   y jest private w B; public A idzie do private B


w obu przypadkach private A jest w private A

#---------------------------b.A::info()--------------------------

#include <iostream>
using namespace std;

class A {
private:
    int x;
public:
    int y;
    void info() {
        cout << "Class A::info(): " << endl;
        cout << "x=" << x << endl;
        cout << "y=" << y << endl;
    }
    int getX() {
        return x;
    }
};

class B : public A {
private:
    int z;
public:
    int v;
    void info() {
        cout << "Class B::info(): " << endl;
        cout << "z=" << z << endl;
        cout << "v=" << v << endl;
        //cout << "x=" << x << endl;
        cout << "x=" << getX() << endl;
        cout << "y=" << y << endl;
    }
};



int main()
{
    A a;
    B b;
    
    a.info();
    //a.x = 1;
    a.y = 2;
    a.info();
    
    cout << "===========" << endl;
    b.info();
    //b.z = 1;
    b.v = 2;
    b.y = 3;
    b.info();
    
    b.A::info();
    
    return 0;
}

#-----------------------WSKAŹNIKI NA KLASĘ-----------------------

#include <iostream>
using namespace std;

class A {
private:
    int x;
public:
    int y;
    A() {
        x=1;
        y=2;
    }
    void info() {
        cout << "Class A::info(): " << endl;
        cout << "x=" << x << endl;
        cout << "y=" << y << endl;
    }
    int getX() {
        return x;
    }
};

class B : public A {
private:
    int z;
public:
    int v;
    B() {
        z=3;
        v=4;
    }
    void info() {
        cout << "Class B::info(): " << endl;
        cout << "z=" << z << endl;
        cout << "v=" << v << endl;
        //cout << "x=" << x << endl;
        cout << "x=" << getX() << endl;
        cout << "y=" << y << endl;
    }
};



int main()
{
    A a;
    B b;
    
    A * pa;
    B * pb;
    
    a.info();
    b.info();
    
    pa = &a;
    pb = &b;
    //pb = &a;      //nie da się
    //pa = &b;      //da się
    
    pa -> info();
    pb -> info();
    
    
    return 0;
}


#- - - - - - - - - - - - (pa = &a;  pb = &b;)

OUTPUT:

Class A::info(): 
x=1
y=2
Class B::info(): 
z=3
v=4
x=1
y=2
Class A::info(): 
x=1
y=2
Class B::info(): 
z=3
v=4
x=1
y=2


#- - - - - - - - - - - - (pa = &a;  pb = &a;)

OUTPUT:

main.cpp: In function ‘int main()’:
main.cpp:56:10: error: invalid conversion from ‘A*’ to ‘B*’ [-fpermissive]
   56 |     pb = &a;
      |          ^~
      |          |
      |          A*


#- - - - - - - - - - - - (pa = &b;  pb = &b;)

OUTPUT:

Class A::info(): 
x=1
y=2
Class B::info(): 
z=3
v=4
x=1
y=2
Class A::info(): 
x=1
y=2
Class B::info(): 
z=3
v=4
x=1
y=2


#----------------------------VIRTUAL-----------------------------

#include <iostream>
using namespace std;

class A {
private:
    int x;
public:
    int y;
    A() {
        x=1;
        y=2;
    }
    virtual void info() {
        cout << "Class A::info(): " << endl;
        cout << "x=" << x << endl;
        cout << "y=" << y << endl;
    }
    int getX() {
        return x;
    }
};

class B : public A {
private:
    int z;
public:
    int v;
    B() {
        z=3;
        v=4;
    }
    void info() {
        cout << "Class B::info(): " << endl;
        cout << "z=" << z << endl;
        cout << "v=" << v << endl;
        //cout << "x=" << x << endl;
        cout << "x=" << getX() << endl;
        cout << "y=" << y << endl;
    }
};



int main()
{
    A a;
    B b;
    
    A * pa;
    B * pb;
    
    a.info();
    b.info();
    
    pa = &b;
    pb = &b;
    
    pa -> info();
    pb -> info();
    
    return 0;
}

#- - - - - - - - - - - - 

OUTPUT:

Class A::info(): 
x=1
y=2
Class B::info(): 
z=3
v=4
x=1
y=2
Class B::info(): 
z=3
v=4
x=1
y=2
Class B::info(): 
z=3
v=4
x=1
y=2

#---------------KLASA WIRTUALNA / ABSTRAKCYJNA ?-----------------

#-------------TABLICA Z ELEMENTAMI RÓŻNEGO RODZAJU---------------

#include <iostream>
using namespace std;

class Object {      //klasa wirtualna
public:
    virtual void info() = 0;    //metoda nie istnieje, nie została zaimplementowana
};

class MyInt: public Object {
    int x;
public:
    MyInt(int x): x(x) {};
    void info() {
        cout << "int: " << x << endl;
    }
};

class MyDouble: public Object {
    double x;
public:
    MyDouble(double x): x(x) {};
    void info() {
        cout << "double: " << x << endl;
    }
};

class MyString: public Object {
    string x;
public:
    MyString(string x): x(x) {};
    void info() {
        cout << "string: " << x << endl;
    }
};



int main()
{
    //Object o;
    MyInt *i = new MyInt(5);
    MyDouble *d = new MyDouble(3.7);
    MyString *s = new MyString("Foo and bar");
    
    Object ** objTab = new Object * [3];
    
    objTab[0] = i;
    objTab[1] = d;
    objTab[2] = s;
    
    for(int i=0; i<3; i++) {
        objTab[i] -> info();
    }
    
    return 0;
}

#- - - - - - - - - - - - 

OUTPUT:

int: 5
double: 3.7
string: Foo and bar

#----------------------------------------------------------------

dziedziczenie wielobazowe -> problem diamentu

interfejsy rozwiązują ten problem

#----------------------------------------------------------------
