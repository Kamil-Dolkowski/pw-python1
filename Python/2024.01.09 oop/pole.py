class Circle:
    def __init__(self, radius):
        self.radius = radius

    def calculate(self):
        return 3.14 * self.radius**2
    


    
circle = Circle(10)
pole = circle.calculate()
print(pole)

circle.radius = 4
pole = circle.calculate()
print(pole)