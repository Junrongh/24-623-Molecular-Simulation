import numpy as np
import matplotlib.pyplot as plt

# t = np.zeros([200, ])
# x = np.zeros([200, ])
# v = np.zeros([200, ])

# for i in range(0, 200):
#     t[i] = i * 0.1
#     x[i] = np.sqrt(2) * np.sin(0.1 * i)
#     v[i] = np.sqrt(2) * np.cos(0.1 * i)


x = np.loadtxt('x_out.txt')
v = np.loadtxt('v_out.txt')


t = np.zeros([20000, ])
u = np.zeros([20000, ])
k = np.zeros([20000, ])
for i in range(0, 20000):
    t[i] = i * 0.001
    u[i] = 0.5 * x[i] * x[i]
    k[i] = 0.5 * v[i] * v[i]

#################################### U - x ####################################

plt.plot(x, u)
# plt.xlim((0, 20))
# plt.ylim((0, 3))
plt.xlabel('x')
plt.ylabel('U')
plt.title('u-x, E = 1')

plt.savefig('q2dux.png')


#################################### x - t ####################################

# plt.plot(t, x)
# plt.xlim((0, 20))
# plt.ylim((0, 3))
# plt.xlabel('t')
# plt.ylabel('x')
# plt.title('x-t')

# plt.show()

#################################### v - t ####################################

# plt.plot(t, v)
# plt.xlim((0, 20))
# plt.ylim((-1.5, 1.5))
# plt.xlabel('t')
# plt.ylabel('v')
# plt.title('v-t')

# plt.show()

#################################### E - t ####################################

# plt.plot(t, u, label='U(x)')
# plt.plot(t, k, label='K(p)')
# plt.plot(t, u + k, label='H =U + K')
# plt.xlim((0, 20))
# plt.ylim((-0.2, 1.4))
# plt.legend(loc='upper right')
# plt.xlabel('t')
# plt.ylabel('Energy')
# plt.title('Energy-t')

# plt.show()

#################################### x - v ####################################

# plt.plot(v, x)
# plt.xlim((-1.5, 1.5))
# plt.ylim((-1.5, 1.5))
# plt.xlabel('v')
# plt.ylabel('x')
# plt.title('v-x')

# plt.show()


