import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('trialout.txt')

initial = data[:, 0]
U = data[:, 1]
x = data[:, 2]
x2 = data[:, 3]

plt.figure(figsize=(7, 5))
plt.plot(initial, U, label='<U>')
plt.plot(initial, x, label='<x>')
plt.plot(initial, x2, label='<x2>')
plt.xlim([-20, 20])
# plt.ylim([-0.2, 1])
plt.xlabel('Initial Condition')
plt.title(r'$<U>, <x>, <x^2>, \beta=0.1$')
plt.legend(loc='upper right')
plt.savefig('2_beta_01.png')
