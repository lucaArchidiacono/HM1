import numpy as np
import matplotlib.pyplot as plt

# Aufgabe 2
bereichDesErlaubten = 10**(-3)

def fixPunkt(start, schritte, alpha):
    values = np.empty(schritte)
    values[0] = start
    for i in range(1, schritte):
        values[i] = alpha*values[i-1]*(1-values[i-1])
    return values

print("0 als StartWert")
print(fixPunkt(0.1, 50, 0))
#gegen 0

print("1 als StartWert")
print(fixPunkt(0.1, 50, 1))
#gegen 0

print("2 als StartWert")
print(fixPunkt(0.1, 50, 2))
#gegen 0.5

print("3 als StartWert")
print(fixPunkt(0.1, 50, 3))
#gegen 0.6

print("4 als StartWert")
print(fixPunkt(0.1, 50, 4))


# Aufgabe 2b
# Der Fixpunkt bedeutet hier, dass nach einer gewissen Zeit die Anzahl Kranker sich nicht mehr veraendert.

# Aufgabe 2c
# k = alpha*k*(1-k) --> k = alpha*k - alpha*k**2 --> k = alpha(k-k**2) --> k/(k-k**2) = a --> 1/(1-k) = a