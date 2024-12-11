#include <iostream>
#include <thread>
#include <vector>

void loop(int n) {
    for (int i=0; i<2000000000; i++);
    std::cout << "Koniec wątku: " << n << std::endl;
}


int main(){
    std::vector<std::thread> threads;
    unsigned int hwThreads = std::thread::hardware_concurrency();
    // hardware_concurrency() może zwrócić '0'
    hwThreads = hwThreads ? hwThreads : 1;

    for (int i=0; i<hwThreads; i++) {
        threads.push_back(std::thread(loop, i));
    }

    for (int i=0; i<hwThreads; i++) {
        std::cout << "Oczekiwanie na wątek" << std::endl;
        threads[i].join();
    }
    return 0;
}