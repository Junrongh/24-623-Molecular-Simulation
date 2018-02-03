import numpy as np
import math
import matplotlib.pyplot as plt

data = np.loadtxt('result.txt')

(N, M) = data.shape
print(N, M)
x_res = []
res = []

for i in range(0, N):
    res.append(np.mean(data[i][1:]))
    x_res.append(data[i][0])
    print res[i]


N = 4000
x = np.zeros([N, ])
U = np.zeros([N, ])
for i in range(0, N):
    x[i] = math.pow(10, (0.001 * i - 2))
    U[i] = math.sqrt(2) / math.pi * math.exp(-x[i])

plt.plot(x, U, label=r'$k^{TST,\ Analytical}_{A\to B}$')
plt.scatter(x_res, res, label=r'$k^{TST,\ MC}_{A\to B}$')
plt.xlabel(r'$\beta$')
plt.ylabel(r'$k^{TST}_{A\to B}$')
plt.legend(loc="upper right")
plt.title(r'$k^{TST}_{A\to B} - \beta$')

plt.savefig('2b.png')
