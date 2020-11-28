import numpy as np
from numpy.core.fromnumeric import diagonal

A= np.array([[8,5,2],
              [5,9,1],
              [4,2,7]])

b= np.array([[19],
              [5],
              [34]])

D = np.diag(np.diag(A))

R= np.triu(A,1)

L= np.tril(A,-1)

x= np.array([[1],
              [-1],
              [3]])

D_inverse = np.linalg.inv(D)

for i in range(3):
    LR = L+R

    DLR = np.matmul(-D_inverse, LR)

    DB = np.matmul(-D_inverse, -b)

    x = np.matmul(DLR, x) + DB
    print("x index:"+str(i+1))
    print(x)
