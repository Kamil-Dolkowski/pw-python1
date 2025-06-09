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
    
    std::cout << "Server started on port: " << port << std::endl;

    while (true) {
        // accept
        socklen_t addr_len = sizeof(addr);
        int fd_recv = accept(fd, (struct sockaddr *) &addr, &addr_len);
        std::cout << "\n====== NEW MESSAGE ======" << std::endl;

        // recv
        char buffer[1024];
        int length = recv(fd_recv, &buffer, sizeof(buffer)-1, 0);
        buffer[length] = '\0';

        std::string data = buffer;
        std::string operation = data.substr(0, data.find(";"));

        if (operation == "reg") {
            std::cout << "=== REGISTRATION ===" << std::endl;
            
            if (users.find(username) == users.end()) {
                users[username] = password;
                std::cout << "- add new user '" << username << "'" << std::endl;
                data = "ok";
                send(fd_recv, data.c_str(), data.size(), 0);
            } else {
                std::cout << "- error: user already exists" << std::endl;
                data = "err";
                send(fd_recv, data.c_str(), data.size(), 0);
            }   
        } else if (operation == "logIn") {
            std::cout << "=== LOG IN ===" << std::endl;
            
            if (users.find(username) != users.end()) {
                if (users[username] == password) {
                    std::cout << "- log in successfully" << std::endl;
                    data = "ok";
                    send(fd_recv, data.c_str(), data.size(), 0);
                } else {
                    std::cout << "- error: wrong password" << std::endl;
                    data = "err;wrong password";
                    send(fd_recv, data.c_str(), data.size(), 0);
                }
            } else {
                std::cout << "- error: user don't exists" << std::endl;
                data = "err;user don't exists";
                send(fd_recv, data.c_str(), data.size(), 0);
            }   
        } else if (operation == "messAll") {

        } else if (operation == "messPriv") {

        } else if (operation == "logOut") {
            // shutdown
            shutdown(fd_recv, SHUT_WR);

            // close
            close(fd_recv);
            std::cout << "- close connection with client" << std::endl;
        } else {
            std::cout << "- unknown operation" << std::endl;
        }

        // send 
        send(fd_recv, data.c_str(), data.size(), 0);
        std::cout << "- send answer to client" << std::endl;
    }
    
    close(fd);

    return 0;
}


// "reg;login;password"

// "logIn;login;password"

// logOut

// "messAll;message"

// "messPriv;username;message"