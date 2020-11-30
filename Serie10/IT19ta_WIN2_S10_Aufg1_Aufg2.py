import numpy as np
from numpy.core.fromnumeric import diagonal


def getDLR(A):
    D = np.diag(np.diag(A))

    R= np.triu(A,1)

    L= np.tril(A,-1)

    return D, L, R

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

[D, L, R] = getDLR(A)
print("Matrix D")
print(D)
print("Matrix R")
print(R)
print("Matrix L")
print(L)

JacobiB = np.matmul(-np.linalg.inv(D), (L+R))
print("JacobiB")
print(JacobiB)
GaussSeidelB = np.matmul(-np.linalg.inv(D+L), R)
print("GaussSeidelB")
print(GaussSeidelB)

#diagonalDominanz checken
def isDDM(m):
    n = m.shape[0]

    for i in range(0, n):          
      
        # for each column, finding 
        # sum of each row. 
        sum = 0
        for j in range(0, n) : 
            sum = sum + abs(m[i][j])      
  
        # removing the  
        # diagonal element. 
        sum = sum - abs(m[i][i]) 
  
        # checking if diagonal  
        # element is less than  
        # sum of non-diagonal 
        # element. 
        if (abs(m[i][i]) < sum) : 
            return False
    return True

def JacobiVerfahren(A, b, x, tolerance):
    [D, L, R] = getDLR(A)

    print("Jaccobi Verfahren")
    D_inverse = np.linalg.inv(D)

    xResults = [x]
    n = 0

    while True:
        LR = L+R

        DLR = np.matmul(-D_inverse, LR)

        DB = np.matmul(-D_inverse, -b)

        x = np.matmul(DLR, x) + DB
        xResults.append(x)
        print("x index:"+str(n+1))
        print(x)

        n += 1

        if abs(np.linalg.norm(xResults[n-1], np.inf) - np.linalg.norm(x, np.inf)) <= tolerance:
            a_Priori_Jacobi = a_Priori(JacobiB, xResults, n)
            print("a-Priori Jacobi")
            print(a_Priori_Jacobi)
            return xResults, n, a_Priori_Jacobi 

def GaussSeidelVerfahren(A, b, x, tolerance):
    [D, L, R] = getDLR(A)

    print("GaussSeidel Verfahren")
    DL_inverse = np.linalg.inv(D+L)

    xResults = [x]
    n = 0

    while True:
        Rx = np.matmul(R, x)
        DLRx = np.matmul(-DL_inverse, Rx)
        DLb = np.matmul(DL_inverse, b)

        x = DLRx+DLb
        xResults.append(x)
        print("x index:"+str(n+1))
        print(x)

        n += 1

        if abs(np.linalg.norm(xResults[n-1], np.inf) - np.linalg.norm(x, np.inf)) <= tolerance:
            a_Priori_GaussSeidel = a_Priori(GaussSeidelB, xResults, n)
            print("a-Priori GaussSeidel")
            print(a_Priori_GaussSeidel)
            return xResults, n, a_Priori_GaussSeidel
    
def Luca_Archidiacono_IT19ta_WIN2_S10_Aufg3a(A, b, x0, tol, opt):
    if opt.lower() == 'jacobi':
        return JacobiVerfahren(A, b, x0, tol)
    else:
        return GaussSeidelVerfahren(A, b, x0, tol)

def a_Posteriori(B, x_Array):
    B_norm = np.linalg.norm(B)
    x = x_Array[-1] - x_Array[-2]
    x_norm = np.linalg.norm(x)
    
    return (B_norm/(1-B_norm))*x_norm

def a_Priori(B, x_Array, n):
    B_norm = np.linalg.norm(B)
    x = x_Array[1] - x_Array[0]
    x_norm = np.linalg.norm(x)

    return (B_norm**n/(1-B_norm))*x_norm

              
if((isDDM(A))) : 
    print ("YES DiagonalDominant") 
else : 
    print ("NO DiagonalDominant") 

tolerance = 10**-4

[jacobi_x_results, n, n2] = JacobiVerfahren(A, b, x, tolerance)
[gaussSeidel_x_results, n, n2] = GaussSeidelVerfahren(A, b, x, tolerance)

a_Posteriori_Jacobi = a_Posteriori(JacobiB, jacobi_x_results[:4])
print("a-posteriori Jacobi")
print(a_Posteriori_Jacobi)
a_Posteriori_GaussSeidel = a_Posteriori(GaussSeidelB, gaussSeidel_x_results[:4])
print("a-posteriori GaussSeidel")
print(a_Posteriori_GaussSeidel)
