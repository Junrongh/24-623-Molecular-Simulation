import numpy as np
import matplotlib.pyplot as plt

data_00 = np.loadtxt('./data/eta00/energy.txt')
data_01 = np.loadtxt('./data/eta01/energy.txt')
data_05 = np.loadtxt('./data/eta05/energy.txt')
data_10 = np.loadtxt('./data/eta10/energy.txt')
data_50 = np.loadtxt('./data/eta50/energy.txt')
data_100 = np.loadtxt('./data/eta100/energy.txt')

N = 100000

total_energy = np.zeros([N, 7])
kinetic_energy = np.zeros([N, 7])
potential_energy = np.zeros([N, 7])

for i in range(0, N):
    total_energy[i][0] = 0.002 * i
    kinetic_energy[i][0] = 0.002 * i
    potential_energy[i][0] = 0.002 * i

total_energy[:, 1] = data_00[:, 3]
total_energy[:, 2] = data_01[:, 3]
total_energy[:, 3] = data_05[:, 3]
total_energy[:, 4] = data_10[:, 3]
total_energy[:, 5] = data_50[:, 3]
total_energy[:, 6] = data_100[:, 3]

kinetic_energy[:, 1] = data_00[:, 2]
kinetic_energy[:, 2] = data_01[:, 2]
kinetic_energy[:, 3] = data_05[:, 2]
kinetic_energy[:, 4] = data_10[:, 2]
kinetic_energy[:, 5] = data_50[:, 2]
kinetic_energy[:, 6] = data_100[:, 2]

potential_energy[:, 1] = data_00[:, 1]
potential_energy[:, 2] = data_01[:, 1]
potential_energy[:, 3] = data_05[:, 1]
potential_energy[:, 4] = data_10[:, 1]
potential_energy[:, 5] = data_50[:, 1]
potential_energy[:, 6] = data_100[:, 1]

################################  Total Energy ################################

plt.figure(figsize=(15, 5))
plt.plot(total_energy[:,0], total_energy[:,1], linewidth=1, label='$\eta=0.0$')
plt.plot(total_energy[:,0], total_energy[:,2], linewidth=1, label='$\eta=0.1$')
# plt.plot(total_energy[:,0], total_energy[:,3], linewidth=1, label='$\eta=0.5$')
# plt.plot(total_energy[:,0], total_energy[:,4], linewidth=1, label='$\eta=1.0$')
# plt.plot(total_energy[:,0], total_energy[:,5], linewidth=1, label='$\eta=5.0$')
plt.plot(total_energy[:,0], total_energy[:,6], linewidth=1, label='$\eta=10.0$')

plt.xlim([0, 200])

plt.xlabel('Time')
plt.ylabel('Total Energy')
plt.title('Total Energy vs t')
plt.legend(loc='center right')
plt.savefig('./test/total.png')

##############################  Kinetic Energy ################################

plt.figure(figsize=(15, 5))
plt.plot(kinetic_energy[:,0], kinetic_energy[:,1], linewidth=1, label='$\eta=0.0$')
plt.plot(kinetic_energy[:,0], kinetic_energy[:,2], linewidth=1, label='$\eta=0.1$')
# plt.plot(kinetic_energy[:,0], kinetic_energy[:,3], linewidth=1, label='$\eta=0.5$')
# plt.plot(kinetic_energy[:,0], kinetic_energy[:,4], linewidth=1, label='$\eta=1.0$')
# plt.plot(kinetic_energy[:,0], kinetic_energy[:,5], linewidth=1, label='$\eta=5.0$')
plt.plot(kinetic_energy[:,0], kinetic_energy[:,6], linewidth=1, label='$\eta=10.0$')

plt.xlim([0, 200])
plt.xlabel('Time')
plt.ylabel('Kinetic Energy')
plt.title('Kinetic Energy vs t')
plt.legend(loc='center right')
plt.savefig('./test/kinetic.png')


#############################  Potential Energy ###############################

plt.figure(figsize=(15, 5))
plt.plot(potential_energy[:,0], potential_energy[:,1], linewidth=1, label='$\eta=0.0$')
plt.plot(potential_energy[:,0], potential_energy[:,2], linewidth=1, label='$\eta=0.1$')
# plt.plot(potential_energy[:,0], potential_energy[:,3], linewidth=1, label='$\eta=0.5$')
# plt.plot(potential_energy[:,0], potential_energy[:,4], linewidth=1, label='$\eta=1.0$')
# plt.plot(potential_energy[:,0], potential_energy[:,5], linewidth=1, label='$\eta=5.0$')
plt.plot(potential_energy[:,0], potential_energy[:,6], linewidth=1, label='$\eta=10.0$')


plt.xlim([0, 200])

plt.xlabel('Time')
plt.ylabel('Potential Energy')
plt.title('Potential Energy vs t')
plt.legend(loc='center right')
plt.savefig('./test/potential.png')
