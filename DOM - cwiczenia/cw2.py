def file_exists(path):          # czy plik istnieje
    try:
        with open(path, "r") as file:
            print("Wczytano plik.")
    except FileNotFoundError:
        print("Brak pliku.")
        
def save(path,txt):             # zapisz coś do pliku
    with open(path, "w") as file:
        file.write(txt)
        print("Zapisano zmiany.")

def read(path):                 # wyświetl, co jest w pliku
    with open(path, "r") as file:
        print(f"W pliku: {file.read()}")

def load(path):                 # załaduj, to co jest w pliku, do zmiennej
    with open(path, "r") as file:
        return file.read()
    
file_path = "lista_plik.txt"

file_exists(file_path)

lista = [1,2,3,4,5]
txt = str(lista[::-1])

# read(file_path)
# save(file_path, txt)
# read(file_path)

# x = load(file_path)
# print(x)

# import re
# x1 = re.findall("\d",x)
# print(x1)
# for i in range(len(x1)):
#     x1[i]=int(x1[i])
# print(x1)

# x1.reverse()
# save(file_path,str(x1))
# read(file_path)



uczniowie = {'imie':('Kamil','Kuba'),
             'nazwisko':('Dółkowski','Kowalski'),
             'wiek':('19','20') }

# print(uczniowie['nazwisko'][0])

# id = int(input("Podaj id ucznia: "))
# print(f"ID: {id}: {uczniowie['imie'][id]} {uczniowie['nazwisko'][id]}, lat {uczniowie['wiek'][id]}")



# uczniowie = {'0':{'imie':'Kamil',
#                   'nazwisko':'Dółkowski',
#                   'wiek':'19'},
#              '1':{'imie':'Kuba',
#                   'nazwisko':'Kowalski',
#                   'wiek':'20'}  }

# print(uczniowie['1']['imie'])
# print(uczniowie['1'].values())

print(uczniowie.get('imiek','brak'))
print(uczniowie.__len__())


owoce = {"jabłko":("czerwony","zielony"),
         "banan":"żółty",
         "kiwi":"zielony"}

print(owoce.pop('jabłko'))
print(owoce)



# t = [1,2,3,3,4]
# print(t.index(3))
# print(min(t))
# print(max(t))

from datetime import datetime
import locale
locale.setlocale(locale.LC_ALL, 'pl_PL')

now = datetime.now()
print(now.strftime("%A"))

import re

txt = "The rain in Spain"
x = re.search(r"\bS\w+", txt)
print(x.group())
a = x.group()
for i in a:
    print(i)



# --------------------------------------------------
"""

zdanie = "   to jest przykładowe zdanie."

# Podzielić zdanie na słowa.
x = zdanie.split()
print(x)
# Połączyć słowa w jedno zdanie.
print(" ".join(x))
# Napisać zdanie z dużej litery.
x = zdanie.strip()
print(x.capitalize())
# Policz 'a' w zdaniu.
print(zdanie.count("e"))
# Wypisz zdanie od tyłu.
print(zdanie[::-1])
# Usuwa spację na początku i końcu zdania.
x = zdanie.strip()
print(x)

"""
import datetime


a = datetime.datetime(2023,11,27,15,30,11,222992)
print(a)
a = datetime.time(11,30,22)
print(a.hour)

now = datetime.datetime.now()
date = now.strftime("%H:%M:%S, %a %d %b %Y")
print(date)

password = "wera1"
print(any(char.isdigit() for char in password))
l="-1"
print(l.isdigit())


# import calendar
# x = calendar.isleap(2023)
# print(x)

# print(calendar.calendar(theyear=2023, w=2,l=1,c=2,m=6))
# print(calendar.month(theyear=2023, themonth=11,w=5,l=1))

import random
r = random.randint(1,10)
print(r)
t = ["a","b","c"]
print(random.choice(t))
random.shuffle(t)
print(t)

def summ(number: str) -> int:
    suma=0
    for digit in number:
        suma+=int(digit)
    return suma

try:
    number = input("Enter number: ")
    print(f"Result: {summ(number)}")
except ValueError:
    print("Error: Enter a number, not word.")