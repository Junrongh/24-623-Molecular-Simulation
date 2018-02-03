import numpy as np
import matplotlib.pyplot as plt

data2 = np.loadtxt('energy2.txt')
data3 = np.loadtxt('energy3.txt')
data4 = np.loadtxt('energy4.txt')
data5 = np.loadtxt('energy5.txt')
data6 = np.loadtxt('energy6.txt')
data7 = np.loadtxt('energy7.txt')
data8 = np.loadtxt('energy8.txt')
data9 = np.loadtxt('energy9.txt')

################################# For 2-9 ######################################

plt.plot(data2[:, 0], data2[:, 3] / 2, label='N=2')
plt.plot(data3[:, 0], data3[:, 3] / 3, label='N=3')
plt.plot(data4[:, 0], data4[:, 3] / 4, label='N=4')
plt.plot(data5[:, 0], data5[:, 3] / 5, label='N=5')
plt.plot(data6[:, 0], data6[:, 3] / 6, label='N=6')
plt.plot(data7[:, 0], data7[:, 3] / 7, label='N=7')
plt.plot(data8[:, 0], data8[:, 3] / 8, label='N=8')
plt.plot(data9[:, 0], data9[:, 3] / 9, label='N=9')


plt.xlim((0, 16))
plt.xlabel('t')
plt.ylabel('Energy')
plt.title('Energy - t')
plt.legend(loc='center left')
plt.show()

N = [2, 3, 4, 5, 6, 7, 8, 9]
Data=[data2, data3, data4, data5, data6, data7, data8, data9]
Labels=['N=2', 'N=3', 'N=4', 'N=5', 'N=6', 'N=7', 'N=8', 'N=9']
for i in range(0, 8):
    plt.scatter(N[i], np.min(Data[i])/N[i], label=Labels[i])
plt.xlabel('Number of atoms')
plt.ylabel('Energy per atom')
plt.legend(loc='upper right')
plt.show()

################################# For fcc ######################################

# plt.plot(data[:, 0], data[:, 1], label='Potential')
# plt.plot(data[:, 0], data[:, 2], label='Kinetic')
# plt.plot(data[:, 0], data[:, 4], label='Total Energy')

# plt.xlim((0, 16))
# plt.xlabel('t')
# plt.ylabel('Energy')
# plt.title('Energy - t')
# plt.legend(loc='center left')
# plt.show()
