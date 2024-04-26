#-----------------------------KLASA, STRUKTURA-------------------------------

klasa, struktura - różnią się widocznością zmiennych

klasa - ograniczony dostęp (private, public)
struktura - pełny dostęp (public)

#----------------------------------------------------------------------------

#include <iostream>
#include <cstdlib>
using namespace std;

/*
struct Rectangle {
    public:
        int width, height;
};
*/

class Rectangle {
    private:
        int width, height;
    public:
        /*
        void setInitValues(int w, int h) {
            width = w;
            height = h;
        }
        */
        void setInitValues(int w, int h);
        int getArea(){
            return width * height;
        }

};

void Rectangle::setInitValues(int w, int h) {
    width = w;
    height = h;
}


int main() {
    Rectangle r1;
    Rectangle r2;
    int a;

    r1.setInitValues(10, 5);
    a = r1.getArea();
    cout << a << endl;

    r2.setInitValues(5, 7);
    a = r2.getArea();
    cout << a << endl;

    return EXIT_SUCCESS;
}

#------------------------------------THIS------------------------------------

#include <iostream>
#include <cstdlib>
using namespace std;

/*
struct Rectangle {
    public:
        int width, height;
};
*/

class Rectangle {
    private:
        int width, height;
    public:
        /*
        void setInitValues(int w, int h) {
            width = w;
            height = h;
        }
        */
        //void setInitValues(int w, int h);
        void setInitValues(int width, int height);
        int getArea(){
            return width * height;
        }

};

void Rectangle::setInitValues(int width, int height) {
    this->width = width;
    this->height = height;
}


int main() {
    Rectangle r1;
    Rectangle r2;
    int a;

    r1.setInitValues(10, 5);
    a = r1.getArea();
    cout << a << endl;

    r2.setInitValues(5, 7);
    a = r2.getArea();
    cout << a << endl;

    return EXIT_SUCCESS;
}

#--------------------------------KONSTRUKTOR---------------------------------

#include <iostream>
#include <cstdlib>
using namespace std;

class Rectangle {
    private:
        int width, height;
    public:
        Rectangle (int width, int height);  // konstruktor
        Rectangle ();  // konstruktor domyślny
        int getArea(){
            return width * height;
        }

};

Rectangle::Rectangle(int width, int height) {  // konstruktor
    this->width = width;
    this->height = height;
}

Rectangle::Rectangle() {  // konstruktor domyślny
    this->width = 1;
    this->height = 1;
}



int main() {
    Rectangle r1(10, 5);
    Rectangle r2;
    int a;

    a = r1.getArea();
    cout << a << endl;

    a = r2.getArea();
    cout << a << endl;

    return EXIT_SUCCESS;
}

#----------------------------------------------------------------------------

#include <iostream>
#include <cstdlib>

#define PI 3.14159265

using namespace std;

class Circle {
    private:
        int radius;
    public:
        Circle (int radius);
        int getArea(){
            return PI * radius * radius;
        }

};

Circle::Circle(int radius) {
    this->radius = radius;
}


int main() {
    Circle c1(5);
    Circle c2 = 5;
    Circle c3 {5};
    Circle c4 = {5};

    cout << c1.getArea() << endl;
    cout << c2.getArea() << endl;
    cout << c3.getArea() << endl;
    cout << c4.getArea() << endl;

    return EXIT_SUCCESS;
}

#----------------------------------------------------------------------------

lista inicjacyjna konstruktora

#- - - - - - - - - - - - - - - - -   [coś nie działa ??] [mój błąd]

#include <iostream>
#include <cstdlib>

#define PI 3.14159265

using namespace std;


class Circle {
    private:
        int radius;
    public:
        Circle (int radius);
        int getArea(){
            return PI * radius * radius;
        }

};

Circle::Circle(int radius): radius(radius) {}


class Rectangle {
    private:
        int width, int height;
    public:
        Rectangle (int width, int height);
        Rectangle ();
        int getArea() {
            return width * height;
        }
};

/*
Rectangle::Rectangle(int width, int height): width(width) {
    this->height = height;
}
*/

Rectangle::Rectangle(int width, int height): width(width), height(height) {}



int main() {
    Circle c1(5);
    Rectangle r1(3, 4);

    cout << c1.getArea() << endl;
    cout << r1.getArea() << endl;

    return EXIT_SUCCESS;
}

#-----------------------------ZMIENNA STATYCZNA------------------------------

zmienne statyczne -> zmienne współdzielone między obiektami

#- - - - - - - - - - - - - - - - - - - 

#include <iostream>
#include <cstdlib>

using namespace std;


void bar(int x) {
    static int acc = 0;

    acc += x;

    cout << acc << endl;
}


int main() {
    bar(5);
    bar(7);
    bar(3);

    return EXIT_SUCCESS;
}

#----------------------------------------------------------------------------

#include <iostream>
#include <cstdlib>

using namespace std;


class C {
        static int counter;
        int x;
    public:
        C (int x) {
            this->x = x*2;
            counter += 1;
        }

        void print(){
            cout << "x=" << x << ", counter=" << counter << endl;
        }

        void change(int x);
};

void C::change(int x) {
    counter += x;
}

int C::counter = 0;


int main() {
    C c1(5);
    c1.print();
    C c2(3);
    c2.print();
    c2.change(17);
    c1.print();

    return EXIT_SUCCESS;
}



OUTPUT:

x=10, counter=1
x=6, counter=2
x=10, counter=19

#----------------------------------------------------------------------------

#include <iostream>
#include <cstdlib>

using namespace std;


class C {
        static int counterPriv;
        int x;
    public:
        static int counterPub;
        C (int x) {
            this->x = x*2;
            counterPriv += 1;
            counterPub += 1;
        }

        void print(){
            cout << "x=" << x << ", counterPriv=" << counterPriv << ", counterPub=" << counterPub << endl;
        }

        void change(int x);
};


class D {
    public:
        static int counter;
};


void C::change(int x) {
    counterPriv += x;
    counterPub += x;
}

int C::counterPriv = 3;
int C::counterPub = 3;
int D::counter = 3;


int main() {
    C c1(5);
    c1.print();
    C c2(3);
    c2.print();
    c2.change(17);
    c1.print();

    cout << C::counterPub << endl;
    cout << D::counter << endl;

    return EXIT_SUCCESS;
}



OUTPUT:

x=10, counterPriv=4, counterPub=4
x=6, counterPriv=5, counterPub=5
x=10, counterPriv=22, counterPub=22
22
3

#----------------------------------------------------------------------------



#----------------------------------------------------------------------------


[dom] 
dobrać się do flag kompilatora C++