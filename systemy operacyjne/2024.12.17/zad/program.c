#include <string.h>
#include <sys/stat.h>
#include <sys/mman.h>
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

void child(shared_t *shr) {

}




int main(int argc, char *argv[]) {
    struct stat statbuf;

    unsigned int final_counter[10];
    
    if (argc != 3) {
        printf("Error: Not enough arguments.\n");
        return -1;
    }

    printf("argc=%d\n", argc);

    int number_of_processes = atoi(argv[2]);

    printf("process(es)=%d\n", number_of_processes);

    int fd = open(argv[1], O_RDONLY); 
    if (fd != 3) {
        return -1;
    }
    printf("fd=%d\n", fd);

    fstat(fd, &statbuf); /* TODO: sprawdzic ret value */
    printf("len=%ld\n", statbuf.st_size);

    char *content = mmap(NULL, statbuf.st_size, PROT_READ, MAP_SHARED, fd, 0);
    printf("content ptr=%p\n", content);
    if (content == NULL) {
        return -1;
    }
    
    int protection = PROT_READ | PROT_WRITE;
    int visibility = MAP_SHARED | MAP_ANONYMOUS;
    shared_t *shr = (shared_t*)mmap(NULL, sizeof(shared_t), protection, visibility, -1, 0);
    if (shr == NULL)
        return -1;

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

    for (int i = 0; i < statbuf.st_size; i++)
    {
        /* [48, 57] */
        if (content[i] >= '0' && content[i] <= '9') { 
            int val = content[i] - '0'; /* content[i] - 48 */
            shr->tab[val]++;
        }
    }

    pid_t pid = fork();
    switch (pid) {
        case -1: // coś poszło nie tak
            break;
        case 0: // jesteśmy w nowym procesie
            child(shr);
            return -5;
        default: // jesteśmy w starym procesie
            // parent(shr);
            break;
    }


    for (int i=0; i<TAB_LENGTH; i++) {
        printf("%d = %d\n", i, shr->tab[i]);
    }

    pthread_mutex_destroy(&shr->mutex);
    munmap(content, statbuf.st_size);
    close(fd);

    return 0;
}