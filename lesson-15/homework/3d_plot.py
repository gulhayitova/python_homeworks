import numpy as np
import matplotlib.pyplot as plt

x_data = np.arange(-5, 5, 0.1)
y_data = np.arange(-5, 5, 0.1)
x, y = np.meshgrid(x_data, y_data)
z = np.cos(x*x+y*y)

fig = plt.figure()
ax = plt.axes(projection='3d')
surf = ax.plot_surface(x, y, z, cmap='winter', edgecolor='none')
ax.set_title("3D Surface Plot of cos(x² + y²)")
fig.colorbar(surf, shrink=0.5, aspect=10)
plt.show()