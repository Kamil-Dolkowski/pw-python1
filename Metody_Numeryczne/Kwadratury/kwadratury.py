import sympy as sp
import matplotlib.pyplot as plt
import numpy as np

MAX_DEPTH = 5_000

# Metody całkowania
def left_rectangles_method(F, a, b, E):
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

def middle_rectangles_method(F, a, b, E):
    n = 1
    last_sum = 0

    while (n < MAX_DEPTH):
        current_sum = 0
        dx = (b-a)/n

        for i in range(n):
            current_sum += F(a + dx*i + 0.5*dx)

        current_sum *= dx

        # print(f"{n}: {current_sum}")

        if n>1 and abs(last_sum - current_sum) <= E:
            break
        else:
            last_sum = current_sum
            n += 1

    return current_sum, n

def right_rectangles_method(F, a, b, E):
    n = 1
    last_sum = 0

    while (n < MAX_DEPTH):
        current_sum = 0
        dx = (b-a)/n

        for i in range(1, n+1):
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

# Wyświetlenie wyników i wykresów dla poszczególnych metod
def print_result_rectangles_method(F, a, b, E, is_figure = True):
    fig = plt.figure()
    fig.suptitle("Metoda prostokątów")

    axs = [
        plt.subplot2grid((2, 4), (0, 0), colspan=2), 
        plt.subplot2grid((2, 4), (0, 2), colspan=2),
        plt.subplot2grid((2, 4), (1, 1), colspan=2)
    ]

    # Prostokąty lewe
    result, n = left_rectangles_method(F, a, b, E)
    print_result_info("prostokąty (lewe)", result, n)
    
    dx = (b-a)/n
    x_rect = np.linspace(a, b-dx, n)
    y_rect = F(x_rect)

    x = np.linspace(a, b, 1000)
    axs[0].plot(x, F(x))
    axs[0].bar(x_rect, y_rect, width=dx, align="edge", alpha=0.5, color="orange", edgecolor="orange", linewidth=1)
    axs[0].set_title("Prostokąty lewe")
    axs[0].set_xlabel("x")
    axs[0].set_ylabel("y")

    # Prostokąty prawe
    result, n = right_rectangles_method(F, a, b, E)
    print_result_info("prostokąty (prawe)", result, n)

    dx = (b-a)/n
    x_rect = np.linspace(a, b-dx, n)
    y_rect = F(x_rect + dx)

    x = np.linspace(a, b, 1000)
    axs[1].plot(x, F(x))
    axs[1].bar(x_rect, y_rect, width=dx, align="edge", alpha=0.5, color="orange", edgecolor="orange", linewidth=1)
    axs[1].set_title("Prostokąty prawe")
    axs[1].set_xlabel("x")
    axs[1].set_ylabel("y")

    # Prostokąty środkowe
    result, n = middle_rectangles_method(F, a, b, E)
    print_result_info("prostokąty (środkowe)", result, n)

    dx = (b-a)/n
    x_rect = np.linspace(a, b-dx, n)
    y_rect = F(x_rect + 0.5*dx)

    x = np.linspace(a, b, 1000)
    axs[2].plot(x, F(x))
    axs[2].bar(x_rect, y_rect, width=dx, align="edge", alpha=0.5, color="orange", edgecolor="orange", linewidth=1)
    axs[2].set_title("Prostokąty środkowe")
    axs[2].set_xlabel("x")
    axs[2].set_ylabel("y")

    if is_figure == True:
        plt.tight_layout()
        plt.show()

def print_result_trapeziums_method(F, a, b, E, is_figure = True):
    result, n = trapeziums_method(F, a, b, E)
    print_result_info("trapezy", result, n)

    x_trap = np.linspace(a, b, n+1)
    y_trap = F(x_trap)

    for i in range(n):
        plt.fill_between([x_trap[i], x_trap[i+1]], [y_trap[i], y_trap[i+1]], alpha=0.5, color="orange")

    x = np.linspace(a, b, 1000)
    plt.plot(x, F(x))
    plt.title("Metoda trapezów")
    plt.xlabel("x")
    plt.ylabel("y")

    if is_figure == True:
        plt.show()

def print_result_simpson_method(F, a, b, E, is_figure = True):
    result, n = simpson_method(F, a, b, E)
    print_result_info("parabole (metoda Simpsona)", result, n)

    x_trap = np.linspace(a, b, n+1)
    y_trap = F(x_trap)

    for j in range(n//2):
        i = 2*j

        # Interpolacja wielomianowa Lagrange'a drugiego stopnia
        x = sp.symbols('x')
        lagrange_formula = y_trap[i] * ((x - x_trap[i+1]) * (x - x_trap[i+2])) / ((x_trap[i] - x_trap[i+1]) * (x_trap[i] - x_trap[i+2]))
        lagrange_formula += y_trap[i+1] * ((x - x_trap[i]) * (x - x_trap[i+2])) / ((x_trap[i+1] - x_trap[i]) * (x_trap[i+1] - x_trap[i+2]))
        lagrange_formula += y_trap[i+2] * ((x - x_trap[i]) * (x - x_trap[i+1])) / ((x_trap[i+2] - x_trap[i]) * (x_trap[i+2] - x_trap[i+1]))

        F_lagrange = sp.lambdify(x, lagrange_formula)

        x_segment = np.linspace(x_trap[i], x_trap[i+2], 1000)
        y_segment = [F_lagrange(x) for x in x_segment]

        plt.fill_between(x_segment, y_segment, alpha=0.5, color="orange")

    x_values = np.linspace(a, b, 1000)
    plt.plot(x_values, F(x_values))
    plt.title("Metoda Simpsona (parabol)")
    plt.xlabel("x")
    plt.ylabel("y")

    if is_figure == True:
        plt.show()


def print_result_info(method_type, result, n):
    print("\n======== ROZWIĄZANIE ========")
    print(f"Metoda: {method_type}")
    print(f"Wynik: {result}")
    if method_type == "parabole (metoda Simpsona)":
        if n < MAX_DEPTH:
            print(f"Ilość podziałów (k=0.5*n): {int(0.5*n)}")
        else:
            print(f"Ilość podziałów (k=0.5*n): {int(0.5*n)} [osiągnięto maksymalną wartość podziałów!]")
    elif n < MAX_DEPTH:
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
    
    choice = input("\nCzy chcesz wykresy? [t/n]: ")
    if choice in ["T", "t"]:
        is_figure = True
    else:
        is_figure = False

    print("\nPodaj metodę (p/t/s/w):")
    print("p - prostokąty")
    print("t - trapezy")
    print("s - parabole (metoda Simpsona)")
    print("w - wszystkie metody (porównanie metod)")
    method = input("Wybór: ")

    if method == "p":
        print_result_rectangles_method(F, a, b, E, is_figure)

    elif method == "t":
        print_result_trapeziums_method(F, a, b, E, is_figure)

    elif method == "s":
        print_result_simpson_method(F, a, b, E, is_figure)
        
    elif method == "w":
        print_result_rectangles_method(F, a, b, E, is_figure)

        print_result_trapeziums_method(F, a, b, E, is_figure)

        print_result_simpson_method(F, a, b, E, is_figure)
    else:
        print("\nBłąd: Niepoprawna wartość.")
        return
    

if __name__ == "__main__":
    main()
    print("\nZakończono program")