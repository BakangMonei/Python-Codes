import matplotlib.pyplot as plt
import numpy as np

a1 = np.array([1, 2, 3, 4])
a2 = np.array(['Masego', 'Loago', 'Tshephang', 'Olebogeng'])
a3 = np.array([50, 56, 80, 75])

results = np.core.records.fromarrays([a1, a2, a3], names='a, b, c')

for i in range(len(a1)):
    print(results[i])

x = [[1, 0], [1, 1]]
y = [[3, 1], [2, 2]]
print(np.matmul(x, y))

# Explanation
'''
each variable is assigned the another through a place value, The first variables are paired to each other in each sets.
'''