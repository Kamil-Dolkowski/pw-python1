# 21.03.2024

#------------------------------------REFERENCJE-------------------------------------------
Referencje - rodzaj aliasu dla innej zmiennej
nie jest to oddzielny obszar pamięci, po zainicjowaniu nie można jej już przypisać do innej zmiennej, zawsze będzie odnosić się do tej samej lokalizacji pamięci

int x = 10;
int& ref = x;   // ref jest referencją do x


#------------------------------------WSKAŹNIKI---------------------------------------------
Wskaźniki - zmienne, które przechowują adres pamięci innej zmiennej

int x = 10;
int* ptr = &x;   // ptr jest wskaźnikiem na x

#----------------------------------DEREFERENCJA---------------------------------------------
Dereferencja - zmiana referencji lub wskaźnika

#----------------------------------------------------------------------------------------------

zmienna vs adres 
inicjalizacja
null
bezpieczeństwo użycia

#----------------------------------------------------------------------------------------------

Semantyka kopiowania - tworzenie kopii obiektów

Płytkie kopanie - kopiowanie jedynie wartości pól obiektu włączając w to adresy pamięci wskaźników, oryginał  i kopia mogą współdzielić ten sam obszar pamięci
Głębokie kopanie

#-------------------------------------PŁYTKIE KOPANIE------------------------------------------

class ShallowCopy {
public:
    int*    


}

#----------------------------------------------------------------------------------------------






# Struktury i klasy w C++

#----------------------------------PODSTAWY KLAS I STRUKTUR------------------------------------

struct Osoba {
    std::string imie;
    int wiek;
};

class Osoba {
private:
    std::string imei;
    int wiek;
public:
    // Metody...
};

#--------------------------------------METODY W KLASACH------------------------------------------


#----------------PRZYKŁAD-----------------

#include <iostream>
#include <string>

class Samochod {
public:
    void ustawMarke(const std::string& m) { marka = m; }
    std::string pobierzMarke() const { return marka; }
    void ustawRok(int r) { rokProdukcji = r; }
    int pobierzRok() const { return rokProdukcji; }

private:
    std::string marka;
    int rokProdukcji;
};

int main() {
    Samochod mojSamochod;
    mojSamochod.ustawMarke("Toyota");
    mojSamochod.ustawRok(2020);

    std::cout << "Marka: " << mojSamochod.pobierzMarke() << std::endl;
    std::cout <<  "Rok produkcji: " << mojSamochod.pobierzRok() << std::endl;

    return 0;
}

#-----------------------------------KONSTRUKTORY---------------------------------------

class Osoba {
public:
    Osoba(std::string im, int w) : imie(im), wiek(w) {}
private:
    std::string imie:
    int wiek;
};

#------------------------------------

#include <iostream>
#include <string>

class Samochod {
public:
    Samochod() {
        std::cout << "Samochód został stworzony." << std::endl;
    }
};

int main() {
    Samochod mojSamochod;

    return 0;
}

#-----------------------------------------ZADANIE----------------------------------------------

Stwórz klasę LampkaNocna, która przy tworzeniu obiektu wypisze na ekranie "Lampka nocna jest teraz włączona.".

#include <iostream>

class LampkaNocna {
public:
    LampkaNocna() {
        std::cout << "Lampka nocna jest teraz włączona." << std::endl;
    }
};

int main() {
    LampkaNocna lampka;
    
    return 0;
}

#-----------------------------------KONSTRUKTORY Z PARAMETRAMI--------------------------------

#include <iostream>
#include <string>

class Samochod {
public:
    Samochod(std::string marka) {
        std::cout << "Samochod marki " << marka << " został stworzony." << std::endl;
    }
};

int main() {
    Samochod("aaa");
    
    return 0;
}

#-----------------------------------------ZADANIE----------------------------------------------

Utwórz klasę Kubek, która przy tworzeniu obiektu przyjmuje 2 parametry: materiał, z którego jest wykonany (np. ceramika, szkło) i pojemnośc w mililitrach, a następnie wypisze te informacje.

#include <iostream>
#include <string>

class Kubek {
public:
    Kubek(std::string material, int pojemnosc) {
        std::cout << "Kubek z materiału (" << material << ") o pojemności (" << pojemnosc << " ml) został stworzony." << std::endl;
    }
};

int main() {
    Kubek k("ceramika", 250);
    
    return 0;
}

#---------------------------------LISTA INICJACYJNA KONSTRUKTORA--------------------------------

#include <iostream>
#include <string>

class Samochod {
    std::string marka;
    int rokProdukcji;
public:
    Samochod(std::string m, int r) : marka(m), rokProdukcji(r) {
        std::cout << "Samochod marki " << marka << ", rok produkcji: " << rokProdukcji << std::endl;
    }
};

int main() {
    Samochod s("Toyota",2020);
    
    return 0;
}

#------------------------------------------ZADANIE---------------------------------------------

Stwórz klasę Telefon, która będzie przechowywać markę telefonu i jego model. Użyj listy inicjalizacyjnej w konstruktorze do przypiusywania tych wartości.

