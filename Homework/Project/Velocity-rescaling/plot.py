import numpy as np
import matplotlib.pyplot as plt

TPdata1 = np.loadtxt('./1step/tp.txt')
TPdata2 = np.loadtxt('./10step/tp.txt')
TPdata3 = np.loadtxt('./100step/tp.txt')


step = TPdata1.shape[0]
t = TPdata1[:, 0]
T1 = TPdata1[:, 1]
P1 = TPdata1[:, 3]
taverageT1 = TPdata1[:, 2]
taverageP1 = TPdata1[:, 4]
T2 = TPdata2[:, 1]
P2 = TPdata2[:, 3]
taverageT2 = TPdata2[:, 2]
taverageP2 = TPdata2[:, 4]
T3 = TPdata3[:, 1]
P3 = TPdata3[:, 3]
taverageT3 = TPdata3[:, 2]
taverageP3 = TPdata3[:, 4]


################################  Temperature #################################

plt.figure(figsize=(7, 5))
plt.plot(t, taverageT1, label='1step')
plt.plot(t, taverageT2, label='10step')
plt.plot(t, taverageT3, label='100step')
plt.xlim([0, 200])
# plt.ylim([85, 115])
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.title('Time-averaged Temperature vs t')
plt.legend(loc='lower right')
plt.savefig('T&aT.png')


################################  Temperature #################################

plt.figure(figsize=(7, 5))
plt.plot(t, taverageT1, label='1step')
plt.plot(t, taverageT2, label='10step')
plt.plot(t, taverageT3, label='100step')
plt.xlim([0, 1])
plt.ylim([80, 105])
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.title('Time-averaged Temperature vs t')
plt.legend(loc='lower right')
plt.savefig('T&aT_s.png')

