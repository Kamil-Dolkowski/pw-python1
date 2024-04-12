#---------------------OD 0 DO 255-----------------------

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



#--------------------UZUPELNIENIE DO 2 (OD -128 DO 127)----------------------


#include <stdio.h>

int main()
{
    int x=0;  
    int t[8],t1[8];
    int i,y,check=0;
    y = x;
    if (y > 0) {
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
    } else {
        y = -x;
        for (i=0;i<8;i++) {
            if (y != 0) {
                t[i] = y % 2;
                y = y/2;
            } else {
                t[i] = 0;   
            }
        }
        
        for (i=0;i<8;i++) {
            if (check == 0) {
                if (t[i] == 1) {
                    
                    check = 1;
                }
                t1[i] = t[i];
        } else {
            if (t[i] == 1) {
                t1[i] = 0;
            } else {
                t1[i] = 1;
            }
        }
        }
        for (i=7;i>=0;i--) {
            printf("%d", t1[i]);
        }
    }
    return 0;
}