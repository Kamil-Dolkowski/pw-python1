class Agent():
    __agents = {}

    def __new__(cls, name):
        if name not in cls.__agents:
            cls.__agents[name] = super().__new__(cls)

        return cls.__agents[name]
    
    def __init__(self, name):
        self.name = name


a1 = Agent("James")
a2 = Agent("Lukas")
a3 = Agent("Aston")
a4 = Agent("Mr Bean")

print(a1 == a3)

a5 = Agent("Aston")

print(a3 == a5)

print(a1 == a5)