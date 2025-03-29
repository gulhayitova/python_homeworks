import numpy as np

coeff = np.array([[4, 5, 6], [3, -1, 1], [2, 1, -2]])
output = np.array([7, 4, 5])
solution = np.linalg.solve(coeff, output)

print(solution)