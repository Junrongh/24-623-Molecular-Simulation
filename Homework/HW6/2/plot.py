import numpy as np
import matplotlib.pyplot as plt

tp=np.loadtxt('p.txt')
energy=np.loadtxt('energy.txt')

plt.figure(figsize=(7, 5))
plt.plot(tp[:, 0], tp[:, 1], linewidth=0.1, label='Pressure')
plt.plot(tp[:, 0], tp[:, 2], label='Averaged Pressure')
plt.xlim([0,1000000])
plt.legend(loc='upper left')
plt.title('Pressure - STEP, TRIALMAX=1')
plt.xlabel('STEP')
plt.ylabel('Pressure')
plt.savefig('P.png')

plt.figure(figsize=(7, 5))
plt.plot(energy[:, 0], energy[:, 1], linewidth=0.1, label='Potential')
plt.plot(energy[:, 0], energy[:, 2], label='Averaged Potential')
plt.xlim([0,1000000])
plt.legend(loc='upper left')
plt.title('Potential - STEP, TRIALMAX=1')
plt.xlabel('STEP')
plt.ylabel('Potential')
plt.savefig('U.png')

