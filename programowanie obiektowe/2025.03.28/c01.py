class Person:
    def __new__(cls, name, age): # Przydzielenie pamięci na dany obiekt
        print("Creating a new Person object")
        instance = super().__new__(cls)
        return instance
    
    def __init__(self, name, age):
        print("Initializing the Person object")
        self.name = name
        self.age = age


person = Person("John", 30)
print(f"{person.name} {person.age}")