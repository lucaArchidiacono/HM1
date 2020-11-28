import numpy as np
import matplotlib.pyplot as plt
import scipy.linalg

# Aufgabe 3


def exercise_3_solver(x, y, min, max):
    deg = 3
    poly = np.polyfit(x, y, deg)

    x01 = np.arange(min, max, 0.1)
    y01 = 0

    for i in range(0, deg+1):
        y01 += poly[i] * (x01 ** (deg-i))

    return (poly, x01, y01)


def linalgSolver():
    """Ax = b mit numpy.linalg.solve
    """
    a = np.array([[1, 0, 0, 0], [1, 2, 4, 8], [1, 9, 81, 729],
                  [1, 13, 169, 2197]])  # Matrix A
    b = np.array([150, 104, 172, 152])  # Vector b

    # Calculation of the solution for x from Ax = b mit numpy.linalg.solve: x = np.linalg.solve(A, b)
    x = np.linalg.solve(a, b)  # Vector x

    print('\nDie Lösung für Ax = b mit den entsprechenden Matrizen lautet'
          ' (berechnet mit numpy.linalg.solve): ')

    print('\nVektor x:')
    print((np.round((x), 2)))

    print('\nMatrix A:')
    print((np.round((a), 2)))

    print('\nVektor b:')
    print((np.round((b), 2)))


x0 = np.array([0, 2, 9, 13])
# Anzahl Tage
y0 = np.array([150, 104, 172, 152])

x1 = np.array([1997, 1999, 2006, 2010])
y1 = y0

x2 = np.array([0, 2, 6, 7, 9, 13])
y2 = np.array([150, 104, 126.8, 143, 172, 152])

polyAngepasst, x01, y01 = exercise_3_solver(x0, y0, -1, 14)
polyNormal, x11, y11 = exercise_3_solver(x1, y1, 1996, 2010)
polyAngepasst, x21, y21 = exercise_3_solver(x2, y2, -1, 14)


# Calculation of the number of days according to the fitted polynom
_97_till_03 = 2003-1997
_97_till_04 = 2004-1997
y3 = np.polyval(polyAngepasst, _97_till_03)
y4 = np.polyval(polyAngepasst, _97_till_04)
x3 = np.array(_97_till_03)
x4 = np.array(_97_till_04)

print('\nGeschätze Anzahl Tage mit hoher UV-Belastung für das Jahr 2003 ist:',
      '{0:.4f}'.format(y3))
print('Geschätze Anzahl Tage mit hoher UV-Belastung für das Jahr 2004 ist:',
      '{0:.4f}'.format(y4))

linalgSolver()

plt.close('all')
plt.figure(1)
plt.title('Number of days with extreme UV exposure in Hawaii (4 Data points)\n'
          'Adjusted (e.g. 0) versus non adjusted data (e.g. 1997)')
plt.minorticks_on()
plt.grid(axis='both', which='major',
         linestyle='-', linewidth=1)
plt.grid(axis='both', which='minor',
         linestyle=':', linewidth=0.5,
         label='original data')
# Graph of the fitted polynome with adjusted data (e.g. 0)
plt.plot(x01 + 1997, y01, dashes=[4, 0],
         label='Fitted Polynomial with adjusted data')
# Graph of the fitted polynome with non adjusted data (e.g. 1997)
plt.plot(x11, y11, dashes=[6, 2],
         label='Fitted Polynomial with non adjusted data')
plt.xlabel('Time')
plt.ylabel('Days')
plt.legend()
plt.show()

# Displaying solution as graph with original fitted polynom
plt.figure(2)
plt.title(
    'Number of days with extreme UV exposure in Hawaii (4 Data points')
plt.minorticks_on()
plt.grid(axis='both', which='major',
         linestyle='-', linewidth=1)
plt.grid(axis='both', which='minor',
         linestyle=':', linewidth=0.5,
         label='original data')
# Scatter plot of the original data
# x0 = np.array([0, 2, 9, 13])
plt.scatter(x0 + 1997, y0, label='Original Data')
# Graph of the fitted polynome (four data points)
plt.plot(x01 + 1997, y01, label='Fitted Polynomial')
# Scatter point of the year 2003
plt.scatter(x3 + 1997, y3, label='Estimation for 2003')
# Scatter point of the year 2004
plt.scatter(x4 + 1997, y4, label='Estimation for 2004')
plt.xlabel('Time')
plt.ylabel('Days')
plt.legend()
plt.show()

# Displaying solution as graph with newly fitted polynom
plt.figure(3)
plt.title(
    'Number of days with extreme UV exposure in Hawaii (6 Data points')
plt.minorticks_on()
plt.grid(axis='both', which='major',
         linestyle='-', linewidth=1)
plt.grid(axis='both', which='minor',
         linestyle=':', linewidth=0.5,
         label='original data')
# Scatter plot of the original data
# x0 = np.array([0, 2, 9, 13])
plt.scatter(x2 + 1997, y2, label='Original and Additional Data')
# Graph of the fitted polynome (four data points)
plt.plot(x01 + 1997, y01, dashes=[4, 0],
         label='Previously Fitted Polynomial')
# Graph of the fitted polynome (six data points)
plt.plot(x21 + 1997, y21, dashes=[6, 2], label='Newly Fitted Polynomial')
plt.xlabel('Time')
plt.ylabel('Days')
plt.legend()
plt.show()
