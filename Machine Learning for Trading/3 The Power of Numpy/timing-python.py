"""Using time function (and how fast is Numpy)"""

import numpy as np
from time import time


def how_long(func, *args):
    """Execute functions with given arguments, and measure execution time."""
    t0 = time()
    result = func(*args)  # all arguments are passed in as-is
    t1 = time()
    return result, t1 - t0


def manual_mean(arr):
    """Compute mean (average) of all elements in the given 2D array."""
    sum = 0
    for i in range(0, arr.shape[0]):
        for j in range(0, arr.shape[1]):
            sum = sum + arr[i, j]
    return sum / arr.size


def numpy_mean(arr):
    return np.mean(arr)


def access_and_modify_array_elem():
    a = np.random.rand(5, 4)
    print("Indexing the array:\n")
    print("Array:\n", a)
    # Slicing
    # Note: Slice n:m:t specifies a range that starts at n, and stops before m, in t steps
    print("Slicing:\n", a[:, 0:3:2])  # will select columns 0, 2 for every row
    # Modify
    a[:, 3] = [1, 2, 3, 4, 5]
    print("Modified a column:\n", a)


def test_run():
    t1 = time()
    print("ML4T")
    t2 = time()
    print("The time taken by print statement is ", t2 - t1, " seconds")
    """Function called by Test Run."""
    nd1 = np.random.random((1000, 10000))  # use a sufficiently large array

    # Time the two functions, retrieving results and execution times
    res_manual, t_manual = how_long(manual_mean, nd1)
    res_numpy, t_numpy = how_long(numpy_mean, nd1)
    print("Manual: {:.6f} ({:.3f} secs.) vs. NumPy: {:.6f} ({:.3f} secs.)".format(
        res_manual, t_manual, res_numpy, t_numpy))

    # Make sure both give us the same answer (upto some precision )
    assert abs(res_manual - res_numpy) <= 10e-6, "Results aren't equal!"

    # Compute speedup
    speedup = t_manual / t_numpy
    print("NumPy mean is", speedup, "times faster than manual for loops.")

    access_and_modify_array_elem()


if __name__ == "__main__":
    test_run()