#include <iostream>
#include <string>

class Telefon {
    std::string marka;
    std::string model;
public:
    Telefon(std::string m, std::string mod) : marka(m), model(mod) {
        std::cout << "Telefon: " << marka << " " << model << "." << std::endl;
    }
};

int main() {
    Telefon t("Samsung", "Galaxy S10");
    return 0;
}

#--------------------------------KONSTRUKTORY DELEGUJĄCE--------------------------------------

#include <iostream>
#include <string>

class Samochod {
    std::string marka;
    int rokProdukcji;
public:
    // Główny konstruktor z listą inicjacyjną
    Samochod(std::string m, int r) : marka(m), rokProdukcji(r) {
        std::cout << "Samochód marki " << marka << ", rok produkcji: " << rokProdukcji << std::endl;
    }
    // Delegujący konstruktor, który używa głównego konstruktora
    Samochod() : Samochod("Nieznana", 0) {
        std::cout << "Tworzenie samochodu o nieznanych parametrach." << std::endl;
    }
};

int main() {
    Samochod samochod1("Toyota", 2020);
    Samochod samochod2();       // ??
    return 0;
}

#-------------------------------------ZADANIE-----------------------------------------------

Stwórz klasę Komputer (producent, model), główny konstruktor (oba parametry), 
konstruktor bezparametrowy deleguje do głównego konstruktora 
wartości domyślne: "Nieznany producent" i "nieznany model"

#include <iostream>
#include <string>

class Komputer {
    std::string producent;
    std::string model;
public:
    // Główny konstruktor z listą inicjacyjną
    Komputer(std::string p, std::string m) : producent(p), model(m) {
        std::cout << "Komputer producenta " << producent << ", model: " << model << std::endl;
    }
    // Delegujący konstruktor, który używa głównego konstruktora
    Komputer() : Komputer("Nieznany producent", "Nieznany model") {
        std::cout << "Tworzenie komputera o nieznanych parametrach." << std::endl;
    }
};

int main() {
    Komputer komp1("INTEL", "x64");
    Komputer komp2();
    return 0;
}

#-----------------------------------KONSTRUKTOR KOPIUJĄCY-------------------------------------

#include <iostream>
#include <string>

class Ksiazka {
    std::string tytul;
    int rokWydania;
public:
    // Konstruktor kopiujący
    Ksiazka(const Ksiazka& k) : tytul(k.tytul), rokWydania(k.rokWydania) {
        std:: cout << "Kopiowanie książki: " << tytul << ", rok wydania: " << rokWydania << std::endl;
    }
    // Konstruktor z parametrami
    Ksiazka(std::string t, int r) : tytul(t), rokWydania(r) {}
};

int main() {
    Ksiazka ksiazka1("Pan Tadeusz", 1856);
    Ksiazka ksiazka2(ksiazka1);
    return 0;
}

#----------------------------------------ZADANIE---------------------------------------------

Zaimplementuj klasę AlbumMuzyczny, zawierającą pola dla nazwy artysty i tytułu albumu. 
Zdefiniuj konstruktor kopiujący, który pozwoli na utworzenie kopii istniejącego albumu,

#include <iostream>
#include <string>

class AlbumMuzyczny {
    std::string artysta;
    std::string tytulAlbumu;
public:
    // Konstruktor kopiujący
    AlbumMuzyczny(const AlbumMuzyczny& a) : artysta(a.artysta), tytulAlbumu(a.tytulAlbumu) {
        std:: cout << "Kopiowanie albumu artysty: " << artysta << ", nazwa albumu: " << tytulAlbumu << std::endl;
    }
    // Konstruktor z parametrami
    AlbumMuzyczny(std::string a, std::string t) : artysta(a), tytulAlbumu(t) {}
};

int main() {
    AlbumMuzyczny oryginalny("Mozart", "Symfonie");
    AlbumMuzyczny kopia(oryginalny);
    return 0;
}

#--------------------------------------METODY STAŁE------------------------------------------

class Licznik {
public:
    Licznik() : wartosc(0) {}

    void zwieksz() {
        ++wartosc;
    }

    int pobierzWartosc() const {
        return wartosc;
    }
private:
    int wartosc;
};

#-----------------------------------------ZADANIE----------------------------------------------

Klasa Osoba, która przechowuje imie (string) i wiek (int) , ....

#include <iostream>
#include <string>

class Osoba {
public:
    Osoba(std::string imie, int wiek) : imie(imie), wiek(wiek) {}
    
    std::string pobierzImie() const {
        return imie;
    }
    
    int pobierzWiek() const {
        return wiek;
    }
    
private:
    std::string imie;
    int wiek;
};

int main() {
    Osoba osoba("Jan", 30);
    std::cout << "Imie: " << osoba.pobierzImie() << ", wiek: " << osoba.pobierzWiek() <<std::endl;
    return 0;
}

#----------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------


#----------------------------------------------------------------------------------------------