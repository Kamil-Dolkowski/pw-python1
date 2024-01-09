class Kwadrat:
    # atrybuty
    width = 0
    height = 0

    def __init__(self, width, height):
        self.width = width
        self.height = height

    @classmethod        # dekorator
    def pole_kwadratu(cls, atrybuty):           # ponowne uruchomienie klasy z danymi parametrami
        return cls(atrybuty, atrybuty)

    @staticmethod       # nie wykorzystują żadnych danych z klasy       # dekorator
    def obwod(a, b):
        return a+b      # 2*a+2*b






# pole = Kwadrat(10,20)
pole = Kwadrat.pole_kwadratu(4)
print(pole.height)

print(Kwadrat.obwod(4,6))