# wydatek/przychód; kwota
# wydatek; 200 
import os

FILENAME = "budzet.txt"


def is_file_exists(file_path):
    return os.path.isfile(file_path)


def load(file_path):
    budget = []
    if is_file_exists(file_path):
        with open(file_path, "r") as file:
            for line in file:
                budget_type, amount = line.strip().split(";")
                budget.append([budget_type, amount])
    else:
        print("Plik nie istnieje.")
    return budget

def show_history(file_path):
    budget = load(file_path)
    print("\n-----HISTORIA-----")
    for record in budget:
        print(f"{record[0]}: {record[1]} zł")

def add(file_path,budget_type,amount):
    budget = load(file_path)
    budget.append([budget_type,amount])
    save(file_path, budget)
    
def save(file_path, budget):
    if is_file_exists(file_path):
        with open(file_path, "w") as file:
            for i in budget:
                file.write(f"{i[0]};{i[1]}\n")

def statistics(file_path):
    budget = load(file_path)
    suma_wydatkow = 0
    suma_przychodow = 0 
    bilans = 0
    for i in budget:
        if i[0] == 'wydatek':
            suma_wydatkow -= float(i[1])
        elif i[0] == 'przychod':
            suma_przychodow += float(i[1])
    bilans = suma_przychodow + suma_wydatkow
    
    suma_wydatkow = "%2.2f" % suma_wydatkow
    suma_przychodow = "%2.2f" % suma_przychodow
    bilans = "%2.2f" % bilans

    print("\n----PODSUMOWANIE----")
    print(f"Przychody: {suma_przychodow} zł")
    print(f"Wydatki: {suma_wydatkow} zł")
    print(f"Bilans: {bilans} zł")
    return suma_przychodow, suma_wydatkow, bilans



print("------POLECENIA------")
print("-h   historia transakcji")
print("-d   dodaj transakcję")
print("-p   podsumowanie")

while True:
    command = input("\nWprowadź polecenie: ")
    if command == '-h':
        show_history(FILENAME)
    elif command == '-d':
        print("")
        budget_type = input("Podaj rodzaj transakcji (przychod/wydatek): ")
        if budget_type == 'przychod' or budget_type == 'wydatek':
            amount = input("Podaj kwotę: ")
            try:
                amount = float(amount)
                amount = "%2.2f" % amount
                add(FILENAME, budget_type, amount)
                print(f"\nDodano do budżetu: {budget_type}, {amount} zł")
            except ValueError:
                print("Błędny zapis kwoty.")
        else:
            print("Błędny zapis rodzaju transakcji. (przychod/wydatek)")
        
    elif command == '-p':
        statistics(FILENAME)
    else:
        break




# Zadanie 1: Kalkulator Budżetu Domowego
# Cel: Napisz program do zarządzania budżetem domowym. Program powinien umożliwić dodawanie wydatków i przychodów, przechowywać je w pliku i generować podsumowanie budżetu.
# Funkcje:
# - Dodawanie wydatku/przychodu.
# - Zapisywanie danych do pliku.    
# - Odczytywanie danych z pliku.    
# - Generowanie podsumowania (np. łącznych wydatków i przychodów).  
# - Wyświetlanie historii transakcji.   
    



# def add(file_path,budget_type,amount):
#     budget = load(file_path)
#     if is_file_exists(file_path):
#         with open(file_path, "a") as file:
#             file.write(f"{budget_type};{amount}\n")
#     return