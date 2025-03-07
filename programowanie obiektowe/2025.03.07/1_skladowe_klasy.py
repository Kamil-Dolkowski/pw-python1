class Foo:
    attr = "Common"

    def __init__(self, arg1, arg2):
        self.attr1 = arg1 # Instance attribute
        self.attr2 = arg2

# Składowe klasy
def main1():
    f1 = Foo(1, "b")
    f2 = Foo(2, "a")

    print(f1.attr2)
    print(f2.attr2)

    f1.attr2 = "e"

    print(f1.attr2)
    print(f2.attr2)

    print(f1.attr)
    print(f2.attr)
    print(Foo.attr)

    Foo.attr = "xxx"

    print(f1.attr)
    print(f2.attr)
    print(Foo.attr)

    f1.attr = "zzz"

    print(f1.attr)
    print(f2.attr)
    print(Foo.attr)

    Foo.attr = "aaa"

    print(f1.attr)
    print(f2.attr)
    print(Foo.attr)

if __name__ == '__main__':
    main1()