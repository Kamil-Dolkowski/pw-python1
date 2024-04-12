#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char ** argv){
    char * option;

    option = argv[1];
  
    printf("argv[1] = %s\n", option);
    printf("argv[1][2] = %c\n", option[2]);
    
    if (strcmp(option, "opcja1") == 0) {
        printf("Wybrano opcje1");
    }
 
    return EXIT_SUCCESS;
}


//--------------------------------INNY SPOSÓB-----------------------------------

#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(int argc, char **argv) {
    char *option;
    
    option = malloc(strlen(argv[1]) + 1);
    strcpy(option, argv[1]);
    
    if (strcmp(option, "opcja1") == 0) {
        printf("Wybrano opcje1");
    } else {
        printf("argv[1] = %s",option);
    }
    
    free(option);
    return 0;
}
