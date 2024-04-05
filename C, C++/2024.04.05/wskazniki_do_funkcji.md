#----------------------------WSKAŹNIK NA FUNKCJĘ----------------------------------

#include <stdio.h>
#include <stdlib.h>

void foo1(void) {
    printf("I'm function 1\n");
}

void foo2(void) {
    printf("I'm function 2\n");
}

int main(void) {
    void (*f)(void);
    
    foo1();
    foo2();
    
    f = foo1;
    f();
    
    return EXIT_SUCCESS;
}

#---------------------------------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>

void none(void) {
    printf("I'm function NONE\n");
}

void foo1(void) {
    printf("I'm function 1\n");
}

void foo2(void) {
    printf("I'm function 2\n");
}

int main(int argc, char **argv) {
    switch (argc) {
        case 1:
            foo1();
            break;
        case 2:
            foo2();
            break;
        default:
            none();
            break;
    }
    
    return EXIT_SUCCESS;
}

#---------------------------------------------------------------------------------

#include <stdio.h>
#include <stdlib.h>

void none(void) {
    printf("I'm function NONE\n");
}

void foo1(void) {
    printf("I'm function 1\n");
}

void foo2(void) {
    printf("I'm function 2\n");
}

int main(int argc, char **argv) {
    void (*f[])(void) = {none, foo1, foo2};
    
    if (argc > 2) {
        argc = 0;
    }
    f[argc]();
    
    return EXIT_SUCCESS;
}

#---------------------------------------------------------------------------------



#---------------------------------------------------------------------------------