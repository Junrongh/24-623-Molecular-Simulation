import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('2b.txt')
evaldata = np.loadtxt('2c_points.txt')

beta = np.log(data[:, 0])
U = data[:, 1]

plt.figure(figsize=(7, 5))
plt.plot(beta, U, label='U-x, analytical results', linewidth=2)
plt.scatter(np.log(evaldata[:, 0]), evaldata[:, 1], label='MC results', s=30, c='red')
plt.xlim([-5, 5])
plt.ylim([-0.1, 1.3])
plt.xlabel(r'$log(\beta)$')
# plt.xscale('log')
plt.title(r'$U - \beta$')
plt.legend(loc='upper right')
plt.savefig('2c.png')
