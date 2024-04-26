#include <stdio.h>

int main()
{
    int i;
    int t[5];
    for (i=0; i<5; i++) {
        printf("%d\n", t[i]);
    }
    return 0;
}



int t[5]; - we wnętrzu funkcji -> losowe liczby
int t[5]; - poza funkcją -> 0 (zera)

#---------------------BADANIE DZIALANIA TABLIC----------------------

#include <stdio.h>

int main()
{
    int i;
    int t[5] = {5, 8, 13, 21, 29};
    for (i=0; i<5; i++) {
        printf("%d\n", t[i]);
    }
    return 0;
}

OUTPUT: 
5
8
13
21
21

#--------------------------

#include <stdio.h>

int main()
{
    int i;
    int t[5] = {5, 8};
    for (i=0; i<5; i++) {
        printf("%d\n", t[i]);
    }
    return 0;
}

OUTPUT: 
5
8
0
0
0

#--------------------------

#include <stdio.h>

int main()
{
    int i;
    int t[5] = {5, 8, 13, 21, 21 ,15, 10};
    for (i=0; i<5; i++) {
        printf("%d\n", t[i]);
    }
    return 0;
}

OUTPUT: 
5
8
13
21
21
\\wyświetla ostrzeżenie\\

#--------------------------

#include <stdio.h>

int main()
{
    int i;
    int t[5] = {5, 8, 13, 21, 21 ,15, 10};
    for (i=0; i<7; i++) {
        printf("%d\n", t[i]);
    }
    return 0;
}

OUTPUT: 
5
8
13
21
21
0
1183728640
\\wyświetla ostrzeżenie\\

#--------------------------

int t[] = {5,8,13,21,29}  ->  utworzy tablicę t[5]



int x;
int i;
int t[5];


int x,i,t[5];

#--------------WPISYWANIE I WYPISYWANIE Z TABLICY-------------------

#include <stdio.h>

int main()
{
    int x;
    int i;
    int t[5];
    for (i=0; i<5; i++) {
        scanf("%d", &x);
        t[i] = x;
    }
    for (i=0; i<5; i++) {
        printf("%d\n", t[i]);
    }
    return 0;
}

#----------------------TABLICA 2-WYMIAROWA--------------------------

int m[3][2] = { {1,2}, {3,4}, {5,6} };

int m[][2] = { {1,2}, {3,4}, {5,6} };

int m[3][2] = {1,2,3,4,5,6};

#---------------------------SZACHOWNICA-----------------------------

tablica 2D:

0 1 0 1
1 0 1 0 
0 1 0 1

#-------------------

#include <stdio.h>

int main()
{
    int i, j, t[3][4];
    for (j=0; j<3; j++) {
        for (i=0; i<4; i++) {
            if (j%2 == 0) { 
                if (i%2 == 0) 
                    t[j][i] = 0;
                else
                    t[j][i] = 1;
            } else {
                if (i%2 == 0) 
                    t[j][i] = 1;
                else
                    t[j][i] = 0;
            }        
        }
    }
    
    for (j=0; j<3; j++) {
        for (i=0; i<4; i++) {
            printf("%d", t[j][i]);
        }
        printf("\n");
    }

    return 0;
}

#--------------WYPELNIANIE TABLICY LOSOWYMI LICZBAMI---------------

#include <stdlib.h>

m[i][j] = rand()



#include <stdlib.h>
#include <time.h>

int main () {
    srand(time(NULL));
    m[i][j] = rand()
}

#-------------------------------------------------------------------

Zad.
Losowe liczby w tablicy, jeśli w komórce liczba jest podzielna 
przez 2 to zmiana na 0, jeśli niepodzielna to zmiana na 1.

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main()
{
    int i, j, v, t[3][4];
    srand(time(NULL));
    
    
    for (j=0; j<3; j++) {
        for (i=0; i<4; i++) {
            v = rand();
            t[j][i] = v%2;
        }
    }
    
    for (j=0; j<3; j++) {
        for (i=0; i<4; i++) {
            printf("%d ", t[j][i]);
        }
        printf("\n");
    }
    
    return 0;
}

#-------------------------5x "1" W TABLICY--------------------------

#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() 
{
    int i, j, v, suma1 = 0, t[3][4];
    srand(time(NULL));
    
    while (suma1 != 5) {
        suma1 = 0;
        for (j=0; j<3; j++) {
            for (i=0; i<4; i++) {
                v = rand();
                t[j][i] = v%2;
                if (v%2 == 1) suma1++;
            }
        }
        
        /*printf("%d\n", suma1);
        
        for (j=0; j<3; j++) {
            for (i=0; i<4; i++) {
                printf("%d ", t[j][i]);
            }
            printf("\n");
        }*/
    }
    
    for (j=0; j<3; j++) {
            for (i=0; i<4; i++) {
                printf("%d ", t[j][i]);
            }
            printf("\n");
    } 
    
    return 0;
}

#---------------------------GRA W STATKI----------------------------

[Niedokończone]


#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() 
{
    int i, j, v, x, y, wynik1, wynik2, suma1=0, t1[3][4], t2[3][4];
    srand(time(NULL));
    
    //komputer
    while (suma1 != 5) {
        suma1 = 0;
        for (j=0; j<3; j++) {
            for (i=0; i<4; i++) {
                v = rand();
                t1[j][i] = v%2;
                if (v%2 == 1) suma1++;
            }
        }
    }
    
    //czlowiek
    suma1 = 0;
    printf("Wpisz pola 0/1:\n");
    while (suma1 != 5) {
        for (j=0; j<3; j++) {
            for (i=0; i<4; i++) {
                scanf("%d",&x);
                t2[j][i] = x;
                if (x == 1) suma1++;
            }
        }
        if (suma1 != 5) printf("Podaj tylko 5x '1'.\n");
    }


    printf("Komputer:\n");
    for (j=0; j<3; j++) {
            for (i=0; i<4; i++) {
                printf("%d ", t1[j][i]);
            }
            printf("\n");
    }
    
    printf("Czlowiek:\n");
    for (j=0; j<3; j++) {
            for (i=0; i<4; i++) {
                printf("%d ", t2[j][i]);
            }
            printf("\n");
    }
    
    while(wynik1 || wynik2 == 5) {
        //gracz
        printf("Podaj pole [][]:\n");
        scanf("%d",&x);
        scanf("%d",&y);
        if (t1[x][y] == 1) {
            printf("Trafienie\n");
            wynik2++;
        } else {
            printf("Pudlo\n");
        }
        
        //Komputer
        x = rand();
        y = rand();
        if (t1[x][y] == 1) {
            printf("Trafienie (komputer)\n");
            wynik1++;
        } else {
            printf("Pudlo (komputer)\n");
        }
    }
    
    
    
    return 0;
}


#-------------------------------------------------------------------