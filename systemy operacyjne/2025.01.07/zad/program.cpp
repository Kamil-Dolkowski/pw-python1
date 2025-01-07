#include <thread>
#include <iostream>
#include <string>
#include <unistd.h>
#include <condition_variable>
#include <fcntl.h>
#include <sys/stat.h>
#include <fstream>



#define TAB_LENGTH 10

std::mutex mutex;
std::condition_variable cv;
unsigned int tab[TAB_LENGTH];

void threadFunc(size_t start, size_t end, std::string content) {
    std::unique_lock lock(mutex);

    unsigned int counter[TAB_LENGTH];

    for (int i=0; i<TAB_LENGTH; i++) {
        counter[i] = 0;
    }

    for (int i = start; i < end; i++) {
        /* [48, 57] */
        if (content[i] >= '0' && content[i] <= '9') { 
            int val = content[i] - '0'; /* content[i] - 48 */
            counter[val]++;
        }
    }

    for (int i=0; i<TAB_LENGTH; i++) {
        //pthread_mutex_lock(&shr->mutex);
        tab[i] += counter[i];
        //pthread_mutex_unlock(&shr->mutex);
    }
}

std::string getFileContent(const std::string& path) {
    std::ifstream file(path);
    std::string content((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());

    return content;
}


int main(int argc, char *argv[]) {
    // std::thread t(threadFunc);
    struct stat statbuf;


    // zerowanie tablicy
    for (int i=0; i<TAB_LENGTH; i++) {
        tab[i] = 0;
    }
    
    if (argc != 3) {
        std::cout << "Error: Not enough arguments.\n";
        return -1;
    }

    int number_of_threads = atoi(argv[2]);

    int fd = open(argv[1], O_RDONLY); 
    if (fd != 3) {
        printf("Error: File does not exists.\n");
        return -1;
    }

    int ret = fstat(fd, &statbuf); 
    if (ret == -1) {
        printf("Error: Can't define size of the file.\n");
        return -1;
    }

    std::string content = getFileContent(argv[1]);

    size_t start = 0;
    size_t shift = statbuf.st_size/number_of_threads;
    size_t end = start + shift;

    



    for (int i=0; i<number_of_threads; i++) {
        std::thread t(threadFunc, start, end, content);
        start = end;
        end = end + shift;
        if (end + shift >= statbuf.st_size) end = statbuf.st_size+1;
    }


    


    for (int i=0; i<number_of_threads; i++) {
        // printf("%d = %d\n", i, pid_table[i]); 
    }

    printf("\nNumber of digits in the file:\n");

    for (int i=0; i<TAB_LENGTH; i++) {
        std::cout << i << " = " << tab[i] << std::endl;
        //printf("%d = %d\n", i, shr->tab[i]);
    }

    close(fd);

    return 0;
}