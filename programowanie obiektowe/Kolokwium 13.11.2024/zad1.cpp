#include <iostream>
#include <cstdlib>
#include <string.h>

class TimeLength {
public:
    TimeLength(const char *_seconds) {
        copy = strdup(_seconds);
        unsigned long value = strtoul(_seconds, NULL, 10);

        hours = value / 3600;
        minutes = (value - hours*3600) / 60;
        seconds = value - hours*3600 - minutes*60;

    };
    ~TimeLength() { delete copy; };
    
    TimeLength(const TimeLength &source) {
        copy = strdup(source.copy);
        hours = source.hours;
        minutes = source.minutes;
        seconds = source.seconds;
    }

    friend std::ostream& operator<<(std::ostream &os, const TimeLength &t);

    // const char * getString() const { return copy; }      // !! const char *   <- tak powinno być 
    char * getString() const { return copy; }
    
    static TimeLength& createZeroLength() {
        static TimeLength zero("0");
        return zero;
    }
    
private:
    char *copy;
    unsigned long hours;
    unsigned long minutes;
    unsigned long seconds;
};

std::ostream& operator<<(std::ostream &os, const TimeLength &t) {
    os << t.hours << "h " << t.minutes << "min " << t.seconds << "sec" ;
    return os;
}


int main() {
    //b)
    TimeLength uptime("19592");
    std::cout << uptime << std::endl;

    //c)
    std::cout << std::endl;
    TimeLength uptimeNew(uptime);

    std::cout << "uptime:" << std::endl;
    std::cout << uptime << std::endl;

    std::cout << std::endl;
    std::cout << "uptimeNew:" << std::endl;
    std::cout << uptimeNew << std::endl;

    //d)
    std::cout << std::endl;
    std::cout << "getString():" << std::endl;
    std::cout << uptime.getString() << std::endl;

    //e)
    std::cout << std::endl;
    std::cout << "createZeroLength(): " << std::endl;
    std::cout << TimeLength::createZeroLength() << std::endl;


    return 0;
}