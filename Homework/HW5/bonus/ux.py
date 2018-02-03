import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('output.txt')

step = data[:, 0]
U = data[:, 1]
x = data[:, 2]
x2 = data[:, 3]

plt.figure(figsize=(7, 5))
plt.scatter(x, U, label='U-x', s=2)
# plt.xlim([-5, 5])
# plt.ylim([-1, 1])
plt.xlabel('x')
plt.title(r'$U-x, \beta=1$')
plt.legend(loc='upper right')
plt.savefig('Uxbeta_10.png')

