import matplotlib.pyplot as plt
import numpy as np

products = ['Product A', 'Product B', 'Product C', 'Product D', 'Product E']
quantity = [200, 150, 250, 175, 225]

plt.bar(products, quantity, color=['#ffb3ba', '#ffdfba', '#ffffba', '#baffc9', '#bae1ff'])
plt.xlabel('Products')
plt.ylabel('Quantity')
plt.show()