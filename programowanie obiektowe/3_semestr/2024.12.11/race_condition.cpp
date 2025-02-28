#include <iostream>
#include <thread>
#include <vector>

volatile int zmienna = 0;

void loop(int n) {
    for (int i=0; i<10000; i++) {
        zmienna++;
    }
}


int main(){
    std::vector<std::thread> threads;
    unsigned int hwThreads = std::thread::hardware_concurrency();
    hwThreads = hwThreads ? hwThreads : 1;

    for (int i=0; i<10; i++) {
        threads.push_back(std::thread(loop, i));
    }

    for (int i=0; i<10; i++) {
        threads[i].join();
    }

    std::cout << zmienna << std::endl;

    return 0;
}