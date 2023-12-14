# wydatek/przychód; kwota
# wydatek ;200 
import os

FILENAME = "budzet.txt"

def validate_budget_type(budget_type):
    return budget_type == 'wydatek' or budget_type == 'przychod'

def validate_amount(amount: str):
    return amount.isdigit()

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
        print("File not exists.")
    return budget

def show_history(file_path):
    budget = load(file_path)
    print("\n-----HISTORIA-----")
    for many in budget:
        print(f"{many[0]}: {many[1]} zł")

def add(file_path,budget_type,amount):
    budget = load(file_path)
    if validate_budget_type(budget_type) and is_file_exists(file_path):
        with open(file_path, "a") as file:
            file.write(f"{budget_type};{amount}\n")
        return

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

    print("\n----STATYSTYKI----")
    print(f"Przychody: {round(suma_przychodow,2)} zł")
    print(f"Wydatki: {round(suma_wydatkow,2)} zł")
    print(f"Bilans: {round(bilans,2)} zł")
    return suma_przychodow, suma_wydatkow, bilans

while True:
    command = input("Enter command: ")
    if command == '-h':
        print("-h   help")



show_history(FILENAME)
statistics(FILENAME)
add(FILENAME,'przychod','25.50')
show_history(FILENAME)