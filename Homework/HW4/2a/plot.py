import numpy as np
import matplotlib.pyplot as plt

TPdata = np.loadtxt('./output/tp.txt')
Momenta = np.loadtxt('./output/momenta.txt')
Energy = np.loadtxt('./output/energy.txt')

step = TPdata.shape[0]
t = TPdata[:, 0]
T = TPdata[:, 1]
P = TPdata[:, 2]
E = Energy[:, 3]
taverageT = np.zeros([step, ])
taverageP = np.zeros([step, ])
taverageE = np.zeros([step, ])
tvarianceE = np.zeros([step, ])
taverageT[0] = T[0]
taverageP[0] = P[0]
taverageE[0] = E[0]
tvarianceE[0] = 0
for i in range(1, step):
    taverageT[i] = np.average(T[0:i])
    taverageP[i] = np.average(P[0:i])
    taverageE[i] = np.average(E[0:i])
    tvarianceE[i] = np.var(E[0:i])


################################  Temperature #################################

plt.figure(figsize=(15, 5))
plt.plot(t, T, linewidth=0.1, label='Temperature')
plt.plot(t, taverageT, label='Time-averaged Temperature')
plt.xlim([0, 200])
plt.ylim([80, 120])
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.title('Temperature & Time-averaged Temperature vs t')
plt.legend(loc='upper right')
plt.savefig('./graph/T&aT.png')

#################################  Pressure ###################################

plt.figure(figsize=(15, 5))
plt.plot(t, P, linewidth=0.1, label='Pressure')
plt.plot(t, taverageP, label='Time-averaged Pressure')
plt.xlim([0, 200])

plt.xlabel('Time')
plt.ylabel('Pressure')
plt.title('Pressure & Time-averaged Pressure vs t')
plt.legend(loc='upper right')
plt.savefig('./graph/P&aP.png')

##################################  Momenta ###################################

plt.figure(figsize=(15, 5))
plt.plot(Momenta[:, 0], Momenta[:, 1], linewidth=0.7, label='x')
plt.plot(Momenta[:, 0], Momenta[:, 2], linewidth=0.7, label='y')
plt.plot(Momenta[:, 0], Momenta[:, 3], linewidth=0.7, label='y')
plt.xlim([0, 200])
plt.ylim([-3e-12, 3e-12])
plt.xlabel('Time')
plt.ylabel('xyz-Momenta')
plt.title('Momenta vs t')
plt.legend(loc='upper right')
plt.savefig('./graph/Momenta.png')

##################################  Energy ####################################

plt.figure(figsize=(15, 5))
plt.plot(Energy[:, 0], Energy[:, 1], linewidth=0.7, label='Potential')
plt.plot(Energy[:, 0], Energy[:, 2], linewidth=0.7, label='Kinetic')
plt.plot(Energy[:, 0], Energy[:, 3], linewidth=0.7, label='Total Energy')
plt.xlim([0, 200])
plt.xlabel('Time')
plt.ylabel('Energy')
plt.title('Energy vs t')
plt.legend(loc='center right')
plt.savefig('./graph/Energy.png')

###########################  Energy Conservation ##############################

plt.figure(figsize=(15, 5))
plt.plot(t, E, linewidth=0.1, label='Total Energy')
plt.plot(t, taverageE, label='Time-averaged Total Energy')
plt.xlim([0, 200])
plt.ylim([-600, -450])
plt.xlabel('Time')
plt.ylabel('Total Energy')
plt.title('Total energy & Time-averaged Total energy vs t')
plt.legend(loc='upper right')
plt.savefig('./graph/E&aE.png')

plt.figure(figsize=(15, 5))
plt.plot(t, tvarianceE, label='Energy Variance')
plt.xlim([0, 200])
plt.ylim([0, 10000])
plt.xlabel('Time')
plt.ylabel('Energy variance')
plt.title('Energy variance vs t')
plt.legend(loc='upper right')
plt.savefig('./graph/Variance.png')
