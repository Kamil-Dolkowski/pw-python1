#include <iostream>
#include <thread>
#include <vector>
#include <atomic>

std::atomic<int> zmienna = 0;

void loop(int n) {
    for (int i=0; i<10000; i++) {
        zmienna.fetch_add(1);
    }
}


int main(){
    std::vector<std::thread> threads;
    unsigned int hwThreads = std::thread::hardware_concurrency(); 
    hwThreads = hwThreads ? hwThreads : 1;

    for (int i=0; i<hwThreads; i++) {
        threads.push_back(std::thread(loop, i));
    }

    for (int i=0; i<hwThreads; i++) {
        threads[i].join();
    }

    std::cout << zmienna.load() << std::endl;

    return 0;
}