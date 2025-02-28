// Napisz funkcję, która zwróci element, który najczęściej się powtarza wraz z liczbą jego wystąpień.

#include <iostream>
#include <vector>
#include <map>

template <typename T>
std::pair<T, unsigned int> 
findMostOccurrences(const std::vector<T> &v) {
    if (v.empty()) {
        throw std::length_error("Vector is empty");
    }

    // Implementacja klasy std::map zapewnia inicjalizację wartości, które nie istnieją w przypadku odwołania przez [].
    std::map<T, size_t> map;
    
    for (const auto &value : v) {
        map[value] += 1;
    }

    std::pair<T, unsigned int> result;
    result.second = 0;

    //for (const std::pair<T, size_t> &value : map) {
    for (const auto &value : map) {
        if (value.second > result.second) {
            result.first = value.first;
            result.second = value.second;
        }
        //std::cout << value.first << " " << value.second << std::endl;
    }

    return result;
}


int main() {
    std::vector<int> numbers = {4,2,3,4,5,6,3,7,3,1,3,5,7,5,3,1,0,9,8,9,0,0,0,9,8,7};

    std::pair<int, unsigned int> result = findMostOccurrences<int>(numbers);
    std::cout << "Najczęściej występuje: " << result.first << std::endl;
    std::cout << "Występuje: " << result.second << " razy" << std::endl;

    return 0;
}