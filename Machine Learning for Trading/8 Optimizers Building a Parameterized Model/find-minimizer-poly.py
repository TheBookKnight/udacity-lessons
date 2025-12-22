"""Fit a line to a given set of data points using optimization."""

import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as spo

def error_poly(C, data):
    """Compute the error between the given polynomial and the observed data.
    Parameters
    ----------
    C: numpy.poly1d object or equivalent array representing polynomial coefficients
    data: 2D array where each row is a point (x, y)
    
    Returns error as a single real value
    -------
    error: float
        The sum of squared errors between the polynomial and the data points.
    """
    x = data[:, 0]
    y = data[:, 1]
    # Evaluate polynomial at each x
    y_fit = np.polyval(C, x)  # np.polyval expects highest degree first
    error = np.sum((y - y_fit) ** 2)
    return error

def fit_poly(data, error_func, degree=3):
    """Fit a polynomial of given degree to the data using the provided error function.
    
    Parameters
    ----------
    data: 2D array where each row is a point (x, y)
    error_func: function that computes the error between a polynomial and observed data
    degree: int
        Degree of the polynomial to fit.
    
    Returns the optimal polynomial coefficients that minimize the error function.
    -------
    C: array
        The optimal polynomial coefficients, highest degree first.
    """
    # Initial guess for polynomial coefficients: all zeros
    C_initial = np.poly1d(np.ones(degree + 1))
    
    # Plot initial guess (optional)
    x_ends = np.linspace(-5, 5, 21)
    y_initial = np.polyval(C_initial, x_ends)
    plt.plot(x_ends, y_initial, 'm--', linewidth=2.0, label='Initial guess')
    
    # Optimize the polynomial coefficients to minimize the error function
    result = spo.minimize(error_func, C_initial, args=(data,), method='SLSQP', options={'disp': False})
    return np.poly1d(result.x) # convert optimal result into a polynomial object

def test_run():
    # Define original polynomial
    l_orig = np.array([1.5, 10, 5, 60, 50]) # 4th degree polynomial coefficients
    print("Original polynomial: C0 = {}, C1 = {}, C2 = {}, C3 = {}, C4 = {}".format(l_orig[0], l_orig[1], l_orig[2], l_orig[3], l_orig[4]))
    Xorig = np.linspace(0, 10, 21)
    Yorig = l_orig[0] * Xorig**4 + l_orig[1] * Xorig**3 + l_orig[2] * Xorig**2 + l_orig[3] * Xorig + l_orig[4]
    plt.plot(Xorig, Yorig, 'b-', linewidth=2.0, label='Original line')
    
    # Generate noisy data points
    noise_sigma = 3.0
    noise = np.random.normal(0, noise_sigma, Yorig.shape)
    data = np.asarray([Xorig, Yorig + noise]).T
    plt.plot(data[:, 0], data[:, 1], 'go', label='Data points')
    
    # Try to fit a polynomial to this data
    l_fit = fit_poly(data, error_poly, degree=4)
    print("Fitted polynomial coefficients: {}".format(l_fit.coefficients))
    plt.plot(data[:, 0], np.polyval(l_fit, data[:, 0]), 'r-', linewidth=2.0, label='Fitted polynomial')
    
    plt.legend()
    plt.title("Polynomial Fitting with Optimization")
    plt.show()
    
if __name__ == "__main__":
    test_run()