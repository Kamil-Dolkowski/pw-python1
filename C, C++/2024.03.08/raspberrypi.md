użytkownik 4, komputer 1

192.168.48.3   - 1  (1-10)
192.168.48.4   - 2  (11-20)

ssh u04@192.168.48.3

password: u04

#------------------------------------------------

Putty - program


putty.exe (the SSH and Telnet client itself)
64-bit x86:     putty.exe       (signature) 
                    ^

#------------------------------------------------

$ gcc program.c                     (kompilacja programu)
$ gcc program.c -o super_program    (zmiana programu wywołującego z a.out na super_program)
$ ./super_program                   (wywołanie programu)
$ ./a.out                           (wywołanie programu) [działa]

$ gcc -E program.c                  (podgląd jak przetwarza procesor (gdzie wstawia #define) )

#-------------------------------ZADANIE - TABLICA STRUKTUR--------------------------------  !!

1. struktura z 2 składowymi;
    int x
    int y
2. tablica zawierająca 10 takich struktur

#-------------KOD---------------

  GNU nano 7.2                                                         program.c
#include <stdio.h>
#include <time.h>
#include <stdlib.h>

struct skladowe {
  int x;
  int y;
};

void wypisz(struct skladowe s) {
  printf("%d %d\n", s.x, s.y);
}

void los(struct skladowe t[10]) {
  for (int i=0; i<10; i++) {
    t[i].x = rand();
    t[i].y = rand();
  }
}

int main() {
  struct skladowe tab[10];
  srand(time(NULL));
  los(tab);

  for (int i=0; i<10; i++) {
    printf("tab[%d]: %d %d\n", i, tab[i].x, tab[i].y);
  }

  return 0;
}

#-----------------------------------------------------------------------------------------
//inicjowanie konkretnego indexu tablicy

#include <stdio.h>

struct skladowe {
  int x;
  int y;
};

void wypisz(struct skladowe s) {
  printf("%d %d\n", s.x, s.y);
}

void init(struct skladowe tab[], int index) {
  tab[index].x = 123;
  tab[index].y = 456;
}

int main() {
  struct skladowe tab[10];

  init(tab, 5);

  wypisz(tab[2]);
  wypisz(tab[5]);

  return 0;
}

#------------------------------------LOSOWE 0-100-----------------------------------------

#include <stdio.h>
#include <time.h>
#include <stdlib.h>

#define TAB_SIZE 10

struct skladowe {
  int x;
  int y;
};

void wypisz(struct skladowe s) {
  printf("%d %d\n", s.x, s.y);
}

void init(struct skladowe tab[], int index) {
  tab[index].x = rand()%101;
  tab[index].y = rand()%101;
}

int main() {
  struct skladowe tab[10];
  srand(time(NULL));
  int i;

  for (i=0; i<TAB_SIZE; i++) {
    init(tab,i);
  }

  for (i=0; i<TAB_SIZE; i++) {
    wypisz(tab[i]);
  }

  return 0;
}

#-----------------------------------ZAD Z FUNKCJAMI----------------------------------------

Funkcje:
1.wypisz wszystkie elementy
2.wyjscie z programu
3.podanie wartosci dla danego elementu

#----------------------------ZAD Z FUNKCJAMI (mój program)---------------------------------

#include <stdio.h>
#include <time.h>
#include <stdlib.h>

#define TAB_SIZE 10

//enum polecenie {PRINT, EXIT, INDEX};

struct skladowe {
  int x;
  int y;
};

void wypisz(struct skladowe s) {
  printf("%d %d\n", s.x, s.y);
}

void init(struct skladowe tab[], int index) {
  tab[index].x = 0;
  tab[index].y = 0;
}

void indexTab(struct skladowe tab[], int index, int x, int y) {
  tab[index].x = x;
  tab[index].y = y;
}

void wypiszTab(struct skladowe tab[]) {
  for (int i=0; i<TAB_SIZE; i++) {
    wypisz(tab[i]);
  }
}

int main() {
  struct skladowe tab[10];
  srand(time(NULL));
  int i;
  int polecenie=0, index, x, y;

  //wyzerowanie tablicy
  for (i=0; i<TAB_SIZE; i++) {
    init(tab,i);
  }

  while(polecenie != 2) {
    printf("\n=========POLECENIA=========\n");
    printf("0 - podanie wartosci dla danego elementu tablicy\n");
    printf("1 - wypisz wszystkie elementy tablicy\n");
    printf("2 - wyjscie z programu\n");
    printf("Podaj polecenie: ");
    scanf("%d",&polecenie);

    switch (polecenie) {
      case 0:
        printf("\nPodaj index: ");
        scanf("%d",&index);
        printf("Podaj x: ");
        scanf("%d",&x);
        printf("Podaj y: ");
        scanf("%d",&y);
        indexTab(tab,index,x,y);
        printf("\nWpisano: tab[%d] = [%d,%d]\n",index,x,y);
        break;
      case 1:
        wypiszTab(tab);
        break;
      case 2:
        break;
      default:
        polecenie = 2;
        break;
    }
  }

  return 0;
}

#----------------------------ZAD Z FUNKCJAMI (Pana program)--------------------------------- [string]

#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define TAB_SIZE 10

enum option {CONTINUE,QUIT};

struct skladowe {
  int x;
  int y;
};

void wypisz(struct skladowe s) {
  printf("%d %d\n", s.x, s.y);
}

void init(struct skladowe tab[], int index) {
  tab[index].x = 0;
  tab[index].y = 0;
}

enum option menu() {
  char buffer[32];

  printf("[a] Wypisz wszystkie\n");
  printf("[s] Ustaw wybrany\n");
  printf("[q] Wyjscie\n");
  printf("Podaj opcje: ");

  //scanf("%s", buffer);
  fgets(buffer,4,stdin);
  buffer[strlen(buffer)-1] = '\0';      //skrócenie o ostatni znak (tutaj znak ENTER ['\n'])


  printf("Dokonany wybór: %s\n", buffer);

  if (strcmp(buffer, "a") == 0) {
    printf("Opcja [a]\n");
  } else if (strcmp(buffer, "s") == 0) {
    printf("Opcja [s]\n");
  } else if (strcmp(buffer, "q") == 0) {
    return QUIT;
  }

  return CONTINUE;
}

int main() {
  srand(time(NULL));

  struct skladowe tab[10];
  int i;
  enum option choice = CONTINUE;

  //wyzerowanie tablicy
  for (i=0; i<TAB_SIZE; i++) {
    init(tab,i);
  }

  while(choice == CONTINUE) {
    choice = menu();
  }

  return 0;
}

#-----------------------------------------------------------------------------------------

fgets(buffer,2,stdin);

#-----------------------------------------------------------------------------------------

4.wypełnij pierwszy lepszy [pusty]
5.wyczyść element
6.statystyka - najmniejszy i największy x,y; średnia z niezerowych x i y






#include <stdio.h>
#include <time.h>
#include <stdlib.h>

#define TAB_SIZE 10

//enum polecenie {PRINT, EXIT, INDEX};

struct skladowe {
  int x;
  int y;
};

void wypisz(struct skladowe s) {
  printf("[%d, %d]\n", s.x, s.y);
}

void init(struct skladowe tab[], int index) {
  tab[index].x = 0;
  tab[index].y = 0;
}

void indexTab(struct skladowe tab[], int index, int x, int y) {
  tab[index].x = x;
  tab[index].y = y;
}

void wypiszTab(struct skladowe tab[]) {
  for (int i=0; i<TAB_SIZE; i++) {
    printf("tab[%d]: ",i);
    wypisz(tab[i]);
  }
}

void max(struct skladowe tab[]) {
    int max_x=0, max_y=0;
    for (int i=0; i<TAB_SIZE; i++) {
        if (tab[i].x > max_x) max_x = tab[i].x;
        if (tab[i].y > max_y) max_y = tab[i].y;
    }
    printf("\nMaksymalny x: %d\n",max_x);
    printf("Maksymalny y: %d\n",max_y);
}

void min(struct skladowe tab[]) {       //nie działa
    int min_x=0, min_y=0;
    for (int i=0; i<TAB_SIZE; i++) {
        if (!(t[i].x == 0 && t[i].y == 0)) {
            if (tab[i].x < min_x) min_x = tab[i].x;
            if (tab[i].y < min_y) min_y = tab[i].y;
        }
    }
    printf("\nMaksymalny x: %d\n",max_x);
    printf("Maksymalny y: %d\n",max_y);
}

void menu() {
    
}

int main() {
  struct skladowe tab[10];
  srand(time(NULL));
  int i;
  int polecenie=0, index, x, y, found=0;

  //wyzerowanie tablicy
  for (i=0; i<TAB_SIZE; i++) {
    init(tab,i);
  }

  while(polecenie != 5) {
    printf("\n======================POLECENIA======================\n");
    printf("0 - wypisz wszystkie elementy tablicy\n");
    printf("1 - podanie wartosci dla danego elementu tablicy\n");
    printf("2 - wypelnij pierwszy wolny element\n");
    printf("3 - wyczysc element\n");
    printf("4 - statystyka\n");
    printf("5 - wyjscie z programu\n");
    printf("\nPodaj polecenie: ");
    scanf("%d",&polecenie);

    switch (polecenie) {
      case 0:
        printf("\n");
        wypiszTab(tab);
        break;
      case 1:
        printf("\nPodaj index: ");
        scanf("%d",&index);
        printf("Podaj x: ");
        scanf("%d",&x);
        printf("Podaj y: ");
        scanf("%d",&y);
        indexTab(tab,index,x,y);
        printf("\n  Wpisano: tab[%d] = [%d,%d]\n",index,x,y);
        break;
      case 2:
        printf("\nPodaj x: ");
        scanf("%d",&x);
        printf("Podaj y: ");
        scanf("%d",&y);
        for (i=0; i<10; i++) {
            if (tab[i].x == 0 && tab[i].y == 0) {
                index = i;
                found = 1;
                indexTab(tab, index, x, y);
                printf("\n  Wpisano w tab[%d] = [%d,%d]\n",index,x,y);
                break;
            }
        }
        if (found == 0) printf("    Nie znaleziono pustego elementu.\n");
        found = 0;
        break;
      case 3:
        printf("\nPodaj index: ");
        scanf("%d",&index);
        init(tab, index);
        printf("\n  Wyczyszczono element tab[%d]\n",index);
        break;
      case 4:
        max(tab);
        
        break;
      case 5:
        printf("\n  Zakonczono program.");
        break;
      default:
        polecenie = 2;
        break;
    }
  }

  return 0;
}





#------------------------------------------------------------------------------------------ Niedokończone



#include <stdio.h>
#include <time.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

#define TAB_SIZE 10
#define MENU_SIZE 3

enum optionCode {UNDEFINED, PRINT_ALL, SET_SELECTED, SET_FREE, RESET, PRINT_STAT, QUIT};

struct skladowe {
  int x;
  int y;
};

struct option {
  enum option code;
  char letter[2];
  char text[32];
};

struct option options[MENU_SIZE] = {
  {PRINT_ALL, "a", "Wypisz wszystkie"},
  {SET_SELECTED, "s", "Ustaw wybrany"},
  {QUIT, "q", "Wyjscie"}
};

void wypisz(struct skladowe s) {
  printf("%d %d\n", s.x, s.y);
}

void init(struct skladowe tab[], int index) {
  tab[index].x = 0;
  tab[index].y = 0;
}

enum optionCode menu() {
  char buffer[5];
  int i;

  for (i=0; i<MENU_SIZE, i++) {
    printf("[%s] %s\n", options[i].letter, options[i].text);
  }
/*
  printf("[a] Wypisz wszystkie\n");
  printf("[s] Ustaw wybrany\n");
  printf("[q] Wyjscie\n");
  printf("Podaj opcje: ");
*/
  //scanf("%s", buffer);
  fgets(buffer,4,stdin);
  buffer[strlen(buffer)-1] = '\0';

  printf("Dokonany wybór: %s\n", buffer);

  for (i=0; i<MENU_SIZE; i++) {
    if(strcmp(buffer, options[i].letter) == 0) {
      return options[i].code;
    }
  }

  return UNDEFINED;
}

void executeAction(enum optionCode choice) {

}

int main() {
  srand(time(NULL));

  struct skladowe tab[10];
  int i;
  enum option choice = CONTINUE;

  //wyzerowanie tablicy
  for (i=0; i<TAB_SIZE; i++) {
    init(tab,i);
  }

  while(choice == CONTINUE) {
    choice = menu();
  }

  return 0;
}






























#include <stdio.h>
#include <time.h>
#include <stdlib.h>

#define TAB_SIZE 10

//enum polecenie {PRINT, EXIT, INDEX};

struct skladowe {
  int x;
  int y;
};

void wypisz(struct skladowe s) {
  printf("[%d, %d]\n", s.x, s.y);
}

void init(struct skladowe tab[], int index) {
  tab[index].x = 0;
  tab[index].y = 0;
}

void indexTab(struct skladowe tab[], int index, int x, int y) {
  tab[index].x = x;
  tab[index].y = y;
}

void wypiszTab(struct skladowe tab[]) {
  for (int i=0; i<TAB_SIZE; i++) {
    printf("tab[%d]: ",i);
    wypisz(tab[i]);
  }
}

void max(struct skladowe tab[]) {
    int max_x=0, max_y=0;
    for (int i=0; i<TAB_SIZE; i++) {
        if (tab[i].x > max_x) max_x = tab[i].x;
        if (tab[i].y > max_y) max_y = tab[i].y;
    }
    printf("\nMaksymalny x: %d\n",max_x);
    printf("Maksymalny y: %d\n",max_y);
}

void min(struct skladowe tab[]) {       //nie działa
    int min_x=0, min_y=0;
    for (int i=0; i<TAB_SIZE; i++) {
        if (!(t[i].x == 0 && t[i].y == 0)) {
            if (tab[i].x < min_x) min_x = tab[i].x;
            if (tab[i].y < min_y) min_y = tab[i].y;
        }
    }
    printf("\nMaksymalny x: %d\n",max_x);
    printf("Maksymalny y: %d\n",max_y);
}

void menu() {
    
}

int main() {
  struct skladowe tab[10];
  srand(time(NULL));
  int i;
  int polecenie=0, index, x, y, found=0;

  //wyzerowanie tablicy
  for (i=0; i<TAB_SIZE; i++) {
    init(tab,i);
  }

  while(polecenie != 5) {
    printf("\n======================POLECENIA======================\n");
    printf("0 - wypisz wszystkie elementy tablicy\n");
    printf("1 - podanie wartosci dla danego elementu tablicy\n");
    printf("2 - wypelnij pierwszy wolny element\n");
    printf("3 - wyczysc element\n");
    printf("4 - statystyka\n");
    printf("5 - wyjscie z programu\n");
    printf("\nPodaj polecenie: ");
    scanf("%d",&polecenie);

    switch (polecenie) {
      case 0:
        printf("\n");
        wypiszTab(tab);
        break;
      case 1:
        printf("\nPodaj index: ");
        scanf("%d",&index);
        printf("Podaj x: ");
        scanf("%d",&x);
        printf("Podaj y: ");
        scanf("%d",&y);
        indexTab(tab,index,x,y);
        printf("\n  Wpisano: tab[%d] = [%d,%d]\n",index,x,y);
        break;
      case 2:
        printf("\nPodaj x: ");
        scanf("%d",&x);
        printf("Podaj y: ");
        scanf("%d",&y);
        for (i=0; i<10; i++) {
            if (tab[i].x == 0 && tab[i].y == 0) {
                index = i;
                found = 1;
                indexTab(tab, index, x, y);
                printf("\n  Wpisano w tab[%d] = [%d,%d]\n",index,x,y);
                break;
            }
        }
        if (found == 0) printf("    Nie znaleziono pustego elementu.\n");
        found = 0;
        break;
      case 3:
        printf("\nPodaj index: ");
        scanf("%d",&index);
        init(tab, index);
        printf("\n  Wyczyszczono element tab[%d]\n",index);
        break;
      case 4:
        max(tab);
        
        break;
      case 5:
        printf("\n  Zakonczono program.");
        break;
      default:
        polecenie = 2;
        break;
    }
  }

  return 0;
}
