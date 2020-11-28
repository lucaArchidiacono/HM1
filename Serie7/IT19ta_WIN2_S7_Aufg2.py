import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg

# Aufgabe 2


def gaussAlgo(A, X):
    # Zu float konvertieren
    A = A.astype(float)
    X = X.astype(float)

    AX = np.append(A, X, axis=1)

    # Dimension von A holen
    n = A.shape[0]

    # Vektor x erstellen aus 0en mit der Dimension (hoehe) von Matrix A
    x = np.zeros(n)

    # Matrix A kopieren
    b = np.copy(A)

    # Gauss Eliminierung
    for i in range(n):
        if AX[i][i] == 0.0:
            raise Exception('Divided by zero detected')
        for j in range(i+1, n):
            ratio = AX[j][i] / AX[i][i]

            for k in range(n + 1):
                AX[j][k] = AX[j][k] - ratio * AX[i][k]

    # Zurueck subtrahieren
    x[n-1] = AX[n-1][n] / AX[n-1][n-1]

    for i in range(n-2, -1, -1):
        x[i] = AX[i][n]

        for j in range(i+1, n):
            x[i] = x[i] - AX[i][j] * x[j]

        x[i] = x[i] / AX[i][i]

    return (AX, n, b, x)


def calcDeterminante(AX, n):
    determinante = 1
    for i in range(0, n):
        determinante *= AX[i][i]

    linalgDeterminante = np.linalg.det(AX[:, 0:n])

    return (determinante, linalgDeterminante)


A = np.array([[0.8, 2.2, 3.6],
              [2.0, 3.0, 4.0],
              [1.2, 2.0, 5.8]])
X = np.array([[2.4],
              [1.0],
              [4.0]])

AX, n, b, x = gaussAlgo(A, X)

determinante, linalgDeterminante = calcDeterminante(AX, n)

P, L, U = scipy.linalg.lu(b)

print('\nDie ursprüngliche erweiterte Matrix sah so aus:')
print(b)

print('\nDie Dreiecksmatrix sieht so aus:')
print(AX[:, 0:n])

print('\nDer Wert der Determinante lautet (berechnet mit der Hauptdiagonale):')
print('\t', '{0:.4f}'.format(determinante))

print('\nDer Wert der Determinante lautet (berechnet mit linalg):')
print('\t', '{0:.4f}'.format(linalgDeterminante))

print('\nDie Lösung lautet: ')
for i in range(n):
    print('X%d = %0.2f' % (i, x[i]), end='\t')

print('\n\nDie Matrizen der LR-Zerlegung (engl. LU decomposition):')
print("\nA = Ausgangs- bzw. Koeffizienten-Matrix:")
print(b)

print("\nP = Pivot- bzw. Permutations-Matrix:")
print(P)

print("\nL = Linke untere Diagonal-Matrix")
print(L)

print("\nR = Rechte obere Diagonal-Matrix")
print(U)
