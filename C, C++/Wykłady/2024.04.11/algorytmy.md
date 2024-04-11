#----------------------STD::SORT--------------------
sortowanie elementów w kontenerze


#include <algorithm>
#include <vector>
#include <iostream>

int main() {
    std::vector<int> vec{4,1,3,5,2};
    std::sort(vec.begin(), vec.end());
    for (int n : vec) {
        std::cout << n << ' ';
    }
    
    return 0;
}


#----------------------STD::FIND--------------------
wyszukiwanie pierwszego wystąpienia wartości w kontenerze
zwraca: iterator do pierwszego znalezionego elementu lub iterator końca kontenera, jeśli wartość nie została znaleziona


#include <algorithm>
#include <vector>
#include <iostream>

int main() {
    std::vector<int> vec{1,2,3,4,5};
    auto it = std::find(vec.begin(), vec.end(), 3);
    if (it != vec.end()) {
        std::cout << "Znaleniono element: " << *it << '\n';
    } else {
        std::cout << "Element nie został znaleziony.\n";
    }
    
    return 0;
}


#----------------------STD::ACCUMULATE--------------------
sumowanie elementów w kontenerze


#include <numeric>
#include <vector>
#include <iostream>

int main() {
    std::vector<int> vec{1,2,3,4,5};
    int sum = std::accumulate(vec.begin(), vec.end(), 0);
    std::cout << "Suma elementów: "<< sum << '\n';
    
    return 0;
}


#----------------------STD::PARTITION--------------------
reorganizuje elementy w kontenerze tak, że elementy spełniające dany predykat znajdą się przed tymi, które go nie spełniają
segregowanie danych według kryteriów


#include <algorithm>
#include <vector>
#include <iostream>

bool is_odd(int n) { return n % 2 == 1; }

int main() {
    std::vector<int> vec{1,2,3,4,5};
    std::partition(vec.begin(), vec.end(), is_odd);
    for (int n : vec) {
        std::cout << n << ' ';
    }
    
    return 0;
}
