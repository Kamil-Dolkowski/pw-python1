zdanie="to jest przyklad do podzialu."
slowa=zdanie.split()
print(slowa)
zdanie= " ".join(slowa)
print(zdanie)

zdanie=zdanie.capitalize() #1 litera mala -> duza
print(zdanie)

count_a=zdanie.count("a")
print(f"Litera 'a' wystepuje {count_a} razy")

text="Python"
text=text[::-1]
print(text)

text=text[:-1]
print(text)

text="Python"
text=text[0:-1]
print(text)