import numpy as np
import matplotlib.pyplot as plt
import math as m

x = np.arange(0.001, 100, 0.001) 

def f(x):
   return 5/np.cbrt(2*x**2)

def g(x):
    return (10**5*2*np.exp(-x/100))

def h(x):
    return (10**2*x/2**5*x)**2


plt.figure()
plt.loglog(x, f(x))
plt.semilogy(x, g(x))
plt.loglog(x, h(x))
plt.grid()
plt.title('Aufgabe 3')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['f(x)', 'g(x)', 'h(x)'])

plt.show()