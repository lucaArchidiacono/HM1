import numpy as np
import matplotlib.pyplot as plt

# Aufgabe 1a
bereichDesErlaubten = 10**(-6)

def f(x):
    return 230*x**4+18*x**3+9*x**2-221*x-9

def ableitungVonF(x):
   return 920*(x)**3+54*(x)**2+18*(x)-221 

def fixPunktGleichungVonF(x):
    return (230*x**4+18*x**3+9*x**2-9)/221

def fixPunktGleichungAbleitungVonF(x):
    return (920*x**3+54*x**2+18*x)/221

def fixPunktIteration(value):
    condition = True
    while condition:
        value = fixPunktGleichungVonF(value)
        condition = fixPunktGleichungVonF(value) > bereichDesErlaubten
    return value

def newtonVerfahren(value):
    condition = True
    while condition:
        value = value - f(value)/ableitungVonF(value)
        condition = f(value) > bereichDesErlaubten
    return value

print(fixPunktIteration(0.1))
# Resultat -> -0.04013122171945701 
print(newtonVerfahren(0.1))
# Resultat -> -0.04065928831575928
# Das FixpunktVerfahren erreicht die Nullstelle erst im Intervall [0.6,1]


# Aufgabe 1b
print(fixPunktGleichungVonF(-0.5))
# Resultat -> 0.024321266968325792 
print(fixPunktGleichungVonF(0.5))
# Resultat -> 0.04468325791855204 

# Die Funktionswerte der Endpunkte des Intervalls [-0.5, 0.5] gehen gegen 0.
# Daraus nehemen wir an dass F([d,e]) in [d,e] liegt.

print(fixPunktGleichungAbleitungVonF(0.5)) # wird maximal fuer x=0.5
# Resultat -> 0.6221719457013575 = alpha

# Aufgabe 1c
# a-Priori Abschaetzung sieht folgendermassen aus:
# |xn-x| <= ((alpha^n)/(1-alpha)) * |x1-x0|
# ((0.6221719457013575**n)/(1-0.6221719457013575))*|0.04468325791855204-0.5|
# n = 45 Iterationen
