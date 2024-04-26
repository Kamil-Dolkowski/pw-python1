# Wprowadzenie do C++

#------------------------------WITAJ ŚWIECIE---------------------------------

#include <iostream>
#include <cstdlib>
using namespace std;

int main() {
    cout << "Witaj świecie" << endl;
    return EXIT_SUCCESS;
}

#- - - - - - - - 

$ g++ prog.cpp

#--------------------------------REFERENCJA----------------------------------

#include <iostream>
#include <cstdlib>
using namespace std;

void foo(int x) {
    x += 2;
}

int foo_1(int x) {
    x += 2;

    return x;
}

void foo_2(int *x) {
    *x += 2;
}

void foo_3(int & x) {     // referencja
    x += 2;
}

int main() {
    int a = 3;

    cout << a << endl;
    //foo(a);
    //a = foo_1(a);
    //foo_2(&a);
    foo_3(a);             // przez referencje
    cout << a << endl;

    return EXIT_SUCCESS;
}

#- - - - - - - - - - - - 

działanie na oryginale (wskaźnik) -> bardziej wydajne, wymaga mniej pamięci

#-----------------------------WARTOŚĆ DOMYŚLNA-------------------------------

#include <iostream>
#include <cstdlib>
using namespace std;

void foo_1(int x, int y, bool debug = false) {
    if (debug) {
        cout << x << ", " << y << ", TRUE" << endl;
    } else {
        cout << x << ", " << y << ", FALSE" << endl;
    }
}

void foo_2(int x, int y=7, bool debug = false) {
    if (debug) {
        cout << x << ", " << y << ", TRUE" << endl;
    } else {
        cout << x << ", " << y << ", FALSE" << endl;
    }
}

int main() {

    foo_1(3, 5);
    foo_1(3, 5, false);
    foo_1(3, 5, true);

    foo_2(3, 9, true);
    foo_2(3, 9);
    foo_2(3);
    //foo_2(3, true);  // Error

    return EXIT_SUCCESS;
}

#-------------------PRZEŁADOWANIA (PRZECIĄŻENIA) FUNKCJI---------------------

overloading - przeciążenie (funkcje o tej samej nazwie, ale innej ilości argumentów)
overreading - nadpisywanie (funkcja niszczy inną funkcję)

funkcje nie mogą się różnić tym, co zwracają

#- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - 

#include <iostream>
#include <cstdlib>
#include <typeinfo>
using namespace std;

void foo_1(int x, int y) {
    cout << "My type is: " << typeid(x).name() << endl;
    cout << "My type is: " << typeid(y).name() << endl;
    cout << x << ", " << y << endl;
}

void foo_1(double x, double y) {
    cout << "My type is: " << typeid(x).name() << endl;
    cout << "My type is: " << typeid(y).name() << endl;
    cout << x << ", " << y << endl;
}

void foo_1(double x, int y) {
    cout << "My type is: " << typeid(x).name() << endl;
    cout << "My type is: " << typeid(y).name() << endl;
    cout << x << ", " << y << endl;
}

void foo_1(int x, double y) {
    cout << "My type is: " << typeid(x).name() << endl;
    cout << "My type is: " << typeid(y).name() << endl;
    cout << x << ", " << y << endl;
}


/*  // Error
double foo_1(double x, double y) {
    cout << "My type is: " << typeid(x).name() << endl;
    cout << x << ", " << y << endl;

    return x + y;
}
*/

int main() {

    foo_1(3, 5);
    foo_1(3.1, 5.3);
    foo_1(3.1, 5);
    foo_1(3, 5.3);

    return EXIT_SUCCESS;
}


OUTPUT:

My type is: i
My type is: i
3, 5
My type is: d
My type is: d
3.1, 5.3
My type is: d
My type is: i
3.1, 5
My type is: i
My type is: d
3, 5.3

#----------------------------------------------------------------------------

#include <iostream>
#include <cstdlib>
#include <typeinfo>
using namespace std;

void foo_2(int x, int y, bool debug) {
    cout << x << ", "  << y << ", " << debug << endl;
}

void foo_2(int x, int y) {
    cout << "1: ";
    foo_2(x, y, false);
}

void foo_2(int x) {
    cout << "2: ";
    foo_2(x, 7, false);
}

void foo_2(int x, bool debug) {
    cout << "3: ";
    foo_2(x, 7, debug);
}


