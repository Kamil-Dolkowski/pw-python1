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
    virtual void normalize() override {
        if (typeid(T).name() == typeid(int).name()) throw std::invalid_argument("Vector with 'int' type can't be normalized.");
        
        double vlength = length();

        if (vlength == 0) throw std::invalid_argument("Vector length = 0.");

        x = x/vlength;
        y = y/vlength;
    }

    T getX() const { return x; }
    T getY() const { return y; }

protected:
    T x;
    T y;
};

template<typename T>
class Vector3D : public Vector2D<T> {
public:
    Vector3D(T _x, T _y, T _z) : Vector2D<T>(_x, _y), z(_z) {}
    virtual ~Vector3D() {}
    virtual double length() const override {
         return sqrt( pow(this->x,2) + pow(this->y,2) + pow(z,2) );
    }
    virtual void normalize() override {
        if (typeid(T).name() == typeid(int).name()) throw std::invalid_argument("Vector with 'int' type can't be normalized.");
        
        double vlength = length();
        
        if (vlength == 0) throw std::invalid_argument("Vector length = 0.");

        this->x = this->x/vlength;
        this->y = this->y/vlength;
        z = z/vlength;
    }
    
    template<typename Y>
    friend std::ostream& operator<<(std::ostream &os, const Vector3D<Y> &v);
    
private:
    T z;
};


template<typename T>
std::ostream& operator<<(std::ostream &os, const Vector2D<T> &v) 
{
    os << "(" << v.getX() << "," << v.getY() << ")" ;
    return os;
}

template<typename T>
std::ostream& operator<<(std::ostream &os, const Vector3D<T> &v) {
    os << "(" << v.x << "," << v.y << "," << v.z << ")" ;
    return os;
}


int main() {
    Vector2D<double> v2d(1,20);
    Vector3D<double> v3d(1,2,3);

    try {
        std::cout << "Vector2D: " << v2d << std::endl;
        std::cout << "length: " << v2d.length() << std::endl;
        
        std::cout << "\nnormalize Vector2D\n" << std::endl;
        v2d.normalize();

        std::cout << "Vector2D: " << v2d << std::endl;
        std::cout << "length: " << v2d.length() << std::endl;
        
        std::cout << "=================================\n";
        
        std::cout << "Vector3D: " << v3d << std::endl;
        std::cout << "length: " << v3d.length() << std::endl;
        
        std::cout << "\nnormalize Vector3D\n" << std::endl;
        v3d.normalize();

        std::cout << "Vector3D: " << v3d << std::endl;
        std::cout << "length: " << v3d.length() << std::endl;

    } catch (const std::exception &e) {
        std::cout << "Error: " << e.what() << std::endl;
    }
    
    return 0;
}


// w normalize() - wyjątek
// normalizacja - podzielenie składowych przez długość