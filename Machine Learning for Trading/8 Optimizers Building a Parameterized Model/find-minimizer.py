"""Fit a line to a given set of data points using optimization."""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as spo

def fit_line(data, error_func):
    """Fit a line to the given data using the provided error function.
    
    Parameters
    ----------
    data: 2D array where each row is a point (x, y)
    error_func: function that computes the error between a line and observed data
    
    Returns the optimal line parameters as a tuple (C0, C1) that minimizes the error function.
    -------
    line: tuple
        The optimal line parameters (slope, y-intercept).
    """
    # Initial guess for line model: slope=0, intercept=mean(y values)
    l_initial = np.array([0, np.mean(data[:, 1])])
    
    # Plot initial guess (optional)
    x_ends = np.array([-5, 5])
    plt.plot(x_ends, l_initial[0] * x_ends + l_initial[1], 'm--', linewidth=2.0, label='Initial guess')
    
    # Optimize the line parameters to minimize the error function
    result = spo.minimize(error_func, l_initial, args=(data,), method='SLSQP', options={'disp': False})
    return result.x

def error(line, data): # error function
    """Compute the error between the given line and the observed data.
    Parameters
    ----------
    line: tuple/list/array (C0, C1) where C0 is slope and C1 is Y-intercept
    data: 2D array where each row is a point (x, y)
    
    Returns error as a single real value
    -------
    error: float
        The sum of squared errors between the line and the data points.
    """
    m, b = line
    x = data[:, 0]
    y = data[:, 1]
    error = np.sum((y - (m * x + b)) ** 2)
    return error

def test_run():
    # Define original line
    l_orig = np.array([4, 2]) # slope, y-intercept
    print("Original line: C0 = {}, C1 = {}".format(l_orig[0], l_orig[1]))
    Xorig = np.linspace(0, 10, 21)
    Yorig = l_orig[0] * Xorig + l_orig[1]
    plt.plot(Xorig, Yorig, 'b-', linewidth=2.0, label='Original line')
    
    # Generate noisy data points
    noise_sigma = 3.0
    noise = np.random.normal(0, noise_sigma, Yorig.shape)
    data = np.asarray([Xorig, Yorig + noise]).T
    plt.plot(data[:, 0], data[:, 1], 'go', label='Data points')
    
    # Try to fit a line to this data
    l_fit = fit_line(data, error)
    print("Fitted line: C0 = {}, C1 = {}".format(l_fit[0], l_fit[1]))
    plt.plot(data[:, 0], l_fit[0] * data[:, 0] + l_fit[1], 'r-', linewidth=2.0, label='Fitted line')
    
    plt.legend()
    plt.title("Line Fitting with Optimization")
    plt.show()
    
if __name__ == "__main__":
    test_run()