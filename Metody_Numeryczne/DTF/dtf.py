# Sub Przycisk1_Kliknięcie()
# 	Range("g4").Value = "Cos"
# 	Range("h4").Value = "Sin"
# 	NN = Range("m1").Value
# 	For m = 0 To NN
# 		sumaCos = 0
# 		sumaSin = 0
# 		For k = 0 To 2 * NN + 1
# 			sumaCos = sumaCos + Range("b" & 5 + k).Value * Cos(2 * WorksheetFunction.Pi() * m * k / (2 * NN + 2))
# 			sumaSin = sumaSin + Range("b" & 5 + k).Value * Sin(2 * WorksheetFunction.Pi() * m * k / (2 * NN + 2))
# 		Next
# 		Range("g" & 5 + m).Value = sumaCos / (2 * NN + 2)
# 		Range("h" & 5 + m).Value = sumaSin / (2 * NN + 2)
# 	Next
# End Sub

import math

y = [1,2,3,4,5,6]
suma_cos = []
suma_sin = []

def dtf(n):
    for m in range(n):
        sumaCos = 0
        sumaSin = 0
        for k in range(2*n+1):
            sumaCos = sumaCos + y[k] * math.cos(2 * math.pi() * m * k / (2 * n + 2))
            sumaSin = sumaSin + y[k] * math.sin(2 * math.pi() * m * k / (2 * n + 2))
    suma_cos[m] = sumaCos / (2 * n + 2)
    suma_sin[m] = sumaSin / (2 * n + 2)

dtf(len(y))
print(suma_cos)