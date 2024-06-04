#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <vector>
using namespace std;

#define FILE "solar_panel_data_20240522.json"
//#define FILE "plik1.txt"


bool isDigit(string text) {
    bool result = true;

    for (int i=0; i<text.length(); i++) {
        if ( !isdigit(text[i]) ) {
            result = false;
            break;
        }
    }

    return result;
}

bool isTimestamp(string & text) {
    bool result=true;

    //sprawdzam dlugosc = 14
    if (text.length() != 14) {
        result = false;
        return result;
    }

    //sprawdzam czy jest to ciag cyfr
    for(int i=0; i<text.length(); i++) {
        if (!isdigit(text[i])) {
            result = false;
            break;
        }
    }

    return result;
}

bool isDoubleAB_CD(string & text) {
    bool result = true;

    if (text[2] != '.') {
        result = false;
    }
    if ( !( isdigit(text[1]) && isdigit(text[3]) ) ) {
        result = false;
    }
    if ( !( isdigit(text[0]) || text[0] == ' ' ) ) {
        result = false;
    }
    if ( !( isdigit(text[4]) || text[4] == ' ' ) ) {
        result = false;
    }

    return result;
}

bool isFactorOf60(int x) {
    int factors[12] = {1,2,3,4,5,6,10,12,15,20,30,60};
    bool result=false;

    for(int i=0; i<12; i++) {
        if(x == factors[i]) result = true;
    }

    return result;
}


void printHoursAndAvg(int hourStart, int minuteStart, int interval, double avgU, double avgI) {
    cout << endl;
    if (hourStart < 10) cout << "0";
    cout << hourStart << ":";
    if (minuteStart < 10) cout << "0";
    cout << minuteStart << "-";

    if (minuteStart + interval == 60) {
        if (hourStart + 1 == 24) {
            cout << "00:00:" << endl;
        } else {
            if (hourStart + 1 < 10) cout << "0";
            cout << hourStart + 1 << ":";
            cout << "00" << ":" << endl;
        }
    } else {
        if (hourStart < 10) cout << "0";
        cout << hourStart << ":";
        if (minuteStart + interval < 10) {
            cout << "0" << minuteStart + interval << ":" << endl;
        } else {
            cout << minuteStart + interval << ":" << endl;
        }
    }
    printf("Napiecie srednie [U]: %0.2f\n", avgU);
    printf("Natezenie srednie [I]: %0.2f\n", avgI);
}

void printDate(string date) {
    string day, month, year;

    day = date.substr(6,2);
    month = date.substr(4,2);
    year = date.substr(0,4);

    cout << day << "." << month << "." << year << ":" << endl;
}


void avg(vector < string > timestamp, vector < double > u, vector < double > i, int interval) {
    int hour, hourStart;
    int minute, minuteStart;
    string date, dateStart;
    int counter=0;
    double sumU=0, sumI=0, avgU, avgI;

    dateStart = timestamp[0].substr(0,8);
    hourStart = stoi(timestamp[0].substr(8,2));
    minuteStart = stoi(timestamp[0].substr(10,2));
    minuteStart = interval * (minuteStart/interval);

    if (interval == 60) {
        cout << "\n======SREDNIE WARTOSCI CO GODZINE======" << endl;
    } else {
        cout << "\n======SREDNIE WARTOSCI CO " << interval << " MINUT======" << endl;
    }

    cout << "\n- - - - - - - - - - - - - - - -" << endl;
    printDate(dateStart);

    for (int x=0; x<u.size(); x++){
        date = timestamp[x].substr(0,8);
        hour = stoi(timestamp[x].substr(8,2));
        minute = stoi(timestamp[x].substr(10,2));

        if (date == dateStart){

            if (hour == hourStart) {
                if (minute < minuteStart + interval) {
                    counter++;
                    sumU += u[x];
                    sumI += i[x];
                } else {
                    avgU = sumU/counter;
                    avgI = sumI/counter;

                    printHoursAndAvg(hourStart, minuteStart, interval, avgU, avgI);

                    minuteStart = interval * (minute/interval);
                    sumU = u[x];
                    sumI = i[x];
                    counter = 1;

                }
            } else {
                avgU = sumU/counter;
                avgI = sumI/counter;

                printHoursAndAvg(hourStart, minuteStart, interval, avgU, avgI);

                hourStart = hour;
                minuteStart = interval * (minute/interval);
                sumU = u[x];
                sumI = i[x];
                counter = 1;
            }
        //jesli inny dzien
        } else {
            avgU = sumU/counter;
            avgI = sumI/counter;

            printHoursAndAvg(hourStart, minuteStart, interval, avgU, avgI);

            dateStart = date;
            hourStart = hour;
            minuteStart = interval * (minute/interval);
            sumU = u[x];
            sumI = i[x];
            counter = 1;

            cout << "\n- - - - - - - - - - - - - - - -" << endl;
            printDate(date);
        }
    }

    //ostatnia wartosc/przedzial
    avgU = sumU/counter;
    avgI = sumI/counter;

    printHoursAndAvg(hourStart, minuteStart, interval, avgU, avgI);
}


