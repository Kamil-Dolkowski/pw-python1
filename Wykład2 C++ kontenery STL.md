# Kontenery dostępne w STL: deque, list, map, set

#-------------------------------------------DEQUE----------------------------------------------

# deque (Double-Ended Queue)
-dynamicznie skalowany kontener (dodawania i usuwanie elementów na początku i na końcu)
-efektywne dodawanie i usuwanie elementów z obu końców
-zapewnia losowy dostęp do elementów (za pomocą operatora indeksowania [] lub metody at() )

(push_front, push_back)
(pop_front, pop_back)

FIFO

**architektura monolityczna, multiserwisowa

# Zastosowania:
-implementacja kolejek zadań
-bufory cykliczne
-przeglądarki historii

#------------------PRZYKLAD-------------------

#include <iostream>
#include <deque>

int main()
{
    std::deque<int> myDeque;
    
    // Dodawanie elementów na końcu i początku
    myDeque.push_back(10);  // deque: 10
    myDeque.push_front(5);  // deque: 5, 10
    
    // Usuwanie elementów z końca i początku
    myDeque.pop_back();     // deque: 5
    myDeque.pop_front();    // deque: (pusty)
    
    // Losowy dostęp do elementów
    myDeque.push_back(15);
    myDeque.push_back(20);
    std::cout << "Element na pozycji 1: " << myDeque[1] << std::endl;
    
    // Rozmiar deque
    std::cout << "Rozmiar deque: " << myDeque.size() << std::endl;

    return 0;
}

#-------------------------------------------LIST--------------------------------------------------

# list (Linked List)
-sekwencyjny kontener reprezentujący listę dwukierunkową 
-umożliwia szybkie wstawianie i usuwanie elementów w dowolnym miejscu listy (insert, erase) (wstawianie i usuwanie też w środku listy)

# Zastosowania:
-implementacja kolejek priorytetowych
-zarządzanie dynamicznymi zbiorami danych
-implementacja stosów i kolejek

#------------------PRZYKLAD-------------------

#include <iostream>
#include <list>

int main()
{
    std::list<int> myList;
    
    // Wstawianie elementów
    myList.push_back(10);   // myList: 10
    myList.push_front(5);   // myList: 5, 10
    auto it = myList.begin();
    advance(it, 1); // Przesuń iterator na drugą pozycję
    myList.insert(it, 7);   // myList: 5, 7, 10
    
    // Usuwanie elementów
    myList.pop_front(); // myList: 7, 10
    myList.erase(++myList.begin()); // myList: 7
    
    // Iteracja po liście
    std::cout << "Elementy listy: ";
    for (int n : myList) {
        std::cout << n << " ";
    }
    std::cout << std::endl;

    return 0;
}

#----------------------------------------------MAP------------------------------------------------

# map (Associative Container)
-przechowuje pary klucz-wartość, z unikalnymi kluczami
-zapewnia szybki dostęp do wartości na podstawie klucza

# Zastosowania:
-słowniki i bazy danych
-cache'owanie wyników (w aplikacjach wumagających szybkiego dostępu) (klucze - unikalne zapytania, wartości - odpowiedzi na te zapytania)
-zarządzanie ustawieniami i konfiguracjami

#------------------PRZYKLAD-------------------

#include <iostream>
#include <map>

int main()
{
    std::map<std::string, int> ocenyStudentow;
    
    // Wstawianie wartości
    ocenyStudentow["Jan Kowalski"] = 5;
    ocenyStudentow["Anna Nowak"] = 4;
    
    // Aktualizacja wartości
    ocenyStudentow["Jan Kowalski"] = 6;
    
    // Dostęp do wartości
    std::cout << "Ocena Jana Kowalskiego: " << ocenyStudentow["Jan Kowalski"] << std::endl;
    
    // Wyszukiwanie klucza
    if (ocenyStudentow.find("Anna Nowak") != ocenyStudentow.end()) {
        std::cout << "Ocena Anny Nowak: " << ocenyStudentow["Anna Nowak"] << std::endl;
    } else {
        std::cout << "Nie znaleziono oceny dla Anny Nowak." << std::endl;
    }
    
    // Iteracja po mapie
    for(auto& para : ocenyStudentow) {
        std::cout << "Student: " << para.first << ", Ocena: " << para.second << std::endl;
    }
    
    return 0;
}

#---------------------------------------------SET-------------------------------------------------

# set (Associative Container)
-przechowuje unikalne elementy w uporządkowanej sekwencji
-duplikaty nie są dozwolone, a porządek ma znaczenie
-automatycznie sortuje elementy przy wstawianiu

# Zastosowania:
-zbiory unikalnych elementów, gdzie kolejność ma znaczenie
-szybkie sprawdzanie obecności elementu w zbiorze
-operacje na zbiorach (np. algorytmy, analiza danych, systemy rekomendacji, algorytmy grafowe)

#------------------PRZYKLAD-------------------

#include <iostream>
#include <set>

int main()
{
    std::set<int> liczby;
    
    // Wstawianie elementów
    liczby.insert(10);
    liczby.insert(5);
    liczby.insert(20);
    liczby.insert(10);  // Ten element nie zostanie dodany, ponieważ jest już obecny
    
    // Sprawdzanie obecności elementu
    if (liczby.find(5) != liczby.end()) {
        std::cout << "Element 5 znajduje się w zbiorze." << std::endl;
    }
    
    // Iteracja po zbiorze
    std::cout << "Elementy zbioru: ";
    for (int liczba : liczby) {
        std::cout << liczba << " ";
    }
    std::cout << std::endl;
    
    return 0;
}

#-------------------------------------------------------------------------------------------------

