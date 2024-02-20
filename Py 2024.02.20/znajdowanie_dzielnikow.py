# Znajdowanie dzielników danej liczby

# -wejscie: liczba całkowita
# -wyjsice: lista/tablica dzielników


def dzielniki(number):
    t = []
    for i in range(1,number+1):
        if number % i == 0:
            t.append(i)
    return t


number = 36

x = dzielniki(number)
print(x)

