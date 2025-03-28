class Person:
    def __init__(self, name):
        self.name = name

class Employee(Person):
    def __init__(self, name, id):
        super().__init__("Best " + name)
        self.name_ = ">" + name + "<"
        self.id = id


e = Employee("John", "007")

print(e.name_)
print(e.name)
print(e.id)