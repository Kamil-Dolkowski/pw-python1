#include <iostream>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <sys/un.h>
#include <unistd.h>
#include <thread>
#include <vector>

// https://stackoverflow.com/questions/14265581/parse-split-a-string-in-c-using-string-delimiter-standard-c
// + ulepszenie o max_elements
std::vector<std::string> split(std::string s, std::string delimiter, int max_elements = 0) {
    size_t pos_start = 0, pos_end, delim_len = delimiter.length();
    std::string token;
    std::vector<std::string> res;
    int n = 1;

    while (((pos_end = s.find(delimiter, pos_start)) != std::string::npos) && n != max_elements) {
        token = s.substr (pos_start, pos_end - pos_start);
        pos_start = pos_end + delim_len;
        res.push_back (token);
        n++;
    }

    res.push_back (s.substr (pos_start));
    return res;
}

void logInUser(int &fd, std::string &username, std::string &password) {
    std::string username;
    std::string password;
    std::string data;
    std::string operation;
    char buffer[1024];

    data = "logIn;" + username + ";" + password;

    send(fd, data.c_str(), data.size(), 0);

    int length = recv(fd, &buffer, sizeof(buffer)-1, 0);
    buffer[length] = '\0';
    data = buffer;

    std::vector dataV = split(data, ";");
    operation = dataV[0];

    if (operation == "err") {
        std::cout << "\nError: " << dataV[1] << std::endl;
    } else {
        std::cout << "\nLog in successfully" << std::endl;
    }
}

void registerUser(int &fd, std::string &username, std::string &password) {
    std::string data;
    std::string operation;
    char buffer[1024];

    data = "reg;" + username + ";" + password;

    send(fd, data.c_str(), data.size(), 0);

    int length = recv(fd, &buffer, sizeof(buffer)-1, 0);
    buffer[length] = '\0';
    data = buffer;

    std::vector dataV = split(data, ";");
    operation = dataV[0];

    if (operation == "err") {
        std::cout << "\nError: " << dataV[1] << std::endl;
    } else {
        std::cout << "\nRegister successfully" << std::endl;

        logInUser(fd, username, password);
    }
}

void getDataFromSocket(int fd) {
    std::string data;

    while (true) {
        char buffer[1024];
        int length = recv(fd, &buffer, sizeof(buffer)-1, 0);
        buffer[length] = '\0';

        data = buffer;
        std::cout << data << std::endl;
    }
}

void getDataFromStdIn(int fd) {
    std::string choice;
    std::string username;
    std::string message;
    std::string data;

    while (true) {
        std::getline(std::cin, choice);

        std::vector choiceV = split(choice, " ", 2);

        if (choiceV[0] == "/a" && choiceV.size() == 2) {
            message = choiceV[1];
            
            data = "messAll;" + message;

            send(fd, data.c_str(), data.size(), 0);
        } else if (choiceV[0] == "/p") {
            choiceV = split(choice, " ", 3);

            if (choiceV.size() == 3) {
                username = choiceV[1];
                message = choiceV[2];

                data = "messPriv;" + username + ";" + message;
                send(fd, data.c_str(), data.size(), 0);
            }
        } else if (choiceV[0] == "/l") {
            data = "logOut";
            send(fd, data.c_str(), data.size(), 0);
            close(fd);
        } 
    }
}



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
    addr.sin_addr.s_addr = inet_pton(AF_INET, "127.0.0.1", &addr.sin_addr);
    addr.sin_port = htons(port);

    connect(fd, (struct sockaddr *) &addr, sizeof(addr));

    std::cout << "1 - log in" << std::endl;
    std::cout << "2 - register" << std::endl;
    std::cout << "Chose option [1/2]: ";
    std::cin >> choice;

    std::cout << "\nuser name: ";
    std::cin >> username;

    std::cout << "password: ";
    std::cin >> password;

    if (choice == "1") {
        logInUser(fd, username, password);
        // std::cout << "\nuser name: ";
        // std::cin >> username;

        // std::cout << "password: ";
        // std::cin >> password;

        // data = "logIn;" + username + ";" + password;

        // send(fd, data.c_str(), data.size(), 0);

        // int length = recv(fd, &buffer, sizeof(buffer)-1, 0);
        // buffer[length] = '\0';
        // data = buffer;

        // std::vector dataV = split(data, ";");
        // operation = dataV[0];

        // if (operation == "err") {
        //     std::cout << "\nError: " << dataV[1] << std::endl;
        // } else {
        //     std::cout << "\nLog in successfully" << std::endl;
        // }

    } else if (choice == "2") {
        // std::cout << "\nuser name: ";
        // std::cin >> username;

        // std::cout << "password: ";
        // std::cin >> password;

        // data = "reg;" + username + ";" + password;

        // send(fd, data.c_str(), data.size(), 0);

        // int length = recv(fd, &buffer, sizeof(buffer)-1, 0);
        // buffer[length] = '\0';
        // data = buffer;

        // std::vector dataV = split(data, ";");
        // operation = dataV[0];

        // if (operation == "err") {
        //     std::cout << "\nError: " << dataV[1] << std::endl;
        // } else {
        //     std::cout << "\nRegister successfully" << std::endl;


        // }

    } else {
        std::cout << "Wrong option" << std::endl;
        shutdown(fd, SHUT_WR);
        close(fd);
        return -1;
    }

    std::cout << "\n===== COMMUNICATOR =====" << std::endl;
    std::cout << "/a [message] - message to all" << std::endl;
    std::cout << "/p [username] [message] - priv message" << std::endl;
    std::cout << "/l - log out\n" << std::endl;

    std::thread dataSocket(getDataFromSocket, fd);
    std::thread dataStdIn(getDataFromStdIn, fd);

    // while (true) {
        // // Select - inicjalizacja
        // fd_set reading, writing, except;

        // struct timeval timeout;
        // timeout.tv_sec = 1;
        // timeout.tv_usec = 0;

        // int max_sock = std::max(fileno(stdin), fd) + 1;
        
        // FD_ZERO( &reading );
        // FD_ZERO( &writing );
        // FD_ZERO( &except );
        
        // FD_SET( fileno(stdin), &reading );
        // FD_SET( fd, &reading );

        // // Select
        // int rd = select(max_sock, &reading, NULL, NULL, &timeout);

        // if (FD_ISSET(fileno(stdin), &reading)) {
        //     std::getline(std::cin, choice);

        //     std::vector choiceV = split(choice, " ", 2);

        //     if (choiceV[0] == "/a" && choiceV.size() == 2) {
        //         message = choiceV[1];
                
        //         data = "messAll;" + message;

        //         send(fd, data.c_str(), data.size(), 0);
        //     } else if (choiceV[0] == "/p") {
        //         choiceV = split(choice, " ", 3);

        //         if (choiceV.size() == 3) {
        //             username = choiceV[1];
        //             message = choiceV[2];

        //             data = "messPriv;" + username + ";" + message;
        //             send(fd, data.c_str(), data.size(), 0);
        //         }
        //     } else if (choiceV[0] == "/l") {
        //         data = "logOut";
        //         send(fd, data.c_str(), data.size(), 0);
        //         close(fd);
        //         break;
        //     } 
        // } else if (FD_ISSET(fd, &reading)) {
        //     char buffer[1024];
        //     int length = recv(fd, &buffer, sizeof(buffer)-1, 0);
        //     buffer[length] = '\0';

        //     data = buffer;
        //     std::cout << data << std::endl;
        // } 
    }

    close(fd);

    return 0;
}