void showParametersIndex(vector < string > timestamp, vector < double > u, vector < double > i, int start, int end) {
    for (int x=start; x<end; x++){
        int hour = stoi(timestamp[x].substr(8,2));
        int minute = stoi(timestamp[x].substr(10,2));

        cout << "timestamp: ";
        if (hour < 10) cout << "0";
        cout << hour << ":";
        if (minute < 10) cout << "0";
        cout << minute << ", ";
        printf("U=%0.2lf, I=%0.2lf\n", u[x], i[x]);
    }

}

void showParametersHours(vector < string > timestamp, vector < double > u, vector < double > i, string start, string end) {
    int hourStart = stoi(start.substr(0,2));
    int minuteStart = stoi(start.substr(3,2));
    int hourEnd = stoi(end.substr(0,2));
    int minuteEnd = stoi(end.substr(3,2));
    int hour, minute;

    for (int x=0; x<u.size(); x++) {
        hour = stoi(timestamp[x].substr(8,2));
        minute = stoi(timestamp[x].substr(10,2));

        if (hourStart <= hour && hour<= hourEnd) {
            if (hour == hourStart && minute < minuteStart) {

            } else if (hour == hourEnd && minute > minuteEnd) {

            } else {
                cout << "timestamp: ";
                if (hour < 10) cout << "0";
                cout << hour << ":";
                if (minute < 10) cout << "0";
                cout << minute << ", ";
                printf("U=%0.2lf, I=%0.2lf\n", u[x], i[x]);
            }
        }
    }

}



//===================================================MAIN==========================================================

