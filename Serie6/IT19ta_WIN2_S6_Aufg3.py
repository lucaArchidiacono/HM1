import numpy as np
import matplotlib.pyplot as plt

# Aufgabe 3

def gaussAlgo(A, b):
    A = A.astype(float)
    b = b.astype(float)
    
    # Dimension
    n = A.shape[0]
    
    # b-Vektor zu A Matrix hinzufuegen
    Ab = np.append(A, b, axis=1)
    
    for j in range(n):
        if A[j][j] == 0: 
            if regularChecken(Ab, j) == -1:
                raise Exception('Matrix nicht regulaer')
            else:
                Ab = reiheTauschen(Ab, j, regularChecken(Ab, j))
        Ab = zahlenUnderDiagonalGuertelZuNull(Ab, j)
    return [Ab[0:n,0:n], detBerechnen(Ab), xBerechnen(Ab)]

# Zeile under der Diagonale zu 0 berechnen
# Ab = Zusammengefuegte Matrix aus A Matrix und b Vektor
# j = Index fuer Reihe
def zahlenUnderDiagonalGuertelZuNull(Ab, j):
    n = Ab.shape[0]
    AC = np.copy(Ab)
    for i in range(j+1, n): # Index fuer Zeile (Startet bei 1 weil man bloss die uebernaechste Zeile aendern moechte (2te Zeile minus 1te Zeile))
        m = Ab[i][j]/Ab[j][j]
        # wie im Script beschrieben auf Seite 45 Kapitel 4.1
        AC[i,:] = AC[i,:] - m*AC[j,:]
    return AC

# Ab = Zusammengefuegte Matrix aus A Matrix und b Vektor
def xBerechnen(Ab):
    n = Ab.shape[0]
    x = np.zeros(n,np.float64)
    i=n-1
    while i>=0:
        sum=0
        for j in range(n):
            sum=sum+Ab[i][j]*x[j]
        x[i]=1/Ab[i][i]*(Ab[i][n]-sum)
        i=i-1    
    return x
        
# Berechnung der Determinante
# Ab = Zusammengefuegte Matrix aus A Matrix und b Vektor
def detBerechnen(Ab):
    det = 1
    n = Ab.shape[0]
    for i in range(n):
        det = det * Ab[i][i]
    return det
    
def regularChecken(A, j):
    n = A.shape[0]
    for i in range(j+1,n):
        if A[i][j] != 0:
            return i
    return -1

def reiheTauschen(A, i, j):
    AC = np.copy(A)
    n = A.shape[0]
    for k in range(n+1):
        AC[i][k] = A[j][k]
        AC[j][k] = A[i][k]
    return AC

A2 = np.array([[2,7,3],[-4,-10,0],[12,34,9]])
b21 = np.array([[25],[-24],[107]])
b22 = np.array([[5],[-22],[42]])

A3 = np.array([[-2,5,4],[-14,38,22],[6,-9,-27]])
b31 = np.array([[1],[40],[75]])
b32 = np.array([[16],[82],[-120]])

print(gaussAlgo(A2,b21))
print(gaussAlgo(A2,b22))

print(gaussAlgo(A3,b31))
print(gaussAlgo(A3,b32))