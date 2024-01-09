def my_decorator(func):
    def wrapper():
        print("Tekst przed funkcją")
        func()
        print("Tekst po wykonaniu funkcji")
    return wrapper


@my_decorator
def czesc():
    print("Hello world!")

czesc()





# enkapsulacja
# dziedziczenie