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


     printf("%s %d %s\n", args[0].name, args[0].type, args[0].value);

      printMin(tab, args, 1);
      //printMin(tab, 7);
      free(args[0].value);
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
		
			// inRange min
			args[0] = arguments_constructor("min", INT, "1");

			// inRange max
			args[1] = arguments_constructor("max", INT, "4");
			// inRange minInclude
		        args[2] = arguments_constructor("min", BOOL, "T");
			// inRange maxInclude
			args[3] = arguments_constructor("max", BOOL, "T");

			// data tab size
			args[4] = arguments_constructor("size", INT, "7");

			 printf("%s %d %s\n", args[0].name, args[0].type, args[0].value);

      			 printf("%s %d %s\n", args[1].name, args[1].type, args[1].value);
			 printf("%s %d %s\n", args[2].name, args[2].type, args[2].value);

		        printInRange(tab, args, 5);
			//printInRange(tab, min, max, minInclude, maxInclude);
			
			free(args[0].value);  //argument_destructor(args[0]);
			free(args[1].value);
			free(args[2].value);
			free(args[3].value);
			free(args[4].value);
		}
	}
	return EXIT_SUCCESS;
}

