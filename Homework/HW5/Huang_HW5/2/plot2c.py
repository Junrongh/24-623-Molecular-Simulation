import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('2c.txt')

N = data.shape[0]
step = data[:, 0]
U = data[:, 1]
avgU = data[:, 2]

plt.figure(figsize=(7, 5))
plt.plot(step, avgU, label='avgU-x', linewidth=1)
plt.xlim([0, N])
plt.ylim([-1E-8, 1E-8])
plt.xlabel('step')
plt.title(r'U - step, $\beta = 100$')
plt.legend(loc='upper right')
plt.savefig('2c_100.png')


# varanceU = np.zeros([N, ])
# varanceU[0] = 0
# for i in range(1, N):
#     varanceU[i] = np.var(U[0:i])
#     print (i)
# plt.figure(figsize=(7, 5))
# plt.plot(step, varanceU, label='avgU-x', linewidth=1)
# plt.xlim([0, N])
# plt.xlabel('step')
# plt.title(r'U - step, $\beta = 0.01$')
# plt.legend(loc='upper right')
# plt.savefig('2c_001var.png')