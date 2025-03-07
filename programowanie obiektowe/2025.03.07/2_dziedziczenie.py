class Foo:
    attr = "Common"

    def __init__(self, arg1, arg2):
        self.attr1 = arg1 # Instance attribute
        self.attr2 = arg2

    def use_me(self):
        print("Foo: use _me")

class Bar(Foo):
    def something_new(self):
        print("Bar: something_new")

class XYZ:
    def xyz(self):
        print("XYZ: xyz")

class Strange(Bar, XYZ):
    pass

# Dziedziczenie
def main2():
    f = Foo(1,3)
    b = Bar(2,4)
    xyz = XYZ()
    s = Strange(5,6)

    b.something_new()
    b.use_me()

    s.something_new()
    s.use_me()
    s.xyz()

if __name__ == '__main__':
    main2()