int main(int argc, char ** argv) {
    fstream plik;
    plik.open(FILE, ios::in);

    string wierszDanych;
    string fragment;
    vector <string> timestamp;
    vector <double> u;
    vector <double> i;

    unsigned int errorLine=1;
    unsigned int errorCount=0;
    unsigned int index;

    string arg1;
    string arg2;

    //-------------SPRAWDZENIE POPRAWNOSCI PODANYCH PARAMETROW--------------

    if (argc != 3) {
        cout << "Error: Invalid number of arguments.\n" << endl;
        cout << "[program.exe -t PARAMETER] " << endl;
        cout << "PARAMETER ::= h / m30 / m5" << endl;
        return EXIT_SUCCESS;
    } else {
        arg1 = argv[1];
        arg2 = argv[2];

        //sprawdzam 1. parametr '-t'
        if (arg1 != "-t") {
            cout << "Error: Command '" << arg1 << "' not exists.\n" << endl;
            cout << "[program.exe -t PARAMETER] " << endl;
            cout << "PARAMETER ::= h / m30 / m5" << endl;
            return EXIT_SUCCESS;
        } 

        //sprawdzam 2. parametr 'h' / 'mXX'
        if (arg2 != "h") {
            if (arg2[0] == 'm') {
                //czy dlugosc arg2 = 2-3 znaki, z czego 2 ostatnie to liczba, ktora jest dzielnikiem 60
                if ( !(arg2.length() > 1 && arg2.length() < 4 && isDigit(arg2.substr(1,2)) && isFactorOf60(stoi(arg2.substr(1,2)))) ) {  
                    cout << "\nInvalid parameter 'm'.\n" << endl;
                    cout << "Possible call: " << endl;
                    cout << "program.exe -t m[factor of 60]" << endl;
                    cout << "Example: program.exe -t m30" << endl;
                    return EXIT_SUCCESS;
                }
            } else {
                cout << "Error: Parameter '" << arg2 << "' not exists.\n" << endl;
                cout << "[program.exe -t PARAMETER] " << endl;
                cout << "PARAMETER ::= h / m30 / m5" << endl;
                return EXIT_SUCCESS;
            }
        }
    }
    //-------------------WYCIAGNIECIE DANYCH Z PLIKU-----------------------

    if (plik.good() == true) {
        while ( !plik.eof() ) {
            getline(plik, wierszDanych);
            index = 0;

            //0. pusta ostatnia linijka
            if (wierszDanych == "") {
                break;
            }

            //1. sprawdzam "timestamp_server"  |  {"timestamp_server": "
            fragment = wierszDanych.substr( index, 22 );

            if (fragment != "{\"timestamp_server\": \"") {
                cout << "Error: Invalid data in file. ";
                cout << "Line: " << errorLine << ", Column: " << index + 1 << "-" << index + 23 << endl;
                errorCount++;
                continue;
            }

            //1.1 sprawdzam timestamp dla "timestamp_server"
            index += 22;
            fragment = wierszDanych.substr( index, 14 );

            if (!isTimestamp(fragment)) {
                cout << "Error: Invalid data in file. ";
                cout << "Line: " << errorLine << ", Column: " << index + 1 << "-" << index + 15 << endl;
                errorCount++;
                continue;
            }

            //2. sprawdzam "data"  |  ", "data": {"
            index += 14;
            fragment = wierszDanych.substr( index, 13 );

            if (fragment != "\", \"data\": {\"") {
                cout << "Error: Invalid data in file. ";
                cout << "Line: " << errorLine << ", Column: " << index + 1 << "-" << index + 14 << endl;
                errorCount++;
                continue;
            }


            index += 10;
            //poszczegolne pomiary
            while (1) {

                //2.1 sprawdzam wartosc timestamp dla "data"
                index += 3;
                fragment = wierszDanych.substr( index, 14 );

                if (!isTimestamp(fragment)) {
                    cout << "Error: Invalid data in file. ";
                    cout << "Line: " << errorLine << ", Column: " << index + 1 << "-" << index + 15 << endl;
                    errorCount++;
                    break;
                }
                timestamp.push_back(fragment);

                //2.2 sprawdzam "U" dla "data"  |  ":{"U":
                index += 14;
                fragment = wierszDanych.substr( index, 7 );

                if (fragment != "\":{\"U\":") {
                    cout << "Error: Invalid data in file. ";
                    cout << "Line: " << errorLine << ", Column: " << index + 1 << "-" << index + 8 << endl;
                    errorCount++;
                    timestamp.pop_back();
                    break;
                }

                //2.3 sprawdzam wartosc "U" dla "data"
                index += 7;
                fragment = wierszDanych.substr( index, 5 );

                if (!isDoubleAB_CD(fragment)) {
                    cout << "Error: Invalid data in file. ";
                    cout << "Line: " << errorLine << ", Column: " << index + 1 << "-" << index + 6 << endl;
                    errorCount++;
                    timestamp.pop_back();
                    break;
                }
                u.push_back(stod(fragment));

                //2.4 sprawdzam "I" dla "data"  |  ,"I":
                index += 5;
                fragment = wierszDanych.substr( index, 5 );

                if (fragment != ",\"I\":") {
                    cout << "Error: Invalid data in file. ";
                    cout << "Line: " << errorLine << ", Column: " << index + 1 << "-" << index + 6 << endl;
                    errorCount++;
                    timestamp.pop_back();
                    u.pop_back();
                    break;
                }

                //2.5 sprawdzam wartosc "I" dla "data"
                index += 5;
                fragment = wierszDanych.substr( index, 5 );

                if (!isDoubleAB_CD(fragment)) {
                    cout << "Error: Invalid data in file. ";
                    cout << "Line: " << errorLine << ", Column: " << index + 1 << "-" << index + 6 << endl;
                    errorCount++;
                    timestamp.pop_back();
                    u.pop_back();
                    break;
                }
                i.push_back(stod(fragment));

                //3. sprawdzam czy koniec pomiaru lub koniec wiersza
                index += 5;
                fragment = wierszDanych.substr( index, 3 );

                //3.a) czy koniec pomiaru
                if (fragment != "},\"") {
                    //3.b) czy koniec wiersza
                    fragment = wierszDanych.substr( index, wierszDanych.length()-index );
                    if (fragment == "}}}"){
                    //koniec wiersza
                    break;
                    } else {
                        cout << "Error: Invalid data in file. ";
                        cout << "Line: " << errorLine << ", Column: " << index + 1 << "-" << index + 4 << endl;
                        errorCount++;
                        break;
                    }
                }
                //kolejny pomiar
            }
            //kolejny wiersz
            errorLine++;
        }

    } else {
        cout << "Error: File not exists." << endl;
    }

    plik.close();

    //-------------------OPERACJE NA DANYCH Z PLIKU-----------------------

    //showParametersIndex(timestamp, u, i, 0, 3);
    //showParametersHours(timestamp, u, i, "10:30", "10:45");

    if (errorCount != 0) {
        char choice;
        cout << endl;
        cout << "Uwaga: Liczba bledow w pliku: " << errorCount << ". Czy chcesz kontynuowac? Y/N" << endl;
        cin >> choice;
        switch (choice) {
            case 'Y':
                //zostanie wykonana dalsza czesc programu
                break;
            case 'y':
                //zostanie wykonana dalsza czesc programu
                break;
            default:
                return EXIT_SUCCESS;
        }
    }


    if (arg2 == "h") {
        avg(timestamp, u, i, 60);
    } 
    if (arg2[0] == 'm') {
        int interval = stoi(arg2.substr(1,2));
        avg(timestamp, u, i, interval);
    }
        
	return EXIT_SUCCESS;
}


//przedzialy czasowe [X,X):

//co 30 min:
//14:00:00 - 14:29:59    ->   14:00-14:30
//14:30:00 - 14:59:59    ->   14:30-15:00

//-----------------------------------------------------------------------------------------

//Problemy:
//-dane w pliku musza byc uporzadkowane od najwczesniejszego do najpozniejszego pomiaru
//-data musi byc poprawnie zapisana (brak pelnej walidacji daty)

//Dzialanie:
//-po wykryciu blednego formatu w pliku reszta danych w wierszu jest pomijana