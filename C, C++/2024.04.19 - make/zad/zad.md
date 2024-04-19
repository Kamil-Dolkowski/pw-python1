
#-------------------MAIN.C----------------------

#include <stdlib.h>
#include <stdio.h>
#include <stdbool.h>
#include <string.h>

#include "function_types.h"
#include "function_min.h"
#include "function_inRange.h"

int main(int argc, char ** argv) {
                   //0  1  2  3  4  5  6
        int tab[] = {5, 1, 2, 7, 3, 4, 6};
        int len;
        char bufferMain[32];

        if (argc == 1) {
                printf("Bad program call\n");
        } else if (argc == 2) {
                if (!strcmp(argv[1], "min")){
                        struct argument args[1];
                        char * buffer;

                        args[0].type = INT;
                        args[0].name = "size";
                        sprintf(bufferMain, "%d", 7);
                        len = strlen(bufferMain);
                        buffer = malloc(sizeof(int)*(len+1));
                        strcpy(buffer, bufferMain);
                        args[0].value = buffer;

                        printMin(tab, args, 1);
                        //printMin(tab, 7);
                        free(buffer);
                }
        } else if (argc == 6) {
                if (!strcmp(argv[1], "inRange")){
                        bool minInclude, maxInclude;
                        int min, max;

                        if (!strcmp(argv[4], "T")) {
                                minInclude = true;
                        } else if (!strcmp(argv[4], "F")) {
                                minInclude = false;
                        } else {
                                printf("Bad program call\n");
                                return EXIT_FAILURE;
                        }

                        if (!strcmp(argv[5], "T")) {
                                maxInclude = true;
                        } else if (!strcmp(argv[5], "F")) {
                                maxInclude = false;
                        } else {
                                printf("Bad program call\n");
                                return EXIT_FAILURE;
                        }

                        min = atoi(argv[2]);
                        max = atoi(argv[3]);

                        struct  argument args[5];
                        char * buffer;

                        args[0].type = INT;
                        args[0].name = "size";
                        sprintf(bufferMain, "%d", 7);
                        len = strlen(bufferMain);
                        buffer = malloc(sizeof(int)*(len+1));
                        strcpy(buffer, bufferMain);
                        args[0].value = buffer;

                        args[1].type = INT;
                        args[1].name = "min";
                        sprintf(bufferMain, "%d", min);
                        len = strlen(bufferMain);
                        buffer = malloc(sizeof(int)*(len+1));
                        strcpy(buffer, bufferMain);
                        args[1].value = buffer;

                        args[2].type = INT;
                        args[2].name = "max";
                        sprintf(bufferMain, "%d", max);
                        len = strlen(bufferMain);
                        buffer = malloc(sizeof(int)*(len+1));
                        strcpy(buffer, bufferMain);
                        args[2].value = buffer;

                        args[3].type = BOOL;
                        args[3].name = "minInclude";
                        sprintf(bufferMain, "%d", minInclude);
                        len = strlen(bufferMain);
                        buffer = malloc(sizeof(int)*(len+1));
                        strcpy(buffer, bufferMain);
                        args[3].value = buffer;

                        args[4].type = BOOL;
                        args[4].name = "maxInclude";
                        sprintf(bufferMain, "%d", maxInclude);
                        len = strlen(bufferMain);
                        buffer = malloc(sizeof(int)*(len+1));
                        strcpy(buffer, bufferMain);
                        args[4].value = buffer;

                        printInRange(tab, args, 5);
                        //printInRange(tab, min, max, minInclude, maxInclude);
                        free(buffer);
                }
        }
        return EXIT_SUCCESS;
}

#-------------------FUNCTION_INRANGE.C----------------------

#include <stdbool.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#include "function_types.h"

void printInRange(int * tab, struct argument * args, int size){
        int min, max;
        bool minInclude, maxInclude;
        int i;

        min = atoi(args[1].value);
        max = atoi(args[2].value);
        
        minInclude = atoi(args[3].value);
        maxInclude = atoi(args[4].value);
        
        
        if (!minInclude){ 
                min += 1;
        }

        if (!maxInclude){ 
                max -= 1;
        }

        for(i=min; i<=max; i++){
                printf("%d ", tab[i]);
        }
        printf("\n");
}

#-------------------FUNCTION_INRANGE.H----------------------

#ifndef FUNCTION_INRANGE
#define FUNCTION_INRANGE

void printInRange(int * tab, struct argument * args, int size);
//void printInRange(int * tab, int min, int max, bool minInclude, bool maxInclude);

#endif

#---------------------FUNCTION_MIN.C------------------------

#include <stdio.h>
#include <stdlib.h>

#include "function_types.h"

void printMin(int * tab, struct argument * args, int size){
        int i;
        int sizeTab;
        int min;

        sizeTab = atoi(args[0].value);
        printf("%s %d\n", args[0].name, sizeTab);

        min = tab[0];

        for(i=1; i<sizeTab; i++){
                if (tab[i]<min){
                        min = tab[i];
                }
        }

        printf("min=%d\n", min);
}

#---------------------FUNCTION_MIN.H------------------------

#ifndef FUNCTION_MIN
#define FUNCTION_MIN

/*
enum ArgType {INT, BOOL};

struct argument {
    char * name;
    enum ArgType type;
    char * value;
};
*/

void printMin(int * tab, struct argument * args, int size);
//void printMin(int * tab, int size);

#endif

#-------------------FUNCTION_TYPES.H-----------------------

#ifndef FUNCTION_TYPES
#define FUNCTION_TYPES

enum ArgType {INT, BOOL};

struct argument {
    char * name;
    enum ArgType type;
    char * value;
};

#endif