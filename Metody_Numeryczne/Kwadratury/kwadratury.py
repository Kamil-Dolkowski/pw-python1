import sympy as sp

MAX_DEPTH = 5_000

def rectangles_method(F, a, b, E):
    n = 1
    last_sum = 0

    while (n < MAX_DEPTH):
        current_sum = 0
        dx = (b-a)/n

        for i in range(n):
            current_sum += F(a + dx*i)

        current_sum *= dx

        # print(f"{n}: {current_sum}")

        if n>1 and abs(last_sum - current_sum) <= E:
            break
        else:
            last_sum = current_sum
            n += 1

    return current_sum, n

def trapeziums_method(F, a, b, E):
    n = 1
    last_sum = 0

    while (n < MAX_DEPTH):
        current_sum = 0
        dx = (b-a)/n

        for i in range(n):
            current_sum += F(a + dx*i) + F(a + dx*(i+1))

        current_sum *= 0.5 * dx

        # print(f"{n}: {current_sum}")

        if n>1 and abs(last_sum - current_sum) <= E:
            break
        else:
            last_sum = current_sum
            n += 1

    return current_sum, n

def simpson_method(F, a, b, E):
    # n = 2k  # n musi być parzyste
    n = 2
    last_sum = 0

    while (n < MAX_DEPTH):
        dx = (b-a)/n
        current_sum = F(a) + F(b)

        for i in range(n//2):
            current_sum += 4 * F(a + dx * (2*i+1))
            if i != n//2 - 1:
                current_sum += 2 * F(a + dx * 2 * (i+1))

        current_sum *= dx/3

        # print(f"{n}: {current_sum}")

        if n>1 and abs(last_sum - current_sum) <= E:
            break
        else:
            last_sum = current_sum
            n += 2

    return current_sum, n

def print_result_info(method_type, result, n):
    print("\n======== ROZWIĄZANIE ========")
    print(f"Metoda: {method_type}")
    print(f"Wynik: {result}")
    if n < MAX_DEPTH:
        print(f"Ilość podziałów (n): {n}")
    else:
        print(f"Ilość podziałów (n): {n} [osiągnięto maksymalną wartość podziałów!]")


def main():
    print("===== KWADRATURY =====")

    x = sp.symbols('x')
    # F_input = "-1*x**2 + 6*x + 1"
    F_input = input("\nPodaj funkcję: ").replace("^", "**")
    if F_input == "":
        print("\nBłąd: Nie wprowadzono żadnej funkcji")
        return
    
    try:
        F = sp.lambdify(x, F_input, "numpy")
        F(0) # Sprawdzenie poprawności konwersji [(x-1)(x+2) <- źle] [(x-1)*(x+2) <- dobrze]
    except:
        print("\nBłąd: Niepoprawny format funkcji")
        return

    print("\nPodaj zakres:")
    try:
        a = float(input("a = "))
        b = float(input("b = "))
        if a > b:
            print("\nBłąd: 'a' nie może być większe od 'b'")
            return
    except:
        print("\nBłąd: 'a' i 'b' muszą być liczbą")
        return

    print("\nPodaj dokładność:")
    try:
        E = float(input("E = "))
    except:
        print("\nBłąd: 'E' musi być liczbą")
        return
    
    if E < 0:
        print("\nBłąd: 'E' nie może być mniejsze od 0")
        return

    print("\nPodaj metodę (p/t):")
    print("p - prostokąty")
    print("t - trapezy")
    print("s - parabole (metoda Simpsona)")
    print("w - wszystkie metody (porównanie metod)")
    method = input("Wybór: ")

    if method == "p":
        result, n = rectangles_method(F, a, b, E)
        print_result_info("prostokąty", result, n)

    elif method == "t":
        result, n = trapeziums_method(F, a, b, E)
        print_result_info("trapezy", result, n)

    elif method == "s":
        result, n = simpson_method(F, a, b, E)
        print_result_info("parabole (metoda Simpsona)", result, n)
        
    elif method == "w":
        result, n = rectangles_method(F, a, b, E)
        print_result_info("prostokąty", result, n)

        result, n = trapeziums_method(F, a, b, E)
        print_result_info("trapezy", result, n)

        result, n = simpson_method(F, a, b, E)
        print_result_info("parabole (metoda Simpsona)", result, n)
    else:
        print("\nBłąd: Niepoprawna wartość.")
        return
    

if __name__ == "__main__":
    main()
    print("\nZakończono program")