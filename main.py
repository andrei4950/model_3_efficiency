import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit
import random


def quadratic(x, a, b, c):
    return a*x**2 + b*x + c


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    x = np.linspace(0, 10, 11)
    print(x)
    err = np.array([random.randint(1, 100)/10 for _ in range(len(x))])
    y = quadratic(x, 1, 0, 0) + err
    print(y)
    plt.scatter(x, y)

    parameters, covariant_matrix = curve_fit(f=quadratic, xdata=x, ydata=y)
    parameter_uncertainties = np.sqrt(covariant_matrix.diagonal())
    print(parameters)
    print(parameter_uncertainties)

    plt.plot(x, quadratic(x, parameters[0], parameters[1], parameters[2]))
    plt.show()


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
