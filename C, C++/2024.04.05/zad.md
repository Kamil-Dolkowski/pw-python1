Zadanie
-tablica intów (10)
-wywoływany z linii poleceń
-PROG min -> minimalna wartość
  *-PROG sort -> posortować dane
  *-PROG sort desc -> posortowane w kolejności malejącej
-PROG inRange min max T/F T/F -> wszystkie wartości w podanym zakresie 
    T/F - czy ta liczba należy do tego zakresu
    
     0 1 2 3 4 5
    [1,2,3,4,5,6]

    PROG inRange 1 3 T F -> 2, 3
    PROG inRange 1 5 T T -> 2, 3, 4, 5, 6 



#-------------------------------------PROGRAM------------------------------------------  [dokończyć]

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

void printMin(int *tab, unsigned int size) {
    int min,i;
    
    min = tab[0];
    for (i=1; i<size; i++) {
        if(tab[i] < min){
            min = tab[i];
        }
    }
    
    printf("min=%d\n", min);
}

void wypiszInRange(int *tab, int min, int max, char option1, char option2) {
    if (option1 == 'T') printf("%d %d ok", min, max);
    
}


enum Option {min, inRange, T, F};

int main(int argc, char **argv) {
    int tab[10]={1,2,3,4,5,6,7,8,9,0};
    enum Option option;
    char c;
    
    
    if (argc < 2) {
        printf("Za mało argumentów.\n");
        return 1;
    }
    
    option = inRange;
    
    if (strcmp(*argv[1],"min") == 0) printf("dd");
    
    switch (option) {
        case min:
            printMin(tab, 10);
            break;
        case inRange:
            wypiszInRange(tab, atoi(argv[2]), atoi(argv[3]), *argv[4], *argv[5]);
            break;
        default:
            
            break;
    }
    
    
    return 0;   
}