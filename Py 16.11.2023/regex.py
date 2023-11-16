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
# [+] - zwraca dowolny znak 

txt = "Dopasoniewuje nie pozycję, która nie jest nraniecą słoniewa."
x=re.findall("nie",txt)
print(x)

x=re.split("\s",txt)
print(x)

x=re.split("\s",txt,1)
print(x)

x=re.sub("nie", "WOW", txt)
print(x)

x=re.sub("\s", "WOW", txt)
print(x)

x=re.sub("\s", "WOW", txt,1)
print(x)

x=re.findall(r'\bnie\b',txt)    #r- tekst raw -nowy wiersz
print(x)

x=re.findall(r'\w',txt)  
print(x)

x=re.findall(r'[\w]+',txt)      # brak kropki
print(x)

x=re.findall(r'[\w\.]+',txt)    # z kropką
print(x)



mail = "jakub.chmielak@pw.edu.pl"

x=re.split("@",mail)
print(x)

x = re.match("^[\w\.]+@[\w\.]+",mail)
print(x)
print(bool(x))



txt1 = "Rok 2023 będzie lepszy."

x=re.sub("\d",'X',txt1)
print(x)



x = re.findall(r"\b[n]\w+",txt)
print(x)



kot = "Nasz kot ma 60 lat i waży 4 kg."
x = re.findall(r"\d+", kot)
print(x)


x = re.search(r"^nasz", kot, re.IGNORECASE)
print(x)


tel = "Mój numer to 623-456-7890."
x = re.search(r"\d{3}-\d{3}-\d{4}",tel)    
print(x)

x = re.search(r"^\d{3}-\d{3}-\d{4}",tel)    # coś jest źle (^)
print(x)

x = re.search(r"\b[4-8][0-9]{2}-\d{3}-\d{4}",tel)
print(x)



text = "Odwiedź https://www.example.com i http://www.anotherdomain.org."
domain_names = re.findall(r'https?://www\.(\w+)', text)
print(domain_names)