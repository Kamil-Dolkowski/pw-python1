import math
import matplotlib.pyplot as plt

MIN_VALUE = 1e-10

def dft(x):
    dft = []
    n = len(x)

    for k in range(n):
        real = 0
        imag = 0
        for i in range(n):
            real += x[i] * math.cos(2*math.pi*k*i/n)
            imag += x[i] * (-1*math.sin(2*math.pi*k*i/n))
        
        if abs(real) < MIN_VALUE:
            real = 0
        if abs(imag) < MIN_VALUE:
            imag = 0
            
        dft.append((real, imag))

    return dft

def inverse_dft(dft):
    x = []
    n = len(dft)

    for i in range(n):
        sum_value = 0
        for k in range(n):
            sum_value += dft[k][0] * math.cos(2*math.pi*k*i/n) - dft[k][1] * math.sin(2*math.pi*k*i/n)
        
        sum_value *= 1/n

        if abs(sum_value) < MIN_VALUE:
            sum_value = 0
            
        x.append(sum_value)

    return x

def modulus_of_complex_number(x):
    real = x[0]
    imag = x[1]

    return math.sqrt(real**2 + imag**2)

def modulus_of_dft(dft):
    mod_values = []

    for number in dft:
        mod_values.append(modulus_of_complex_number(number))

    return mod_values

def get_print_complex_number(x):
    if x[1] < 0:
        return f"{x[0]}{x[1]}i"
    else:
        return f"{x[0]}+{x[1]}i"


def main():
    print("===== DFT - Dyskretna Transformata Fouriera =====")

    print("\nFORMAT PLIKU: (.csv/.txt)")
    print("x;y")
    print("<int/float>;<int/float>")

    input_file = input("\nPodaj nazwę pliku z danymi: ")

    x = []
    y = []

    try:
        with open(input_file, "r") as file:
            next(file)
            for line in file:
                x_, y_ = line.strip().split(";")
                if x_ == "" or y_ == "":
                    raise ValueError
                x.append(float(x_.replace(",", "."))) # zamiana ',' na '.' [1,5 -> 1.5]
                y.append(float(y_.replace(",", ".")))
    except FileNotFoundError:
        print("\nBłąd: Nie znaleziono pliku o takiej nazwie.")
        return
    except ValueError:
        print("\nBłąd: Niepoprawna zawartość pliku.")
        return

    # y = [math.sin(i*math.pi/4) for i in range(16)]

    dft_values = dft(y)
    dft_mod_values = modulus_of_dft(dft_values)

    # print("\n======= DFT =======")
    # for i in range(len(dft_values)):
    #     print(f"{i}: {get_print_complex_number(dft_values[i])}")

    # print("\n======= |DFT| =======")
    # for i in range(len(dft_mod_values)):
    #     print(f"{i}: {dft_mod_values[i]}")

    n = len(dft_mod_values)
    freq = [i for i in range(n//2)]

    plt.subplot(2,1,1)
    plt.plot(x,y)
    plt.title("sygnał zaszumiony")
    plt.xlabel("x")
    plt.ylabel("y")

    plt.subplot(2,1,2)
    plt.bar(freq, dft_mod_values[: len(dft_mod_values) // 2]) # połowa 'dft_mod_values'
    plt.title("|DFT|")
    plt.xlabel("x")
    plt.ylabel("|DFT|")
    plt.tight_layout()
    plt.show()

    print("\n======= USUWANIE SZUMÓW =======")
    try:
        noise_max_value = float(input("Podaj próg usunięcia szumów: "))
    except:
        print("\nBłąd: Niepoprawna wartość.")
        return

    dft_after_delete_noise = []

    for i in range(len(dft_mod_values)):
        if dft_mod_values[i] < noise_max_value:
            dft_after_delete_noise.append((0, 0))
        else:
            dft_after_delete_noise.append(dft_values[i])

    y_from_inverse = inverse_dft(dft_after_delete_noise)

    plt.subplot(3,1,1)
    plt.plot(x,y)
    plt.title("sygnał zaszumiony")
    plt.xlabel("x")
    plt.ylabel("y")

    plt.subplot(3,1,2)
    plt.bar(freq, dft_mod_values[: len(dft_mod_values) // 2]) # połowa 'dft_mod_values'
    plt.title("|DFT|")
    plt.xlabel("x")
    plt.ylabel("|DFT|")

    plt.subplot(3,1,3)
    plt.plot(x,y_from_inverse)
    plt.title("sygnał odszumiony")
    plt.xlabel("x")
    plt.ylabel("y")
    plt.tight_layout()
    plt.show()

    choice = input("\nChcesz zapisać wyniki do pliku? [t/n]: ")
    if choice in ["T", "t"]:
        filename = input("Podaj nazwę pliku wynikowego: ")

        with open(filename, "w") as file:
            file.write("x;y\n")

            for i in range(len(y_from_inverse)):
                file.write(f"{x[i]};{y_from_inverse[i]}")

                if i != len(y_from_inverse) - 1:
                    file.write("\n")

        print(f"\nZapisano wyniki do pliku '{filename}'")

if __name__ == "__main__":
    main()
    print("\nZakończono program")