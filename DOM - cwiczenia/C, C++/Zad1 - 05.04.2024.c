
#include <stdio.h>
#include <stdbool.h>
#include <string.h>
#include <stdlib.h>

void printMin(int * tab, int size);
void printInRange(int * tab, int min, int max, bool minInclude, bool maxInclude);


int main(int argc, char **argv) {
    int tab[10]={6,2,3,4,5,1,7,8,9,10};
    int min, max, minInclude, maxInclude;
    
    
    if (argc < 2) {
        printf("ERROR: Za mało argumentów.\n");
        printf("Prawidłowe wywołanie programu: \n");
        printf("PROGRAM min\n");
        printf("PROGRAM inRange MIN MAX T/F T/F");
        return 1;
    }
    
    // funkcje (min, inRange)
    if (strcmp(argv[1], "min") == 0) {
        if (argc == 2) {
            printMin(tab, 10);
        } else {
            printf("ERROR: Za dużo argumentów dla funkcji 'min'.\n");
        }
    } else
    if (strcmp(argv[1], "inRange") == 0) {
        if (argc == 6) {
            min = atoi(argv[2]);
            max = atoi(argv[3]);
            
            // argv[4]  T/F
            if (strcmp(argv[4],"T") == 0) {
                minInclude = 1;
            } else if (strcmp(argv[4],"F") == 0) {
                minInclude = 0;
            } else {
                printf("ERROR: Błędna wartość -> PROGRAM %s %s %s [??]\n", argv[1], argv[2], argv[3]);
                printf("Powinno być: T/F\n");
                return 1;
            }
            
            // argv[5]  T/F
            if (strcmp(argv[5],"T") == 0) {
                maxInclude = 1;
            } else if (strcmp(argv[5],"F") == 0) {
                maxInclude = 0;
            } else {
                printf("ERROR: Błędna wartość -> PROGRAM %s %s %s %s [??]\n", argv[1], argv[2], argv[3], argv[4]);
                printf("Powinno być: T/F\n");
                return 1;
            }
            printInRange(tab, min, max, minInclude, maxInclude);
        } else {
            printf("ERROR: Nieodpowiednia ilość argumentów dla funkcji 'inRange'.\n");
        }
    } else {
        printf("ERROR: Brak takiego polecenia.\n");
    }
    
    
    /*
    printMin(tab, 10);
    printInRange(tab, 2, 4, 0, 0);
    printInRange(tab, 2, 4, 1, 0);
    printInRange(tab, 2, 4, 0, 1);
    printInRange(tab, 2, 4, 1, 1);
    */

    return 0;
}


void printMin(int * tab, int size) {
    int min,i;
    
    min = tab[0];
    for (i=1; i<size; i++) {
        if (tab[i] < min) {
            min = tab[i];
        }
    }
    
    printf("Wartość minimalna w tablicy: %d\n", min);
}

void printInRange(int * tab, int min, int max, bool minInclude, bool maxInclude) {
    int i;
    
    if (min <= max) {
        if (minInclude == 0 && maxInclude == 0) {
            printf("Liczby z zakresu (%d, %d):\n", min, max);
            for (i=min+1; i<=max-1; i++) {
                printf("%d ", tab[i]);
            }
        } 
        if (minInclude == 0 && maxInclude == 1) {
            printf("Liczby z zakresu (%d, %d]:\n", min, max);
            for (i=min+1; i<=max; i++) {
                printf("%d ", tab[i]);
            }
        }    
        if (minInclude == 1 && maxInclude == 0) {
            printf("Liczby z zakresu [%d, %d):\n", min, max);
            for (i=min; i<=max-1; i++) {
                printf("%d ", tab[i]);
            }
        }
        if (minInclude == 1 && maxInclude == 1) {
            printf("Liczby z zakresu [%d, %d]:\n", min, max);
            for (i=min; i<=max; i++) {
                printf("%d ", tab[i]);
            }
        }
    } else {
        printf("ERROR: MIN nie może być większe od MAX.");
    } 
    printf("\n");
}
