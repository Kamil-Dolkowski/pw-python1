#include <iostream>
#include <sys/stat.h>
#include <sys/types.h>
#include <stdlib.h>
#include <fcntl.h>
#include <unistd.h>


int main() {
    const char pathname[] ="/tmp/fifo";
    if (mkfifo(pathname, 0666) != 0) {
        printf("Failed to create fifo\n");
        exit(EXIT_FAILURE);
    }

    int fd = open(pathname, O_RDONLY);
    if (fd < 0) {
        exit(EXIT_FAILURE);
    }

    ssize_t length = 0;
    while(length != -1) {
        char buffer[1024];
        length = read(fd, buffer, sizeof(buffer));
        if (length > 0) {
            write(STDOUT_FILENO, buffer, length);
        }
    }
    
    close(fd);

    return 0;
}