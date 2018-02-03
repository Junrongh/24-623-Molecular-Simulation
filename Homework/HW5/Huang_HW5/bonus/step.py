import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('avgoutput.txt')

step = range(0, data.shape[0])
U = data[:, 0]
x = data[:, 1]
x2 = data[:, 2]

plt.figure(figsize=(7, 5))
plt.plot(step, U, label='<U>')
plt.plot(step, x, label='<x>')
plt.plot(step, x2, label='<x2>')
plt.xlim([0, 1000000])
plt.ylim([-0.2, 1])
plt.xlabel('Maximum Trial Move')
plt.title(r'$<U>, <x>, <x^2>, \beta=10$')
plt.legend(loc='upper right')
plt.savefig('stepbeta_10.png')
