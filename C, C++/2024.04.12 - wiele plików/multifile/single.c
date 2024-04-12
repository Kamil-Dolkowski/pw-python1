#include <stdio.h>
#include <stdlib.h>

typedef int TYPE;

struct ImportantStructure {
    TYPE value;
    char * description;
};

void bar(struct ImportantStructure s);
void helperFunction();

int main(void) {
    struct ImportantStructure is;
    bar(is);
    return EXIT_SUCCESS;
}

void bar(struct ImportantStructure s) {
    printf("Function: bar\n");
    helperFunction();
}

void helperFunction() {
    printf("Function: helperFunction\n");
}

