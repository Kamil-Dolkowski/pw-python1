#include <stdio.h>
#include <stdlib.h>
#include <string.h>

struct uczen {
    char *imie;
    char *nazwisko;
    int *oceny;
};

int main(void) {
    int choice=0;
    struct uczen uczniowie[1];
    struct uczen *uczniowie_nowi;
    char imie_z[20], nazwisko_z[20];
    char *imie, *nazwisko;
    int liczbaUczniow=0;
    
    
    while (choice != 4) {
        printf("====POLECENIA====\n");
        printf("0 - dodaj studenta\n");
        printf("1 - wyswietl studentow\n");
        printf("2 - dodaj ocene\n");
        printf("3 - usun ocene\n");
        printf("4 - zakoncz program\n");
        printf("Wprowadź polecenie: ");
        scanf("%d",&choice);
        
        switch(choice) {
            case 0:
                printf("Podaj imie: ");
                scanf("%s",imie_z);
                imie = malloc(sizeof(char)*strlen(imie_z));
                for (int i=0;i<strlen(imie_z);i++) {
                    imie[i] = imie_z[i];
                }
                
                printf("Podaj nazwisko: ");
                scanf("%s",nazwisko_z);
                nazwisko = malloc(sizeof(char)*strlen(nazwisko_z));
                for (int i=0;i<strlen(nazwisko_z);i++) {
                    nazwisko[i] = nazwisko_z[i];
                }
                
                liczbaUczniow++;
                uczniowie_nowi = malloc((sizeof(char)+sizeof(char)+sizeof(int))*liczbaUczniow);
                for(int i=0;i<liczbaUczniow-1;i++) {
                    uczniowie_nowi[i] = uczniowie[i];
                }
                for(int i=0;i<liczbaUczniow-1;i++) {
                    uczniowie[i] = uczniowie_nowi[i];
                }
                free(uczniowie_nowi);
                
                uczniowie[liczbaUczniow-1].imie = imie;
                uczniowie[liczbaUczniow-1].nazwisko = nazwisko;
                printf("Dodano ucznia: %s %s\n",uczniowie[liczbaUczniow-1].imie, uczniowie[liczbaUczniow-1].nazwisko);
                
                
                break;
            case 1:
                for (int i=0;i<liczbaUczniow;i++) {
                    printf("Student %d: %s %s\n",i,uczniowie[i].imie,uczniowie[i].nazwisko);
                }
            
                break;
            case 4:
                printf("\nZakonczono program.\n");
                break;
        }
    }
    
    return 0;
}

// Struktura: imie, nazwisko, tablica ocen