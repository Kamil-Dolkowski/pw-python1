# paradygmat programowania - zbiór wzorców, sposób patrzenia programisty i sterowania, aby program działał, szablon prawidłowego programowania

class Car:
    # atrybuty klasy (współdzielone ?)
    kolor = "Czerwony"
    
    def __init__(self, make, model, year):      # Konstruktor  -  Dunder methods    # metoda inicjacyjna
        # atrybuty instancji
        self.make = make
        self.model = model
        self.__year = year       # ukryta klasa
    
    def get_year(self):
        return self.__year
    def set_year(self, new_year):
        self.__year = new_year








car = Car("Toyota", "Camry", 2023)
print(car.kolor)
car.kolor = "Zielony"
print(car.kolor)

car.__year = 2020
print(car.__year)

print(car.get_year())
car.set_year(2020)