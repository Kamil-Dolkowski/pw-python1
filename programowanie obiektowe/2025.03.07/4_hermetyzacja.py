class Foo:
    attr = "Common"

    def __init__(self, arg1, arg2):
        self.attr1 = arg1 # Instance attribute
        self.attr2 = arg2
        self._attr_prot = 2 * arg1
        self.__attr_priv = 10 * arg1

    def get_priv(self):
        return self.__attr_priv

# Hermetyzacja
def main():
    f = Foo(1, "a")
    print(f.attr1)
    print(f._attr_prot)
    # print(f.__attr_priv) # AttributeError: 'Foo' object has no attribute '__attr_priv'.
    print(f.get_priv())

if __name__ == '__main__':
    main()