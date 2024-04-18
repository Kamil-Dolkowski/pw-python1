# Modyfikatory constexpr i consteval. Wykonywanie kodu w trakcie kompilacji.

#-------------------------------------------------------------------------------------------------------------------

modyfikatory
umożliwiają wykonywanie obliczeń w trakcie kompilacji
znaczne zwiększenie wydajności w czasie wykonywania programu

#-------------------------------------------------------------------------------------------------------------------

# constexpr
zmienna musi mieć wartość stałą, która jest znana w czasie kompilacji
jest ewoulowana w czasie kompilacji

constexpr int factorial(int n) {
    return n <= 1 ? 1 : n * factorial(n - 1);
}

int main() {
    constexpr int val = factorial(5); // Obliczane w czasie kompilacji
    return 0;
}

#-------------------------------------------------------------------------------------------------------------------

# consteval
musi być wyaołana i ewaluowana w czasie kompilacji
nie można jej używać w czasie wykonania

consteval int square(int n) {
    retur n*n;
}

...

#-------------------------------------------------------------------------------------------------------------------

# Podsumowanie:
constexpr - w czasie kompilacji i w czasie wykonania
consteval - wyłącznie w czasie kompilacji

#-------------------------------------------------------------------------------------------------------------------
