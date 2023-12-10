import numpy
import matplotlib.pyplot as plt

# E=BSw*sin(wt)

B = float(input("Podaj B: "))
S = float(input("Podaj S: "))
w = float(input("Podaj w (omega): "))


T = (2*numpy.pi)/w

z = T*1.6

x = numpy.linspace (0,z,1000)   # oś t
y = B*S*w*numpy.sin(w*x)        # oś E

print("")







plt.plot(x, y)
plt.axhline(y=0,lw=1,color='black')
# plt.legend(['f(t)'])
plt.title('Wykres napięcia od czasu')
plt.xlabel('t [s]')
plt.ylabel('E [V]')
plt.grid(True)
plt.show()


# https://stackoverflow.com/questions/40642061/how-to-set-axis-ticks-in-multiples-of-pi-python-matplotlib