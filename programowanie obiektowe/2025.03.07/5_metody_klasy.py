class Foo:
    cls_attr = "Class attribute"

    def __init__(self, arg1, arg2):
        self.attr1 = arg1 # Instance attribute
        self.attr2 = arg2

    @classmethod
    def method_1(cls):
        print(cls.cls_attr)
        return "class method"
    
    @staticmethod
    def method_2():
        # print(cls.cls_attr) # NameError: name 'cls' is not defined
        # print(cls_attr) # NameError: name 'cls_attr' is not defined.
        return "static method"

# Metody klasy
def main():
    print(Foo.method_1())
    print(Foo.method_2())

    f = Foo(1, "a")

    print("---")

    print(f.method_1()) # ? - jakie konsekwencje
    print(f.method_2()) # ? - jakie konsekwencje

if __name__ == '__main__':
    main()