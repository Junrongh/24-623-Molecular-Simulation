import numpy as np
import math
import matplotlib.pyplot as plt

data = np.loadtxt('result.txt')

(N, M) = data.shape
print(N, M)
x_res = []
res = []

for i in range(0, N-1):
    res.append(np.mean(data[i][1:]))
    x_res.append(data[i][0])
    print res[i]

for i in range(0, N-1):
    x_res[i]=math.log10(x_res[i])
    res[i]=math.log10(res[i])


N = 4000
x = np.zeros([N, ])
U = np.zeros([N, ])
for i in range(0, N):
    x[i] = math.pow(10, (0.001 * i - 2))
    U[i] = math.sqrt(2) / math.pi * math.exp(-x[i])
    x[i] = math.log10(x[i])
    U[i] = math.log10(U[i])

plt.plot(x, U, label=r'$k^{TST,\ Analytical}_{A\to B}$')
plt.scatter(x_res, res, label=r'$k^{TST,\ MC}_{A\to B}$')
plt.xlabel(r'$log(\beta)$')
# plt.xlim([-2, 2])
# plt.ylim([-45, 1])
plt.ylabel(r'$log(k^{TST}_{A\to B})$')
plt.legend(loc="lower left")
plt.title(r'$log(k^{TST}_{A\to B}) - log(\beta)$')

plt.savefig('2b_log.png')
