import pandas as pd
import numpy as np
from sympy import symbols, expand, sympify
import matplotlib.pyplot as plt
import sys
import time

MAX_NUMBER_OF_POINTS = 5
RESULT_FILE = "interpolacja_wynik.csv"
PRECISION = 0.1

# === Wyznaczanie tablicy ilorazów różnicowych
def ilorazy_roznicowe(df_nodes):
    df_nodes.reset_index(inplace=True, drop=True) # aby indeksy df_nodes zaczynały się od 0
    n = len(df_nodes)
    a = df_nodes['y'].tolist()

    for i in range(0,n):
        for j in range(n-1,i,-1):
            a[j] = (a[j] - a[j-1]) / (df_nodes['x'][j] - df_nodes['x'][j-1-i])
    return a

# === Funkcja interpolacyjna (wzór interpolacyjny Newtona) [obliczenia wartości]
# Funkcja nieużywana (starsza wersja) (wolniejsza)
def interpolacja(x, df_nodes, a) -> float:
    y = a[0]
    length = len(a)
    for i in range(1,length):
        element = a[i]
        for j in range(0,i):
            element *= (x - df_nodes['x'][j])
        y += element
    return y

# Funkcja używana (szybsza)
def interpolacja_postac_ogolna(x, F) -> float:
    x_symbol = symbols('x')
    return F.subs(x_symbol, x)

# === Wzory
# postać ogólna (wykorzystywana do obliczeń - mniejsza ilość operacji)
def interpolacja_wzor_postac_ogolna(df_nodes, a) -> str:
    df_nodes.reset_index(inplace=True, drop=True)
    F_str = interpolacja_wzor(df_nodes, a)
    
    # Zamiana funkcji z postaci sumy iloczynów na postać ogólną (zmniejszenie ilości operacji)
    F = sympify(F_str)
    expanded_F = expand(F)
    return expanded_F

# postać suma iloczynów
def interpolacja_wzor(df_nodes, a) -> str:
    wzor = f"{a[0]}"
    length = len(a)

    if length > 1:
        wzor += " + "
        for i in range(1,length):
            wzor += f"{a[i]}*"
            for j in range(0,i):
                wzor += f"(x - {df_nodes['x'][j]})"
                if j != i-1:
                    wzor +="*"
            if i != length-1: 
                wzor +=" + "
    return wzor

# Funkcja dzieli cały przedział danych na mniejsze przedziały, w których jest dokonywana interpolacja
def interpolacja_dla_całego_przedziału(df_nodes, df_all):
    x_values = []
    df_interpolate = pd.DataFrame({'x': x_values})
    intervals = len(df_nodes) // MAX_NUMBER_OF_POINTS
    if intervals == 0:
        intervals = 1

    print("\nWyznaczanie interpolacji: ", end="")
    begin = time.time()

    ## podział na przedziały, w których jest maksymalnie (MAX_NUMBER_OF_POINTS + 1) węzłów, 
    ## z czego ostatni węzeł jest taki sam co pierwszy węzeł kolejnego przedziału, aby zachować ciągłość funkcji
    ## np. [0,1,2] ; [2,3,4] ; [4,5,6] (podane liczby to indeksy węzłów)

    for i in range(intervals):
        sys.stdout.write(f"\rWyznaczanie interpolacji: {int(100 * i / intervals)}%")
        sys.stdout.flush()

        df_nodes_group = df_nodes.iloc[i * MAX_NUMBER_OF_POINTS : (i+1) * MAX_NUMBER_OF_POINTS+1]
        
        min_value = df_nodes_group['x'].min()
        if df_all['x'].min() < min_value and i == 0: # jeśli pierwszy podział, weź pod uwagę najmniejszy punkt do wyznaczenia jako początek przedziału interpolacji
            min_value = df_all['x'].min()

        max_value = df_nodes_group['x'].max()
        if df_all['x'].max() > max_value and i == intervals-1: # jeśli ostatni podział, weź pod uwagę największy punkt do wyznaczenia jako koniec przedziału interpolacji
            max_value = df_all['x'].max()

        a = ilorazy_roznicowe(df_nodes_group)
        F = interpolacja_wzor_postac_ogolna(df_nodes_group, a)

        x_values = []
        x_i = min_value

        while x_i < max_value:
            x_values.append(x_i)
            x_i += PRECISION

        x_values.append(max_value)

        df_interpolate_current = pd.DataFrame({'x': x_values})
        df_interpolate = pd.concat([df_interpolate, df_interpolate_current]) # połączenie obecnego przedziału z wcześniejszymi

        df_interpolate['F(x)'] = df_interpolate.apply(lambda row: interpolacja_postac_ogolna(row['x'], F) if min_value <= row['x'] <= max_value else row['F(x)'], axis=1)

    sys.stdout.write(f"\rWyznaczanie interpolacji: 100%\n")
    sys.stdout.flush()

    end = time.time()
    print(f"Czas operacji: {(end - begin):.2f}s")

    return df_interpolate


