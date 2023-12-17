import numpy
import matplotlib.pyplot as plt

# E=BSw*sin(wt)

# wykres1

print("")
print("------Wykres 1-----\n")

B = float(input("Podaj B[T]: "))
S = float(input("Podaj S[m^2]: "))
w = float(input("Podaj w[rad/s] (omega): "))

T = (2*numpy.pi)/w

Emax = B*S*w
Emin = -B*S*w

print(f"\nEmax: {round(Emax,2)} V")
print(f"Emin: {round(Emin,2)} V")
print(f"T: {round(T,3)} s")

z = T*2.5   # zasięg wyrażony w wielokrotnościach T

x=numpy.linspace(0,z,1001)   # oś t
y = B*S*w*numpy.sin(w*x)        # oś E

print("")

# oś X
l = int(z*numpy.pi/(T/4)) + (z*numpy.pi%(T/4)>0)

tick_pos = [i*(T/4) for i in range(0,l+1)]
labels = [round(i*(T/4),2) for i in range(0,l+1)]

plt.xticks(tick_pos, labels)

# wykres2

print("")
print("-----Wykres 2-----\n")

B1 = float(input("Podaj B[T]: "))
S1 = float(input("Podaj S[m^2]: "))
w1 = float(input("Podaj w[rad/s] (omega): "))

T1 = (2*numpy.pi)/w1

E1max = B1*S1*w1
E1min = -B1*S1*w1

print(f"\nEmax: {round(E1max,2)} V")
print(f"Emin: {round(E1min,2)} V")
print(f"T: {round(T1,3)} s")

y1 = B1*S1*w1*numpy.sin(w1*x)        # oś E

print("")



# główny program

plt.plot(x, y)
plt.plot(x, y1)
plt.legend(['Wykres 1', 'Wykres 2'])
plt.axhline(y=0,lw=1,color='black')
plt.title('Wykres napięcia od czasu')
plt.xlabel('t [s]')
plt.ylabel('E [V]')
plt.grid(True)
plt.show()