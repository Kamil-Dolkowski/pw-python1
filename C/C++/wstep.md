#include <stdio.h>      (lub "stdio.h" -> bieżąca ścieżka pliku/katalogu)

int main() {
    printf("Witaj swiecie\n");
    return 0;
}


#---------------------IF----------------------

if (!(x>5)) {

} else {
    if (...) {

    }
}



|| - or
&& - and

#-------------------FOR-----------------------

for (i=0; i<5; i++) {

}



i = 3;
x = ++i;   // 4
y = i++;   // 4

#---------------------------------------------

int main () {
    int i;

}



for (int i=0; i<5; i++) {

}

#-------------WHILE / DO WHILE----------------

while () {

}


do {

} while ();

#---------------ZAD. CHOINKA------------------

*
**
***
****
*****

#---program----

#include <stdio.h>

int main()
{
    int i;
    int j;
    for (i=0; i<5; i++) {
        for (j=0; j<i;j++) {
            printf("*");
        }
        printf("*\n");
    }
    
    return 0;
}

#-----------------SWITCH---------------------

switch (x) {
    case 1:
        ..
    case 2:
        ..
        break;
    case 5:
        ..
}



switch (x) {
    case .. :
        ..
    default:    // inna (niewymieniona) opcja x'a
        ..
}

#----------ZAD. CHOINKA (SWITCH)-------------

#include <stdio.h>

int main()
{
    int i;
    for (i=0; i<5; i++) {
            switch (i) {
                case 4:
                    printf("*");
                case 3:
                    printf("*");
                case 2:
                    printf("*");
                case 1:
                    printf("*");
                case 0:
                    printf("*");
            }
        printf("\n");
    }    
    return 0;
}
