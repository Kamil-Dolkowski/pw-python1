#-----------WARTOSC MAX CHAR'A [W BITACH]----------------

#include <stdio.h>
#include <limits.h>

int main()
{
    printf("%d\n", CHAR_BIT);
    return 0;
}

#-------------WARTOSC MAX INT'A [W BITACH]----------------

#include <stdio.h>
#include <limits.h>

int main()
{
    printf("%d\n", INT_MAX);
    return 0;
}

#-----------NA ILU BAJTACH ZAPISANY JEST CHAR--------------

#include <stdio.h>
#include <limits.h>

int main()
{
    printf("%d\n", sizeof(char));
    return 0;
}
\\wypisze wartość i ostrzeżenie



#include <stdio.h>
#include <limits.h>

int main()
{
    printf("%ld\n", sizeof(char));
    return 0;
}
\\wypisze wartość

#------------------PRZESUNIECIA BITOWE---------------------

            |
x = 0000 0000
? = 0000 0001
    0000 0001  OR

#-------------------------

#include <stdio.h>
#include <limits.h>

int main()
{
    char x;              
    x=0;                    //0000 0000
    printf("%d\n", x);
    x = x | 1;              //0000 0001
    printf("%d\n", x);
    x = x << 1;             //0000 0010
    printf("%d\n", x);
    x = x | 1;              //0000 0011
    printf("%d\n", x);
    
    
    x = x << 7;             
    printf("%d\n", x);
    x = x >> 7;             
    printf("%d\n", x);

    return 0;
}

OUTPUT:
0
1
2
3
-128
-1

#-------------------------

#include <stdio.h>
#include <limits.h>

int main()
{
    unsigned char x;              
    x=0;                    //0000 0000
    printf("%d\n", x);
    x = x | 1;              //0000 0001
    printf("%d\n", x);
    x = x << 1;             //0000 0010
    printf("%d\n", x);
    x = x | 1;              //0000 0011
    printf("%d\n", x);
    
    
    x = x << 7;             
    printf("%d\n", x);
    x = x >> 7;             
    printf("%d\n", x);

    return 0;
}

OUTPUT:
0
1
2
3
128
1

#---------------------------------------------------------

00000100    - > 11111011 -> 251
00100100
00000000
  |  |


char x;
x = 0;
x = x | (4+32);

#-----------------------

#include <stdio.h>
#include <limits.h>

int main()
{
    char x;
    x = 0;
    x = x | (4+32);    
    printf("%d\n", x);
    x = x & 251;
    printf("%d\n", x);
    x = ~x;
    printf("%d\n", x);

    return 0;
}

OUTPUT:
36
32
-33

#------------------------%d \ %c--------------------------

"%d\n" - liczba
"%c\n" - znak [ASCII]

#---------------------------------------------------------

char x jako ciąg 0 i 1 -> 00001100
x=12


[niedokończone]

#include <stdio.h>
#include <limits.h>

int main()
{
    char x=12, i;
    //0000 1100
    
    x = x | 1;
    
    printf("%d\n", x);
    
    for (i=0; i<8; i++) {
        
    }
    
    
    return 0;
}

#---------------------------------------------------------
#---------------------------------------------------------