def wyznacz_wartosc(x, df_nodes) -> float:
    intervals = len(df_nodes) // MAX_NUMBER_OF_POINTS
    if intervals == 0:
        intervals = 1

    for i in range(intervals):
        df_nodes_group = df_nodes.iloc[i * MAX_NUMBER_OF_POINTS : (i+1) * MAX_NUMBER_OF_POINTS+1]
        
        max_value = df_nodes_group['x'].max()

        if x > max_value and i != intervals-1: # jeśli x nie należy do obecnego przedziału i jeśli nie jest to ostatni podział, przejdź dalej
            continue
        else:
            # jeśli x należy do obecnego przedziału, oblicz y
            a = ilorazy_roznicowe(df_nodes_group)
            F = interpolacja_wzor_postac_ogolna(df_nodes_group, a)

            return interpolacja_postac_ogolna(x, F)

# ================================================


def main():
    print("\nSPOSOBY ODCZYTU DANYCH:")
    print("1 - 1 plik: z wezlami i z punktami do wyznaczenia przy pomocy interpolacji")
    print("2 - 2 pliki: plik_1 z wezlami i plik_2 z punktami do wyznaczenia przy pomocy interpolacji")

    print("\nFORMAT PLIKU: (.csv/.txt)")
    print("x;y")
    print("<int/float>;<int/float>")
    option = input("\nPodaj sposób odczytu danych [1/2]: ")

    if option == "1":
        file = input("Podaj nazwę pliku z danymi: ")

        # ====== ODCZYT DANYCH Z PLIKU ======
        try:
            df_all = pd.read_csv(file, delimiter=';', dtype={'x': float, 'y': float})
        except FileNotFoundError:
            print("\nBlad: Nie znaleziono pliku o takiej nazwie.")
            return
        except ValueError:
            # Konwersja zapisanej w pliku liczby float z przecinkiem na kropkę
            try:
                df_all = pd.read_csv(file, delimiter=';', dtype={'x': float, 'y': float}, decimal=",")
            except:
                print("\nBlad: Niepoprawna zawartość pliku.")
                return

        df_all.sort_values(by='x', inplace=True)
        df_all.reset_index(inplace=True, drop=True)

        # df_nodes - tylko węzły
        df_nodes = df_all.dropna()
        df_nodes.reset_index(inplace=True, drop=True)

        df_all['F(x)'] = np.nan

        # print("\nDane z pliku:")
        # print(df_all)

        df_interpolate = interpolacja_dla_całego_przedziału(df_nodes, df_all)

        # df_to_calc - punkty do interpolacji
        df_to_calc = df_all[df_all['y'].isnull()].copy()
        df_to_calc['F(x)'] = df_to_calc['x'].apply(lambda x: wyznacz_wartosc(x, df_nodes))

        # df_interpolate['sin(x)'] = df_interpolate['x'].apply(lambda x: 1000 * np.sin(x))

        # ====== WYKRES ======
        plt.plot(df_interpolate['x'], df_interpolate['F(x)'], '-', label="F(x)")
        plt.plot(df_all['x'], df_all['y'], 'o', label="w - węzły")
        plt.plot(df_to_calc['x'], df_to_calc['F(x)'], 'o', label="y - obliczone wartości")
        # plt.plot(df_interpolate['x'], df_interpolate['sin(x)'], '-', label="sin(x)")
        plt.legend(loc='best')
        plt.title("Interpolacja Newtona")
        plt.xlabel("x")
        plt.ylabel("F(x)")
        plt.show()

    elif option == "2":
        file_nodes = input("Podaj nazwę pliku z węzłami: ")
        file_to_calc = input("Podaj nazwę pliku z punktami do wyznaczenia przy pomocy interpolacji: ")

        # ====== ODCZYT DANYCH Z PLIKU ======
        try:
            df_nodes = pd.read_csv(file_nodes, delimiter=';', dtype={'x': float, 'y': float})
            df_to_calc = pd.read_csv(file_to_calc, delimiter=';', dtype={'x': float})
        except FileNotFoundError:
            print("\nBłąd: Nie znaleziono pliku/plików o takiej nazwie.")
            return
        except ValueError:
            # Konwersja zapisanej w pliku liczby float z przecinkiem na kropkę
            try:
                df_nodes = pd.read_csv(file_nodes, delimiter=';', dtype={'x': float, 'y': float}, decimal=",")
                df_to_calc = pd.read_csv(file_to_calc, delimiter=';', dtype={'x': float, 'y': float}, decimal=",")
            except:
                print("\nBlad: Niepoprawna zawartość pliku.")
                return

        # print("\nDane z pliku z węzłami:")
        # print(df_nodes)

        # print("\nDane z pliku z punktami do wyznaczenia:")
        # print(df_xes)

        df_all = pd.concat([df_nodes, df_to_calc])
        df_all['F(x)'] = np.nan

        df_all.sort_values(by='x', inplace=True)
        df_all.reset_index(inplace=True, drop=True)

        df_nodes.sort_values(by='x', inplace=True)
        df_nodes.reset_index(inplace=True, drop=True)

        df_interpolate = interpolacja_dla_całego_przedziału(df_nodes, df_all)

        df_to_calc['F(x)'] = df_to_calc['x'].apply(lambda x: wyznacz_wartosc(x, df_nodes))

        # ====== WYKRES ======
        plt.plot(df_interpolate['x'], df_interpolate['F(x)'], '-', label="F(x)")
        plt.plot(df_all['x'], df_all['y'], 'o', label="w - węzły")
        plt.plot(df_to_calc['x'], df_to_calc['F(x)'], 'o', label="y - obliczone wartości")
        plt.legend(loc='best')
        plt.title("Interpolacja Newtona")
        plt.xlabel("x")
        plt.ylabel("F(x)")
        plt.show()

    else:
        print("\nBłąd: Brak takiej opcji.")
        return
    

    # ====== PLIK Z WYNIKAMI ======
    option = input("\nCzy chcesz zapisać wyniki interpolacji do pliku? [t/n]: ")
    if option in ["T", "t"]:
        df_interpolate.to_csv(RESULT_FILE, index=False, sep=";")
        print(f"Zapisano wyniki do pliku '{RESULT_FILE}'")
    

    # ====== WYZNACZANIE DOWOLNEJ WARTOŚCI ======
    option = input("\nChcesz za pomocą obliczonej interpolacji wyznaczyć wartość dla danego X? [t/n]: ")
    if option in ["T", "t"]:
        try:
            x = float(input("Podaj x: "))
        except:
            print("\nBłąd: Podano niepoprawną wartość.")
            return
        
        if x > df_all['x'].max() or x < df_all['x'].min():
            print("\nUwaga! Podana wartość jest spoza zakresu interpolacji!")

        y = wyznacz_wartosc(x, df_nodes)

        print(f"\nF({x}) = {y}")

        # ====== WYKRES ======
        plt.plot(df_interpolate['x'], df_interpolate['F(x)'], '-', label="F(x)")
        plt.plot(df_all['x'], df_all['y'], 'o', label="w")
        plt.plot(df_to_calc['x'], df_to_calc['F(x)'], 'o', label="y")
        plt.plot(x, y, 'o', markersize=10, label=f"F({x})")
        plt.legend(loc='best')
        plt.xlabel("x")
        plt.ylabel("F(x)")
        plt.show()


if __name__ == "__main__":
    main()
    print("\nZakończono program")