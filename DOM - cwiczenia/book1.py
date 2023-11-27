import os
def load(path):
    return os.path.exists(path)

def read(path):
    with open(path, "r") as file:
        return file.read()
    
def add(path, text):
    with open(path, "a") as file:
        return file.write(f"{text}\n")

# is file exists
file_path = "book.txt"
if load(file_path):
    print("Wczytano plik.")
else:
    print("Brak pliku.")

text = "Nowa linijka."
print(read(file_path))
add(file_path, text)

