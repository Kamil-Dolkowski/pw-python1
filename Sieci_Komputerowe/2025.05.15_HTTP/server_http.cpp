#include <iostream>
#include <sys/socket.h>
#include <netinet/in.h>
#include <sys/un.h>
#include <string>
#include <iostream>
#include <fstream>


int main(int argc, char **argv) {
    // pobranie numeru portu
    int port = std::stoi(argv[1]);
    std::cout << "port = " << port << std::endl;

    // odczyt z /proc/uptime
    std::string buffer;

    std::ifstream ProcUptimeFile("/proc/uptime");
    getline (ProcUptimeFile, buffer);
    std::string uptime = buffer.substr(0, buffer.find(" ")); 
    std::cout << "uptime = " << uptime << std::endl;

    ProcUptimeFile.close();

    // socket
    int fd = socket(PF_INET, SOCK_STREAM, IPPROTO_TCP);
    std::cout << fd << std::endl;

    // setsockopt
    int value = 1;
    if (setsockopt(fd, SOL_SOCKET, SO_REUSEADDR, (const char*)&value, sizeof(value)) < 0) {
        fprintf(stderr, "Failed to set SO_REUSEADDR\n");
    }

    // bind
    struct sockaddr_in addr;
    memset((char*)&addr, 0, sizeof(addr));
    addr.sin_family = AF_INET;
    addr.sin_addr.s_addr = htonl(INADDR_ANY);
    addr.sin_port = htons(port);

    bind(fd, (struct sockaddr *) &addr, sizeof(addr));

    // listen
    listen(fd, 2);

    // accept
    accept(fd, (struct sockaddr *) &addr, sizeof(addr));

    int length = recv(fd, &buffer, sizeof(buffer), 0);
    std::cout << length << std::endl;


    return 0;
}


// 0.0.0.0 <- nasłuchiwanie na wszystkich portach?
// 127.0.0.1 <- serwer nie dostępny z zewnątrz
// socket <- socket serwera
// accept <- socket danego klienta


// === TCP ===
// socket
// bind
// listen
// accept
// send / recv
// close