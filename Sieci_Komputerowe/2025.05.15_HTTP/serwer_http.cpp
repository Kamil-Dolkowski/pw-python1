#include <iostream>
#include <sys/socket.h>
#include <netinet/in.h>
#include <sys/un.h>
#include <string>
#include <iostream>
#include <sstream>
#include <fstream>
#include <unistd.h>


int main(int argc, char **argv) {
    // blokada uruchomienia z konta root
    if (getuid() == 0) {
        fprintf(stderr, "Error: You can't run this program with root\n");
        return -1;
    }

    // pobranie numeru portu (jeśli brak, to domyślnie 80)
    int port = 80;

    if (argc > 1) {
        port = std::stoi(argv[1]);
    }

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

    bind(fd, (struct sockaddr *) &addr, sizeof(addr));

    // listen
    listen(fd, 10);

    std::cout << "Postawiono serwer HTTP na porcie: " << port << std::endl;
    
    while (true) {
        // accept
        socklen_t addr_len = sizeof(addr);
        int fd_recv = accept(fd, (struct sockaddr *) &addr, &addr_len);
        std::cout << "\nOdebrano połączenie od klienta" << std::endl;

        // recv
        char buffer[1024];
        int length = recv(fd_recv, &buffer, sizeof(buffer)-1, 0);
        buffer[length] = '\0';

        // odczyt z /proc/uptime
        std::string fileBuffer;

        std::ifstream ProcUptimeFile("/proc/uptime");
        getline(ProcUptimeFile, fileBuffer);
        std::string uptime = fileBuffer.substr(0, fileBuffer.find(" ")); 
        std::cout << "uptime = " << uptime << std::endl;

        ProcUptimeFile.close();

        // send 
        std::ostringstream oss;
        oss << "HTTP/1.0 200 OK\r\n"
            << "Content-Type: text/plain; charset=UTF-8\r\n"
            << "Connection: close\r\n"
            << "Content-Length: " << uptime.size() << "\r\n";

        std::string http_header = oss.str();
        std::string http_buffer = http_header + "\r\n" + uptime;

        send(fd_recv, http_buffer.c_str(), http_buffer.size(), 0);
        std::cout << "Wysłano odpowiedź HTTP" << std::endl;
        
        // shutdown
        shutdown(fd_recv, SHUT_WR);

        // close
        close(fd_recv);
        std::cout << "Zakończono połączenie z klientem" << std::endl;
    }
    
    close(fd);

    return 0;
}


// INADDR_ANY (0.0.0.0) <- nasłuchiwanie na wszystkich interfejsach sieciowych - serwer jest dostępny z zewnątrz
// INADDR_LOOPBACK (127.0.0.1) <- adres lokalny (loopback) - serwer nie jest dostępny z zewnątrz