import numpy as np
import matplotlib.pyplot as plt

# Aufgabe 2
bereichDesErlaubten = 10**(-3)
d = 10
volumenMax = 471
startWert = 9

def formelFuerKugelVolumen(x):
    return np.pi/3 * x**2 * (3 * d/2 - x) - volumenMax

def formelFuerKugelVolumenAbgeleitet(x):
    return -np.pi*(x-10)*x

def newtonVerfahren(startWert):
    value = startWert
    condition = True
    while condition:
        value = value - formelFuerKugelVolumen(value)/formelFuerKugelVolumenAbgeleitet(value)
        print(value)
        print(np.absolute(formelFuerKugelVolumen(value)))
        condition = np.absolute(formelFuerKugelVolumen(value)) > bereichDesErlaubten
    return value

print(newtonVerfahren(startWert))
#7.658217376951713
#20.094514506173937
#8.014876532191066
#1.109810252795512
#8.03707967743404
#0.004680726030699134
#8.037174118831357
#8.510124871463631e-08
#8.037174118831357