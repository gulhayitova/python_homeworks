import numpy as np

resistance = np.array([[10, -2, 3], [-2, 8, -1], [3, -1, 6]])
voltage = np.array([12, -5, 15])
current = np.linalg.solve(resistance, voltage)
print(current)