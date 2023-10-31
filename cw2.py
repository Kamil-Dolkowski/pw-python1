#Słownik, gdzie kluczami są nazwy owoców, a wartościami ich kolory.
owoce={
    "jabłko": ("czerwony","zielony"),
    "banan":"żółty",
    "kiwi":"zielony"
        } #klucz:wartosc

# kolor=input("Podaj kolor: ")
# owoc=input("Podaj owoc: ")
# for kolor in owoce.values():
#     print(kolor)

# for owoc, kolor in owoce:
#     print(f"{owoc}:{kolor}".format(owoc,kolor))       #nie działa?

# print(owoce)
# print(owoce['banan'])
# print(owoce.keys())
# print(owoce.values())
# print(owoce.items())

# print(owoce.clear())
# print(owoce.pop("banan"))
# print(owoce)
# print(owoce.get("banan",0))

# owoc=input("Podaj nazwe owoca: ")
# if owoce.get(owoc,0) != 0:
#     print("Jest w koszyku")
# else:
#     print("Brak")

# klucz, wartosc = owoce.popitem("banan")




# slownik1={'a': 1, 'b':2}
# slownik2={'b': 3, 'c':4}

# slownik1.update(slownik2)
#slownik1={'a': 1,'b':3, 'c':4}
# print(slownik1)

# slownik2=slownik1.copy()
# print(slownik2)




lista=[1,2,3]

print(lista)
print(lista[0])
lista.append(4)
print(lista)
lista.extend([4,5,6])
print(lista)

lista.insert(3,"cos")
print(lista)

lista.remove(4)
print(lista)

lista.pop(4)
lista.count(4)
lista.reverse()
print(lista)
lista.remove("cos")
lista.sort()
print(lista)