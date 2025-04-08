import matplotlib.pyplot as plt
import numpy


x = numpy.linspace(-10, 10, 100)
y = x**2 - 4*x + 4

plt.plot(x, y, color = 'r')
plt.xlabel('x', loc = 'right')
plt.ylabel('f(x)', loc = 'top')
plt.title("Equation x^2 - 4x + 4")
plt.show()