import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('energy.txt')

plt.plot(data[:, 0], data[:, 1], label='Potential')
plt.plot(data[:, 0], data[:, 2], label='Kinetic')
plt.plot(data[:, 0], data[:, 3], label='Total energy')
plt.xlim((0, 2))

plt.xlabel('t')
plt.ylabel('Energy')
plt.title('U, K, E - t')
plt.legend(loc='center right')
plt.show()


mon = np.loadtxt('momenta.txt')
plt.plot(data[:, 0], mon[:, 0], label='x-direction')
plt.plot(data[:, 0], mon[:, 1], label='y-direction')
plt.plot(data[:, 0], mon[:, 2], label='z-direction')

plt.xlabel('t')
plt.ylabel('Momenta in xyz direction')
plt.ylim([-1e-13, 1e-13])
plt.title('Momenta - t')
plt.legend(loc='upper right')
plt.show()
