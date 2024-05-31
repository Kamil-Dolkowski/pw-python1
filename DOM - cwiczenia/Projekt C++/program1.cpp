#include <iostream>
#include <fstream>
#include <string>
#include <cstdlib>
#include <vector>
using namespace std;

//#define FILE "solar_panel_data_20240522.json"
#define FILE "plik.txt"


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

void avg(vector < string > timestamp, vector < double > u, vector < double > i, int interval) {
    int hour, hourStart;
    int minute, minuteStart;
    int counter=0;
    double sumU=0, sumI=0, avgU, avgI;

    hourStart = stoi(timestamp[0].substr(8,2));
    //minuteStart = stoi(timestamp[0].substr(10,2));
    minuteStart = 0;

    for (int x=0; x<u.size(); x++){
        hour = stoi(timestamp[x].substr(8,2));
        minute = stoi(timestamp[x].substr(10,2));

        if (hour == hourStart) {
            if (minute < minuteStart + interval) {
                counter++;
                sumU += u[x];
                sumI += i[x];
            } else {
                if (counter == 0) {
                    //jesli pierwszy pomiar nie nalezy  do [HH:00-HH:interval)
                    minuteStart = interval * (minute/interval);
                    sumU += u[x];
                    sumI += i[x];
                    counter++;
                } else {
                    avgU = sumU/counter;
                    avgI = sumI/counter;

                    cout << endl;
                    if (hourStart < 10) cout << "0";
                    cout << hourStart << ":";
                    if (minuteStart < 10) cout << "0";
                    cout << minuteStart << "-";
                    if (hourStart < 10) cout << "0";
                    cout << hourStart << ":";
                    if (minuteStart + interval < 10) cout << "0";
                    cout << minuteStart + interval << ":" << endl;
                    printf("Napiecie srednie [U]: %f\n", avgU);
                    printf("Natezenie srednie [I]: %f\n", avgI);

                    minuteStart = minuteStart + interval;
                    sumU = u[x];
                    sumI = i[x];
                    counter = 1;
                }
            }
        } else {
            // godz - pelnaGodzina:
            avgU = sumU/counter;
            avgI = sumI/counter;

            cout << endl;
            if (hourStart < 10) cout << "0";
            cout << hourStart << ":";
            if (minuteStart < 10) cout << "0";
            cout << minuteStart << "-";
            if (hourStart + 1 < 10) cout << "0";
            cout << hourStart + 1 << ":00:" << endl;
            printf("Napiecie srednie [U]: %f\n", avgU);
            printf("Natezenie srednie [I]: %f\n", avgI);

            hourStart = hour;
            minuteStart = 0;
            sumU = u[x];
            sumI = i[x];
            counter = 1;
        }
    }


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




int main(int argc, char ** argv) {
    fstream plik;
    plik.open(FILE, ios::in);

    string wierszDanych;
    string fragment;
    vector < string > timestamp;
    vector < double > u;
    vector < double > i;

    //-------------------WYCIAGNIECIE DANYCH Z PLIKU-----------------------

    if (plik.good() == true) {

        while ( !plik.eof() ) {
            getline(plik, wierszDanych);
            //cout << wierszDanych << endl;
            //cout << endl;

            if (wierszDanych == "") {
                break;
            }

            //1. sprawdzam "timestamp_server"  |  {"timestamp_server": "
            fragment = wierszDanych.substr( 0, 22 );
            //cout << fragment << endl;

            if (fragment != "{\"timestamp_server\": \"") {
                cout << "Error: Invalid data in file." << endl;
                return EXIT_SUCCESS;
            }

            //1.1 sprawdzam timestamp dla "timestamp_server"
            fragment = wierszDanych.substr( 22, 14 );
            //cout << fragment << endl;

            if (!isTimestamp(fragment)) {
                cout << "Error: Invalid data in file." << endl;
                return EXIT_SUCCESS;
            }

            //2. sprawdzam "data"  |  ", "data": {"
            fragment = wierszDanych.substr( 36, 13 );
            //cout << fragment << endl;

            if (fragment != "\", \"data\": {\"") {
                cout << "Error: Invalid data in file." << endl;
                return EXIT_SUCCESS;
            }


            int index = 46;
            //poszczegolne pomiary
            while (1) {

                //2.1 sprawdzam wartosc timestamp dla "data"
                index += 3;
                fragment = wierszDanych.substr( index, 14 );
                //cout << fragment << endl;

                if (!isTimestamp(fragment)) {
                    cout << "Error: Invalid data in file." << endl;
                    return EXIT_SUCCESS;
                }
                timestamp.push_back(fragment);

                //2.2 sprawdzam "U" dla "data"  |  ":{"U":
                index += 14;
                fragment = wierszDanych.substr( index, 7 );
                //cout << fragment << endl;

                if (fragment != "\":{\"U\":") {
                    cout << "Error: Invalid data in file." << endl;
                    return EXIT_SUCCESS;
                }

                //2.3 sprawdzam wartosc "U" dla "data"
                index += 7;
                fragment = wierszDanych.substr( index, 5 );
                //cout << fragment << endl;

                if (!isDoubleAB_CD(fragment)) {
                    cout << "Error: Invalid data in file." << endl;
                    return EXIT_SUCCESS;
                }
                u.push_back(stod(fragment));

                //2.4 sprawdzam "I" dla "data"  |  ,"I":
                index += 5;
                fragment = wierszDanych.substr( index, 5 );
                //cout << fragment << endl;

                if (fragment != ",\"I\":") {
                    cout << "Error: Invalid data in file." << endl;
                    return EXIT_SUCCESS;
                }

                //2.5 sprawdzam wartosc "I" dla "data"
                index += 5;
                fragment = wierszDanych.substr( index, 5 );
                //cout << fragment << endl;

                if (!isDoubleAB_CD(fragment)) {
                    cout << "Error: Invalid data in file." << endl;
                    return EXIT_SUCCESS;
                }
                i.push_back(stod(fragment));

                //3. sprawdzam czy koniec pomiaru lub koniec wiersza
                index += 5;
                fragment = wierszDanych.substr( index, 3 );
                //cout << fragment << endl;

                //3.a) czy koniec pomiaru
                if (fragment != "},\"") {
                    //3.b) czy koniec wiersza
                    if (fragment == "}}}"){
                    //cout << "==koniec wiersza" << endl;
                    //koniec wiersza
                    break;
                    } else {
                        cout << "Error: Invalid data in file." << endl;
                        return EXIT_SUCCESS;
                    }
                }
                //kolejny pomiar
            }
            //kolejny wiersz
        }

    } else {
        cout << "Plik nie istnieje." << endl;
    }

    plik.close();

    //-------------------OPERACJE NA DANYCH Z PLIKU-----------------------
    //przedzialy godzinowe [X,X)

    //showParametersIndex(timestamp, u, i, 7000, 9000);
    //showParametersHours(timestamp, u, i, "10:30", "10:45");

    if (argc != 3) {
        cout << "Error: Invalid number of arguments. " << endl;
        cout << "[program.exe -t PARAMETER] " << endl;
        cout << "PARAMETER ::= h / m30 / m5" << endl;
    }

    string arg1 = argv[1];
    string arg2 = argv[2];

    if (arg1 == "-t") {
        if (arg2 == "h") {
            avg(timestamp, u, i, 60);
        } else if (arg2[0] == 'm' && isDigit(arg2.substr(1,2)) ) {
            int interval = stoi(arg2.substr(1,2));
            avg(timestamp, u, i, interval);
        }
    }

    //avg(timestamp, u, i, 20);



	return EXIT_SUCCESS;
}
