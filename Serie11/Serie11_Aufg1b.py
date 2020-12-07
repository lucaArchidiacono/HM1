import numpy as np
import cmath

i = 1
x = 4*np.cos(-40)+4*np.sin(-40)*i+2*np.exp(i*30)-3
y = 1.5*i

print(np.arctan2(x, y))


