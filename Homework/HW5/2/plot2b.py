import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('2b.txt')

beta = np.log10(data[:, 0])
U = data[:, 1]

plt.figure(figsize=(7, 5))
plt.plot(beta, U, label='U-x, analytical results', linewidth=2)
plt.xlim([-2, 2])
plt.ylim([-0.1, 1.3])
plt.xlabel(r'$log(\beta)$')
# plt.xscale('log')
plt.title(r'$U - \beta$')
plt.legend(loc='upper right')
plt.savefig('2b.png')
