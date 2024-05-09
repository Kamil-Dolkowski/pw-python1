class Person:
    def __init__(self, name):
        self.name = name



person = Person("Jon")
person.wiek = 30    # atrybut dynamiczny

print(person.wiek)