int main() {

    foo_2(3, 9, true);
    foo_2(3, 9);
    foo_2(3);
    foo_2(3, true);

    return EXIT_SUCCESS;
}

#----------------------------------------------------------------------------

#include <iostream>
#include <cstdlib>
#include <typeinfo>
using namespace std;

void foo_2(int x, int y) {
    cout << x << ", "  << y << endl;
}

void foo_2(int x, int y, bool debug = false) {
    cout << x << ", "  << y << ", " << debug << endl;
}


int main() {

    foo_2(5, 7, true);
    //foo_2(5, 7);  // Error

    return EXIT_SUCCESS;
}

#--------------------------------SZABLON-------------------------------------

#include <iostream>
#include <cstdlib>
#include <typeinfo>
using namespace std;

/*
void foo_1(int x, int y) {
    cout << "My type is: " << typeid(x).name() << endl;
    cout << "My type is: " << typeid(y).name() << endl;
    cout << x << ", " << y << endl;
}

void foo_1(double x, double y) {
    cout << "My type is: " << typeid(x).name() << endl;
    cout << "My type is: " << typeid(y).name() << endl;
    cout << x << ", " << y << endl;
}
*/

template <typename T>
void foo_1(T x, T y) {
    cout << "My type is: " << typeid(x).name() << endl;
    cout << "My type is: " << typeid(y).name() << endl;
    cout << x << ", " << y << endl;
}


int main() {

    foo_1<int>(3, 5);
    foo_1<double>(3.1, 5.3);

    return EXIT_SUCCESS;
}

#-------------------------------EKSPERYMENT----------------------------------

#include <iostream>
#include <cstdlib>
#include <typeinfo>
using namespace std;


template <typename T>
void foo_1(T x, T y) {
    cout << "T: 1" << endl;
    cout << "My type is: " << typeid(x).name() << endl;
    cout << "My type is: " << typeid(y).name() << endl;
    cout << x << ", " << y << endl;
}

template <typename T, typename H>
void foo_1(T x, H y) {
    cout << "T: 2" << endl;
    cout << "My type is: " << typeid(x).name() << endl;
    cout << "My type is: " << typeid(y).name() << endl;
    cout << x << ", " << y << endl;
}


int main() {

    foo_1<int>(3, 5);
    foo_1<double>(3.1, 5.3);

    foo_1(3, 5);
    foo_1<int, int>(3, 5);
    foo_1<int, double>(3, 5);  // wygenerowana 3 funkcja

    return EXIT_SUCCESS;
}



OUTPUT:

T: 1
My type is: i
My type is: i
3, 5
T: 1
My type is: d
My type is: d
3.1, 5.3
T: 1
My type is: i
My type is: i
3, 5
T: 2
My type is: i
My type is: i
3, 5
T: 2
My type is: i
My type is: d
3, 5

#------------------ELEMENT PARAMETRYZUJĄCY I EKSPERYMENT---------------------

#include <iostream>
#include <cstdlib>
#include <typeinfo>
using namespace std;

/*
template <typename T, typename H>
void foo_1(T x, H y) {
    cout << "T: 1" << endl;
    cout << "My type is: " << typeid(x).name() << endl;
    cout << "My type is: " << typeid(y).name() << endl;
    cout << x << ", " << y << endl;
    cout << (x * y) << endl;
}
*/

template <typename T, int y>  // y to nie zmienna, a dodatkowy parametr, element parametryzujący
void foo_2(T x) {
    cout << "T: 2" << endl;
    cout << "My type is: " << typeid(x).name() << endl;
    cout << "My type is: " << typeid(y).name() << endl;
    cout << x << ", " << y << endl;
    cout << (x * y) << endl;
}


int main() {

    //foo_1(5, 7);
    foo_2<int, 7>(5);
    foo_2<int, 3>(5);
    //int z = 9;
    //foo_2<int, z>(5);  // nie zadziała




    // EKSPERYMENT (sprawdzenie adresów funkcji) [nie działa] ??

    void (*p1)(int) = &foo_2<int, 7>;
    void (*p2)(int) = &foo_2<int, 3>;

    (*p1)(6);

    cout << static_cast<void(*)(int)>(p1) << endl;
    cout << p2 << endl;

    return EXIT_SUCCESS;
}

#----------------------------------------------------------------------------


