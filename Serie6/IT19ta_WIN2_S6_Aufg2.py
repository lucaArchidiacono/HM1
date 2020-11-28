import numpy as np
import matplotlib.pyplot as plt

# Aufgabe 2

def gaussAlgo(A, b):
    A = A.astype(float)
    b = b.astype(float)
    
    # Dimension
    n = A.shape[0]
    
    # b-Vektor zu A Matrix hinzufuegen
    Ab = np.append(A, b, axis=1)
    
    for j in range(n):
        Ab = columnUnderDiagToZero(Ab, j)
    return [Ab[0:n,0:n], calcDet(Ab), solveWithTriag(Ab)]

# Zeile under der Diagonale zu 0 berechnen
# Ab = Zusammengefuegte Matrix aus A Matrix und b Vektor
# j = Index fuer Reihe
def columnUnderDiagToZero(Ab, j):
    n = Ab.shape[0]
    AC = np.copy(Ab)
    for i in range(j+1, n): # Index fuer Zeile (Startet bei 1 weil man bloss die uebernaechste Zeile aendern moechte (2te Zeile minus 1te Zeile))
        m = Ab[i][j]/Ab[j][j]
        # wie im Script beschrieben auf Seite 45 Kapitel 4.1
        AC[i,:] = AC[i,:] - m*AC[j,:]
    return AC

# Ab = Zusammengefuegte Matrix aus A Matrix und b Vektor
def solveWithTriag(Ab):
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
def calcDet(Ab):
    det = 1
    n = Ab.shape[0]
    for i in range(n):
        det = det * Ab[i][i]
    return det
    
    
A1 = np.array([[4,-1,-5],[-12,4,17],[32,-10,-41]])
b11 = np.array([[-5],[19],[-39]])
b12 = np.array([[6],[-12],[48]])

print(gaussAlgo(A1,b11))
print(gaussAlgo(A1,b12))