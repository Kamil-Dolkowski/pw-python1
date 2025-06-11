#include <iostream>
#include <sys/socket.h>
#include <netinet/in.h>
#include <sys/un.h>
#include <unistd.h>
#include <mutex>
#include <thread>
#include <csignal>
#include <map>
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

volatile sig_atomic_t stop = 0;

void handle_sigint(int signal) {
    stop = 1;
}

std::map<std::string, std::string> registeredUsers;
std::map<std::string, int> activeUsers;
std::vector<std::thread> userThreads;

std::mutex mutex;

void sendListOfActiveUsers(int &fd) {
    std::string data = "\n===== ACTIVE USERS =====\n";

    std::lock_guard<std::mutex> lock(mutex);

    for (auto& user : activeUsers) {
        data += "- " + user.first + "\n";
    }

    send(fd, data.c_str(), data.size(), 0);
}

void sendToAllUsers(std::string &data, std::string username = "") {
    std::lock_guard<std::mutex> lock(mutex);

    for (auto& user : activeUsers) {
        send(user.second, data.c_str(), data.size(), 0);
    }

    if (username != "") {
        std::cout << "- user '" + username + "' send message to all users" << std::endl;
    } else {
        std::cout << "- send message to all users" << std::endl;
    }
    
}

std::string getUsernameByFd(int fd) {
    std::lock_guard<std::mutex> lock(mutex);

    for (auto& user : activeUsers) {
        if (user.second == fd) {
            return user.first;
        }
    }

    return "";
}

void userThread(int fd_recv) {
    std::string username;
    bool isLoggedIn = false;

    while (true) {
        // recv
        char buffer[1024];
        int length = recv(fd_recv, &buffer, sizeof(buffer)-1, 0);

        if (length <=0 ) {
            if (!isLoggedIn) {
                username = "not-logged-in";
            }
            std::cout << "- lost connection with user '" + username + "'" << std::endl;
            if (isLoggedIn) {
                std::lock_guard<std::mutex> lock(mutex);
                activeUsers.erase(username);
                close(fd_recv);
                std::cout << "- user '" + username + "' deactivated" << std::endl;
            }
            break;
        }
        buffer[length] = '\0';

        std::string data = buffer;
        std::vector<std::string> dataV = split(data, ";");

        std::string operation = dataV[0];
        std::string password;
        std::string message;

        if (operation == "reg") {
            // std::cout << "== REGISTRATION" << std::endl;
            
            username = dataV[1];
            password = dataV[2];

            std::lock_guard<std::mutex> lock(mutex);
            if (registeredUsers.find(username) == registeredUsers.end()) {
                registeredUsers[username] = password;

                std::cout << "- add new user '" << username << "'" << std::endl;

                data = "ok";
                send(fd_recv, data.c_str(), data.size(), 0);
            } else {
                std::cout << "- error: user already exists" << std::endl;

                data = "err";
                send(fd_recv, data.c_str(), data.size(), 0);
            }   
        } else if (operation == "logIn") {
            // std::cout << "== LOG IN" << std::endl;
            
            username = dataV[1];
            password = dataV[2];

            // std::lock_guard<std::mutex> lock(mutex);
            if (registeredUsers.find(username) != registeredUsers.end()) {
                if (activeUsers.find(username) != activeUsers.end()) {
                    std::cout << "Error: user '" + username + "' is already logged in" << std::endl;

                    data = "err;user '" + username + "'is already logged in";
                    send(fd_recv, data.c_str(), data.size(), 0);
                } else if (registeredUsers[username] == password) {
                    std::cout << "- user '" + username + "' logged in successfully" << std::endl;

                    isLoggedIn = true;
                    activeUsers[username] = fd_recv;
                    data = "ok";
                    send(fd_recv, data.c_str(), data.size(), 0);
                    sendListOfActiveUsers(fd_recv);

                    data = "User '" + username + "' was joined the chat";
                    sendToAllUsers(data);
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
            // std::cout << "== MESSAGE TO ALL" << std::endl;

            message = dataV[1];
            data = "<" + username + "> " + message;

            sendToAllUsers(data, username);
        } else if (operation == "messPriv") {
            // std::cout << "== PRIVATE MESSAGE" << std::endl;

            std::string recv_username = dataV[1];
            message = dataV[2];

            std::lock_guard<std::mutex> lock(mutex);

            if (activeUsers.find(recv_username) != activeUsers.end()) {
                int fd_priv = activeUsers[recv_username];

                data = "[priv] <" + username + "> " + message;

                send(fd_priv, data.c_str(), data.size(), 0);
                std::cout << "- user '" + username + "' send private message to user '" + recv_username + "'" << std::endl;
            } else {
                data = "err;user '" + recv_username + "' doesn't exist or isn't active";
                send(fd_recv, data.c_str(), data.size(), 0);
                std::cout << "- error: user '" + recv_username + "' doesn't exists or isn't active" << std::endl;
            }

        } else if (operation == "logOut") {
            std::cout << "- log out user '" + username +"'" << std::endl;
            mutex.lock();
            activeUsers.erase(username);
            mutex.unlock();

            data = "User '" + username + "' was left the chat";
            sendToAllUsers(data);

            // shutdown
            shutdown(fd_recv, SHUT_WR);

            // close
            close(fd_recv);
            std::cout << "- close connection with client (user '" + username + "')" << std::endl;
            break;
        } else if (operation == "allUsers") {
            sendListOfActiveUsers(fd_recv);
        }
    }
}

int main() {
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

    bind(fd, (struct sockaddr *) &addr, sizeof(addr));

    // listen
    listen(fd, 10);
    
    std::cout << "Server started on port: " << port << std::endl;

    while (true) {
        // accept
        socklen_t addr_len = sizeof(addr);
        int fd_recv = accept(fd, (struct sockaddr *) &addr, &addr_len);

        std::cout << "== NEW CONNECTION" << std::endl;
        if (fd_recv >= 0) {
            userThreads.push_back(std::thread(userThread, fd_recv));
        } 

    }

    for (auto& user : activeUsers) {
        shutdown(user.second, SHUT_WR);
        close(user.second);
    }

    for (auto& userThread : userThreads) {
        userThread.join();
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

// allUsers