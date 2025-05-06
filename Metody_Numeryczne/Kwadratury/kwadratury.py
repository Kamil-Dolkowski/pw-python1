import pandas as pd
import matplotlib.pyplot as plt

def main():
    print("===== KWADRATURY =====")

    print("\nFORMAT PLIKU: (.csv/.txt)")
    print("x;y")
    print("<int/float>;<int/float>")

    file = input("\nPodaj nazwę pliku z danymi: ")

    try:
        df = pd.read_csv(file, delimiter=';')
    except FileNotFoundError:
        print("\nBłąd: Nie znaleziono pliku o takiej nazwie.")
        return
    
    print("\nPodaj zakres:")
    a = input("a = ")
    b = input("b = ")

    print("\nPodaj metodę (p/t):")
    print("p - prostokaty")
    print("t - trapezy")
    method = input("Wybór: ")

if __name__ == "__main__":
    main()
    print("\nZakończono program")