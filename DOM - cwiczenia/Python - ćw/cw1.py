zdanie = "   to jest przykładowe zdanie."

# Podzielić zdanie na słowa.
# Połączyć słowa w jedno zdanie.
# Napisać zdanie z dużej litery.
# Policz 'a' w zdaniu.
# Wypisz zdanie od tyłu.
# Usuwa spację na początku i końcu zdania.

slowa=zdanie.split()
print(slowa)

text=" ".join(slowa)
print(text)

text = zdanie.capitalize()
print(text)

ile_a = zdanie.count("a")
print(ile_a)

text1 = zdanie[::-1]
print(text1)

text1 = zdanie[0:2]
print(text1)

text1 = zdanie.strip()
print(text1)
