
# Łączenie kodu napisanego w C i C++

#-------------------------------------------------------------------------------------------------------------------

# Użycie extern "C" w C++

kompilator traktuje zawarte w niej deklaracje jako C

extern "C" {
    void funkcja_z_C();
}

extern "C" {
    void funkcja1_z_C();
    void funkcja2_z_C();
}

#---------------------------------

#ifdef __cplusplus
extern "C" {
#endif

void funkcja1_z_C();
void funkcja2_z_C();

#ifdef __cplusplus
}
#endif

#-------------------------------------------------------------------------------------------------------------------

# Linkowanie
upewnij się, że pliki C są kompilowane przez kompilator C, a pliki C++ przez kompilator C++
następnie linkuj wszystkie obiekty ...

#-------------------------------------------------------------------------------------------------------------------

# Różnice w traktowaniu zmiennych i konwencjach
-konwencje nazewnictwa
-zmienne globalne (zmienne globalne w C wymagaja użycia extern "C")
-zarządzanie pamięcią


#-------------------------------------------------------------------------------------------------------------------
