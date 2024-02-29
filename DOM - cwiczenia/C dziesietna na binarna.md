#include <stdio.h>

int main()
{
    unsigned char x=4;  
    int t[8];
    int i,y;
    y = x;
    for (i=0;i<8;i++) {
        if (y != 0) {
            t[i] = y % 2;
            y = y/2;
        } else {
            t[i] = 0;
        }
    }
    
    for (i=7;i>=0;i--) {
        printf("%d", t[i]);
    }

    return 0;
}