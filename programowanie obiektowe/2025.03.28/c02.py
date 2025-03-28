class Foo:
    def __new__(cls):
        print("Foo: __new__")
        return super().__new__(cls)
    
    def __init__(self):
        print("Foo: __init__")

class Bar:
    def __new__(cls):
        print("Bar: __new__")
        return Foo()
    
    def __init__(self):
        print("Bar: __init__")


b = Bar()
print(isinstance(b, Foo))