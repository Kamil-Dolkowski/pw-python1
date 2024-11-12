#include <iostream>
#include <cstring>

class Array {
public:
    Array(unsigned int _length) : length(_length) {
        table = new int [length]; 
        for (int i=0; i<length; i++) {
            table[i] = 0;
        }
    }
    ~Array(){
        delete table;
    }
    Array(const Array &source) {
        length = source.length;
        table = new int [length];
        for (int i=0; i<length; i++) {
            table[i] = source.table[i];
        }
    }

    void addIndex(int index, int value) {
        table[index] = value;
    }
    void print() const {
        std::cout << "[";
        for (int i=0; i<length; i++) {
            std::cout << table[i] ;
            if (i < length- 1) std::cout << ", ";
        }
        std::cout << "]";
    }

   

    int operator[](unsigned int value) {
        if (value < length) {
            return table[value];
        }
        return 0;
    }



    friend std::ostream& operator<<(std::ostream &os, const Array &a);

private:
    int *table;
    unsigned int length;
};

std::ostream& operator<<(std::ostream &os, const Array &a) {
    os << "[";
    for (int i=0; i<a.length; i++) {
        os << a.table[i] ;
        if (i < a.length- 1) os << ", ";
    }
    os << "]";
    return os;
}




int main() {
    Array arrayA(5);
    Array arrayB(arrayA);
    // array.print();


    std::cout << "A: " << arrayA << std::endl;
    std::cout << "B: " << arrayB << std::endl;
    arrayA.addIndex(3, 2);
    std::cout << "A: " << arrayA << std::endl;
    std::cout << "B: " << arrayB << std::endl;
    std::cout << arrayA[3];



    return 0;
}