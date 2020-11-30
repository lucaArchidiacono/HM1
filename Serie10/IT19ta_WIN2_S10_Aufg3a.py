import numpy as np
from IT19ta_WIN2_S10_Aufg1_Aufg2 import JacobiVerfahren
from IT19ta_WIN2_S10_Aufg1_Aufg2 import GaussSeidelVerfahren


A= np.array([[8,5,2],
              [5,9,1],
              [4,2,7]])
print("Matrix A")
print(A)

b= np.array([[19],
              [5],
              [34]])
print("Vektor b")
print(b)


x= np.array([[1],
              [-1],
              [3]])
print("Vektor x")
print(x)


def Luca_Archidiacono_IT19ta_WIN2_S10_Aufg3a(A, b, x0, tol, opt):
    if opt.lower() == 'jacobi':
        [xResults, n, a_priori] = JacobiVerfahren(A, b, x0, tol)
        return xResults[-1], len(xResults), a_priori
    else:
        [xResults, n, a_priori] = GaussSeidelVerfahren(A, b, x0, tol)
        return xResults[-1], len(xResults), a_priori

if __name__ == "__main__":
    print(Luca_Archidiacono_IT19ta_WIN2_S10_Aufg3a(A, b, x, 10**-4, "jacobi"))