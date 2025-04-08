import numpy as np
import matplotlib.pyplot as plt

x = np.random.uniform(0, 10, size=100)
y = np.random.uniform(0, 10, size=100)
colors = np.random.randint(100, size=100)

plt.scatter(x, y, c=colors, cmap='cool', alpha=0.9)
plt.xlabel('x')
plt.ylabel('y')
plt.title("Scatter plot", color='purple')
plt.grid()
plt.show()