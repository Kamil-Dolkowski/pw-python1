owoce = {"banan":"żółty",
         "jabłko":"zielony",
         "truskawka":"czerwony"}

owoce.get('banany',0)
print(owoce.get('banany',0))
print(owoce)


lista=[1,2,3]
print(lista[1])

lista.append(4)
print(lista)

lista.extend([4,5,6])
print(lista)

lista.insert(2,"XD")
print(lista)

lista.remove(4)
print(lista)

print(lista[::-1])
lista.remove("XD")
lista.sort()
print(lista)
