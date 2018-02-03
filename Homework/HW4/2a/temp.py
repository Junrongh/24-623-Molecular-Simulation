import numpy as np
import matplotlib.pyplot as plt

TPdata = np.loadtxt('./output/tp.txt')
Momenta = np.loadtxt('./output/momenta.txt')
Energy = np.loadtxt('./output/energy.txt')

step = TPdata.shape[0]
t = TPdata[:, 0]

P = TPdata[:, 2]
E = Energy[:, 1]

taverageP = np.zeros([step, ])
taverageE = np.zeros([step, ])

taverageP[0] = P[0]
taverageE[0] = E[0]


for i in range(1, step):

    taverageP[i] = np.average(P[0:i])
    taverageE[i] = np.average(E[0:i])



plt.figure(figsize=(7, 5))
plt.plot(t, P, linewidth=0.1, label='Pressure')
plt.plot(t, taverageP, label='Time-averaged Pressure')
plt.xlim([0, 200])
plt.xlabel('Time')
plt.ylabel('Pressure')
plt.title('Pressure & Time-averaged Pressure vs t')
plt.legend(loc='upper right')
plt.savefig('./graph/P&aP_68.png')


plt.figure(figsize=(7, 5))
plt.plot(Energy[:, 0], Energy[:, 1], linewidth=0.7, label='Potential')
plt.plot(Energy[:, 0], Energy[:, 2], linewidth=0.7, label='Kinetic')
plt.plot(Energy[:, 0], Energy[:, 3], linewidth=0.7, label='Total Energy')
plt.plot(Energy[:, 0], taverageE, linewidth=1, label='Averaged Potential')
plt.xlim([0, 200])
plt.xlabel('Time')
plt.ylabel('Energy')
plt.title('Energy vs t')
plt.legend(loc='center right')
plt.savefig('./graph/Energy_68.png')

print E[step-1]
print P[step-1]