import numpy as np
import matplotlib.pyplot as plt

Energy = np.loadtxt('./output/energy.txt')

# Constant value input.
EPSILON = 1.67e-21
N = 256
kB = 1.3806e-23
T = 100
MASS = 6.63e-26

# Cut the first 100s off to get a more general result.
t = Energy[50000:, 0]
E = Energy[50000:, 3]
step = E.shape[0]
# Calc <E>
eavgE = np.average(E)

calcE = np.zeros([step, ])
for i in range(1, step):
    calcE[i] = (E[i] - eavgE) * (E[i] - eavgE) * EPSILON * EPSILON

C = np.average(calcE) / ((N - 1) * kB * T * T) / MASS

print(eavgE, C)
