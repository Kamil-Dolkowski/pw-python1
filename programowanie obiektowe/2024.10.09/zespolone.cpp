//https://en.cppreference.com/w/cpp/language/operators

// ========Complex:========     a+bi

// -a
// a + b
// a - b
// a += b
// a -= b
// a (Complex) * b (double)
// std::ostream <<

//-------------------------

//a + b / a - b
//Complex + complex = Complex (new)

//a += b / a -= b
//Complex + Complex = Complex (old)

//=============================================================

#include <iostream>

class Complex {
public:
    Complex(double _re, double _im)
    {
        re = _re;
        im = _im;
    };
    Complex(double _re) 
    {
        re = _re;
        im = 0;
    };
    
    double real() const
    {
        return re;
    };
    double imag() const 
    {
        return im;
    };
    
    Complex operator+(const Complex &c) 
    {
        return Complex(re + c.re, im + c.im);
    };
    Complex operator-(const Complex &c) 
    {
        return Complex(re - c.re, im - c.im);
    };
    
    Complex& operator+=(const Complex &c)
    {
        re = re + c.re;
        im = im + c.im;
        return *this;
    };
    Complex& operator-=(const Complex &c) 
    {
        re = re - c.re;
        im = im - c.im;
        return *this;
    };
    
    Complex operator-() // operator unarny (jednoargumentowy)
    {
        return Complex(-re, -im);
    }; 
    Complex operator*(double x) 
    {
        return Complex(re * x, im);
    };
    
private:
    double re;
    double im;
};

std::ostream& operator<<(std::ostream &os, const Complex &c) 
{
    if (c.imag() < 0) {
        os << c.real() << c.imag() << "i";
    } else {
        os << c.real() << "+" << c.imag() << "i";
    }
    return os;
};



int main()
{
    Complex a(1,2);
    Complex b(2,2);
    Complex c(a+b);
    
    a+=b;
    std::cout << a;

    return 0;
}











