# # Napisz funkcję, która obliczy sumę cyfr liczby całkowitej.
# def suma_cyfr(liczba: str) -> int:
#     suma=0
#     for i in liczba:
#         suma+=int(i)
#     return suma

# try:
#     liczba=input("Podaj liczbę całkowitą: ")
#     if liczba.isdigit():
#         print(f"Suma cyfr tej liczby: {suma_cyfr(liczba)}")
#     else: 
#         print("Please enter only digits.")
# except ValueError:
#     print("Invalid input.")





# Napisz program obliczający wskaźnik masy ciała (BMI) na podstawie wzrostu i wagi użytkownika.

# bmi = waga / (wzrost ** 2)
# 18.5 >      Niedowaga
# 18.5 - 24.9 Prawidłowa waga
# 25 - 29.9   Nadwaga
# > 30        Otyłość

def check_float(number) -> bool:
    try:
        float(number)
        return True
    except ValueError:
        return False
    
def bmi_oblicz(waga: float, wzrost: float) -> float:
    bmi = waga / (wzrost ** 2)
    return bmi_kom(bmi)
    
def bmi_kom(bmi: float) -> str:
    if bmi <= 18.5:
        return "Niedowaga"
    elif 18.5 < bmi <= 25:
        return "Prawidłowa waga"
    elif 25 < bmi < 30:
        return"Nadwaga"
    else:
        return "Otyłość"

waga = float(input("Podaj wagę: "))
wzrost = float(input("Podaj wzrost: "))/100

bmi = bmi_oblicz(waga, wzrost)
print(bmi_oblicz(waga, wzrost))