# Wyjątki

wyjątek - zdarzenie, które wystepuje podczas wykonania programu i zakłóca normalny przepływ instrukcji

Zalety:
-zwiekszenie czytelności kodu, ułatwienie obsługi błędów, separacja logiki programu od logiki obsługi błędów

#-------------------------------------------------------------------------------------------------------------------

# Rzucanie wyjątków (throw):
np. throw std::runtime_error("Błąd!");

Przechwytywanie wyjątków (try i catch):

Blok finally (catch(...)): 

Specyfikacja wyjątków (throw()): 

#-------------------------------------------------------------------------------------------------------------------

# Przechwytywanie wyjątków (try i catch):

#include <iostream>
#include <stdexcept> // Do obsługi standardowych wyjątków

int main() {
    try {
        // Symulacja błędu - rzucamy wyjątek
        throw std::runtime_error("Wystąpił błąd!");
    } catch (const std::runtime_error& e) {
        // Przechwytujemy wyjątek i wyświetlamy jego wiadomość
        std::cout << "Wyjątek: " << e.what() << std::endl;
    }

    return 0;
}

#-------------------------------------------------------------------------------------------------------------------

# Przechwytywanie dowolnego wyjątku

try {
    // kod, który może rzucić dowolny wyjątek
} catch (const std::exception& e) {
    // Obsługa wyjątków standardowych
    std::cout << "Wyjątek standardowy: " << e.what() << std::endl;
} catch (...) {
    // Obsłuag dowolnych wyjątków
    std::cout << "Nieznany wyjątek przechwycony" << std::endl;
}

#-------------------------------------------------------------------------------------------------------------------

# Best practise:
-zasoby i wyjątki (RAII) - smart pointers do automatycznego zwalniania zasobów
-standardowe wyjątki
-własne klasy wyjątków

#-------------------------------------------------------------------------------------------------------------------

# Hierarchia wyjątków:
-std::exception <- klasa bazowa (zawiera wirtualną funkcję what())
-std::logic_error (std::invalid_argument, std::domain_error, std::length_error, std_out_of_range)
-std::runtime_error (std::range_error, std::overflow_error, std::underflow_error)
-std::bad_alloc - alokacja pamięci
-std::bad_cast
-std::bad_typeid

#-------------------------------------------------------------------------------------------------------------------

# Kiedy używać?:
std::logic_error -> błedy w logice programu
std::runtime_error -> niełatwe do przewidzenia i uniknięcia
std::bad_alloc -> problemy z alokacją pamięci
std::bad_cast std::bad_typeid -> specyficzne typy

#-------------------------------------------------------------------------------------------------------------------

# Przykład użycia RAII:

class Resource {
public:
    Resource() { std::cout << "Zasób alokowany\n"; }
    ~Resource() { std::cout << "Zasób zwalniany\n"; }
};

int main() {
    try {
        Resource r;
        throw std::runtime_error("Błąd");
    } catch (...) {
        std::cout <<  "Wyjątek przechwycony\n";
    }
    // Zasób zostanie zwolniony tutaj, niezależnie od wyjątku
    return 0;
}

#-------------------------------------------------------------------------------------------------------------------

# Użycie własnych klas wyjątków

#include <iostream>
#include <exception>

// Definicja własnej kalsy wyjątku
class MyException : public std::exception {
public:
    MyException(const char* message) : msg_(message) {}

    const char* what() const noexcept override {
        return msg_;
    }

private:
    const char* msg_;
};


int main() {
    try {
        // Rzucamy nasz własny wyjątek
        throw MyException("Wystąpił mój wyjątek!");
    } catch (const MyException& e) {
        // Przechwytujemy i obsługujemy nasz własny wyjątek
        std::cout << "Mój wyjątek mówi: " << e.what() << std::endl;
    }

    return 0;
}

#-------------------------------------------------------------------------------------------------------------------

# Obsługa różnych typów wyjątków:

#include <iostream>
#include <stdexcept>
#include <vector>

int main() {
    try {
        std::vector<int> vec;
        // Symualcja błędu - dostęp do nieistniejącego elementu
        std::cout << vec.at(10);
    } catch (const std::out_of_range& e) {
        // Specyficzna obsługa wyjątku związana z zakresem
        std::cout << "Wyjątek zakresu: " << e.what() << std::endl;
    } catch (const std::exception& e) {
        // Ogólna obsługa innych wyjątków
        std::cout << "Wyjątek standardowy: " << e.what() << std::endl;
    }

    return 0;
}

#-------------------------------------------------------------------------------------------------------------------
