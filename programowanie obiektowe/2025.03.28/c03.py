class Square:
    def __init__(self, side_length):
        self.side_length = side_length

class Rectangle:
    def __new__(cls, width, height):
        if width == height:
            return Square(width)
        return super().__new__(cls)
    
    def __init__(self, width, height):
        self.width = width
        self.height = height

r1 = Rectangle(2, 3)
r2 = Rectangle(5, 5)

print(type(r1))
print(type(r2))