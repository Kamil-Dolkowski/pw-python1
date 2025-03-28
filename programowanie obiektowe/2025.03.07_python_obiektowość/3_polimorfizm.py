class Foo:
    attr = "Common"

    def __init__(self, arg1, arg2):
        self.attr1 = arg1 # Instance attribute
        self.attr2 = arg2

    def use_me(self):
        print("Foo: use _me")

    def poly(self):
        print("Foo: poly")

class Bar(Foo):
    def something_new(self):
        print("Bar: something_new")

    def poly(self):
        print("Bar: poly")

class XYZ:
    def xyz(self):
        print("XYZ: xyz")

    def poly(self):
        print("XYZ: poly")

class Strange(Bar, XYZ):
    pass

# Polimorfizm
def main():
    f = Foo(1,3)
    b = Bar(2,4)
    xyz = XYZ()
    s = Strange(5,6)

    b.something_new()
    b.use_me()

    s.something_new()
    s.use_me()
    s.xyz()

    f.poly()
    b.poly()
    xyz.poly()

    collection = [f, b, xyz]

    for e in collection:
        print(type(e))
        e.poly()

if __name__ == '__main__':
    main()