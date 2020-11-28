import numpy as np
import matplotlib.pyplot as plt
import math as m

# Aufgabe 1
x = np.linspace(-3,3)

def f(x):
    return m.e**(x**2)+x**(-3)-10

def ableitungVonF(x):
   return 2*x*m.e**(x**2)-(3/x**4)

def newtonVerfahren(start, schritte):
    value = np.empty(schritte)
    value[0] = round(start, 4)
    for i in range(1, schritte):
        value[i] = round(value[i-1] - f(value[i-1])/ableitungVonF(value[i-1]), 4)
    return value

def vereinfachteNewtonVerfahren(start, schritte):
    value = np.empty(schritte)
    value[0] = round(start, 4)
    for i in range(1, schritte):
        value[i] = round(value[i-1] - f(value[i-1])/ableitungVonF(start), 4)
    return value

def sekantenVerfahren(start, schritte):
    value = np.empty(schritte)
    value[0] = round(start, 4)
    for i in range(1, schritte):
        value[i] = round(value[i-1] - ((value[i-1]-value[i-2])/(f(value[i-1]-f(value[i-2])))) * f(value[i-2]), 4)
    return value

#newtonVerfahren
xStart0 = np.linspace(2,3)
print("NewtonVerfahren")
for i in xStart0:
    print("x-Stelle: "+str(i))
    print(newtonVerfahren(i, 10))


#vereinfachtesNewtonVerfahren
xStart1 = np.linspace(0.5, 3)
print("Vereinfachtes NewtonVerfahren")
for i in xStart1:
    print("x-Stelle: "+str(i))
    print(vereinfachteNewtonVerfahren(i, 10))


#sekantenVerfahren
xStart2 = np.linspace(-1, 3)
print("SekantenVerfahren mit Startwert -1.0")
for i in xStart2:
    print("x-Stelle: "+str(i))
    print(vereinfachteNewtonVerfahren(i, 10))

xStart3 = np.linspace(-1.2, 3)
print("SekantenVerfahren mit Startwert -1.2")
for i in xStart3:
    print("x-Stelle: "+str(i))
    print(vereinfachteNewtonVerfahren(i, 10))

plt.figure()
plt.plot(x, f(x))
plt.grid()
plt.title('Aufgabe 1')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['f(x)'])

plt.show()

#Nullstellen von der Funktion f(x) sind:
#1te Nullstelle = -1.5265 
#2te Nullstelle = 0.4856 
#3te Nullstelle = 1.5076