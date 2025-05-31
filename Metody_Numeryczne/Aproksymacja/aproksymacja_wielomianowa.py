import pandas as pd
import sympy as sp
import matplotlib.pyplot as plt

# Wyznacznik macierzy (wersja rekurencyjna)
def det(A):
    n = len(A)

    if n == 1:
        return A[0][0]
    
    else:
        det_result = 0

        for i in range(n):
            # A_ij <- macierz A ze skreślonym i-tym wierszem i j-tą kolumną
            # dla uproszczenia: j = 0
            A_ij = [row[1:] for i_, row in enumerate(A) if i_ != i] # wiersze oprócz wiersza i oraz kolumny oprócz j=0 (row[1:])

            det_result += (-1)**i * A[i][0] * det(A_ij)

    return det_result

# Obliczanie współczynników funkcji
def calc_a(df, m): # df - zbiór danych, m - stopień wielomianu
    # Inicjalizacje macierzy o odpowiednich rozmiarach
    xsum = [0 for _ in range(2*m +1)]
    A = [[0]*(m+1) for _ in range(m+1)]
    b = [0 for _ in range(m+1)]

    for i in range(2*m +1):
        xsum[i] = sum(df['x']**i)

    for i in range(m+1):
        for j in range(m+1):
            A[i][j] = xsum[i+j]

        b[i] = sum(df['x']**i * df['y'])

    # A * a = b
    # Wyznaczenie macierzy odwrotnej do macierzy A
    A_1 = [[0]*(m+1) for _ in range(m+1)]

    detA = det(A)

    for i in range(m+1):
        for j in range(m+1):
            T = [row[:j] + row[j+1:] for i_, row in enumerate(A) if i_ != i] # macierz A bez wiersza i oraz bez kolumny j

            A_1[i][j] = ((-1)**(i+j) * det(T)) / detA

    # A_1 * b = a
    # Wyznaczenie macierzy współczynników funkcji
    a = [0 for _ in range(m+1)]

    for i in range(m+1):
        for j in range(m+1):
            a[i] += A_1[i][j] * b[j]

    a.reverse()

    return a

def main():
    print("===== APROKSYMACJA WIELOMIANOWA =====")

    print("\nFORMAT PLIKU: (.csv/.txt)")
    print("x;y")
    print("<int/float>;<int/float>")

    file = input("\nPodaj nazwę pliku z danymi: ")

    try:
        df = pd.read_csv(file, delimiter=';', dtype={'x': float, 'y': float})
    except FileNotFoundError:
        print("\nBłąd: Nie znaleziono pliku o takiej nazwie.")
        return
    except ValueError:
        # Konwersja zapisanej w pliku liczby float z przecinkiem na kropkę
        try:
            df = pd.read_csv(file, delimiter=';', dtype={'x': float, 'y': float}, decimal=",")
        except:
            print("\nBlad: Niepoprawna zawartość pliku.")
            return

    # print("\nDane z pliku:")
    # print(df)

    plt.plot(df['x'], df['y'], 'o', label="w")
    plt.legend(loc='best')
    plt.show()

    try:
        m = int(input("\nPodaj stopień wielomianu aproksymacji: "))
        if (m <= 0):
            raise ValueError("Value < 0")
    except ValueError:
        print("\nBłąd: Błędna wartość")
        return

    print("\n==== ROZWIĄZANIE ====")

    a = calc_a(df, m)

    print("\nWzór funkcji aproksymującej:")
    formula = "y = "
    for i in range(len(a)):
        if i != 0:
            if a[i] >= 0:
                formula += " + "
            else:
                formula += " - "

        formula += f"{abs(a[i])}"

        if i != len(a)-1:
            formula += f" * x^{len(a)-1-i}" 

    print(formula)

    formula_cleaned = formula.replace("^", "**") # zamiana "^" na "**" (potęgowanie w pythonie)
    formula_cleaned = formula_cleaned[4:] # usunięcie "y = " z początku

    x = sp.symbols('x')
    expr = sp.sympify(formula_cleaned)
    F = sp.lambdify(x, expr)

    Y = df['x'].apply(lambda x: F(x))
    
    plt.plot(df['x'], Y, '-', label="Y")
    plt.plot(df['x'], df['y'], 'o', label="w")
    plt.legend(loc='best')
    plt.show()

if __name__ == "__main__":
    main()
    print("\nZakończono program")