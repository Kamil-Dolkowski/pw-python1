gcc program.c   -> C
g++ program.c   -> C++

plik.h -> header

plik.h -> nie może być dołączony więcej niż raz !

#------------------------------------------------------------------

Wykorzystywane pliki:
--------(jeden plik)--------
-single.c

-------(wiele plików)-------
-types.h
-functions.h
-functions.c
-main.c

#------------------------------------------------------------------ [single.c]

#include <stdio.h>
#include <stdlib.h>

typedef int TYPE;

struct ImportantStructure {
    TYPE value;
    char * description;
};

void bar(struct ImportantStructure s);
void helperFunction();

int main(void) {
    struct ImportantStructure is;
    bar(is);
    return EXIT_SUCCESS;
}

void bar(struct ImportantStructure s) {
    printf("Function: bar\n");
    helperFunction();
}

void helperFunction() {
    printf("Function: helperFunction\n");
}

#------------------------------------------------------------------ [types.h]

#ifndef TYPES_H      // Czy preprocesor wie o TYPES_H       (jeśli wie, to pomija resztę)
#define TYPES_H      // Preprocesor dowiaduje się o TYPES_H

#endif

#------------------------------------------------------------------

#include <stdio.h>  <- pliki globalne

#include "types.h"  <- pliki lokalne

#-----------------------------------

$ gcc -c functions.c    <- kompilacja bez main()    (?)


$ gcc main.c functions.c -o

$ gcc main.c functions.c    (!) kompilacja programu z wieloma plikami (trzeba wymienić wszystkie pliki .c)

$ ./a.out           uruchomienie programu

#---------------------------------------------------------------------PLIKI------------------------------------------------------------------

#------------------------------MAIN.C-------------------------------

#include <stdlib.h>

#include "types.h"
#include "functions.h"

int main(void) {
    struct ImportantStructure is;
    bar(is);

    return EXIT_SUCCESS;
}

#---------------------------FUNCTIONS.C----------------------------

#include <stdio.h>

#include "types.h"
#include "functions.h"

void bar(struct ImportantStructure s) {
    printf("Function: bar\n");
    helperFunction();
}

void helperFunction() {
    printf("Function: helperFunction\n");
}

#---------------------------FUNCTIONS.H----------------------------

#ifndef FUNCTIONS_H
#define FUNCTIONS_H

void bar(struct ImportantStructure s);
void helperFunction();

#endif

#---------------------------TYPES.H-------------------------------

#ifndef TYPES_H      // instrukcja warunkowa preprocesora
#define TYPES_H

typedef int TYPE;

struct ImportantStructure {
    TYPE value;
    char * description;
};

#endif

#------------------------------------------------------------------

#---------------------------------------------------------------------------------------------------------------------------------------------
