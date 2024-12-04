#include <iostream>

template <typename T>
class SharedPtr {
private:
    int *refCounter;
    T *ptr;
public:
    SharedPtr(T* ptr) {
        this->ptr = ptr;
        this->refCounter = new int;
        *this->refCounter = 1;
    }
    SharedPtr(const SharedPtr& source) {
        std::cout << "Kopiowanie" << std::endl;
        this->refCounter = source.refCounter;
        this->ptr = source.ptr;
        (*this->refCounter)++;
    }
    ~SharedPtr() {
        (*this->refCounter)--;
        if (*this->refCounter == 0) {
            std::cout << "Zwalnianie pamięci" << std::endl;
            delete ptr;
            delete refCounter;
        }
    }
};


int main() {
    SharedPtr<int> jakisInt(new int);
    SharedPtr<int> kopia(jakisInt);
    SharedPtr<int> kopia1(jakisInt);
    SharedPtr<int> kopia2(jakisInt);

    return 0;
}