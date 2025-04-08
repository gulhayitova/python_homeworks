import numpy as np
import matplotlib.pyplot as plt
x = np.linspace(-10, 10, 100)
e = np.e

top_l = x**3
np.where # because log(x+1) is not continuous at x<=-1
top_r = np.sin(x)
bottom_l = e**x
bottom_r = np.log10(x+1)

plt.figure(figsize=(10, 8)) # make it bigger
plt.suptitle('Functions', fontsize=16) # big title

plt.subplot(2, 2, 1)
plt.plot(x, top_l, color='red', label='y=x^3')
plt.xlabel('x')
plt.ylabel('y')
plt.legend()

plt.subplot(2, 2, 2)
plt.plot(x, top_r, color='blue', label='y=sin(x)')
plt.xlabel('x')
plt.ylabel('y')
plt.legend(loc='upper left')

plt.subplot(2, 2, 3)
plt.plot(x, bottom_l, color='green', label='y=e^x')
plt.legend()
plt.xlabel('x')
plt.ylabel('y')

plt.subplot(2, 2, 4)
plt.plot(x, bottom_r, color='purple', label='y=log(x+1)')
plt.legend(loc='upper left')
plt.xlabel('x')
plt.ylabel('y')
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.show()