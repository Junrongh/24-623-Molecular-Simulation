import numpy as np
import matplotlib.pyplot as plt
x_start = np.loadtxt('result.txt')
N = x_start.shape[0]
STEP = 150
xmin = np.min(x_start)
xmax = np.max(x_start)
M = int(np.floor((xmax - xmin) * STEP)) + 1
x = np.zeros([M, ])
y = np.zeros([M, ])
print (xmin, xmax, M)
y_cal = np.zeros([M, ])
for i in range(0, M):
    x[i] = xmin + 1.0 * i / STEP
    y_cal[i] = np.exp(-0.1 * (x[i] * x[i] * x[i] * x[i] - 2 * x[i] * x[i] + 1)) / 1.95253

for i in range(0, N):
    index = int(np.floor((x_start[i] - xmin) * STEP))
    y[index] = y[index] + 1

y = y / (1.0 * N / STEP)

plt.plot(x, y, label='NVT ensemble')
plt.plot(x, y_cal, label='Analytical distribution')
plt.legend(loc='upper left')
plt.title('NVT MC ensemble vs. Analytical distribution')
plt.savefig('x_dist.png')
