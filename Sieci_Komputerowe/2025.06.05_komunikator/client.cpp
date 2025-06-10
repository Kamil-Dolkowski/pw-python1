#include <iostream>
#include <sys/socket.h>
#include <netinet/in.h>
#include <sys/un.h>
#include <unistd.h>
#include <string>

int main() {
    std::string choice;
    std::string data;
    std::string operation;
    std::string username;
    std::string password;
    std::string message;
    char buffer[1024];

    int port = 5000;

    // socket
    int fd = socket(PF_INET, SOCK_STREAM, IPPROTO_TCP);

    // setsockopt
    int value = 1;
    if (setsockopt(fd, SOL_SOCKET, SO_REUSEADDR, (const char*)&value, sizeof(value)) < 0) {
        fprintf(stderr, "Error: Failed to set SO_REUSEADDR\n");
    }

    // connect
    struct sockaddr_in addr;
    memset((char*)&addr, 0, sizeof(addr));
    addr.sin_family = AF_INET;
    addr.sin_addr.s_addr = htonl(INADDR_ANY);
    addr.sin_port = htons(port);

    connect(fd, (struct sockaddr *) &addr, sizeof(addr));

    std::cout << "1 - log in" << std::endl;
    std::cout << "2 - register" << std::endl;
    std::cout << "Chose option [1/2]: ";
    std::cin >> choice;

    if (choice == "1") {
        std::cout << "\nuser name: ";
        std::cin >> username;

        std::cout << "password: ";
        std::cin >> password;

        data = "logIn;" + username + ";" + password;

        send(fd, data.c_str(), sizeof(data)-1, 0);

        int length = recv(fd, &buffer, sizeof(buffer)-1, 0);
        buffer[length] = '\0';
        data = buffer;

        operation = data.substr(0, data.find(";"));

        if (operation == "err") {
            std::cout << "\nError: " << data.substr(data.find(";")) << std::endl;
        } else {
            std::cout << "\nLog in successfully" << std::endl;
        }

    } else if (choice == "2") {
        std::cout << "\nuser name: ";
        std::cin >> username;

        std::cout << "password: ";
        std::cin >> password;

        data = "reg;" + username + ";" + password;

        send(fd, data.c_str(), sizeof(data)-1, 0);

        int length = recv(fd, &buffer, sizeof(buffer)-1, 0);
        buffer[length] = '\0';
        data = buffer;

        operation = data.substr(0, data.find(";"));

        if (operation == "err") {
            std::cout << "\nError: " << data.substr(1, data.find(";")) << std::endl;
        } else {
            std::cout << "\nRegister successfully" << std::endl;
        }

    } else {
        std::cout << "Wrong option" << std::endl;
    }

    std::cout << "\\a [message] - message to all" << std::endl;
    std::cout << "\\p [username] [message] - priv message" << std::endl;
    std::cout << "\\l - log out" << std::endl;
    std::cin >> choice;

    while (true) {
        if (choice.substr(0,1) == "\\a") {
            message = choice.substr(2,choice.size()-2);

            data = "messAll;" + message;
            send(fd, data.c_str(), sizeof(data)-1, 0);
        } else if (choice.substr(0,1) == "\\p") {
            message = choice.substr(2,choice.size()-2);

            data = "messAll;" + message;
            send(fd, data.c_str(), sizeof(data)-1, 0);
        } else if (choice.substr(0,1) == "\\l") {
            data = "logout";
            send(fd, data.c_str(), sizeof(data)-1, 0);
        } else {

        }
    }

    // buffer = "reg;login;password";

    data = "reg;login;password";

    send(fd, &buffer, sizeof(buffer)-1, 0);

    data = "log;login;password";

    send(fd, data.c_str(), sizeof(buffer)-1, 0);

    close(fd);

    return 0;
}