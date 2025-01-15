#include <iostream>
#include <math.h>

template<typename T>
class Vector {
public:
    virtual ~Vector() {}

    virtual double length() const = 0;
    virtual void normalize() = 0;
protected:
    Vector() {}
};

template<typename T>
class Vector2D : public Vector<T> {
public:
    Vector2D(T _x, T _y) : x(_x), y(_y) {}
    virtual ~Vector2D() {}

    virtual double length() const override {
        return sqrt( pow(x,2) + pow(y,2) );
    }
    virtual void normalize() override {}

    T getX() { return x; }
    T getY() { return y; }
private:
    T x;
    T y;
};

// template<typename T>
// class Vector3D : private Vector2D<T> {
// public:
//     Vector3D() {}
//     virtual ~Vector3D() {}
//     virtual double length() const override {
//          return sqrt( pow(x,2) + pow(y,2) + pow(z,2) );
//     }
//     virtual void normalize() override {}
// private:
//     T z;
// };


template<typename T>
std::ostream& operator<<(std::ostream &os, const Vector2D<T> &v) 
{
    os << "(" << v.getX() << "," << v.getY() << ")" << std::endl;
    return os;
}




int main() {
    Vector2D<int> v2d(4,3);
    std::cout << v2d.length() << std::endl;
    std::cout << v2d << std::endl;

    return 0;
}


// w normalize() - wyjątek
// normalizacja - podzielenie składowych przez długość