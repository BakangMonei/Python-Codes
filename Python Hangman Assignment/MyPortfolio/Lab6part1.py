# ACTIVITY 1
import matplotlib.pyplot as plt
import numpy as np

x = np.array([2, 4, 6, 8])
print('Original array: ')
print(x)
print('Test if none of the elements is 0')
print(np.all(x))
x = np.array([0, 2, 4, 6, 8])
print(x)
print('Test if none of the elements is 0')
print(np.all(x))

# checking if elements are numbers or not
b = np.array([100, 90, np.nan, np.inf, 1.02])
print(b)
print(np.isfinite(b))

# check if a number is scalar type or not
c = np.array([1 + 1j, 1 + 0j, 4.5, 3, 2, 2j])
print('The original array is: ', c)
print(np.iscomplex(c))
print(np.isreal(c))
print(np.isscalar(3.1))
print(np.isscalar([3.1]))
# A program that creates 3*4 filled with values from 50 to 61
m = np.arrange(50, 62).reshape((3, 4))
print(m)

# ACTIVITY 2
'''
To Be attended
'''

# ACTIVITY 3
'''
The code will not run because the declared variables are not available
'''