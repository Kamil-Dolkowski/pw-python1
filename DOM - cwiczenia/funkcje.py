# def max_min(a: float, b: float,c: float ) -> float:
#     return max(a,b,c), min(a,b,c)
# print(max_min(1,3,5))

# def lenght(word: str) -> int:
#     return len(word)
# print(lenght("kamil"))

# def silnia(n: int) -> int:
#     if n==0:
#         return 1
#     else:
#         return n*silnia(n-1)
# x=int(input("Podaj liczbe: "))
# print(silnia(x))



# # walidacja adresu e-mail
# # username@op.pl
# def validate_email(email: str) -> str:
#     if email.count("@") != 1:
#         raise ValueError("To nie jest adres mailowy.")
#     elem = email.split("@")
#     print(elem)
#     if 6 > len(elem[0]) > 36:
#         raise ValueError("To nie jest adres mailowy.")
#     return True


# email = input("Podaj e-mail: ")
# print(validate_email(email))



# def validate_password(password):
#     mam_cyfre=any(char.isdigit() for char in password)
#     mam_wielka_litere=any(char.isupper() for char in password)
#     dlugosc=len(password)>=8
#     return mam_cyfre and mam_wielka_litere and dlugosc

# haslo=input("Wprowadź hasło: ")
# if validate_password(haslo):
#     print("Mam silne hasło.")
# else:
#     print("Mam słabe hasło.")

# text="Komp-ut3r"
# czy_cyfra = any(char=="-" for char in text)
# print (czy_cyfra)


ip="123.146.090.225"

def validate_ip(ip: str) -> bool:
    parts=ip.split(".")
    if len(parts) != 4:
        return False
    for i in parts:
        if not i.isdigit() or not (0 <=int(i) <=255):
            return False
    return True
        
if validate_ip("123.255.178.090"):
    print("Poprawne IP.")
else:
    print("Niepoprawne IP.")

import calendar
print(calendar.calendar(theyear=2023, w=2, l=1, c=2, m=6))