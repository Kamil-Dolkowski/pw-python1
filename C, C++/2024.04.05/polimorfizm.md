#----------------------------------------MAX W TABLICY------------------------------------------

#include <stdio.h>
#include <stdlib.h>

int getMaxInt(int *tab, unsigned int size) {
    int i;
    int max = tab[0];

    for (i=1; i<size; i++) {
        if (tab[i] > max) {
            max = tab[i];
        }
    }

    return max;
}

int main(void) {
    int tabOfInts[] = {3,2,1,5,6,4};
    
    printf("max=%d\n", getMaxInt(tabOfInts, 6));
    
    return EXIT_SUCCESS;
}

#----------------------------------------MAX W TABLICY------------------------------------------ (inna wersja) (z deklaracją istnienia funkcji)

#include <stdio.h>
#include <stdlib.h>

int getMaxInt(int *tab, unsigned int size);     // <- deklaracja o istnieniu tej funkcji
//int getMaxInt(int *, unsigned int);           // inny sposób deklaracji

int main(void) {
    int tabOfInts[] = {3,2,1,5,6,4};
    
    printf("max=%d\n", getMaxInt(tabOfInts, 6));
    
    return EXIT_SUCCESS;
}

int getMaxInt(int *tab, unsigned int size) {
    int i;
    int max = tab[0];

    for (i=1; i<size; i++) {
        if (tab[i] > max) {
            max = tab[i];
        }
    }

    return max;
}

#---------------------------------------SPAGHETTI CODING----------------------------------------

SPAGHETTI CODING - powielanie kodu
taki sam kod dla różnych typów danych (tu getMax dla 'int' i 'double')

#-------------------------------

#include <stdio.h>
#include <stdlib.h>

int getMaxInt(int *tab, unsigned int size);
double getMaxDouble(double *tab, unsigned int size);

int main(void) {
    int tabOfInts[] = {3,2,1,5,6,4};
    double tabOfDoubles[] = {3.3, 2.2, 1.1, 5.5, 6.6, 4.4};
    
    printf("max=%d\n", getMaxInt(tabOfInts, 6));
    printf("max=%f\n", getMaxDouble(tabOfDoubles, 6));
    
    return EXIT_SUCCESS;
}

int getMaxInt(int *tab, unsigned int size) {
    int i;
    int max = tab[0];
    
    for (i=1; i<size; i++) {
        if (tab[i] > max) {
            max = tab[i];
        }
    }
    
    return max;
}

double getMaxDouble(double *tab, unsigned int size) {
    int i;
    double max = tab[0];
    
    for (i=1; i<size; i++) {
        if (tab[i] > max) {
            max = tab[i];
        }
    }
    
    return max;
}

#------------------------POLIMORFIZM - FUNKCJA DLA WIELU TYPÓW DANYCH---------------------------    [DOM - zadanie]

#include <stdio.h>
#include <stdlib.h>

enum argumentType {INT, DOUBLE};

void getMax(void *tabPoly, unsigned int size, enum argumentType type);  //*tabPoly | Poly - polimorfizm


int main(void) {
    int tabOfInts[] = {3,2,1,5,6,4};
    double tabOfDoubles[] = {3.3, 2.2, 1.1, 5.5, 6.6, 4.4};
    
    getMax(tabOfInts, 6, INT);
    getMax(tabOfDoubles, 6, DOUBLE);
    
    return EXIT_SUCCESS;
}

void getMax(void *tabPoly, unsigned int size, enum argumentType type) {
    int i;
    
    if (type == INT) {
        int max;
        int *tab = (int *)tabPoly;
        
        max = tab[0];
        for (i=1; i<size; i++) {
            if (tab[i] > max) {
                max = tab[i];
            }
        }
        printf("max=%d\n", max);
    } else if (type == DOUBLE) {
        double max;
        double *tab = (double *)tabPoly;
        
        max = tab[0];
        for (i=1; i<size; i++) {
            if (tab[i] > max) {
                max = tab[i];
            }
        }
        printf("max=%f\n", max);
    }
}

#-----------------------ZWRÓCENIE DOWOLNEGO TYPU DANYCH (PRZEZ STRUKTURĘ)-----------------------

