#--------------------------------------------WSKAŹNIK-----------------------------------------------
//wskaźnik - adresowanie pośrednie

#include <stdio.h>

void swap(int v, int w) {
    int tmp;
    
    tmp = v;
    v = w;
    w = tmp;
}

void swapNew(int *v, int *w) {
    int tmp;
    
    tmp = *v;
    *v = *w;
    *w = tmp;
}

int main(void) {
    int x = 2;
    int y = 5;
    
    int *pointer;     //wskaźnik
    
    pointer = &x;
    printf("%d %d %d\n", x, y, *pointer);
    pointer = &y;
    printf("%d %d %d\n", x, y, *pointer);
    *pointer = 123;
    printf("%d %d %d\n", x, y, *pointer);   //x=2 y=123
    swap(x,y);
    printf("%d %d %d\n", x, y, *pointer);   //x=2 y=123  - nie zadziałało -> w funkcji są kopie zmiennych, nie oryginały
    swapNew(&x,&y);
    printf("%d %d %d\n", x, y, *pointer);   //x=123 y=2  - zadziałało -> do funkcji przekazano wskaźniki, co umożliwiło działanie na oryginalnych zmiennych (na ich adresach)
    
    return 0;
}

OUTPUT:
2 5 2
2 5 5
2 123 123
2 123 123
123 2 2

#-----------------------------PRZEKAZYWANIE ELEMENTÓW DO PROGRAMU-----------------------------------

#include <stdio.h>

int main(int argc, char **argv) {
    
    printf("Liczba argumentów: %d\n", argc);
    
    for (int i=0; i<argc; i++) {
        printf("argument %d: %s\n", i, argv[i]);
    }
    
    return 0;
}



INPUT:
$ ./a.out program.c kam dol pw

OUTPUT:
Liczba argumentów: 4
argument 0: ./a.out
argument 1: kam
argument 2: dol
argument 3: pw

#-------------------------------

//argc - liczba elementów
//char *argv - wskaźnik na napis \ tablica znaków \ tablica 1-wymiarowa
//char **argv - wskaźnik do wskaźnika \ tablica napisów \ tablica 2-wymiarowa (o różnych długościach)
// ' ' - znak
// " " - napis

#---------------------------------------TABLICA A WSKAŹNIK-----------------------------------------

#include <stdio.h>

int main(void) {
    int tab[3] = {3,5,7};
    int *p;
    
    printf("%d\n", tab[0]);
    printf("%d\n", *tab);
    
    printf("%d\n", tab[1]);
    //printf("%d\n", *(tab++));     // To nie będzie działać
    printf("%d\n", *(tab+1));
    
    p = tab;    
    printf("%d\n", *(++p));
    
    return 0;
}

#-----------------------------------------MALLOC I CALLOC-------------------------------------------

malloc, calloc - tworzą tablicę o określonym rozmiarze (w bajtach)

malloc - zostawia, to co jest
calloc - zeruje, to co jest

#------------------------------

#include <stdio.h>
#include <stdlib.h>
#define SIZE 5

int main(void) {
    int *tabM;
    int *tabC;

    tabM = malloc(sizeof(int)*SIZE);
    tabC = calloc(SIZE, sizeof(int));

    if (tabM != NULL) {
        for (int i=0; i<SIZE; i++) {
            printf("%d\n", tabM[i]);
        }
    }

    if (tabC != NULL) {
        for (int i=0; i<SIZE; i++) {
            printf("%d\n", tabC[i]);
        }
    }

    free(tabM);    //zwolnienie pamieci
    free(tabC);

    return 0;
}

#--------------------------------------------ZADANIE------------------------------------------------

program uruchamia się z linii poleceń -> podanie liczby 
utworzyc tablicę o rozmiarze tej liczby
pobrać liczby -> tyle ile wynosi rozmiar tablicy
wypisanie elementów tablicy

#----------------KOD (mój)---------------

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {
    int *tabM;
    int size,x;

    size = atoi(argv[2]);

    tabM = malloc(sizeof(int)*size);

    for (int i=0; i<size; i++) {
        printf("Podaj liczbe %d: ", i);
        scanf("%d",&x);
        tabM[i] = x;
    }

    printf("\nTABLICA:\n");
    for (int i=0; i<size; i++) {
        printf("[%d] %d\n", i, tabM[i]);
    }

    free(tabM);

    return 0;
}

#----------------KOD (Pana)---------------

#include <stdio.h>
#include <stdlib.h>

int main(int argc, char **argv) {
    int size;
    int *tab;
    
    if (argc < 2) {
        printf("Za mało argumentów\n");
        printf("Poprawne wywołanie:\n");
        printf("NAZWA_PROGRAMU LICZBA_NATURALNA\n");
        
        return -1;
    }
    
    size = atoi(argv[1]);
    
    printf("Przydzielam pamięć na %d elementów.\n", size);

    tab = malloc(sizeof(int)*size);
    
    for (int i=0;i<size; i++) {
        printf("Podaj element %d: ", i);
        scanf("%d",&(tab[i]));
    }
    
    for (int i=0;i<size; i++) {
        printf("%d\n",tab[i]);
    }
    
    free(tab);
    
    return 0;
}

#--------------------------------------------ZADANIE------------------------------------------------

Struktura: imie, nazwisko, tablica ocen [nie ma limitu liczby ocen]
tablica dynamiczna

#----------------KOD (mój)---------------



#---------------------------------------------------------------------------------------------------


# DOKOŃCZYĆ !!!!!!!!!


#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct student {
    char *imie;
    char *nazwisko;
    int *oceny;
};



int main() {
    int size;
    char imie[10];
    int choice;
    char *tab_imie;
    
    printf("====POLECENIA====\n");
    printf("1 - dodaj studenta\n");
    printf("Wprowadź polecenie: ");
    scanf("%d",&choice);
    
    switch (choice) {
        case 1:
            printf("Imie: ");
            scanf("%s",imie);
            size = strlen(imie);
            
            //printf("size %d",size);
            tab_imie = malloc(sizeof(int)*size);
            tab_imie = imie;
            printf("imie1: %s",tab_imie);
            
            break;
        default:
            break;
    }
    
    
    
    
    return 0;
}