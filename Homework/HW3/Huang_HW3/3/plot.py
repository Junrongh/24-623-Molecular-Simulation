import numpy as np
import matplotlib.pyplot as plt

TPdata = np.loadtxt('tp.txt')
Momenta = np.loadtxt('momenta.txt')
Energy = np.loadtxt('energy.txt')

step = TPdata.shape[0]
t = TPdata[:, 0]
T = TPdata[:, 1]
P = TPdata[:, 2]
taverageT = np.zeros([step, ])
taverageP = np.zeros([step, ])
taverageT[0] = T[0]
taverageP[0] = P[0]
for i in range(1, step):
    taverageT[i] = np.average(T[0:i])
    taverageP[i] = np.average(P[0:i])

print taverageT[step - 1]
print taverageP[step - 1]

################################  Temperature #################################

plt.figure(figsize=(7, 5))
plt.plot(t, T, linewidth=0.1, label='Temperature')
plt.plot(t, taverageT, label='Time-averaged Temperature')
plt.xlim([0, 200])
plt.ylim([85, 115])
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.title('Temperature & Time-averaged Temperature vs t')
plt.legend(loc='upper right')
plt.savefig('./test/T&aT.png')

#################################  Pressure ###################################

plt.figure(figsize=(7, 5))
plt.plot(t, P, linewidth=0.1, label='Pressure')
plt.plot(t, taverageP, label='Time-averaged Pressure')
plt.xlim([0, 200])
# plt.ylim([-2e7, 7e7])
plt.xlabel('Time')
plt.ylabel('Pressure')
plt.title('Pressure & Time-averaged Pressure vs t')
plt.legend(loc='upper right')
plt.savefig('./test/P&aP.png')

##################################  Momenta ###################################

plt.figure(figsize=(9, 5))
plt.plot(Momenta[:, 0], Momenta[:, 1], linewidth=0.7, label='x')
plt.plot(Momenta[:, 0], Momenta[:, 2], linewidth=0.7, label='y')
plt.plot(Momenta[:, 0], Momenta[:, 3], linewidth=0.7, label='y')
plt.xlim([0, 200])
plt.ylim([-3e-12, 3e-12])
plt.xlabel('Time')
plt.ylabel('xyz-Momenta')
plt.title('Momenta vs t')
plt.legend(loc='upper right')
plt.savefig('./test/Momenta.png')

##################################  Energy ####################################

plt.figure(figsize=(7, 5))
plt.plot(Energy[:, 0], Energy[:, 1], linewidth=0.7, label='Potential')
plt.plot(Energy[:, 0], Energy[:, 2], linewidth=0.7, label='Kinetic')
plt.plot(Energy[:, 0], Energy[:, 3], linewidth=0.7, label='Total Energy')
plt.xlim([0, 200])
plt.xlabel('Time')
plt.ylabel('Energy')
plt.title('Energy vs t')
plt.legend(loc='center right')
plt.savefig('./test/Energy.png')
