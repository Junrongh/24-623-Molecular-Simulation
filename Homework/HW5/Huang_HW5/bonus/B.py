import numpy as np
import math
import matplotlib.pyplot as plt

x = np.zeros([2000, ])
b = np.zeros([2000, ])
for i in range(0, 2000):
    x[i] = -10 + i * 0.01
    b[i] = math.exp(-x[i] / 2) / (math.exp(-x[i] / 2) + math.exp(x[i] / 2))

plt.figure(figsize=(7, 5))
plt.plot(x, b, color='black')
plt.xlabel(r'$\Delta U = U_n - U_o$')
plt.ylabel(r'$B$')
plt.savefig('B_kawasaki')

x = np.zeros([1000, ])
b = np.zeros([1000, ])
xn = np.zeros([1000, ])
bn = np.ones([1000, ])
for i in range(0, 1000):
    x[i] = i * 0.01
    xn[i] = i * (-0.01)
    b[i] = math.exp(-x[i])

plt.figure(figsize=(7, 5))
plt.plot(x, b, color='black')
plt.plot(xn, bn, color='black')
plt.xlabel(r'$\Delta U = U_n - U_o$')
plt.ylabel(r'$B$')
plt.savefig('B')

