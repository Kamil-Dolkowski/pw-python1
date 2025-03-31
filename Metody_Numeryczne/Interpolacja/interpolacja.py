import pandas as pd
from sympy import symbols, expand, sympify
import matplotlib.pyplot as plt

# Wyznaczenie tablicy ilorazów różnicowych
def ilorazy_roznicowe(df_nodes):
    n = len(df_nodes)
    a = df_nodes['y'].tolist()
    for i in range(0,n):
        for j in range(n-1,i,-1):
            a[j] = (a[j] - a[j-1]) / (df_nodes['x'][j] - df_nodes['x'][j-1-i])
    return a

# Funkcja interpolacyjna (wzór interpolacyjny Newtona)
def interpolacja(x, df_nodes, a):
    y = a[0]
    length = len(a)
    for i in range(1,length):
        element = a[i]
        for j in range(0,i):
            element *= (x - df_nodes['x'][j])
        y += element
    return y

def interpolacja_postac_ogolna(x, F):
    x_symbol = symbols('x')
    return F.subs(x_symbol, x)

# Wzory
def interpolacja_wzor_postac_ogolna(df_nodes, a):
    x = symbols('x')
    F_str = interpolacja_wzor(df_nodes, a)
    F = sympify(F_str)
    expanded_F = expand(F)
    return expanded_F

def interpolacja_wzor(df_nodes, a):
    wzor = f"{a[0]} + "
    length = len(a)
    for i in range(1,length):
        wzor += f"{a[i]}*"
        for j in range(0,i):
            wzor += f"(x - {df_nodes['x'][j]})"
            if j != i-1:
                wzor +="*"
        if i != length-1: 
            wzor +=" + "
    return wzor

# Wygładzenie wykresu
def interpolacja_wykres(df_all, a, precision = 1):
    x_values = []
    x_i = df_all['x'].min()

    while x_i < df_all['x'].max():
        x_values.append(x_i)
        x_i += precision

    x_values.append(df_all['x'].max())

    df_interpolate = pd.DataFrame({'x': x_values})

    df_nodes = df_all.dropna()
    df_nodes.reset_index(inplace=True, drop=True)
    
    F = interpolacja_wzor_postac_ogolna(df_nodes, a)

    df_interpolate['F(x)'] = df_interpolate['x'].apply(lambda x: interpolacja_postac_ogolna(x, F))

    plt.plot(df_interpolate['x'], df_interpolate['F(x)'], '-', label="F2(x)")
    plt.plot(df_all['x'], df_all['y'], 'o', label="y2")
    plt.legend(loc='best')
    plt.show()

# ================================================

def main():

    print("\nSPOSOBY ODCZYTU DANYCH:")
    print("1 - 1 plik: z węzłami i z punktami do wyznaczenia przy pomocy interpolacji")
    print("2 - 2 pliki: plik_1 z węzłami i plik_2 z punktami do wyznaczenia przy pomocy interpolacji")

    print("\nFORMAT PLIKU: (.csv/.txt)")
    print("x;y")
    print("<int/float>;<int/float>")
    option = input("\nPodaj sposób odczytu danych [1/2]: ")

    if option == "1":
        file = input("Podaj nazwę pliku z danymi: ")

        try:
            df_all = pd.read_csv(file, delimiter=';')
        except FileNotFoundError:
            print("\nBłąd: Nie znaleziono pliku o takiej nazwie.")
            return
        df_nodes = df_all.dropna()
        df_nodes.reset_index(inplace=True, drop=True)


        print("\nDane z pliku:")
        print(df_all)

        print("\nTablica ilorazów różnicowych:")
        a = ilorazy_roznicowe(df_nodes)
        print(f"a = {a}")

        F = interpolacja_wzor_postac_ogolna(df_nodes, a)

        df_all['F(x)'] = df_all['x'].apply(lambda x: interpolacja_postac_ogolna(x, F))

        print("\nDane z pliku z wartościami interpolowanymi:")
        print(df_all)

        plt.plot(df_all['x'], df_all['F(x)'], '-', label="F(x)")
        plt.plot(df_all['x'], df_all['y'], 'o', label="w")
        plt.legend(loc='best')
        plt.show()

    elif option == "2":
        file_nodes = input("Podaj nazwę pliku z węzłami: ")
        file_xes = input("Podaj nazwę pliku z punktami do wyznaczenia przy pomocy interpolacji: ")
        try:
            df_nodes = pd.read_csv(file_nodes, delimiter=';')
            df_xes = pd.read_csv(file_xes, delimiter=';')
        except FileNotFoundError:
            print("\nBłąd: Nie znaleziono pliku/plików o takiej nazwie.")
            return

        print("\nDane z pliku z węzłami:")
        print(df_nodes)

        print("\nDane z pliku z punktami do wyznaczenia:")
        print(df_xes)

        print("\nTablica ilorazów różnicowych:")
        a = ilorazy_roznicowe(df_nodes)
        print(f"a = {a}")

        F = interpolacja_wzor_postac_ogolna(df_nodes, a)

        df_xes['F(x)'] = df_xes['x'].apply(lambda x: interpolacja_postac_ogolna(x, F))

        print("\nDane z pliku z wartościami interpolowanymi:")
        print(df_xes)

        df_nodes['F(x)'] = df_nodes['x'].apply(lambda x: interpolacja_postac_ogolna(x, F))

        df_all = pd.concat([df_xes, df_nodes], axis=0)
        df_all = df_all.sort_values('x').reset_index(drop=True)

        plt.plot(df_all['x'], df_all['F(x)'], '-', label="F(x)")
        plt.plot(df_nodes['x'], df_nodes['y'], 'o', label="w")
        plt.legend(loc='best')
        plt.show()
    else:
        print("\nBłąd: Brak takiej opcji.")
        return
    
    # === Wypisanie wzoru ===

    option = input("\nWypisać wzór interpolacyjny Newtona? [T/N]: ")
    if option in ["T", "t"]:
        option = input("\nKtórą postać wzoru wypisać? [O/I]\n(ogólną/iloczynową): ")
        if option in ["O", "o"]:
            print("\nWzór interpolacyjny Newtona (postać ogólna):")
            wzor = interpolacja_wzor_postac_ogolna(df_nodes, a)
            print(f"F(x) = {wzor}")
            
        elif option in ["I", "i"]:
            print("\nWzór interpolacyjny Newtona (postać iloczynowa):")
            wzor = interpolacja_wzor(df_nodes, a)
            print(f"F(x) = {wzor}")

        else:
            print("\nBłąd: Niepoprawny wybór.")

    # === Wygładzanie wykresu ===

    option = input("\nChcesz wygładzić wykres? [T/N]\n(za pomocą interpolacji): ")
    if option in ["T", "t"]:
        try:
            precision = float(input("Wpisz dokładność wykresu: "))
        except ValueError:
            precision = 1
        interpolacja_wykres(df_all, a, precision)

    

if __name__ == "__main__":
    main()
    print("\nZakończono program")