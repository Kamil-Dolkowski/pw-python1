# def powitanie():
#     print("Witaj w świecie Pythona!")
# powitanie()

# def powitanie(imie):
#     print(f"Witaj, {imie}!")
# imie=input("Podaj imie: ")
# powitanie(imie)

# def max_min(a,b,c):
#     return max(a,b,c), min(a,b,c)
# print(max_min(3,5,2))

# def dlugosc_ciagu(wyraz):
#     return len(wyraz)
# wyraz=input("Podaj wyraz: ")
# print(dlugosc_ciagu(wyraz))

# def silnia(n):
#     if n==0:
#         return 1
#     else:
#         return n*silnia(n-1)
# print(silnia(5))

# def suma(a: int, b: int) -> int:
#     return a+b
# print(suma(4,3))

# import requests
# response = requests.get('https://www.google.com')
# print(response.status_code)
# print(response.text)
### $ pip3 install requests







# Zad.1  Walidacja adresu e-mail
# username@pw.edu.pl
# -czy istnieje @
# -jaki jest username
# -jaka jest domena
# -brak spacji, :, ;

# -czy istnieje @                   ^
# -walidacja pustych znaków         
# -username ma od 6-30 znaków       ^
# -domena to pw.edu.pl              


# def validate_email(email):
#     #czy jest 1x @ 
#     if email.count('@') != 1:
#         raise ValueError("To nie jest adres mailowy.")
#     #podział adresu na username i domenę
#     parametr=email.split('@')
#     #czy domena to 'pw.edu.pl'
#     if parametr[1] !='pw.edu.pl':
#         raise ValueError("To nie jest adres mailowy.")
#     #czy username ma od 6-30 znaków
#     if 6<=len(parametr[0]) <=30:
#         print("ok")


# try:
#     validate_email('kamil.dolkowski@pw.edu.pl')
# except ValueError as e:
#     print(f"Komunikat błędu: {e}")


#  *
# username=parametr[0]
# domena=parametr[1]







#Zad.2 Silne haslo. Musi miec przynajmniej 8 znaków, w tym 1 cyfre i 1 wielką litere.

# password.isdigit()
# password.isupper()
# any()

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





#Zad.3 Czy nazwa użytkownika składa się wyłącznie z liter i cyfr oraz czy ma od 3 do 16 znaków.

# def validate_username(username):
#     return username.isalnum() and 3 <= len(username) <=16


# username=input("Podaj nazwe użytkownika: ")
# if validate_username(username):
#     print("tak")
# else:
#     print("nie")






#Zad.4 Czy ciąg jest adresem IPv4. 4 sekcje z liczb od 0 do 255, oddzielonych kropkami.
#192.168.128.1

# def validate_ip(ip):
#     parts=ip.split('.')
#     if len(parts) !=4:
#         return False
#     for part in parts:
#         if not part.isdignit( or not 0<= int(part) <225):
#             return False
#     return True

# print(validate_ip('192.1.1.222'))








#Zad.5 Czy NIP jest prawidłowy.

nip='1234567890'
def validate_nip(nip:str):
    weights=[6,5,7,2,3,4,5,6,7]
    #spawdzamy czy mamy 10 znaków
    #sprawdzamy czy wszystkie są cyframi

    if len(nip) != 10:
        return False
    if not nip.isdigit():
        return False
    suma=0
    for i in range(9):
        suma += int(nip[i]) * weights[i]
    if suma%11 == 10 and suma%11 != int(nip[9]):
        return False
    return True

if validate_nip('6543256988'):
    print("Nip jest ok.")
else:
    print("Nip jest zly.")


