#include <iostream>
#include <fstream>
#include <queue>

class Process {
public:
    Process(std::string _name, size_t _length, size_t _start) : name(_name), length(_length), start(_start), time_left(_length) {}
    ~Process() {}

    void print_process() {
        std::cout << "name: " << name << std::endl;
        std::cout << "length: " << length << std::endl;
        std::cout << "start: " << start << std::endl;
        std::cout << "time left: " << time_left << std::endl;
    }

    std::string get_name() { return name; }
    size_t get_length() { return length; }
    size_t get_start() { return start; }

    int time_left;

private:
    std::string name;
    size_t length;
    size_t start;
};

class RoundRobinScheduler {
public:
    RoundRobinScheduler(const char* _file, size_t _time_quantum) {
        file = _file;
        time_quantum = _time_quantum;
        
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
        size_t stop_time = 0;
        size_t execution_time = 0;

        // jeśli dla simulation_time = 0 nie ma żadnych procesów
        if (waiting_processes.front().get_start() != 0) std::cout << "T=0: No processes currently available" << std::endl;

        while(!waiting_processes.empty() || !executing_processes.empty()) {

            // std::cout << "====simulation time: " << simulation_time << std::endl;

            // Sprawdzamy, czy są dostępne jakieś procesy do uruchomienia w danym momencie czasowym, 
            // jeżeli tak to przenosimy je z kolejki oczekującej na kolejkę szeregowania.
            for (int i=0; i < waiting_processes.size(); i++) {
                if (waiting_processes.front().get_start() == simulation_time) {
                    std::cout << "T=" << simulation_time << ": ";
                    std::cout << "New process " << waiting_processes.front().get_name() ; 
                    std::cout << " is waiting for execution (length=" << waiting_processes.front().get_length() << ")" << std::endl;

                    executing_processes.push(waiting_processes.front());
                    waiting_processes.pop();
                } else {
                    break;
                }
            }

            // Jeżeli kolejka szeregowania nie jest pusta, to bierzemy pierwszy element i pozwalamy mu 
            // działać przez określony kwant czasu (lub aż zakończy swoje działanie, jeżeli trwa krócej).
            if (!executing_processes.empty()) {

                // std::cout << "execution time : " << execution_time << std::endl;
                // std::cout << "stop time : " << stop_time << std::endl;
                // std::cout << "first: " << executing_processes.front().get_name() << std::endl;
                
                if (executing_processes.front().time_left == stop_time && execution_time == 0) {
                     // wywłaszczenie procesu
                    if (executing_processes.front().time_left != 0) {
                        executing_processes.push(executing_processes.front());
                        executing_processes.pop();

                    } else {
                        // zakończenie działania procesu
                        std::cout << "T=" << simulation_time << ": ";
                        std::cout << "Process " << executing_processes.front().get_name() << " has been finished" << std::endl;

                        executing_processes.pop();
                    }
                }


                // nowy proces
                if (!executing_processes.empty() && execution_time == 0) {
                    if (executing_processes.front().time_left - time_quantum <= 0) {
                        stop_time = 0;
                        execution_time = executing_processes.front().time_left;

                        std::cout << "T=" << simulation_time << ": ";
                        std::cout << executing_processes.front().get_name() << " will be running for " << executing_processes.front().time_left << " time units. " ; 
                        std::cout << "Time left: 0" << std::endl;
                    } else {
                        
                        if (executing_processes.front().time_left - time_quantum < time_quantum) {
                            execution_time = time_quantum;
                            stop_time = executing_processes.front().time_left - time_quantum;
                        } else {
                            execution_time = time_quantum;
                            stop_time = executing_processes.front().time_left - time_quantum;
                        }
                        

                        std::cout << "T=" << simulation_time << ": ";
                        std::cout << executing_processes.front().get_name() << " will be running for " << time_quantum << " time units. " ; 
                        std::cout << "Time left: " << executing_processes.front().time_left - time_quantum << std::endl;
                    }
                
                }
                
                execution_time--;
                executing_processes.front().time_left--;

            }

            // print_executing_processes();

            simulation_time++;

            // if (simulation_time == 12) break;

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

    void print_executing_processes() {
        std::queue<Process> q = executing_processes;

        std::cout << "EXECUTING PROCESSES: \n" << std::endl;

        while (!q.empty()) {
            q.front().print_process();
            q.pop();
            std::cout << "" << std::endl;
        }
    }

private:
    std::string file;
    int time_quantum;
    std::queue<Process> waiting_processes;
    std::queue<Process> executing_processes;
};



int main(int argc, char* argv[]) {

    if (argc != 3) {
        std::cout << "Error: Invalid number of arguments." << std::endl;
        return -1;
    }

    RoundRobinScheduler scheduler(argv[1], atoi(argv[2]));

    scheduler.run(); 

    //scheduler.print_waiting_processes();

    return 0;
}