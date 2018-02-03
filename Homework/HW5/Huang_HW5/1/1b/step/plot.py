import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('trialout.txt')

step = data[:, 0]
U = data[:, 1]
x = data[:, 2]
x2 = data[:, 3]

plt.figure(figsize=(7, 5))
plt.plot(step, U, label='<U>')
plt.plot(step, x, label='<x>')
plt.plot(step, x2, label='<x2>')
plt.xlim([0, 1000000])
plt.ylim([-5, 15])
plt.xlabel('Maximum Step Size')
plt.title(r'$<U>, <x>, <x^2>, \beta=0.1$')
plt.legend(loc='upper right')
plt.savefig('1_beta_01.png')
