
import numpy as np
import timeit

from IT19ta_WIN2_S10_Aufg3a import Luca_Archidiacono_IT19ta_WIN2_S10_Aufg3a

dim = 3000
A = np.diag(np.diag(np.ones((dim,dim))*4000))+np.ones((dim,dim))
dum1 = np.arange(1,np.int(dim/2+1),dtype=np.float64).reshape((np.int(dim/2),1))
dum2 = np.arange(np.int(dim/2),0,-1,dtype=np.float64).reshape((np.int(dim/2),1))  
x = np.append(dum1,dum2,axis=0)
b = A@x
x0 = np.zeros((dim,1))
tol = 10**-4

def IT19ta_WIN_S10_Aufg3b():
    time_jacobi = timeit.timeit(
        "Luca_Archidiacono_IT19ta_WIN2_S10_Aufg3a(A, b, x0, tol, 'jacobi')",
        "from __main__ import Luca_Archidiacono_IT19ta_WIN2_S10_Aufg3a, A, b, x0, tol",
        number=1)
    print(f'time for Jacobi:       {time_jacobi}')

    time_gauss_seidel = timeit.timeit(
        "Luca_Archidiacono_IT19ta_WIN2_S10_Aufg3a(A, b, x0, tol, 'gauss_seidel')",
        "from __main__ import Luca_Archidiacono_IT19ta_WIN2_S10_Aufg3a, A, b, x0, tol",
        number=1)
    print(f'time for Gauss-Seidel: {time_gauss_seidel}')


IT19ta_WIN_S10_Aufg3b()

