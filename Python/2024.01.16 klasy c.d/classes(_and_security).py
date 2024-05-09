# Książka "Wprowadzenie do bezpieczeństwa IT"
# atak zero-day
# chipy w kablach USB zbierające dane

#------------------------------------------------------------------------------------------------------

# class ParentClass:
#     def speak(self):
#         print("Jestem rodzicem.")

# class ChildClass(ParentClass):
#     def speak(self):
#         super().speak() # "Jestem rodzicem."
#         print("Jestem dzieckiem.")

# child = ChildClass()
# child.speak()

#------------------------------------------POLIMORFIZM--------------------------------------------------

# def area(shape):
#     return shape.calculate_area()

# class Circle:
#     def __init__(self, radius):
#         self.radius = radius
    
#     def calculate_area(self):
#         return 3.14 * self.radius ** 2
    
# class Rectangle:
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def calculate_area(self):
#         return self.width * self.height
    


# circle = Circle(5)
# rectangle = Rectangle(4,3)

# print("Pole koła: ", area(circle))
# print("Pole prostokąta: ", area(rectangle))

#--------------------------------------------------------------------------------------------------------

# class Animal:
#     def speak(self):
#         pass

# class Dog(Animal):
#     def speak(self):
#         return "Hau!"
    
# class Cat(Animal):
#     def speak(self):
#         return "Miau!"
    
# def make_animal_speak(animal):
#     return animal.speak()
    
# dog = Dog()
# cat = Cat()

# print(make_animal_speak(dog))
# print(make_animal_speak(cat))

#---------------------------------------KLASY ABSTRAKCYJNE-------------------------------------------------

# from abc import ABC, abstractmethod

# class Shape(ABC):       # nie można tu wykorzystać metod inicjacyjnych !
#     @abstractmethod
#     def calculate_area(self):
#         pass

# class Circle(Shape):
#     def __init__(self, radius):
#         self.radius = radius
    
#     def calculate_area(self):
#         return 3.14 * self.radius ** 2
    
# class Rectangle(Shape):
#     def __init__(self, width, height):
#         self.width = width
#         self.height = height

#     def calculate_area(self):
#         return self.width * self.height
    


# circle = Circle(5)
# rectangle = Rectangle(4,3)

# print("Pole koła: ", circle.calculate_area())
# print("Pole prostokąta: ", rectangle.calculate_area())

#-----------------------------------------MAGICZNE METODY-----------------------------------------------

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self) -> str:
        return f"{self.name}, {self.age} lat"


person = Person("Alicja", 33)
print(str(person))





# zmienne prywatne i zmienne silnie prywatne
# hermetyzacja
# set'ery get'ery


