import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('trialout.txt')

trial = data[:, 0]
U = data[:, 1]
x = data[:, 2]
x2 = data[:, 3]

plt.figure(figsize=(7, 5))
plt.plot(trial, U, label='<U>')
plt.plot(trial, x, label='<x>')
plt.plot(trial, x2, label='<x2>')
plt.xlim([0, 20])
plt.ylim([-1, 1])
plt.xlabel('Maximum Trial Move')
plt.title(r'$<U>, <x>, <x^2>, \beta=10$')
plt.legend(loc='upper right')
plt.savefig('2_beta_10.png')
