import numpy as np
import matplotlib.pyplot as plt

TPdata = np.loadtxt('tp.txt')
Momenta = np.loadtxt('momenta.txt')
Energy = np.loadtxt('energy.txt')

step = TPdata.shape[0]
t = TPdata[:, 0]
T = TPdata[:, 1]
P = TPdata[:, 3]
taverageT = TPdata[:, 2]
taverageP = TPdata[:, 4]


################################  Temperature #################################

plt.figure(figsize=(7, 5))
plt.plot(t, T, linewidth=0.1, label='Temperature')
plt.plot(t, taverageT, label='Time-averaged Temperature')
plt.xlim([0, 200])
# plt.ylim([85, 115])
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.title('Temperature & Time-averaged Temperature vs t')
plt.legend(loc='upper right')
plt.savefig('./test/T&aT.png')


################################  Temperature #################################

plt.figure(figsize=(7, 5))
plt.plot(t, T, linewidth=0.8, label='Temperature')
plt.plot(t, taverageT, label='Time-averaged Temperature')
plt.xlim([0, 20])
# plt.ylim([85, 115])
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.title('Temperature & Time-averaged Temperature vs t')
plt.legend(loc='lower right')
plt.savefig('./test/T&aT_s.png')

#################################  Pressure ###################################

plt.figure(figsize=(7, 5))
plt.plot(t, P, linewidth=0.1, label='Pressure')
plt.plot(t, taverageP, label='Time-averaged Pressure')
plt.xlim([0, 200])
plt.ylim([2e7, 9e7])
plt.xlabel('Time')
plt.ylabel('Pressure')
plt.title('Pressure & Time-averaged Pressure vs t')
plt.legend(loc='upper right')
plt.savefig('./test/P&aP.png')

##################################  Momenta ###################################

plt.figure(figsize=(7, 5))
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
