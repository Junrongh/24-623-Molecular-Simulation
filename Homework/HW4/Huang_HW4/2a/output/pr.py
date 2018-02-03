import numpy as np
import matplotlib.pyplot as plt

pr3data = np.loadtxt('hw3pr.txt')
pr4data = np.loadtxt('hw4pr.txt')
N = pr3data.shape[0]

################################  Temperature #################################

plt.figure(figsize=(7, 5))
for i in range(0,N):
    plt.scatter(pr3data[i][1], pr3data[i][3], color='red')
plt.plot(pr3data[:,1], pr3data[:,3], c='blue', label='HW3')

for i in range(0,N):
    plt.scatter(pr4data[i][1], pr4data[i][2], color='red')
plt.plot(pr4data[:,1], pr4data[:,2], c='yellow', label='HW4')

plt.xlabel('Density')
plt.ylabel('Pressure')
plt.title('Pressure - Density')
plt.grid(True, linestyle = "-", color = "gray", linewidth = "0.1") 
plt.legend(loc='upper left') 
plt.savefig('./test/pr.png')

