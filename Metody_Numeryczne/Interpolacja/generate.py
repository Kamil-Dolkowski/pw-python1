import random
import math

with open('dane4.csv', "w") as file:
    file.write("x;y\n")

    for x in range(0,1_000):
        # y = x+2
        y = math.sin(x)*1000
        file.write(f"{x};{y}\n")
    # for i in range(3,10):
    #     x = random.randint(10,1000)/10
    #     file.write(f"{x};\n")