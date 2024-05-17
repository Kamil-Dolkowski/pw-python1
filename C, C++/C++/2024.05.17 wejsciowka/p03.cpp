#include <iostream>
#include <cstdlib>
#include <string>
using namespace std;

class Clock {
private:
  unsigned int year;
  unsigned int month;
  unsigned int day;

  unsigned int hour;
  unsigned int minute;
  unsigned int sec;
public:
  void printDateTime();
  void setTime(unsigned int year, unsigned int month, unsigned int day, unsigned int hour, unsigned int minute, unsigned int sec);
  void setTime(unsigned int year, unsigned int month, unsigned int day);
  void setTime(unsigned int hour, unsigned int minute);
};

void Clock::printDateTime() {
  string monthF = to_string(month);
  string dayF = to_string(day);
  string hourF = to_string(hour);
  string minuteF = to_string(minute);
  string secF = to_string(sec);

  if (month<10) {
    monthF = '0' + monthF;
  }
  if (day<10) {
    dayF = '0' + dayF;
  }
  if (hour<10) {
    hourF = '0' + hourF;
  }
  if (minute<10) {
    minuteF = '0' + minuteF;
  }
  if (sec<10) {
    secF = '0' + secF;
  }

  cout << year << "-" << monthF << "-" << dayF << ", ";
  cout << hourF << ":" << minuteF << ":" << secF << endl;
  //printf("%u-%u-%u, %u:%u:%u\n",year,month,day,hour,minute,sec);
}

void Clock::setTime(unsigned int year, unsigned int month, unsigned int day, unsigned int hour, unsigned int minute, unsigned int sec = 0) {
  setTime(year, month, day);
  //this->year = year;
  //this->month = month;
  //this->day = day;

  setTime(hour, minute);
  //this->hour = hour;
  //this->minute = minute;

  this->sec = sec;
}

void Clock::setTime(unsigned int year, unsigned int month, unsigned int day) {
  this->year = year;
  this->month = month;
  this->day = day;
}

void Clock::setTime(unsigned int hour, unsigned int minute) {
  this->hour = hour;
  this->minute = minute;
}



int main() {
  Clock c;
  // Ustawienie 2024-05-10, 08:30:20
  c.setTime(2024, 5, 10, 8, 30, 20);
  c.printDateTime();

  // Ustawienie 2024-05-10, 08:30:00
  c.setTime(2024, 5, 10, 8, 30);
  c.printDateTime();

  // Ustawienie 2024-05-10, godzina pozostaje bez zmian
  c.setTime(2024, 5, 10);
  c.printDateTime();

  // Ustawienie godziny na 08:30:00, data pozostaje bez zmian
  c.setTime(8, 30);
  c.printDateTime();

  cout << "====================" << endl;

  // Ustawienie 2024-05-10, 08:30:20
  c.setTime(2024, 5, 10, 8, 30, 20);
  c.printDateTime();

  // Ustawienie 2023-04-02, 01:03:00
  c.setTime(2023, 4, 2, 1, 3);
  c.printDateTime();

  // Ustawienie 2022-12-06, godzina pozostaje bez zmian
  c.setTime(2022, 12, 6);
  c.printDateTime();

  // Ustawienie godziny na 15:45:00, data pozostaje bez zmian
  c.setTime(15, 45);
  c.printDateTime();

  return 0;
}

