import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('result.txt')

STEP = data[:, 0]
N = data.shape[0]
M = data.shape[1]

mean = []
var = []

fig=plt.figure(figsize=(10, 5))
ax1 = fig.add_subplot(111)
for i in range(N):
    for j in range(1, M):
        ax1.scatter(STEP[i], data[i][j], c='blue', s=1)
    mean.append(np.mean(data[i][1:]))
    var.append(np.var(data[i][1:]))
    
ax1.scatter(STEP, mean, c='red', s=10)
ax1.plot(STEP, mean, color='orange', label='mean')
ax1.legend(loc='upper left')

ax2 = ax1.twinx()
ax2.scatter(STEP, var, c='red', s=10)
ax2.plot(STEP, var, label='variance')
plt.xlim([0, 1050000])
plt.xlabel(r'$\STEP$')
ax1.set_ylabel(r'$k^{TST}_{A\to B}$')
ax2.set_ylabel('variance')
ax2.legend(loc='upper right')
ax2.set_ylim([0, 3E-4])
plt.title(r'$k^{TST}_{A\to B}\ vs.\ STEP,\ trial_{max}=1.2,\ \epsilon=0.05,\ \beta=0.1$')


plt.savefig('result.png')
