import numpy as np
import matplotlib.pyplot as plt

n = np.random.normal(0, 1, 1000)

plt.hist(n, 30, alpha=0.5, color='blue', edgecolor='pink')
plt.title('Histogram', color='hotpink')
plt.ylabel('frequency')
plt.xlabel('values')
plt.show()