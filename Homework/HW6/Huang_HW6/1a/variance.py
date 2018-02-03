import numpy as np
import matplotlib.pyplot as plt

energy = np.loadtxt('energy.txt')

N = 1000000
idx = range(0, N, 1)
E = []
for i in idx:
    E.append(energy[i, 2])

E_var = []
idx = range(10, N, 10)
for i in idx:
    E_var.append(np.var(E[:i]))
    print i


plt.figure(figsize=(7, 5))
plt.plot(idx, E_var, label='Variance')
plt.xlim([0, 1000000])
plt.legend(loc='upper left')
plt.title('Energy Variance - STEP, TRIALMAX=0.1')
plt.xlabel('STEP')
plt.ylabel('Variance')
plt.savefig('var.png')
