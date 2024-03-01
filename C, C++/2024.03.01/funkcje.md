#---------------------INFORMACJE OGÓLNE----------------------

void nazwaFunkcji(void);    <- wzmianka o istnieniu funkcji (z ';' na końcu)

#----------------------

void nazwaFunkcji(void) {   <- funkcja, która nic nie zwraca i nie przyjmuje żadnych argumentów

}

#----------------------

int doMath(int x, int y) {
    
}

#--------------PRZYKŁAD / SPOSOBY UKŁADU TEKSTU--------------

#include <stdio.h>

int doMath(int x, int y) {
    int result;
    
    result = x + y;
    
    return result;
}

int main()
{
    int r = doMath(5, 7);
    
    printf("123456789\n");
    printf(">%d<\n", r);
    printf(">%5d<\n", r);
    printf(">%-5d<\n", r);
    printf(">%05d<\n", r);
    printf(">%5.2f<\n", (float)r);
    
    return 0;
}

#------------------WZMIANKA O UŻYCIU FUKCJI------------------

#include <stdio.h>

int doMath(int x, int y);

int main()
{
    int r = doMath(5, 7);
    
    printf("123456789\n");
    printf(">%d<\n", r);
    printf(">%5d<\n", r);
    printf(">%-5d<\n", r);
    printf(">%05d<\n", r);
    printf(">%5.2f<\n", (float)r);
    
    return 0;
}

int doMath(int x, int y) {
    int result;
    
    result = x + y;
    
    return result;
}

#---------------------WYPISANIE TABLICY----------------------

#include <stdio.h>

#define TAB_SIZE 6      // "stała" | zastępuje TAB_SIZE na '6' w kodzie 

const int TAB_SIZE = 6;

int doMath(int x[], int size) {         // int x[]  lub  int *x  |  do funkcji przekazywany jest wskaźnik tablicy
    int s;
    for (s=0; s<size; s++) {
        printf("%d\n", x[s]);
    }
}

int main()
{
    int t[TAB_SIZE] = {1,2,3,4,5,6};
    
    doMath(t, TAB_SIZE);
    
    return 0;
}

#---------------------------STAŁA----------------------------

#include <stdio.h>

const int TAB_SIZE = 6;     // stała | zmienna tylko do odczytu

int doMath(int x[], int size) {
    int s;
    for (s=0; s<size; s++) {
        printf("%d\n", x[s]);
    }
}


int main()
{
    int t[6] = {1,2,3,4,5,6};
    //int t[TAB_SIZE] = {1,2,3,4,5,6};  <- błąd | tablicy nie można utworzyć przez zmienną
    
    doMath(t, TAB_SIZE);
    
    return 0;
}

#-------------ZMIANA WARTOSCI TABLICY W FUNKCJI-------------

// przekazana tablica do funkcji jest oryginalną tablicą !!!
// funkcja nie działa na kopii tablicy !!

#include <stdio.h>

#define TAB_SIZE 6

int doMath(int *x, int size) {
    int s;
    for (s=0; s<size; s++) {
        printf("%d\n", x[s]);
        x[s] *= -1;
    }
}


int main()
{
    int t[TAB_SIZE] = {1,2,3,4,5,6};  
    int i;
    
    doMath(t, TAB_SIZE);
    
    printf("==================\n");
    
    for (i = 0; i<TAB_SIZE; i++) {
        printf("%d\n", t[i]);
    }
    
    return 0;
}

#----------------- ! ZWRACANIE TABLICY ! ------------------

// dodawanie 2 wektorów
 
#include <stdio.h>

#define TAB_SIZE 3

void addV(int x[], int y[], int v[], int size) {
    int s;
    
    for (s=0; s<size; s++) {
        v[s] = x[s] + y[s];
    }
}    

int main()
{
    int v1[TAB_SIZE] = {1,2,3}; 
    int v2[TAB_SIZE] = {4,5,6};
    int v[TAB_SIZE];
    int i;
    
    addV(v1, v2, v, TAB_SIZE);
    
    for (i=0; i<TAB_SIZE; i++) {
        printf("%d ", v[i]);
    }

    return 0;
}

#---------------DODAWANIE WEKTORÓW 2D i 3D-------------------

#include <stdio.h>

#define _3D 3
#define _2D 2

void addV(int x[], int y[], int v[], int size) {
    int s;
    
    for (s=0; s<size; s++) {
        v[s] = x[s] + y[s];
    }
}    

int main()
{
    int v1_3d[_3D] = {1,2,3}; 
    int v2_3d[_3D] = {4,5,6};
    int v_3d[_3D];
    
    int v1_2d[_2D] = {1,2}; 
    int v2_2d[_2D] = {4,5};
    int v_2d[_2D];
    
    int i;
    
    addV(v1_3d, v2_3d, v_3d, _3D);
    
    for (i=0; i<_3D; i++) {
        printf("%d\n", v_3d[i]);
    }
    printf("===================\n");
    
    addV(v1_2d, v2_2d, v_2d, _2D);
    
    for (i=0; i<_2D; i++) {
        printf("%d\n", v_2d[i]);
    }
    
    printf("===================\n");
    
    addV(v1_3d, v2_2d, v_3d, _3D);
    
    for (i=0; i<_3D; i++) {
        printf("%d\n", v_3d[i]);
    }
    
    return 0;
}


OUTPUT:
5
7
9
=============
5
7
=============
5
7
8       <- błąd (poprawnie -> 3)

#----------------------ZABAWA TABLICĄ------------------------

// wychodzenie poza tablicę

#include <stdio.h>

int main() {
    int a[3] = {1,2,3}; 
    int x = 100;
    int b[3] = {4,5,6};
    int y = 200;
    int c[3] = {7,8,9};
    
    /*  Kolejność ustalona przez kompilator:
    int x = 100;
    int y = 200;
    int a[3] = {1,2,3}; 
    int b[3] = {4,5,6};
    int c[3] = {7,8,9};
    */
    
    printf("%d\n", b[-4]);
    
    return 0;
}

#--------------------DZIAŁANIE TABLICY---------------------

int t[3] = {1,2,3}

    |       |       |       |
| | | | | |1| | | |2| | | |3| | | |
     ^       ^       ^
     t       t+1     t+2


t[0] (t+0)
t[1] (t+1)
t[2] (t+2)

//nazwa tablicy to adres początku tablicy (zerowego elementu)

#---------------ZMIENNA A TABLICA W FUNKCJI------------------

#--------ZMIENNA---------

int y = 7;

cosInnego(y);

void cosInnego(int x) {

}

// y jest liczbą 
// x jest kopią y -> zmiana x nie zmienia y

#--------TABLICA---------

int y[] = {7};

cosInnego(y);

void cosInnego(int x[]) {

}

// y jest adresem początku tablicy
// x jest kopią y, ale x i y są adresami początku tablicy -> tablicę można zmieniać -> zmiana x zmienia y

#------------------------------------------------------------
