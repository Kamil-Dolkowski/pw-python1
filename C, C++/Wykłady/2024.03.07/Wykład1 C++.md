STL (Standard Template Library) - zestaw szablonów klas i funkcji -> algorytmy, kontenery i iteratory -> wygoda, efektywność

# Składniki STL:
-kontenery - zapewniają przechowywanie danych w różnych strukturach, takich jak listy, wektory, kolejki, stosy, itp.
-algorytmy - oferują zestaw gotowych algorytmów do przetwarzania danych (sortowanie, wyszukiwanie, transformacje, itp.)
-iteratory - umożliwiają ogólne operacje na elementach kontenerów (przeglądanie, dostęp, modyfikacja danych)

# Dlaczego warto korzystać z STL?
-gotowe rozwiązania
-przenośność kodu
-efektywność i wydajność
-bogactwo funkcji
-standardowy interfejs

# Kontenery:
-obiekty, które przechowują inne obiekty
-organizowanie danych w różnych strukturach, np. wektory, listy, kolejki, stosy

# Algorytmy:
-funkcje, które operują na elementach kontenerów
-gotowe rozwiązania, np. sortowanie
-niezależne od typu kontenera

# Iteratory:
-obiekty, które umożliwiają poruszanie się po elementach kontenerów

# Kontenery sekwencyjne:
-std::vector:
-std::list:
-std::deque:

# std::vector (najczęściej używany)
-dynamiczny rozmiar
-szybki dostęp - czas odczytu nie zależy od ilości elementów
-wykorzystanie pamięci - w pamięci procesora (blisko procesora)
-iteratory - (różne typy ?)
-operacje na końcach (push_back, pop_back)
-przenoszenie i kopiowanie
-wielokrotne zastosowanie - różne typy danych

# Podstawowa składnia std::vector  (niepełne)
#include <vector>
std::vector <typ danych> <nazwa wektora>

#----------------------------------------------------------------------------------------------

#include <vector>

int main()
{
    // Inicjalizacja pustego wektora
    std::vector<int> vec;
    
    // Inicjalizacja wektora z określoną ilością elementów i wartością domyślną
    std::vector<int> vec2(5,0); // Wektor z 5 elementami o wartości 0
    
    // Inicjalizacja wektora z innego wektora
    std::vector<int> vec3 = {1,2,3,4,5};
    
    // Kopiowanie zawartości innego wektora
    std::vector<int> vec4(vec3);

    return 0;
}

#----------------------------------------------------------------------------------------------

#include <vector>

int main()
{
    std::vector<int> vec;
    vec.push_back(10);
    vec.push_back(20);
    
    vec.pop_back();
    
    return 0;
}

#----------------------------------------------------------------------------------------------

#include <iostream>
#include <vector>

int main()
{
    std::vector<int> vec = {1,2,3,4,5};
    
    int value = vec[2];
    
    int first = vec.front();
    int last = vec.back();
    
    for (int i = 0; i< vec.size(); ++i) {
        std::cout << vec[i] << " ";
    }
    std::cout << std::endl;
    
    return 0;
}

#----------------------------------------------------------------------------------------------

# Dynamiczne zarządzanie pamięcią
-std::vector zarządza pamięcią dynamicznie przy użyciu alokacji pamięci
-elastyczna zmiana rozmiaru

std::vector zastępuje tradycyjne tablice w C++, ponieważ oferuje dynamiczny rozmiar, co pozwala na elastyczne zarządzanie pamięcią.

przekazywanie std::vector jako argumentu funkcji

#----------------------------------------------------------------------------------------------

#include <iostream>
#include <vector>

void processVector(const std::vector<int>& vec) {
    for (int i : vec) {
        std::cout << i << " ";
    }
    std::cout << std::endl;
}

int main()
{
    std::vector<int> intVector = {1,2,3,4,5};
    std::vector<double> doubleVector = {1.1,2.2,3.3,4.4,5.5};
    
    std::vector<int> arrayReplacement = {10,20,30,40,50};
    
    processVector(arrayReplacement);
    
    return 0;
}

#----------------------------------------------------------------------------------------------

#include <iostream>
#include <vector>

int main()
{
    std::vector<int> vec;
    
    vec.push_back(10);
    vec.push_back(20);
    vec.push_back(30);
    
    std::cout << "Zawartość wektora: ";
    for (int i : vec) {
        std::cout << i << " ";
    }
    std::cout << std::endl;
    
    std::cout << "Element o indeksie 1: " << vec[1] << std::endl;
    
    vec.pop_back();
    
    std::cout << "Aktualny rozmiar wektora: " << vec.size() << std::endl;
    
    return 0;
}

#----------------------------------------------------------------------------------------------

#include <iostream>
#include <vector>
#include <list>
#include <chrono>

int main()
{
    const int N = 1000000;
    std::vector<int> vec;
    std::list<int> lst;
    
    auto startVec = std::chrono::high_resolution_clock::now();
    for (int i = 0; i < N; ++i) {
        vec.push_back(i);
    }
    
    auto endVec = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> timeVec = endVec - startVec;
    std::cout << "Czas dodawania do wektora: " << timeVec.count() << " sekund" << std::endl;
    
    auto startList = std::chrono::high_resolution_clock::now();
    for (int i = 0; i < N; ++i) {
        lst.push_back(i);
    }
    
    auto endList = std::chrono::high_resolution_clock::now();
    std::chrono::duration<double> timeList = endList - startList;
    std::cout << "Czas dodawania do listy: " << timeList.count() << " sekund" << std::endl;
    
    return 0;
}

#----------------------------------------------------------------------------------------------

# STL - podsumowanie:
-gotowe rozwiązania
-efektywność
-przenośność
-przejrzystość