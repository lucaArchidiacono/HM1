import numpy as np
import matplotlib.pyplot as plt
import math as m

xb = np.arange(1.1,1.3,10**-7)

def h(x):
    return np.sqrt((100*(x**2))-(200*x)+99)

plt.figure()
# aufgabe b
plt.semilogy(xb, h(xb))
plt.grid()
plt.title('Aufgabe 4')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['f(x)', 'g(x)', 'h(x)'])

plt.show()

'''
c) 
Umformen als sqrt(10x - 9)*sqrt(10x - 11). 
Dadurch fällt x^2 weg, was die Kondition verbessert. 
10x-11 bleibt allerdings schlecht, da dieser Term um x=1.1 weiterhin sehr nahe bei 0 liegt.
'''