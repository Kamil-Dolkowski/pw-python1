#include <iostream>
#include <sys/socket.h>
#include <netinet/in.h>
#include <arpa/inet.h>
#include <sys/un.h>
#include <unistd.h>
#include <thread>
#include <csignal>
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

volatile sig_atomic_t stop = 0;
int fd;

void handle_sigint(int signal) {
    std::cout << "\nClosing connection and exit ..." << std::endl;
    stop = 1;
}

bool logInUser(int &fd, std::string &username, std::string &password) {
    std::string data;
    std::string operation;
    char buffer[1024];

    data = "logIn;" + username + ";" + password;

    send(fd, data.c_str(), data.size(), 0);

    int length = recv(fd, &buffer, sizeof(buffer)-1, 0);
    buffer[length] = '\0';
    data = buffer;

    std::vector<std::string> dataV = split(data, ";");
    operation = dataV[0];

    if (operation == "err") {
        std::cout << "\nError: " << dataV[1] << std::endl;
        shutdown(fd, SHUT_WR);
        close(fd);
        return false;
    } else {
        std::cout << "\nLog in successfully" << std::endl;

        std::cout << "\n===== COMMUNICATOR =====" << std::endl;
        std::cout << "/a [message] - message to all" << std::endl;
        std::cout << "/p [username] [message] - priv message" << std::endl;
        std::cout << "/u - active users" << std::endl;
        std::cout << "/l - log out" << std::endl;

        return true;
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

    std::vector<std::string> dataV = split(data, ";");
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

    while (stop != 1) {
        // Select - inicjalizacja
        fd_set reading;

        struct timeval timeout;
        timeout.tv_sec = 1;
        timeout.tv_usec = 0;

        int max_sock = fd + 1;
        
        FD_ZERO( &reading );
        FD_SET( fd, &reading );

        // Select
        int rd = select(max_sock, &reading, NULL, NULL, &timeout);

        if (FD_ISSET(fd, &reading)) {
            char buffer[1024];
            int length = recv(fd, &buffer, sizeof(buffer)-1, 0);
            if (length <= 0) {
                std::cout << "\nConnection lost" << std::endl;
                stop = 1;
                break;
            }
            buffer[length] = '\0';

            data = buffer;
            std::vector<std::string> dataV = split(data, ";");

            if (dataV[0] == "err") {
                std::cout << "(!) Error: " + dataV[1] << std::endl;
            } else {
                std::cout << data << std::endl;
            }
        }
    }

    data = "logOut";
    send(fd, data.c_str(), data.size(), 0);
    std::cout << "\nLogged out" << std::endl;
}

void getDataFromStdIn(int fd) {
    std::string choice;
    std::string username;
    std::string message;
    std::string data;

    while (stop != 1) {
        // Select - inicjalizacja
        fd_set reading;

        struct timeval timeout;
        timeout.tv_sec = 1;
        timeout.tv_usec = 0;

        int max_sock = fileno(stdin) + 1;
        
        FD_ZERO( &reading );
        FD_SET( fileno(stdin), &reading );

        // Select
        int rd = select(max_sock, &reading, NULL, NULL, &timeout);

        if (FD_ISSET(fileno(stdin), &reading)) {
            std::getline(std::cin, choice);

            std::vector<std::string> choiceV = split(choice, " ", 2);

            // Message to all active users
            if (choiceV[0] == "/a" && choiceV.size() == 2) {
                message = choiceV[1];
                
                data = "messAll;" + message;

                send(fd, data.c_str(), data.size(), 0);
            } 
            // Private message
            if (choiceV[0] == "/p") {
                choiceV = split(choice, " ", 3);

                if (choiceV.size() == 3) {
                    username = choiceV[1];
                    message = choiceV[2];

                    data = "messPriv;" + username + ";" + message;
                    send(fd, data.c_str(), data.size(), 0);
                }
            } 
            // Log out
            if (choiceV[0] == "/l") {
                stop = 1;

                data = "logOut";
                send(fd, data.c_str(), data.size(), 0);
                
                break;
            } 
            // Print list of all active users
            if (choiceV[0] == "/u") {
                data = "allUsers";
                send(fd, data.c_str(), data.size(), 0);
            }
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
    fd = socket(PF_INET, SOCK_STREAM, IPPROTO_TCP);

    // setsockopt
    int value = 1;
    if (setsockopt(fd, SOL_SOCKET, SO_REUSEADDR, (const char*)&value, sizeof(value)) < 0) {
        fprintf(stderr, "Error: Failed to set SO_REUSEADDR\n");
    }

    // connect
    struct sockaddr_in addr;
    memset((char*)&addr, 0, sizeof(addr));
    addr.sin_family = AF_INET;
    inet_pton(AF_INET, "127.0.0.1", &addr.sin_addr);
    addr.sin_port = htons(port);

    int status = connect(fd, (struct sockaddr *) &addr, sizeof(addr));
    if (status < 0) {
        std::cout << "\nError: Cannot connect to server" << std::endl;
        return -1;
    }

    std::cout << "1 - log in" << std::endl;
    std::cout << "2 - register" << std::endl;
    std::cout << "Chose option [1/2]: ";
    std::cin >> choice;

    if (choice != "1" && choice != "2") {
        std::cout << "Wrong option" << std::endl;
        shutdown(fd, SHUT_WR);
        close(fd);
        return -1;
    }

    std::cout << "\nusername: ";
    std::cin >> username;

    std::cout << "password: ";
    std::cin >> password;

    if (choice == "1") {
        bool loggedIn = logInUser(fd, username, password);
        if (loggedIn == false) {
            return -1;
        }
    } 
    if (choice == "2") {
        registerUser(fd, username, password);
    } 

    std::signal(SIGINT, handle_sigint);

    std::thread dataSocket(getDataFromSocket, fd);
    std::thread dataStdIn(getDataFromStdIn, fd);

    dataSocket.join();
    dataStdIn.join();

    shutdown(fd, SHUT_RDWR);
    close(fd);

    return 0;
}