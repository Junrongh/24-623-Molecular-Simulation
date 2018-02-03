import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('result.txt')

epsilon = data[:, 0]
N = data.shape[0]
M = data.shape[1]
mean = []
var = []

fig=plt.figure(figsize=(10, 5))
ax1 = fig.add_subplot(111)
for i in range(N):
    for j in range(1, M):
        ax1.scatter(epsilon[i], data[i][j], c='blue', s=3)
    mean.append(np.mean(data[i][1:]))
    var.append(np.var(data[i][1:]))
ax1.scatter(epsilon, mean, c='red', s=15)
ax1.plot(epsilon, mean, color='orange', label='mean')
ax1.legend(loc='upper left')

ax2 = ax1.twinx()
ax2.scatter(epsilon, var, c='red', s=15)
ax2.plot(epsilon, var, label='variance')
plt.xlim([0.00, 0.20])
plt.xlabel(r'$\epsilon$')
ax1.set_ylabel(r'$k^{TST}_{A\to B}$')
ax2.set_ylabel('variance')
ax2.legend(loc='upper right')
ax2.set_ylim([0, 5E-3])
plt.title(r'$k^{TST}_{A\to B}\ vs.\ \epsilon,\ trial_{max}=1.0,\ \beta=0.1$')


plt.savefig('result.png')
