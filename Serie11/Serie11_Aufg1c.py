import numpy as np

z1 = (2+i)/(1-2i)
z2 = 2*np.exp((np.pi)i/3)
z3 = 4*np.cos(30)+4*np.sin(30)i

result = (z1*z3)/(0.5*z2)
print(result)
