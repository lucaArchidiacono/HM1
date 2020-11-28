import numpy as np
import matplotlib.pyplot as plt
import math as m

xa = np.arange(1.099999, 1.1001, 10**-7)

def h(x):
    return np.sqrt((100*(x**2))-(200*x)+99)

plt.figure()
# aufgabe a
plt.plot(xa, h(xa))
plt.grid()
plt.title('Aufgabe 4')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(['f(x)', 'g(x)', 'h(x)'])

plt.show()
