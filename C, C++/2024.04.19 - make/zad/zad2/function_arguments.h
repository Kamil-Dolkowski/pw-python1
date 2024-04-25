#ifndef FUNCTION_ARGUMENTS
#define FUNCTION_ARGUMENTS

struct argument arguments_constructor(char * name, enum ArgType type, char * dataStr);
void arguments_destructor(struct argument args);

#endif
