#----------------------------------TRUE / FALSE------------------------------------

#include <stdio.h>

enum boolean {TRUE, FALSE};

int main() {
    enum boolean x;
    
    x = TRUE;
    
    printf("%d\n", x);
    
    if (x == TRUE) {
        printf("!!!\n");
    }
    


    x = 123;
    
    printf("%d\n", x);
    
    return 0; 
}

#---------------------------------DNI TYGODNIA-------------------------------------

#include <stdio.h>

enum boolean {TRUE, FALSE};
enum dniTygodnia {PN, WT, SR, CZ, PT, SOB, NDZ};

int main() {
    enum boolean x;
    
    enum dniTygodnia dzien;
    
    dzien = PT;
    
    switch(dzien) {
        case PN:
            printf("Poniedziałek");
            break;
        case WT:
            printf("Wtorek");
            break;
        case SR:
            printf("Środa");
            break;
        case CZ:
            printf("Czwartek");
            break;
        case PT:
            printf("Piątek");
            break;
        case SOB:
            printf("Sobota");
            break;
        case NDZ:
            printf("Niedziela");
            break;
    }
    
    return 0; 
}

#-----------------------------------ZADANIE----------------------------------------

// tab 2D 2x3
// poprosic użytk o wartosci tabl

#-------------------------

#include <stdio.h>

int main() {
    int t[2][3];
    int r,c,x;
    
    for (r=0; r<2; r++) {
        for (c=0; c<3; c++) {
            printf("Podaj wartosc: ");
            scanf("%d",&x);
            t[r][c] = x;
        }
    }
    
    printf("\nTABLICA\n");
    
    for (r=0; r<2; r++) {
        for (c=0; c<3; c++) {
            printf("%d ",t[r][c]);
        }
        printf("\n");
    }
    
    return 0; 
}