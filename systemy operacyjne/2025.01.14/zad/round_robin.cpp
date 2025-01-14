#include <iostream>
#include <fstream>
#include <queue>

class Process {
public:
    Process(std::string _name, size_t _length, size_t _start) : name(_name), length(_length), start(_start) {}
    ~Process() {}

    void print_process() {
        std::cout << "name: " << name << std::endl;
        std::cout << "length: " << length << std::endl;
        std::cout << "start: " << start << std::endl;
    }
private:
    std::string name;
    size_t length;
    size_t start;
};

class RoundRobinScheduler {
public:
    RoundRobinScheduler(const char* _file, size_t _time) {
        file = _file;
        time = _time;
        
        std::string temp;
        std::ifstream ReadFile(file);

        std::string name;
        size_t length;
        size_t start;

        std::string delimiter = ",";

        while (getline(ReadFile, temp)) {
            for (int i=0; i<3; i++) {
                size_t pos = temp.find(delimiter);
                std::string token = temp.substr(0, pos);
                temp.erase(0, temp.find(delimiter) + delimiter.length());

                switch (i) {
                    case 0:
                        name = token;
                        break;
                    case 1:
                        length = stoi(token);
                        break;
                    case 2:
                        start = stoi(token);
                        break;
                }
            }
    
            waiting_processes.push(Process(name, length, start));
        }
    }

    void run() {
        size_t simulation_time = 0;

        while(!waiting_processes.empty() || !executing_processes.empty()) {
            std::cout << "a" << std::endl;
            for (int i=0; i<waiting_processes; i++)
        }

        std::cout << "T=" << simulation_time << ": ";
        std::cout << "No more processes in queues" << std::endl;
    }

    void print_waiting_processes() {
        std::queue<Process> q = waiting_processes;

        std::cout << "WAITING PROCESSES: \n" << std::endl;

        while (!q.empty()) {
            q.front().print_process();
            q.pop();
            std::cout << "" << std::endl;
        }
    }

private:
    std::string file;
    size_t time;
    std::queue<Process> waiting_processes;
    std::queue<Process> executing_processes;
};



int main(int argc, char* argv[]) {

    RoundRobinScheduler scheduler(argv[1], atoi(argv[2]));

    scheduler.run(); // dokończyć !

    //scheduler.print_waiting_processes();

    return 0;
}