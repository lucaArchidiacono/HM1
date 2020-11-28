import numpy as np

def Gruppe_S9_Aufg2(A, As, b, bs):
    x = np.linalg.solve(A, b)
    xs = np.linalg.solve(As, bs)
    Aa = np.linalg.norm(A - As, np.inf) / np.linalg.norm(A, np.inf)
    ba = np.linalg.norm(b - bs, np.inf) / np.linalg.norm(b, np.inf)
    Ac = np.linalg.cond(A, np.inf)
    xmax = 'NaN'
    if Ac * Aa < 1:
        xmax = Ac * (Aa + ba) / (1 - Ac * Aa)
    xobs = np.linalg.norm(x - xs, np.inf) / np.linalg.norm(x, np.inf)
    return [x, xs, xmax, xobs]

b = np.array([[5720.],
              [3300.],
              [836.]])
bs = np.array([[5820.],
               [3400.],
               [936.]])
A = np.array([[20., 30., 10.], [10., 17., 6.], [2, 3, 2]])
As = np.array([[19.9, 29.9, 9.9], [9.9, 16.9, 5.9], [1.9, 2.9, 1.9]])

result = Gruppe_S9_Aufg2(A, As, b, bs)
print('x: {}'.format(result[0]))
print('xs: {}'.format(result[1]))
print('xmax: {}'.format(result[2]))
print('xobs: {}'.format(result[3]))
