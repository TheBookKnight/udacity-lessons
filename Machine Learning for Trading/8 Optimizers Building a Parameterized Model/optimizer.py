"""Minimize an objective function, using SciPy optimizers."""
    
from unittest import result
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import scipy.optimize as spo

def f(X):
    """Give a scalar X, return some value (a real number)"""
    Y = (X - 1.5) ** 2 + 0.5
    print("X = {}, Y = {}".format(X, Y)) # for tracing
    return Y

def test_run():
    """Minimize the function f() starting from an initial guess."""
    Xguess = 2.0
    print("Minima found at:")
    # SLSQP is Sequential Least SQuares Programming optimizer
    min_result = spo.minimize(f, Xguess, method='SLSQP', options={'disp': True})
    print("Result: {}".format(min_result))
    
    # Plot the function and the minima
    Xplot = np.linspace(0.5, 2.5, 21)
    Yplot = f(Xplot)
    plt.plot(Xplot, Yplot)
    plt.plot(min_result.x, min_result.fun, 'ro') # red dot at minima
    plt.title("Minima of an objective function")
    plt.show()

if __name__ == "__main__":
    test_run()