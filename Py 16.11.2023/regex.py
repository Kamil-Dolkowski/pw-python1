## python -m ensurepip --upgrade
### pip install regex

import re

txt = "Dopasowuje pozycję, która nie jest granicą słowa."
x = re.search("^Dopasowuje.*słowa.$", txt)
print(x)


# findall - zwraca listę zawierającą wszystkie wystąpienia
# search - zwraca obiekt match, jeśli w dowolnym miejscu znajdzie dopasowanie
# split - zwraca listę, w której ciągu znaków został podzielony przy każdym dopasowaniu
# sub - zastępuje jedno lub więcej wystąpień

# [a-z] - zwraca dopasowania pasujące do wzoru od a-z, małe litery
# [a-k] - 
# [a-zA-Z] - 
# [0-9] - 
# [678] - 
# [michal] - zwraca użyte znaki alfabetu
# [^michal] - zwraca wszystkie znaki poza tymi -> c
# 00-62
# [0-6][0-9] -> 56 -/> 72
# [+] - zwraca dowolny znak ? zwraca '+' ?

txt = "Dopasoniewuje nie pozycję, która nie jest graniecą słoniewa."
x=re.findall("nie",txt)
print(x)

