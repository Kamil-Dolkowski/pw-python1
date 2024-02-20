# Algorytm Euklidesa (NWD)

# -wejscie: 2 liczby
# -wyjscie: 1 liczba


def euklides(a,b):
    while a != b:
        if a < b:
            b = b - a
        else:
            a = a - b
    return a



a = 48
b = 12

x = euklides(a,b)
print(x)




# inny sposób:


def euklides1(a,b):
    while b:
        a, b = b, a % b
    return a


x = euklides(a,b)
print(x)