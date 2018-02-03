import numpy as np
import matplotlib.pyplot as plt

N=2000
x=np.zeros([N,])
U=np.zeros([N,])
h=np.zeros([N/2,])
for i in range(0, N):
    x[i]=0.002*i-2
    U[i]=x[i]*x[i]*x[i]*x[i]-2*x[i]*x[i]+1
for i in range(0, N/2):
    h[i]=4*(x[i]+1)*(x[i]+1)

plt.plot(x, U, label='U')
plt.plot(x[:N/2], h, label='harmonic approximation')
plt.xlim([-1.5, 1.5])
plt.ylim([0, 1.6])
plt.xlabel('x')
plt.ylabel('U')
plt.legend(loc="upper right")
plt.title('U(x) & harmonic approximation')

plt.savefig('1a.png')