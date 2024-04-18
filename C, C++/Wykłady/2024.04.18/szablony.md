# Szablony

#-------------------------------------------------------------------------------------------------------------------

szablony - pozwalają na pisanie funkcji i klas w sposób ogólny, by mogły pracować z różnymi typami danych
utrzymanie czystości i klarowności kodu

#-------------------------------------------------------------------------------------------------------------------

# Szablony funkcji

template <typename T>
T max(T a, T b) {
    return (a > b) ? a : b;
}

int main() {
    std::cout << max<int>(1, 2) << std::endl;           // Użycie z typem int
    std::cout << max<double>(3.5, 2.5) << std::endl;    // Użycie z typem double
    std::cout << max<char>('a', 'b') << std::endl;      // Użycie z typem char
    return 0;
}

#-------------------------------------------------------------------------------------------------------------------

# Szablony klas

template <typename T>
class Box {
private:
    T content;
public:
    void set(T newContent) {
        content = newContent;
    }

    T get() const {
        return content;
    }
};

int main() {
    Box<int> intBox;
    intBox.set(123);
    std::cout << intBox.get() << std::endl; // Wypisuje 123

    Box<std::string> stringBox;
    stringBox.set("Test");
    std::cout << stringBox.get() << std::endl; // Wypisuje "Test"
    return 0;
}

#-------------------------------------------------------------------------------------------------------------------

# Kluczowe informacje o szablonach

Dedukcja typów: kompilator jest w stanie wydedukować typ argumentów szablonu na podst. kontekstu wywołania (pominięcie jawnej specyfikacji typu)
Specjalizacja: można zdefiniować specjalizacje szablonów dla konkretnych typów danych, które zachowują się inaczej niż ogólny szablon
Szablony a efektywność: szablony mogą zwiększyć rozmiar kodu wynikowego (każdy typ danych generuje odrębną instancję funkcji/klasy, jednakże kompilatory są zoptymalizowane i minimalizują ten efekt)

#-------------------------------------------------------------------------------------------------------------------
