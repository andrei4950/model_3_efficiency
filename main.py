# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import matplotlib.pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')


    """"parameters, covariant_matrix = curve_fit(f=fit_function, xdata=processed_times, ydata=distances, sigma=distance_err,
                                             absolute_sigma=True, p0=p0)
    parameter_uncertainties = np.sqrt(covariant_matrix.diagonal())
    print(parameters)
    print(parameter_uncertainties)""""

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
