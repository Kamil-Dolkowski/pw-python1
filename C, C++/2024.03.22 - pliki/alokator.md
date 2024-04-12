#------------------------------------TABLICA DYNAMICZNA----------------------------------------

[]
[1] -> [1, ]
[1,2] -> [1,2, , ]
[1,2,3, ]
[1,2,3,4] -> [1,2,3,4, , , , ]

#---------------------------------------WSTĘPNY KOD--------------------------------------------

#include <stdio.h>
#include <stdlib.h>

struct DynamicTable {
    unsigned int size;
    int *elements;
};

int main(void) {
    struct DynamicTable tab;

    //printf("%d\n", tab.elements[0]);   ->   "Naruszenie ochrony pamięci"
    tab.elements = malloc(sizeof(int)*10);
    tab.elements[0] = 1;
    printf("%d\n", tab.elements[0]);
    free(tab.elements);
    printf("%d\n", tab.elements[0]);

    return 0;
}

#--------------------------------------INFO I MESSAGE------------------------------------------

#include <stdio.h>
#include <stdlib.h>

enum InfoCode {ERROR, SUCCESS};

struct Info {
    enum InfoCode code;
};

struct DynamicTable {
    unsigned int size;
    int *elements;
};



void printMessage(struct Info info) {
    switch (info.code) {
        case ERROR:
            printf("Error\n");
            break;
        case SUCCESS:
            printf("Success\n");
            break;
        default:
            printf("Unknown message\n");
            break;
    }
}

struct Info addElement(struct DynamicTable *table, int element) {
    struct Info info = {SUCCESS};
    return info;
}



int main(void) {
    struct DynamicTable tab;
    struct Info result;

    result = addElement(&tab, 3);
    printMessage(result);

    return 0;
}

#----------------------------------------------------------------------------------------------

elem        1   2   3   4   5   6   7   8   9   
size = 0    1   2   4   4   8   8   8   8   16   
idx  = 0    0   1   2   3   4   5   6   7   8

#-----CIEKAWOSTKA----- *

#include <stdio.h>

int main()
{
    int x=4294967295;
    
    printf("%u\n",x);
    printf("%d\n",x);

    return 0;
}

OUTPUT:
4294967295
-1

#----------------------------------STWORZENIE TABLICY (SIZE=0)----------------------------------

#include <stdio.h>
#include <stdlib.h>

enum InfoCode {ERROR, SUCCESS};

struct Info {
    enum InfoCode code;
};

struct DynamicTable {
    unsigned int size;
    unsigned int idx;
    int *elements;
};



void printMessage(struct Info info) {
    switch (info.code) {
        case ERROR:
            printf("Error\n");
            break;
        case SUCCESS:
            printf("Success\n");
            break;
        default:
            printf("Unknown message\n");
            break;
    }
}

void printDynamicTable(struct DynamicTable table) {
    int i;
    printf("size: %u, last element index: %u\n",table.size,table.idx);
    for (i=0; i<=table.idx; i++) {
        printf("[%02d]: %d\n", i, table.elements[i]);
    }
}

struct Info addElement(struct DynamicTable *table, int element) {
    struct Info info = {SUCCESS};

    //printf("%d\n",(*table).size);     inna wersja tego, co niżej
    //printf("%d\n", table->size);
    if (table->size == 0) {
        table->elements = malloc(sizeof(int)*1);
        if (table->elements == NULL) {
            info.code = ERROR;
            return info;
        }
        table->size = 1;
        table->idx = 0;
        table->elements[table->idx] = element;
    }

    return info;
}



int main(void) {
    struct DynamicTable tab = {0,0,NULL};
    struct Info result;

    result = addElement(&tab, 3);
    printMessage(result);
    printDynamicTable(tab);

    return 0;
}

#-------------------------------POWIĘKSZANIE TABLICY (SIZE>0)----------------------------------

#include <stdio.h>
#include <stdlib.h>

enum InfoCode {ERROR, SUCCESS};

struct Info {
    enum InfoCode code;
};

struct DynamicTable {
    unsigned int size;
    unsigned int idx;
    int *elements;
};



void printMessage(struct Info info) {
    switch (info.code) {
        case ERROR:
            printf("Error\n");
            break;
        case SUCCESS:
            printf("Success\n");
            break;
        default:
            printf("Unknown message\n");
            break;
    }
}

void printDynamicTable(struct DynamicTable table) {
    int i;
    printf("size: %u, last element index: %u\n",table.size,table.idx);
    for (i=0; i<=table.idx; i++) {
        printf("[%02d]: %d\n", i, table.elements[i]);
    }
}

