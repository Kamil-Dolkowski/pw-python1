import random

with open('dane2.csv', "w") as file:
    file.write("x;y\n")
    x=-50
    for x in range(0,300):
        y = x+2
        file.write(f"{x};{y}\n")
    # for i in range(3,10):
    #     x = random.randint(10,1000)/10
    #     file.write(f"{x};\n")