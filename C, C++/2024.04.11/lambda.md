#-----------------------------------LAMBDA-------------------------------------

lambda - anonimowe funkcje -> szybkie i zwięzłe operacje na miejscu
przydatne w algorytmach STL

[capture][parameters] -> return_type {body}

#---------------

#include <iostream>

int main() {
    auto sum = [](int a, int b) -> int { return a+b; };
    std::cout << sum(5,3); // OUTPUT: 8
    
    return 0;
}

#-----------------------------KLAUZULA CAPTURE----------------------------------

kontroluje, które zmienne z zewnętrznego zakresu są "chwytane" (dostępne) wewnątrz wyrażenia lambda

#---------------

#include <iostream>

int main() {
    int x = 4;
    auto access_by_value = [=]() { std::cout << "Dostęp przez wartość: " << x << std::endl; }; 
    auto access_by_reference = [&]() { std::cout << "Dostęp przez referencję przed zmianą: " << x << " "; ++x; std::cout << "po zmianie: " << x << std::endl; }; 
    
    access_by_value();  // Dostęp przez wartość, x pozostaje niezmienione
    access_by_reference();  // Dostęp przez referencję, x jest modyfikowalne

    return 0;
}

#----------------------------WYRAŻENIA LAMBDA W STL-----------------------------

umożliwiają definicję niestandardowych operacji bez potrzeby tworzenia oddzielnych funkcji
Są szczególnie użyteczne w algorytmach takich jak: std::sort, std::for_each, std::transform

#---------------

#include <algorithm>
#include <vector>
#include <iostream>

int main() {
    std::vector<int> vec{1,2,3,4,5};
    std::for_each(vec.begin(), vec.end(), [](int& n) { n *= 2; });
    
    std::cout << "Elementy po podwojeniu: ";
    for(int n : vec) {
        std::cout << n << ' ';
    }
    std::cout << std::endl;

    return 0;
}

#-------------------ZAAWANSOWANE ZASTOSOWANIE WYRAŻEŃ LAMBDA-------------------

tworzenie skomplikowanych filtrów, operacji mapowania, redukcji w sposób zwięzły i czytelny
klauzula capture pozwala na elastyczne zarządzanie zakresem i zmiennymi

#---------------

#include <algorithm>
#include <vector>
#include <iostream>

int main() {
    std::vector<int> vec{1,2,3,4,5};
    int threshold = 3;
    
    vec.erase(std::remove_if(vec.begin(), vec.end(), [threshold](int n) { return n < threshold; }), vec.end());
    
    std::cout << "Elementy większe lub równe 3: ";
    for (int n :vec) {
        std::cout << n << ' ';
    }
    std::cout << std::endl;

    return 0;
}

#-----------------------------------ZADANIE-------------------------------------

filtr danych wejściowych (wektor liczb całkowitych), zostawiając tylko te liczby, które są parzyste, a następnie je podwaja

#--------------------

#include <algorithm>
#include <vector>
#include <iostream>

int main() {
    std::vector<int> input{1,2,3,4,5,6,7,8,9,10};
    std::vector<int> filtered;
    std::vector<int> transformed;
    
    // Filtrowanie: usuwamy liczby nieparzyste
    std::copy_if(input.begin(), input.end(), std::back_inserter(filtered), [](int x) { return x % 2 == 0; }); // Wyrażenie lambda sprawdza parzystość
    
    // Transformacja: podwajamy wartości
    std::transform(filtered.begin(), filtered.end(), std::back_inserter(transformed), [](int x) { return x * 2; }); // Wyrażenie lambda podwaja wartość
    
    // Wyświetlanie wyników
    std::cout << "Przefiltrowane i przetransformowane dane: ";
    for (int n : transformed) {
        std::cout << n << " ";
    }
    std::cout << std::endl;
    
    return 0;
}