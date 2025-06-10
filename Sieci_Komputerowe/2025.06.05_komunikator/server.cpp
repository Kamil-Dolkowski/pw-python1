#include <iostream>
#include <sys/socket.h>
#include <netinet/in.h>
#include <sys/un.h>
#include <unistd.h>
#include <mutex>
#include <thread>
#include <map>
#include <string>
#include <vector>

// https://stackoverflow.com/questions/14265581/parse-split-a-string-in-c-using-string-delimiter-standard-c
std::vector<std::string> split(std::string s, std::string delimiter) {
    size_t pos_start = 0, pos_end, delim_len = delimiter.length();
    std::string token;
    std::vector<std::string> res;

    while ((pos_end = s.find(delimiter, pos_start)) != std::string::npos) {
        token = s.substr (pos_start, pos_end - pos_start);
        pos_start = pos_end + delim_len;
        res.push_back (token);
    }

    res.push_back (s.substr (pos_start));
    return res;
}


int main() {
    std::map<std::string, std::string> usersLogging;
    std::map<std::string, int> users;
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

    // accept
    socklen_t addr_len = sizeof(addr);
    int fd_recv = accept(fd, (struct sockaddr *) &addr, &addr_len);
    std::cout << "\n====== NEW MESSAGE ======" << std::endl;

    while (true) {
        // recv
        char buffer[1024];
        int length = recv(fd_recv, &buffer, sizeof(buffer)-1, 0);
        buffer[length] = '\0';

        std::string data = buffer;
        std::vector dataV = split(data, ";");

        std::string operation = dataV[0];
        std::string username;
        std::string password;
        std::string message;

        if (operation == "reg") {
            std::cout << "=== REGISTRATION ===" << std::endl;
            
            username = dataV[1];
            password = dataV[2];

            if (usersLogging.find(username) == usersLogging.end()) {
                usersLogging[username] = password;

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
            
            username = dataV[1];
            password = dataV[2];

            if (usersLogging.find(username) != usersLogging.end()) {
                if (usersLogging[username] == password) {
                    std::cout << "- log in successfully" << std::endl;

                    users[username] = fd_recv;
                    data = "ok";
                    send(fd_recv, data.c_str(), data.size(), 0);
                } else {
                    std::cout << "- error: wrong password" << std::endl;

                    data = "err;wrong password";
                    send(fd_recv, data.c_str(), data.size(), 0);
                }
            } else {
                std::cout << "- error: user doesn't exists" << std::endl;

                data = "err;user doesn't exists";
                send(fd_recv, data.c_str(), data.size(), 0);
            }   
        } else if (operation == "messAll") {
            std::cout << "=== MESSAGE TO ALL ===" << std::endl;

            message = dataV[1];
            data = "<" + username + "> " + message;

            for (auto& user : users) {
                send(user.second, data.c_str(), data.size(), 0);
            }

            std::cout << "- send message to all users" << std::endl;
        } else if (operation == "messPriv") {
            std::cout << "=== PRIVATE MESSAGE ===" << std::endl;

            std::string recv_username = dataV[1];
            message = dataV[2];

            if (usersLogging.find(recv_username) != usersLogging.end()) {
                int fd = users[recv_username];

                data = "[priv] <" + username + "> " + message;

                send(fd, data.c_str(), data.size(), 0);
                std::cout << "- send private message" << std::endl;
            } else {
                data = "err;user doesn't exist";
                send(fd_recv, data.c_str(), data.size(), 0);
                std::cout << "- error: user doesn't exists" << std::endl;
            }

        } else if (operation == "logOut") {
            // shutdown
            shutdown(fd_recv, SHUT_WR);

            // close
            close(fd_recv);
            std::cout << "- close connection with client" << std::endl;
            break;
        } else {
            std::cout << "- unknown operation" << std::endl;
        }

        // send 
        send(fd_recv, data.c_str(), data.size(), 0);
        std::cout << "- send answer to client" << std::endl;
    }
    
    close(fd);
    std::cout << "\nServer turned off" << std::endl;

    return 0;
}


// "reg;login;password"

// "logIn;login;password"

// logOut

// "messAll;message"

// "messPriv;username;message"