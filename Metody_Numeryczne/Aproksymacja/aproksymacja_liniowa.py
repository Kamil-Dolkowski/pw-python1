import pandas as pd
import matplotlib.pyplot as plt

def calc_a1(df):
    n = len(df)
    x = df['x']
    y = df['y']
    a1 = (n * sum(x * y) - sum(x) * sum(y)) / (n * sum(x**2) - (sum(x))**2)
    return a1

def calc_a0(df):
    n = len(df)
    x = df['x']
    y = df['y']
    a0 = (sum(x**2) * sum(y) - sum(x * y) * sum(x)) / (n * sum(x**2) - (sum(x))**2)
    return a0

def main():
    print("===== APROKSYMACJA LINIOWA =====")

    print("\nFORMAT PLIKU: (.csv/.txt)")
    print("x;y")
    print("<int/float>;<int/float>")

    file = input("\nPodaj nazwę pliku z danymi: ")

    try:
        df = pd.read_csv(file, delimiter=';')
    except FileNotFoundError:
        print("\nBłąd: Nie znaleziono pliku o takiej nazwie.")
        return

    # print("\nDane z pliku:")
    # print(df)

    print("\n==== ROZWIĄZANIE ====")

    a1 = calc_a1(df)
    print(f"\na1 = {a1}")

    a0 = calc_a0(df)
    print(f"a0 = {a0}")

    print("\nWzór funkcji aproksymującej:")
    print(f"y = {a1} * x + {a0}")

    Y = df['x'].apply(lambda x : a1 * x + a0)
    
    plt.plot(df['x'], Y, '-', label="Y")
    plt.plot(df['x'], df['y'], 'o', label="w")
    plt.legend(loc='best')
    plt.show()

if __name__ == "__main__":
    main()
    print("\nZakończono program")