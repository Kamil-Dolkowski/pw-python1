// Zad. 1

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main(int argc, char **argv) {
    srand(time(NULL));
    int min, max, number, liczba, i;
    FILE *file;

    if (argc < 5) {
        printf("Przekazano za mało argumentów.\n");
        printf("Format wywolania: \n");
        printf("program MIN MAX NUMBER FILE\n");
        return 1;
    }

    file = fopen(argv[4], "wt");

    min = atoi(argv[1]);
    max = atoi(argv[2]);
    number = atoi(argv[3]);

    i = number;
    while (i > 0) {
        liczba = rand() % (max+1);
        if (liczba > min) {
            i--;
            fprintf(file, "%d\n", liczba);
            printf("%d\n",liczba);
        }
    }

    fclose(file);

    return 0;
}


//---------------------------------------------------------------------------------

// Zad. 2

#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int calculateSum(int *tab, int size);
double calculateAvg(int *tab, int size);
void printTab(int * tab, int size);

int main(int argc, char **argv) {
    FILE *file;
    int *tab;
    char * action;
    int number=0,x,i;
    
    action = argv[2];
    
    if (argc < 3) {
        printf("Przekazano za mało argumentów.\n");
        printf("Format wywolania: \n");
        printf("program FILE ACTION\n");
        return 1;
    }

    file = fopen(argv[1], "rt");

    if (file) {
        while(!feof(file)){
            fscanf(file, "%d\n", &x);
            number++;
        }
        
        fclose(file);
        file = fopen(argv[1], "rt");
        
        tab = malloc(sizeof(int)*number);
        
        i=0;
        while(!feof(file)){
            fscanf(file, "%d\n", &tab[i]);
            i++;
        }
        
        fclose(file);
        
        if (!strcmp(action, "sum")){
            printf("sum=%d\n", calculateSum(tab, i));
        } else if (!strcmp(action, "avg")){
            printf("avg=%f\n", calculateAvg(tab, i));
        } else {
            printf("Nieznana operacja");
        }
    }

    //printTab(tab, number);
    
    free(tab);

    return 0;
}


int calculateSum(int *tab, int size) {
    int i, sum=0;
    
    for(i=0; i<size; i++) {
        sum += tab[i];
    }
    
    return sum;
}

double calculateAvg(int *tab, int size) {
    double avg;
    int i, sum;
    
    sum = calculateSum(tab, size);
    avg = (double)sum/size;
    
    return avg;
}

void printTab(int * tab, int size) {
    int i;
    
    printf("TABLICA:\n");
    for (i=0; i<size; i++) {
        printf("%d\n",tab[i]);
    }
}

