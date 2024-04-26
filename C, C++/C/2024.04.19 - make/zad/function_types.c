#include <stdio.h>
#include <string.h>

#include "function_types.h"

struct argument arguments_constructor(char * name, enum ArgType type, char * dataStr) {
    struct argument arg;
    char bufferMain[32];
    char * buffer;
    int len;

    arg.type = type;
    arg.name = name;

    sprintf(bufferMain, "%s", dataStr);
    len = strlen(bufferMain);
    buffer = malloc(sizeof(int)*(len+1));
    strcpy(buffer, bufferMain);
    arg.value = buffer;

    return arg;
}