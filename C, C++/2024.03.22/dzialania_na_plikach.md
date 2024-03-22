#----------------------------------------------------------------------------------------------

#include <stdio.h>

int main(void) {
    FILE *fileIn, *fileOut;

    fileIn = fopen("dane.txt", "rt");
    fileOut = fopen("out.txt", "wt");

    fclose(fileIn);
    fclose(fileOut);

    return 0;
}

#------------------------------KOPIOWANIE Z PLIKU DO PLIKU------------------------------ 

#include <stdio.h>

int main(void) {
    FILE *fileIn, *fileOut;
    char c;

    fileIn = fopen("dane.txt", "rt");
    fileOut = fopen("out.txt", "wt");

    if (fileIn == NULL || fileOut == NULL) {
        printf("File error\n");
        return 1;
    }

    while ( (c=fgetc(fileIn)) != EOF ) {
        fputc(c, fileOut);
    }

    fclose(fileIn);
    fclose(fileOut);

    return 0;
}

#----------------------KOPIOWANIE Z PLIKU DO PLIKU (INNY SPOSÓB)------------------------

#---------TRYB TEKSTOWY---------- 

#include <stdio.h>

int main(void) {
    FILE *fileIn, *fileOut;
    char c;

    fileIn = fopen("dane.txt", "rt");
    fileOut = fopen("out.txt", "wt");

    if (fileIn == NULL || fileOut == NULL) {
        printf("File error\n");
        return 1;
    }

    while ( 1 ) {
        c = fgetc(fileIn);
        if (feof(fileIn)) {
            break;
        }
        putc(c, stdout);
        fputc(c, fileOut);
    }

    fclose(fileIn);
    fclose(fileOut);

    return 0;
}

#------------TRYB BINARNY-------------

#include <stdio.h>

int main(void) {
    FILE *fileIn, *fileOut;
    char c;
    int n;

    fileIn = fopen("dane.txt", "rb");
    fileOut = fopen("out.txt", "wb");

    if (fileIn == NULL || fileOut == NULL) {
        printf("File error\n");
        return 1;
    }

    while ( 1 ) {
        n = fread(&c,sizeof(char),1,fileIn);
        if (n == 0) {
            break;
        }
        putc(c, stdout);
        fwrite(&c,sizeof(char),1,fileOut);
    }

    fclose(fileIn);
    fclose(fileOut);

    return 0;
}

#----------------------------------------------------------------------------------------------

#include <stdio.h>

int main(void) {
    int x;
    FILE *file;

    x=5;

    file = fopen("test.txt", "at");     //tekstowy
    fprintf(file, "%d", x);
    fclose(file);

    file = fopen("test.txt", "ab");     //binarny
    fwrite(&x,sizeof(int),1,file);
    fclose(file);

    return 0;
}



$ hd test.txt

00000000  35 05 00 00 00                                    |5....|
00000005

#----------------------------------------------------------------------------------------------

#include <stdio.h>

int main(int argc, char **argv) {
    FILE *fileIn, *fileOut;
    char c;

    if (argc != 3) {
        printf("Bad number of arguments\n");
        return 1;
    }

    fileIn = fopen(argv[1], "rt");
    fileOut = fopen(argv[2], "wt");

    if (fileIn == NULL || fileOut == NULL) {
        printf("File error\n");
        return 1;
    }

    while ( 1 ) {
        c = fgetc(fileIn);
        if (feof(fileIn)) {
            break;
        }
        putc(c, stdout);
        fputc(c, fileOut);
    }

    fclose(fileIn);
    fclose(fileOut);

    return 0;
}



 $ ./a.out out.txt res.txt

#----------------------------------------ZADANIE-----------------------------------------------

# 1 program:
z linii polecen, 4 argumenty (3 liczby + nazwa_pliku): 
1 - początek zakresu, 2 - koniec zakresu, 3 - ile liczb z zakresu wybrać/wylosować,
wylosowane liczby zapisać do pliku

program MIN MAX NUMBER FILE


# 2 program: 
przyjmuje 2 argumenty: 1 - nazwa pliku z liczbami, 2 - info jaką operację należy wykonać (SUM - suma, AVG - średnia liczb)

program FILE ACTION

#-----------PROGRAM 1-------------

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
            fprintf(file, "%d,", liczba);
            printf("%d\n",liczba);
        }
    }

    fclose(file);

    return 0;
}


#-----------PROGRAM 2-------------      [dokończyć !!]

#include <stdio.h>

enum Operation {SUM, AVG};


void sum() {

}

int main(int argc, char **argv) {
    FILE *file;
    int *tab;
    char c;
    enum Operation operacja;


    if (argc < 3) {
        printf("Przekazano za mało argumentów.\n");
        printf("Format wywolania: \n");
        printf("program FILE ACTION\n");
        return 1;
    }

    file = fopen(argv[1], "rt");

    if (file == NULL) {
        printf("File error\n");
        return 1;
    }

    while ( 1 ) {
        c = fgetc(file);
        if (feof(file)) {
            break;
        }
        printf("%s",c);
        //putc(c, stdout);
        //fputc(c, fileOut);
    }


    fclose(file);


    operacja = argv[2];

    switch (operacja) {
        case SUM:
            //sum(tab);
            break;
        case AVG:
            //avg(tab);
            break;
        default:
            printf("Brak takiej operacji.\n");
            break;
    }

    return 0;
}