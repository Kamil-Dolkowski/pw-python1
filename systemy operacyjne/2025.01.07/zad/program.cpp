#include <thread>
#include <iostream>
#include <string>
#include <unistd.h>
#include <fcntl.h>
#include <sys/stat.h>
#include <fstream>
#include <vector>
#include <mutex>

#define TAB_LENGTH 10

std::mutex mutex;
unsigned int tab[TAB_LENGTH];

void threadFunc(unsigned long int start, unsigned long int end, std::string content) {
    unsigned int counter[TAB_LENGTH];

    // std::cout << "thread: start=" << start << ", end=" << end << std::endl;

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
        std::unique_lock lock(mutex);
        tab[i] += counter[i];
    }
}

std::string getFileContent(const std::string& path) {
    std::ifstream file(path);
    std::string content((std::istreambuf_iterator<char>(file)), std::istreambuf_iterator<char>());

    return content;
}



int main(int argc, char *argv[]) {
    struct stat statbuf;
    std::vector<std::thread> threads;

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

    unsigned long int start = 0;
    unsigned long int shift = statbuf.st_size/number_of_threads;
    unsigned long int end = start + shift;

    
    for (int i = 0; i < number_of_threads; i++) {
        // std::cout << i << ": start=" << start << ", end=" << end << ", shift=" << shift << std::endl;
        threads.push_back(std::thread(threadFunc, start, end, content));
        start = end;
        if (end + shift >= statbuf.st_size) {
            end = statbuf.st_size;
        } else {
            end = end + shift;
        }
    }

    for (int i = 0; i < number_of_threads; i++) {
        threads[i].join();
    }

    printf("\nNumber of digits in the file:\n");

    for (int i = 0; i < TAB_LENGTH; i++) {
        std::cout << i << " = " << tab[i] << std::endl;
    }

    close(fd);
    
    return 0;
}