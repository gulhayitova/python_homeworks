import numpy
import matplotlib.pyplot as plt

pi = numpy.pi
x = numpy.linspace(0, 2*pi, 50)
y1 = numpy.sin(x)
y2 = numpy.cos(x)

plt.subplot(2, 2, 1)
plt.plot(x, y1, linestyle='--', color='blue', label='sin(x)')
# plt.subplot(2, 2, 2)
plt.plot(x, y2, linestyle='--', color='red', label='cos(x)')
plt.tight_layout()
plt.legend(loc='upper center')
# plt.legend(loc='upper right', title='Legend Title', shadow=True, fancybox=True)
# plt.legend(handlelength=4)
# plt.legend(framealpha=0.5)  # 0 = totally see-through, 1 = solid

plt.show()