#include <iostream>
#include <sys/socket.h>
#include <netinet/in.h>
#include <sys/un.h>
#include <unistd.h>
#include <mutex>
#include <thread>
#include <map>
#include <string>

int main() {
    std::map<std::string, std::string> users;

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

    int status = bind(fd, (struct sockaddr *) &addr, sizeof(addr));

    // listen
    listen(fd, 10);
    
    std::cout << "Postawiono serwer na porcie: " << port << std::endl;

    while (true) {
        // accept
        socklen_t addr_len = sizeof(addr);
        int fd_recv = accept(fd, (struct sockaddr *) &addr, &addr_len);
        std::cout << "\nOdebrano połączenie od klienta" << std::endl;

        // recv
        char buffer[1024];
        int length = recv(fd_recv, &buffer, sizeof(buffer)-1, 0);
        buffer[length] = '\0';

        std::string data = buffer;
        std::cout << data << std::endl;

        std::string operation = data.substr(0, data.find(";"));

        std::cout << operation << std::endl;

        if (operation == "reg") {
            std::cout << "Rejestracja" << std::endl;
            
            if (users.find(username) == users.end()) {
                users[username] = password;
            }
            
            
        }

        // "reg;login;password"

        // "log;login;password"

        // "messAll;message"

        // "messPriv;username;message"


        // send 
        send(fd_recv, data.c_str(), data.size(), 0);
        std::cout << "Wysłano odpowiedź" << std::endl;
        
        // shutdown
        shutdown(fd_recv, SHUT_WR);

        // close
        close(fd_recv);
        std::cout << "Zakończono połączenie z klientem" << std::endl;
    }
    
    close(fd);

    



    return 0;
}