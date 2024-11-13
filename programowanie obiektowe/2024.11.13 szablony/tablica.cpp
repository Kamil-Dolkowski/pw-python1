// Tablica o określonym rozmiarze

#include <iostream>
#include <cstring>

//size_t - nie ma znaków typu, np. '-'

template <class T, size_t n>

class Array {
public:
    Array() {}
    Array(T value) {
        for (size_t i=0; i<n; i++) {
            buffer[i] = value;
        }
    }


    T& operator[](std::size_t idx) {
        // Zmienna statyczna, aby istniała po wyjściu z funkcji.
        static T fallback = 0;
        return (idx >= n) ? fallback : buffer[idx]; 
        // return buffer[idx]; 
    };
    const T& operator[](std::size_t idx) const { 
        // Zmienna statyczna, aby istniała po wyjściu z funkcji.
        static T fallback = 0;
        return (idx >= n) ? fallback : buffer[idx]; 
        // return buffer[idx]; 
    };

private:
    T buffer[n];
};





int main() {
    Array<int, 2> arr(123);
    std::cout << arr[100000] << std::endl;

    std::cout << "Zmiana wartości:" << std::endl;
    std::cout << arr[0] << std::endl;
    arr[0] = 321;
    std::cout << arr[0] << std::endl;

    return 0;
}