#include <stdio.h>
#include <stdlib.h>

enum argumentType {INT, DOUBLE};

struct polyType {
    int i;
    double d;
};

struct polyType getMax(void *tabPoly, unsigned int size, enum argumentType type);  //*tabPoly | Poly - polimorfizm


int main(void) {
    int tabOfInts[] = {3,2,1,5,6,4};
    double tabOfDoubles[] = {3.3, 2.2, 1.1, 5.5, 6.6, 4.4};
    struct polyType result1, result2;
    
    result1 = getMax(tabOfInts, 6, INT);
    result2 = getMax(tabOfDoubles, 6, DOUBLE);
    
    printf("max=%d\n",result1.i);
    printf("max=%f\n",result2.d);
    
    return EXIT_SUCCESS;
}

struct polyType getMax(void *tabPoly, unsigned int size, enum argumentType type) {
    int i;
    struct polyType result;
    
    if (type == INT) {
        int max;
        int *tab = (int *)tabPoly;
        
        max = tab[0];
        for (i=1; i<size; i++) {
            if (tab[i] > max) {
                max = tab[i];
            }
        }
        result.i = max;
    } else if (type == DOUBLE) {
        double max;
        double *tab = (double *)tabPoly;
        
        max = tab[0];
        for (i=1; i<size; i++) {
            if (tab[i] > max) {
                max = tab[i];
            }
        }
        result.d = max;
    }
    
    return result;
}

#--------------------------------------UNIA VS STRUKTURA----------------------------------------

#include <stdio.h>
#include <stdlib.h>

enum argumentType {INT, DOUBLE};

struct polyType {
    int i;      // 4B
    double d;   // 8B
};              // 12B (16B - powiększone, aby ta structura miała odpowiednią długość)

union polyTypeU {
    int i;      // 4B
    double d;   // 8B
};              // max(4,8) (8B)

struct polyType getMax(void *tabPoly, unsigned int size, enum argumentType type);  //*tabPoly | Poly - polimorfizm


int main(void) {
    int tabOfInts[] = {3,2,1,5,6,4};
    double tabOfDoubles[] = {3.3, 2.2, 1.1, 5.5, 6.6, 4.4};
    struct polyType result1, result2;
    
    // === experyment ===
    printf("%ld\n", sizeof(int));               // 4
    printf("%ld\n", sizeof(double));            // 8
    printf("%ld\n", sizeof(struct polyType));   // 16
    printf("%ld\n", sizeof(union polyTypeU));   // 8
    // === experyment ===
    
    result1 = getMax(tabOfInts, 6, INT);
    result2 = getMax(tabOfDoubles, 6, DOUBLE);
    
    printf("max=%d\n",result1.i);
    printf("max=%f\n",result2.d);
    
    return EXIT_SUCCESS;
}

struct polyType getMax(void *tabPoly, unsigned int size, enum argumentType type) {
    int i;
    struct polyType result;
    
    if (type == INT) {
        int max;
        int *tab = (int *)tabPoly;
        
        max = tab[0];
        for (i=1; i<size; i++) {
            if (tab[i] > max) {
                max = tab[i];
            }
        }
        result.i = max;
    } else if (type == DOUBLE) {
        double max;
        double *tab = (double *)tabPoly;
        
        max = tab[0];
        for (i=1; i<size; i++) {
            if (tab[i] > max) {
                max = tab[i];
            }
        }
        result.d = max;
    }
    
    return result;
}

#-------------------------ZWRÓCENIE DOWOLNEGO TYPU DANYCH (PRZEZ UNIĘ)--------------------------

#include <stdio.h>
#include <stdlib.h>

enum argumentType {INT, DOUBLE};

union polyType {
    int i;      
    double d;   
};              

union polyType getMax(void *tabPoly, unsigned int size, enum argumentType type);  //*tabPoly | Poly - polimorfizm


int main(void) {
    int tabOfInts[] = {3,2,1,5,6,4};
    double tabOfDoubles[] = {3.3, 2.2, 1.1, 5.5, 6.6, 4.4};
    union polyType result1, result2;
    
    result1 = getMax(tabOfInts, 6, INT);
    result2 = getMax(tabOfDoubles, 6, DOUBLE);
    
    printf("max=%d\n",result1.i);
    printf("max=%f\n",result2.d);
    
    return EXIT_SUCCESS;
}

