import numpy
import matplotlib.pyplot as plt

# E=BSw*sin(wt)

# 1
B = int(input("Podaj B: "))
S = int(input("Podaj S: "))
w = int(input("Podaj w (omega): "))

x = numpy.linspace (0,10,1000)   # oś t
y = B*S*w*numpy.sin(w*x)        # oś U

print("")

# 2
B1 = int(input("Podaj B1: "))
S1 = int(input("Podaj S1: "))
w1 = int(input("Podaj w1 (omega): "))

x = numpy.linspace (0,10,1000)  # oś t
y1 = B1*S1*w1*numpy.sin(w1*x)   # oś U



plt.plot(x, y)
plt.plot (x, y1)
plt.axhline(y=0,lw=1,color='black')
plt.legend(['f(t)','f1(t)'])
plt.title('Wykres napięcia od czasu')
plt.xlabel('t [s]')
plt.ylabel('E [V]')
plt.grid(True)
plt.show()


# https://stackoverflow.com/questions/40642061/how-to-set-axis-ticks-in-multiples-of-pi-python-matplotlib