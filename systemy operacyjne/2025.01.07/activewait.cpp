// aktywne czekanie (pętla while) zużywa 100% CPU
#include <thread>
#include <iostream>
#include <string>
#include <unistd.h>

std::string sharedString;
volatile bool flag = false;

void threadFunc() {
    std::cout << "wątek oczekuje na zmianę flagi\n";
    while(!flag);
    sleep(3);

    std::cout << "wątek zaczyna działanie\n";
    std::cout << sharedString << std::endl;
    sharedString = "Kot ma Alę.";

    flag = false;
}

int main() {
    std::thread t(threadFunc);
    sleep(3);

    sharedString = "Ala ma kota.";
    std::cout << "main zmienia flagę\n";
    flag = true;

    while(flag);
    std::cout << sharedString << std::endl;

    t.join();
    // t.join() -> sprząta po aktywnym wątku (kiedy program się zakończy, a wątek nadal działa, nie zwraca błędu i po nim "sprząta")
    return 0;
}