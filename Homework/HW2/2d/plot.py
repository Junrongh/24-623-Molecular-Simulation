import numpy as np
import matplotlib.pyplot as plt

# t = np.zeros([200, ])
# x = np.zeros([200, ])
# v = np.zeros([200, ])

# for i in range(0, 200):
#     t[i] = i * 0.1
#     x[i] = np.sqrt(2) * np.sin(0.1 * i)
#     v[i] = np.sqrt(2) * np.cos(0.1 * i)


x1_05 = np.loadtxt('x1_0.5_out.txt')
x2_05 = np.loadtxt('x2_0.5_out.txt')
x1_10 = np.loadtxt('x1_1_out.txt')
x2_10 = np.loadtxt('x2_1_out.txt')
x1_20 = np.loadtxt('x1_2_out.txt')
x2_20 = np.loadtxt('x2_2_out.txt')
v1 = np.loadtxt('v1_out.txt')
v2 = np.loadtxt('v2_out.txt')


t = np.zeros([20000, ])
u1_05 = np.zeros([20000, ])
u2_05 = np.zeros([20000, ])
u1_10 = np.zeros([20000, ])
u2_10 = np.zeros([20000, ])
u1_20 = np.zeros([20000, ])
u2_20 = np.zeros([20000, ])
k1 = np.zeros([20000, ])
k2 = np.zeros([20000, ])
for i in range(0, 20000):
    t[i] = i * 0.001
    u1_05[i] = x1_05[i] * x1_05[i] * x1_05[i] * x1_05[i] - 2 * x1_05[i] * x1_05[i] + 1
    u2_05[i] = x2_05[i] * x2_05[i] * x2_05[i] * x2_05[i] - 2 * x2_05[i] * x2_05[i] + 1
    u1_10[i] = x1_10[i] * x1_10[i] * x1_10[i] * x1_10[i] - 2 * x1_10[i] * x1_10[i] + 1
    u2_10[i] = x2_10[i] * x2_10[i] * x2_10[i] * x2_10[i] - 2 * x2_10[i] * x2_10[i] + 1
    u1_20[i] = x1_20[i] * x1_20[i] * x1_20[i] * x1_20[i] - 2 * x1_20[i] * x1_20[i] + 1
    u2_20[i] = x2_20[i] * x2_20[i] * x2_20[i] * x2_20[i] - 2 * x2_20[i] * x2_20[i] + 1
    k1[i] = 0.5 * v1[i] * v1[i]
    k2[i] = 0.5 * v2[i] * v2[i]

choose = []

for i in range(0, 100):
    choose.append(20000/100*i)

#################################### x - t ####################################

# plt.plot(t, x1)
# plt.plot(t, x2)
# plt.xlim((0, 20))
# plt.ylim((-2, 2))
# plt.xlabel('t')
# plt.ylabel('x')
# plt.title('x-t, E = 2')

# plt.show()

#################################### u - x ####################################

plt.plot(x1_20, u1_20, c='red', label='E=2', lw='7')
plt.plot(x2_20, u2_20, c='red', lw='7')
plt.plot(x1_10, u1_10, c='blue', label='E=1', lw='4')
plt.plot(x2_10, u2_10, c='blue', lw='4')
plt.plot(x1_05, u1_05, c='yellow', label='E=0.5', lw='1')
plt.plot(x2_05, u2_05, c='yellow', lw='1')

plt.xlim((-2, 2))
plt.ylim((-0.1, 2.1))
plt.xlabel('x')
plt.ylabel('u')
plt.legend(loc='upper center')
plt.title('u - x, E = 0.5, 1, 2')

plt.show()

#################################### x - v ####################################


# plt.plot(x1, v1)
# plt.plot(x2, v2)
# plt.xlim((-2, 2))
# plt.ylim((-2.5, 2.5))
# plt.xlabel('x')
# plt.ylabel('v')
# plt.title('x - v, E = 0.25, 1, 2')

# plt.show()

