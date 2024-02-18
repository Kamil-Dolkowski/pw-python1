import os
file_path = "book.txt"

def add(path, text):
    with open(path, "w") as file:
        file.write(text)
        print(f"Wpisano do pliku: {text}")

def read(path):
    with open(path, "r") as file:
        return file.read()
# with open("book.txt", "w") as file:
#     file.write("Hello!")
#     print("Wpisano do pliku")

# def silnia(n):
#     if n ==0:
#         return 1
#     return n*silnia(n-1)

# liczba = int(input("Podaj liczbe: "))
# silnia(liczba)
# # text = "Kamil jest super"
# text = f"Silnia z {liczba}: {str(silnia(liczba))}"
# add(file_path, text)

def load(path):
    return os.path.exists(file_path)



if load(file_path):
    print("Plik wczytany.")
else:
    print("Brak pliku.")
print(f"Zawartość pliku: {read(file_path)}")
text = "Kamil jest super"
add(file_path, text)
