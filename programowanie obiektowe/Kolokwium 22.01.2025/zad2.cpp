// Kamil Dółkowski 334531
#include <iostream>
#include <vector>
#include <algorithm>

template<typename T>
class Sorter {
public:
    virtual std::vector<T> sort(bool descending) = 0;
    ~Sorter() {}
protected:
    Sorter(const std::vector<T>& _v) {
        for (const auto &value : _v) {
            v.push_back(value);
        }
    };

    std::vector<T> v;
};

// O(n)
template<typename T>
class BubbleSort : Sorter<T> {
public:
    BubbleSort(const std::vector<T>& _v) : Sorter<T>(_v) {
        for (const auto &value : _v) {
            v.push_back(value);
        }
    }

    virtual std::vector<T> sort(bool descending) override {
        T temp;

        for (int i=0; i < v.size(); i++) {
            for (int j=0; j < v.size() - 1; j++) {
                if (v[j] > v[j+1]) {
                    temp = v[j+1];
                    v[j+1] = v[j];
                    v[j] = temp;
                }
            }
        }

        if (descending == true) {
            std::reverse(v.begin(), v.end());
        } 
        
        return v;
    };

private:
    std::vector<T> v;

};

template<typename T>
void printVector(const std::vector<T> &v) {
    std::cout << "v = {" ;

    for (int i=0; i < v.size(); i++) {
        std::cout << v[i];
        if (i < v.size() - 1) std::cout << ", ";
    }

    std::cout << "}" << std::endl;
}




int main() {
    std::vector<double> v{5.2, -5.1, 6, 10.001, 1111};
    auto s = BubbleSort(v);

    printVector(v);
    std::cout << std::endl;

    v = s.sort(true);
    std::cout << "sort(true):" << std::endl;
    printVector(v);

    std::cout << std::endl;

    v = s.sort(false);
    std::cout << "sort(false):" << std::endl;
    printVector(v);

    return 0;
}