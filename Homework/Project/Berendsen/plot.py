import numpy as np
import matplotlib.pyplot as plt

TPdata1 = np.loadtxt('./tau05/tp.txt')
TPdata2 = np.loadtxt('./tau1/tp.txt')
TPdata3 = np.loadtxt('./tau5/tp.txt')


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
plt.plot(t, taverageT1, label=r'$\tau=0.5$')
plt.plot(t, taverageT2, label=r'$\tau=1.0$')
plt.plot(t, taverageT3, label=r'$\tau=5.0$')
plt.xlim([0, 200])
# plt.ylim([85, 115])
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.title('Time-averaged Temperature vs t')
plt.legend(loc='lower right')
plt.savefig('T&aT.png')


################################  Temperature #################################

plt.figure(figsize=(7, 5))
plt.plot(t, taverageT1, label=r'$\tau=0.5$')
plt.plot(t, taverageT2, label=r'$\tau=1.0$')
plt.plot(t, taverageT3, label=r'$\tau=5.0$')
plt.xlim([0, 50])
# plt.ylim([80, 105])
plt.xlabel('Time')
plt.ylabel('Temperature')
plt.title('Time-averaged Temperature vs t')
plt.legend(loc='lower right')
plt.savefig('T&aT_s.png')

