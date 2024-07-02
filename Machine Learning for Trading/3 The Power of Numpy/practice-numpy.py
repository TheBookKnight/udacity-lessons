"""Operations on arrays."""

import numpy as np


def get_min_and_max_along_row_and_column():
    np.random.seed(693)  # seed the random number generator
    a = np.random.randint(0, 10, size=(5, 4))  # 5x4 random integers in [0, 10]
    print("Array:\n", a)

    # Statistics: min, max, mean (across rows, cols, and overall)
    print("Minimum of each column:\n", a.min(axis=0))
    print("Maximum of each row:\n", a.max(axis=1))
    print("Mean of all elements:\n", a.mean())  # leave out the axis arg


def test_run():
    get_min_and_max_along_row_and_column()


if __name__ == "__main__":
    test_run()
