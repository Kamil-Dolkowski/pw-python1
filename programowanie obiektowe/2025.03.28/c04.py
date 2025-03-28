class Singleton:
    __ins = None

    def __new__(cls):
        if cls.__ins is None:
            print("Create instance")
            cls.__ins = super().__new__(cls)

        return cls.__ins

obj1 = Singleton()
obj2 = Singleton()
obj3 = Singleton()

print(obj1)
print(obj2)
print(obj3)