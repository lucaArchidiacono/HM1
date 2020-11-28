import numpy as np
import matplotlib.pyplot as plt
import math as m

# Aufgabe 1

#a)
leftTable = np.array([[20,10,0],
                     [50,30,20],
                     [200,150,100]])
rightTable = np.array([150,470,2150])

print(np.linalg.solve(leftTable,rightTable))

#Flugzeug A fliegt 4 mal
#Flugzeug B fliegt 7 mal
#Flugzeug C fliegt 3 mal

#b)
rightTable = np.array([120,350,1600])

print(np.linalg.solve(leftTable,rightTable))

#Flugzeug A fliegt 3 mal
#Flugzeug B fliegt 6 mal
#Flugzeug C fliegt 1 mal