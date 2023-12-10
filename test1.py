import numpy
import matplotlib.pyplot as plt

# E=BSw*sin(wt)

B = float(input("Podaj B: "))
S = float(input("Podaj S: "))
w = float(input("Podaj w (omega): "))


T = (2*numpy.pi)/w

z = T*2.5   # zasięg wyrażony w wielokrotnościach T

x=numpy.linspace(0,z,1001)   # oś t
y = B*S*w*numpy.sin(w*x)        # oś E

print("")


l = int(z*numpy.pi/(T/4)) + (z*numpy.pi%(T/4)>0)

tick_pos_x = [i*(T/4) for i in range(0,l+1)]
labels_x = [round(i*(T/4),2) for i in range(0,l+1)]

plt.xticks(tick_pos_x, labels_x)





Emax = B*S*w*numpy.sin(w*T/4)
Emin = -B*S*w*numpy.sin(w*T/4)

tick_pos_y = list(numpy.linspace(Emin,Emax,9))
for i in range(0,len(tick_pos_y)-1):
    if tick_pos_y[i] > 0:
        tick_pos_y[i]=int(tick_pos_y[i])
        
print(tick_pos_y)
tick_pos_y = tick_pos_y+[Emax,Emin]
labels_y = tick_pos_y

plt.yticks(tick_pos_y,labels_y)





plt.plot(x, y)
plt.axhline(y=0,lw=1,color='black')
# plt.axhline(y=y1,lw=1,color='black')
# plt.legend(['E(t)'])
plt.title('Wykres napięcia od czasu')
plt.xlabel('t [s]')
plt.ylabel('E [V]')
plt.grid(True)
# plt.show()


# https://stackoverflow.com/questions/40642061/how-to-set-axis-ticks-in-multiples-of-pi-python-matplotlib
