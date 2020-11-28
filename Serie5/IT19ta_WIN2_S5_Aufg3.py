import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return np.pi/3 * x**2 * (3/2 * 10 - x) - 471

def sekantenVerfahren(f, x0, x1, tol):
    condition = True
    while condition:
        x1Plus1 = x1 - (((x1-x0)/(f(x1)-f(x0)))*f(x1))
        x0 = x1
        x1 = x1Plus1
        condition = np.absolute(f(x1)) > tol
    return x1

print(sekantenVerfahren(f, 10, 9, 10**(-3)))

# Das Problem am Newtonverfahren ist, dass man eine Ableitung einer unbekannten Funktion machen muss.
# Da man dies generisch machen muesste, sehen wir hier ein Problem. 