struct Info addElement(struct DynamicTable *table, int element) {
    struct Info info = {SUCCESS};
    int *newTable;
    int i;

    //printf("%d\n",(*table).size);     inna wersja tego, co niżej
    //printf("%d\n", table->size);
    if (table->size == 0) {
        table->elements = malloc(sizeof(int)*1);
        if (table->elements == NULL) {
            info.code = ERROR;
            return info;
        }
        table->size = 1;
        table->idx = 0;
        (table->elements)[table->idx] = element;
    } else {
        if (table->idx<(table->size)-1) {
            table->idx += 1;
            (table->elements)[table->idx] = element;
        } else {
            printf("Resize\n");
            newTable = malloc(sizeof(int) * (table->size) * 2);
            for(i=0; i<(table->size); i++) {
                newTable[i] = table->elements[i];
            }
            table->size *= 2;
            table->idx += 1;
            free(table->elements);
            table->elements = newTable;
            (table->elements)[table->idx] = element;
        }
    }

    return info;
}



int main(void) {
    struct DynamicTable tab = {0,0,NULL};
    struct Info result;

    result = addElement(&tab, 3);
    printMessage(result);
    printDynamicTable(tab);

    result = addElement(&tab, 5);
    printMessage(result);
    printDynamicTable(tab);

    result = addElement(&tab, 7);
    printMessage(result);
    printDynamicTable(tab);

    result = addElement(&tab, 9);
    printMessage(result);
    printDynamicTable(tab);

    result = addElement(&tab, 11);
    printMessage(result);
    printDynamicTable(tab);

    result = addElement(&tab, 13);
    printMessage(result);
    printDynamicTable(tab);

    result = addElement(&tab, 15);
    printMessage(result);
    printDynamicTable(tab);

    return 0;
}

#-----------------------------------------TYPEDEF---------------------------------------------

#include <stdio.h>
#include <stdlib.h>

typedef int Element;

enum InfoCode {ERROR, SUCCESS};

struct Info {
    enum InfoCode code;
};

struct DynamicTable {
    unsigned int size;
    unsigned int idx;
    Element *elements;
};



void printMessage(struct Info info) {
    switch (info.code) {
        case ERROR:
            printf("Error\n");
            break;
        case SUCCESS:
            printf("Success\n");
            break;
        default:
            printf("Unknown message\n");
            break;
    }
}

void printDynamicTable(struct DynamicTable table) {
    int i;
    printf("size: %u, last element index: %u\n",table.size,table.idx);
    for (i=0; i<=table.idx; i++) {
        printf("[%02d]: %d\n", i, table.elements[i]);
    }
}

struct Info addElement(struct DynamicTable *table, int element) {
    struct Info info = {SUCCESS};
    Element *newTable;
    int i;

    //printf("%d\n",(*table).size);     inna wersja tego, co niżej
    //printf("%d\n", table->size);
    if (table->size == 0) {
        table->elements = malloc(sizeof(int)*1);
        if (table->elements == NULL) {
            info.code = ERROR;
            return info;
        }
        table->size = 1;
        table->idx = 0;
        (table->elements)[table->idx] = element;
    } else {
        if (table->idx<(table->size)-1) {
            table->idx += 1;
            (table->elements)[table->idx] = element;
        } else {
            printf("Resize\n");
            newTable = malloc(sizeof(int) * (table->size) * 2);
            for(i=0; i<(table->size); i++) {
                newTable[i] = table->elements[i];
            }
            table->size *= 2;
            table->idx += 1;
            free(table->elements);
            table->elements = newTable;
            (table->elements)[table->idx] = element;
        }
    }

    return info;
}



int main(void) {
    struct DynamicTable tab = {0,0,NULL};
    struct Info result;

    result = addElement(&tab, 3);
    printMessage(result);
    printDynamicTable(tab);

    result = addElement(&tab, 5);
    printMessage(result);
    printDynamicTable(tab);

    result = addElement(&tab, 7);
    printMessage(result);
    printDynamicTable(tab);

    result = addElement(&tab, 9);
    printMessage(result);
    printDynamicTable(tab);

    result = addElement(&tab, 11);
    printMessage(result);
    printDynamicTable(tab);

    result = addElement(&tab, 13);
    printMessage(result);
    printDynamicTable(tab);

    result = addElement(&tab, 15);
    printMessage(result);
    printDynamicTable(tab);

    return 0;
}

#----------------------------------------------------------------------------------------------
