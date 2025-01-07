#include <thread>
#include <iostream>
#include <string>
#include <unistd.h>
#include <condition_variable>

std::mutex mutex;
std::condition_variable cv;
std::string sharedString;
volatile bool flag = false;

void threadFunc() {
    std::cout << "wątek oczekuje na zmianę flagi\n";

    std::unique_lock lock(mutex); // automatyczny lock() na muteksie
    cv.wait(lock, []{ return flag; });

    // kontynuujemy wykonanie, gdy flaga zostanie zmieniona na true

    std::cout << "wątek zaczyna działanie\n";
    std::cout << sharedString << std::endl;
    sharedString = "zmiana w thread";

    // mutex unlock w destruktorze unique_lock
}

int main() {
    std::thread t(threadFunc);
    sleep(3);

    {
        std::lock_guard lock(mutex); // mutex lock
        sharedString = "zmiana w main()";
        flag = true;
        cv.notify_one();
        // mutex unlock w destruktorze lock_guard
    }

    t.join();
    return 0;
}