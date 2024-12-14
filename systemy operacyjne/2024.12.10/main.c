#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <string.h>

char *buffer = NULL;
char *fileName = NULL;

void handler_sigint(int signo) {
    char choice[1];
    choice[0] = 'c';

    while(choice[0] != 'y' && choice[0] != 'n') {
        printf("\nCzy na pewno zakończyć program? (y/n): ");
        scanf("%1s", choice);

        if (choice[0] == 'y') {
            printf("Zakończono program.\n");
            exit(EXIT_FAILURE);
        } else if (choice[0] == 'n') {
            return;
        } else {
            printf("Błąd: Niepoprawny wybór.\n");
        }
    }
}

void handler_sigusr1(int signo) {
    FILE *file = fopen(fileName, "r");
    if (file != NULL) {
        if (fseek(file, 0L, SEEK_END) == 0) {
            long int bufsize = ftell(file);

            if (bufsize == -1) {
                printf("Błąd: nie określono rozmiaru pliku.\n");
                exit(EXIT_FAILURE);
            }

            buffer = malloc(sizeof(char) * (bufsize + 1));

            if (fseek(file, 0L, SEEK_SET) != 0) {
                printf("Błąd: nie znaleziono poczatku pliku.\n");
                exit(EXIT_FAILURE);
            }

            size_t newLen = fread(buffer, sizeof(char), bufsize, file);

            if (ferror(file) != 0) {
                fputs("Błąd: błąd podczas wczytywania pliku.", stderr);
            } else {
                buffer[newLen++] = '\0';
            }
        }

        fclose(file);
    } else {
        printf("Błąd: nie znaleziono pliku '%s'.\n", fileName);
        exit(EXIT_FAILURE);
    }

    return;
}

void handler_sigusr2(int signo) {
    if (buffer != NULL) {
        free(buffer);
    }
    return;
}






int main(int argc, char **argv) {
    pid_t pid = getpid();
    fileName = argv[1];

    struct sigaction act_sigusr1 = { 0 }, act_sigusr2 = { 0 }, act_sigint = { 0 };
    act_sigusr1.sa_handler = &handler_sigusr1;
    act_sigusr2.sa_handler = &handler_sigusr2;
	act_sigint.sa_handler = &handler_sigint;

	if (sigaction(SIGUSR1, &act_sigusr1, NULL) == -1)
	{
		exit(EXIT_FAILURE);
	}

	if (sigaction(SIGUSR2, &act_sigusr2, NULL) == -1)
	{
		exit(EXIT_FAILURE);
	}

    if (sigaction(SIGINT, &act_sigint, NULL) == -1)
	{
		exit(EXIT_FAILURE);
	}
    

    if (argv[1]){
        while (1) {
            printf("\n==Zawartość pliku %s:\n", argv[1]);
            
            kill(pid, SIGUSR2);
            kill(pid, SIGUSR1);

            printf("%s\n",buffer);

            sleep(1);
        }
    } else {
        printf("Błąd: Nie podano ścieżki do pliku.\n");
        return -1;
    }

    return 0;
}