def something():
    ff = Foo("Krzysio")

class Foo:
    def __init__(self, name):
        self.name = name
        print(f"Foo ({self.name}): __init__")

    def __del__(self):
        print(f"Foo ({self.name}): __del__")

f = Foo("Aston")
g = Foo("Lukas")

del f

x = input("Wpisz coś: ")

something()

y = []

print(y[0])
print("Jestem tutaj")