union polyType getMax(void *tabPoly, unsigned int size, enum argumentType type) {
    int i;
    union polyType result;
    
    if (type == INT) {
        int max;
        int *tab = (int *)tabPoly;
        
        max = tab[0];
        for (i=1; i<size; i++) {
            if (tab[i] > max) {
                max = tab[i];
            }
        }
        result.i = max;
    } else if (type == DOUBLE) {
        double max;
        double *tab = (double *)tabPoly;
        
        max = tab[0];
        for (i=1; i<size; i++) {
            if (tab[i] > max) {
                max = tab[i];
            }
        }
        result.d = max;
    }
    
    return result;
}

#-----------------------------------PREPROCESOR - MAKRO-----------------------------------------

#include <stdio.h>
#include <stdlib.h>

#define FOO(x) (7*x*x)                      // *


enum argumentType {INT, DOUBLE};

union polyType {
    int i;      
    double d;   
};              

union polyType getMax(void *tabPoly, unsigned int size, enum argumentType type);  //*tabPoly | Poly - polimorfizm


int main(void) {
    int tabOfInts[] = {3,2,1,5,6,4};
    double tabOfDoubles[] = {3.3, 2.2, 1.1, 5.5, 6.6, 4.4};
    union polyType result1, result2;
    
    printf("%d\n", FOO(5));                     // *   OUTPUT: 175     (7*5*5)
    
    result1 = getMax(tabOfInts, 6, INT);
    result2 = getMax(tabOfDoubles, 6, DOUBLE);
    
    printf("max=%d\n",result1.i);
    printf("max=%f\n",result2.d);
    
    return EXIT_SUCCESS;
}

union polyType getMax(void *tabPoly, unsigned int size, enum argumentType type) {
    int i;
    union polyType result;
    
    if (type == INT) {
        int max;
        int *tab = (int *)tabPoly;
        
        max = tab[0];
        for (i=1; i<size; i++) {
            if (tab[i] > max) {
                max = tab[i];
            }
        }
        result.i = max;
    } else if (type == DOUBLE) {
        double max;
        double *tab = (double *)tabPoly;
        
        max = tab[0];
        for (i=1; i<size; i++) {
            if (tab[i] > max) {
                max = tab[i];
            }
        }
        result.d = max;
    }
    
    return result;
}

#---------------------------------PREPROCESOR - MAKRO KODU--------------------------------------

$ gcc program.c -E

#---------------------

#include <stdio.h>
#include <stdlib.h>

#define maxLoop(_max) \
        typeof(_max) max; \
        typeof(_max) *tab = (typeof(_max) *)tabPoly; \
        max = tab[0]; \
        for (i=1; i<size; i++) { \
            if (tab[i] > max) { \
                max = tab[i]; \
            } \
        }


enum argumentType {INT, DOUBLE};

union polyType {
    int i;      
    double d;   
};              

union polyType getMax(void *tabPoly, unsigned int size, enum argumentType type);  //*tabPoly | Poly - polimorfizm


int main(void) {
    int tabOfInts[] = {3,2,1,5,6,4};
    double tabOfDoubles[] = {3.3, 2.2, 1.1, 5.5, 6.6, 4.4};
    union polyType result1, result2;
    
    
    result1 = getMax(tabOfInts, 6, INT);
    result2 = getMax(tabOfDoubles, 6, DOUBLE);
    
    printf("max=%d\n",result1.i);
    printf("max=%f\n",result2.d);
    
    return EXIT_SUCCESS;
}

union polyType getMax(void *tabPoly, unsigned int size, enum argumentType type) {
    int i;
    union polyType result;
    
    if (type == INT) {
        maxLoop(result.i)
        result.i = max;
    } else if (type == DOUBLE) {
        maxLoop(result.d)
        result.d = max;
    }
    
    return result;
}

#-----------------------------------------------------------------------------------------------


#-----------------------------------------------------------------------------------------------

W DOMU
[DOM - zadanie]

getMax
zwrócić wskaźnik void
(void *getMax)

