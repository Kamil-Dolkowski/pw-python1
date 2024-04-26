#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#include "function_types.h"
#include "function_min.h"
#include "function_inrange.h"
#include "function_arguments.h"


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

/*
      args[0].type = INT;
      args[0].name = "size";

      sprintf(bufferMain, "%d", 7);
      len = strlen(bufferMain);
      buffer = malloc(sizeof(int)*(len+1));
      strcpy(buffer, bufferMain);
      args[0].value = buffer;
*/
      //args[0] = arguments_constructor("size", INT, dataStr)
      args[0] = arguments_constructor("size", INT, "7");

      printMin(tab, args, 1);
      //printMin(tab, 7);
      arguments_destructor(args[0]);
		}
	} else if (argc == 6) {
		if (!strcmp(argv[1], "inRange")){
			bool minInclude, maxInclude;
			int min, max;

			if (strcmp(argv[4], "T") && strcmp(argv[4], "F")) {
				printf("Bad program call\n");
				return EXIT_FAILURE;
			}
			
			if (strcmp(argv[5], "T") && strcmp(argv[5], "F")) {
				printf("Bad program call\n");
				return EXIT_FAILURE;
			}
			
			struct argument args[5];
                        char * buffer;
		
		    // data tab size
			args[0] = arguments_constructor("size", INT, "7");
			// inRange min
			args[1] = arguments_constructor("min", INT, argv[2]);
			// inRange max
			args[2] = arguments_constructor("max", INT, argv[3]);
			// inRange minInclude
		    args[3] = arguments_constructor("min", BOOL, argv[4]);
			// inRange maxInclude
			args[4] = arguments_constructor("max", BOOL, argv[5]);
			
			
		    printInRange(tab, args, 5);
			//printInRange(tab, min, max, minInclude, maxInclude);
			
			arguments_destructor(args[0]);  //argument_destructor(args[0]);
			arguments_destructor(args[1]);
			arguments_destructor(args[2]);
			arguments_destructor(args[3]);
			arguments_destructor(args[4]);
		}
	}
	return EXIT_SUCCESS;
}

