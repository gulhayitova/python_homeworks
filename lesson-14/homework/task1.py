import numpy as np

def F_to_C(arr):
    return (arr - 32) * 5 / 9
vectorized_func = np.vectorize(F_to_C)

temp_F = np.array([32, 68, 100, 212, 77])
temp_C = vectorized_func(temp_F)
print(temp_C)