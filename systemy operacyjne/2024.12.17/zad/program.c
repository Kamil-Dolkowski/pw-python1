#include <string.h>
#include <sys/stat.h>
#include <sys/mman.h>
#include <sys/wait.h>
#include <fcntl.h>
#include <stdio.h>
#include <unistd.h>
#include <pthread.h>
#include <stdlib.h>

#define TAB_LENGTH 10

typedef struct shared {
    int tab[TAB_LENGTH];
    pthread_mutex_t mutex;
} shared_t;






int main(int argc, char *argv[]) {
    struct stat statbuf;

    unsigned int counter[TAB_LENGTH];

    // zerowanie tablicy
    for (int i=0; i<TAB_LENGTH; i++) {
        counter[i] = 0;
    }
    
    if (argc != 3) {
        printf("Error: Not enough arguments.\n");
        return -1;
    }

    // printf("argc=%d\n", argc);

    int number_of_processes = atoi(argv[2]);

    int *pid_table = malloc(sizeof(int)*number_of_processes);

    // printf("process(es)=%d\n", number_of_processes);

    int fd = open(argv[1], O_RDONLY); 
    if (fd != 3) {
        printf("Error: File does not exists.\n");
        return -1;
    }
    // printf("fd=%d\n", fd);

    int ret = fstat(fd, &statbuf); 
    if (ret == -1) {
        printf("Error: Can't define size of the file.\n");
        return -1;
    }
    // printf("len=%ld\n", statbuf.st_size);

    char *content = mmap(NULL, statbuf.st_size, PROT_READ, MAP_SHARED, fd, 0);
    // printf("content ptr=%p\n", content);
    if (content == NULL) {
        printf("Error: Problem with file's content.\n");
        return -1;
    }
    
    int protection = PROT_READ | PROT_WRITE;
    int visibility = MAP_SHARED | MAP_ANONYMOUS;
    shared_t *shr = (shared_t*)mmap(NULL, sizeof(shared_t), protection, visibility, -1, 0);
    if (shr == NULL)
        return -1;

    // zerowanie tablicy
    for (int i=0; i<TAB_LENGTH; i++) {
        shr->tab[i] = 0;
    }

    pthread_mutexattr_t mutexattr;
    if (pthread_mutexattr_init(&mutexattr) != 0)
        return -2;
    if (pthread_mutexattr_setpshared(&mutexattr, PTHREAD_PROCESS_SHARED) != 0)
        return -3;
    if (pthread_mutex_init(&shr->mutex, &mutexattr) != 0)
        return -4;


    size_t start = 0;
    size_t shift = statbuf.st_size/number_of_processes;
    size_t end = start + shift;

    



    for (int i=0; i<number_of_processes; i++) {
        // printf("Pętla %d: ", i);
        // printf("start: %ld , end %ld , ", start, end);
        pid_t pid = fork();
        
        switch (pid) {
            case -1: // coś poszło nie tak
                printf("Error: Problem with fork().\n");

                break;
            case 0: // jesteśmy w nowym procesie
                // printf("Child %d\n", pid);

                for (int i = start; i < end; i++) {
                    /* [48, 57] */
                    if (content[i] >= '0' && content[i] <= '9') { 
                        int val = content[i] - '0'; /* content[i] - 48 */

                        // pthread_mutex_lock(&shr->mutex);
                        // shr->tab[val]++;
                        // pthread_mutex_unlock(&shr->mutex);
                        
                        counter[val]++;
                    }
                }

                for (int i=0; i<TAB_LENGTH; i++) {
                    pthread_mutex_lock(&shr->mutex);
                    shr->tab[i] += counter[i];
                    pthread_mutex_unlock(&shr->mutex);
                }

                return 0;

                break;
            default: // jesteśmy w starym procesie
                // printf("Parent %d\n", pid);

                pid_table[i] = pid;
                break;
        }

        start = end;
        end = end + shift;
        if (end + shift >= statbuf.st_size) end = statbuf.st_size+1;

    }


    


    for (int i=0; i<number_of_processes; i++) {
        waitpid(pid_table[i], NULL, 0);
        // printf("%d = %d\n", i, pid_table[i]); 
    }

    printf("\nNumber of digits in the file:\n");

    for (int i=0; i<TAB_LENGTH; i++) {
        printf("%d = %d\n", i, shr->tab[i]);
    }

    pthread_mutex_destroy(&shr->mutex);
    munmap(content, statbuf.st_size);
    close(fd);

    return 0;
}