import numpy as np
import matplotlib.pyplot as plt

prdata = np.loadtxt('pr.txt')
N = prdata.shape[0]

################################  Temperature #################################

plt.figure(figsize=(7, 5))
for i in range(0,N):
    plt.scatter(prdata[i][1], prdata[i][3], color='red')

plt.plot(prdata[:,1], prdata[:,3], c='blue')

plt.xlabel('Density')
plt.ylabel('Pressure')
plt.title('Pressure - Density')
plt.grid(True, linestyle = "-", color = "gray", linewidth = "0.1")  
plt.savefig('./test/pr.png')

