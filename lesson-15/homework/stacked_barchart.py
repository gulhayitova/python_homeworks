import matplotlib.pyplot as plt
import numpy as np

A_product = np.array([50, 60, 45, 45])
B_product = np.array([30, 40, 45, 35])
C_product = np.array([65, 75, 55, 55])
D_product = np.array([35, 60, 40, 40])
E_product = np.array([50, 60, 70, 45])
periods = ['T1', 'T2', 'T3', 'T4']

plt.bar(periods, A_product, label='Product A', color='#a8e6cf')
plt.bar(periods, A_product, bottom=A_product, label='Product B', color='#dcedc1')
plt.bar(periods, C_product, bottom=A_product+B_product, label='Product C', color='#ffd3b6')
plt.bar(periods, D_product, bottom=A_product+B_product+C_product, label='Product D', color='#ffaaa5')
plt.bar(periods, E_product, bottom=A_product+B_product+C_product+D_product, label='Product E', color='#ff8b94')
plt.legend(bbox_to_anchor=(1, 1))
plt.xlabel('Time periods')
plt.ylabel('Quantities')
plt.show()