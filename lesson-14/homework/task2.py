import numpy as np

def power(n, p):
    return n**p
vector_p = np.vectorize(power)

arr1 = np.array([2, 3, 4, 5])
arr2 = np.array([1, 2, 3, 4])
powered = vector_p(arr1, arr2)
print(powered)