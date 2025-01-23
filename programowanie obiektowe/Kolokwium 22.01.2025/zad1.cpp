// Kamil Dółkowski 334531
#include <iostream>

template <typename T>
class Shape {
public:
    virtual T area() const = 0;
};

template <typename T>
class Rectangle : Shape<T> {
public:
    Rectangle(T _x, T _y) {
        if (_x == 0 || _y == 0) throw std::logic_error("Can't initialize Rectangle with area = 0.");

        x = _x;
        y = _y;
    }
    ~Rectangle() {}

    virtual T area() const override {
        return x * y;
    };
    
private:
    T x;
    T y;
};

template <typename T>
class Square : Rectangle<T> {
public:
    Square(T _x) : Rectangle<T>(_x,_x) {
        if (_x == 0) throw std::logic_error("Can't initialize Square with area = 0.");

        x = _x;
    }
    ~Square() {}

    virtual T area() const override {
        return x * x;
    };

private:
    T x;
};




int main() {
    try {
        Rectangle<int> rectangleI(2,3);
        Rectangle<double> rectangleD(2.5,2);
        // Rectangle<int> rectangleZero(0,1);

        Square<int> squareI(3);
        Square<double> squareD(1.5);
        // Square<int> squareZero(0);

        std::cout << "Area rectangleI: " << rectangleI.area() << std::endl;
        std::cout << "Area rectangleD: " << rectangleD.area() << std::endl;

        std::cout << "Area squareI: " << squareI.area() << std::endl;
        std::cout << "Area squareD: " << squareD.area() << std::endl;

        std::cout << std::endl;

        Square<int> squareZero(0);

    } catch (const std::exception &e) {
        std::cerr << "Error: " << e.what() << std::endl;
    }

    return 0;
}