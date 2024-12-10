#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <signal.h>
#include <string.h>

void handler(int signo)
{
	printf("Wystąpił sygnał %d (%s)\n", 
	       signo,
	       strsignal(signo));

	exit(EXIT_FAILURE);
}

long int findSize(char *fileName) 
{ 
    FILE* fp = fopen(fileName, "r"); 
  
    if (fp == NULL) { 
        printf("File Not Found!\n"); 
        return -1; 
    } 
  
    fseek(fp, 0L, SEEK_END); 
  
    long int size = ftell(fp); 
  
    fclose(fp); 
  
    return size; 
} 







int main(int argc, char **argv) {
    char *buffer;
    long int fileSize;

    struct sigaction act = { 0 };
	act.sa_handler = &handler;
	if (sigaction(SIGUSR1, &act, NULL) == -1)
	{
		exit(EXIT_FAILURE);
	}

	if (sigaction(SIGUSR2, &act, NULL) == -1)
	{
		exit(EXIT_FAILURE);
	}


    


    if (argv[1]){
        fileSize = findSize(argv[1]);
        buffer = malloc(fileSize*sizeof(char));

        FILE * file;
        file = fopen(argv[1], "r");

        if (file==NULL){
            printf("Error: file does not exists.\n");
            return -1;
        }

        printf("File size: %ld\n",fileSize);
        fgets(buffer, fileSize, file);

        printf("File:\n%s\n",buffer);
        



        fclose(file);
        

    } else {
        printf("Error: No path argument.\n");
        return -1;
    }
    
    

    

    return 0;
}