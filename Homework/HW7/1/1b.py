import numpy as np
import math
import matplotlib.pyplot as plt

N = 4000
x = np.zeros([N, ])
U = np.zeros([N, ])
for i in range(0, N):
    x[i] = math.pow(10, (0.001 * i - 2))
    U[i] = math.sqrt(2) / math.pi * math.exp(-x[i])
    x[i] = math.log10(x[i])
    U[i] = math.log10(U[i])

plt.plot(x, U, label=r'$k^{TST}_{A\to B}$')
plt.xlabel(r'$log(\beta)$')
plt.xlim([-2, 2])
plt.ylim([-45, 1])
plt.ylabel(r'$log(k^{TST}_{A\to B})$')
plt.legend(loc="upper right")
plt.title(r'$log(k^{TST}_{A\to B}) - log(\beta)$')

plt.savefig('1b.png')
