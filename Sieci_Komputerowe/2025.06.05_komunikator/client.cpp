#include <iostream>
#include <sys/socket.h>
#include <netinet/in.h>
#include <sys/un.h>
#include <unistd.h>

int main() {
    std::string username = "user";
    std::string password = "password";

    int port = 5000;

    // socket
    int fd = socket(PF_INET, SOCK_STREAM, IPPROTO_TCP);

    // setsockopt
    int value = 1;
    if (setsockopt(fd, SOL_SOCKET, SO_REUSEADDR, (const char*)&value, sizeof(value)) < 0) {
        fprintf(stderr, "Error: Failed to set SO_REUSEADDR\n");
    }

    // bind
    struct sockaddr_in addr;
    memset((char*)&addr, 0, sizeof(addr));
    addr.sin_family = AF_INET;
    addr.sin_addr.s_addr = htonl(INADDR_ANY);
    addr.sin_port = htons(port);

    connect(fd, (struct sockaddr *) &addr, sizeof(addr));

    char buffer[1024] = "reg;login;password";

    send(fd, &buffer, sizeof(buffer)-1, 0);

    close(fd);

    return 0;
}