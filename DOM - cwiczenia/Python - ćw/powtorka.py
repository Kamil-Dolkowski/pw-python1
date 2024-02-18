# Napisz funkcję, która obliczy sumę cyfr liczby całkowitej.

# def summ(number: int) -> int:
#     result=0
#     for i in number:
#         result+=int(i)
#     return result


# try:
#     number = input("Enter number: ")
#     if number.isdigit():
#         print(f"Digits' sum: {summ(number)}")
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
        if not number.isdigit():
            return False
        return True

def bmi_count(weight: float,height: float) -> float:
    bmi = weight / (height ** 2)
    return bmi_comm(bmi)

def bmi_comm(bmi: float) -> str:
    if bmi < 18.5:
        return ("Niedowaga")
    elif 18.5 <= bmi < 25:
        return ("Prawidłowa waga")
    elif 25 <= bmi < 30:
        return ("Nadwaga")
    else:
        return ("Otyłość")


# print(check_float("340"))

# while True:
try:
        weight = int(input("Enter weight: "))
        height = int(input("Enter height: ")) / 100
        print(bmi_count(weight,height))
        # break
except ValueError:
        print("Error: Invalid input.")
