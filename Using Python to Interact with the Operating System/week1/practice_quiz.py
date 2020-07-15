
''''Can you identify the error in the following code?''''

#!/usr/bin/env python3''' Shebang '''

import numpy as np

def numpyArray():
    x = np.array([[1, 2, 3], [4, 5, 6]], np.int32)
    y = numpy.array([[3, 6, 2], [9, 12, 8]], np.int32)
    return x*y
print(numpyArray())


""" The y variable is not calling the numpy module properly"""
