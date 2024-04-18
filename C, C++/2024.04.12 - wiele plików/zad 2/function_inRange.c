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