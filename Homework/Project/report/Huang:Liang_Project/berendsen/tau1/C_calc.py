import numpy as np
import matplotlib.pyplot as plt

TPdata = np.loadtxt('tp.txt')
Momenta = np.loadtxt('momenta.txt')
Energy = np.loadtxt('energy.txt')

m = 6.63E-26
epsilon = 1.67E-21
kB = 1.3806E-23


step = TPdata.shape[0]
t = TPdata[:, 0]
T = TPdata[:, 1]
P = TPdata[:, 3]
taverageT = TPdata[:, 2]
taverageP = TPdata[:, 4]

avg_E = np.average(Energy[5000:, 3])
print avg_E

c_v = np.var(Energy[5000:, 3]) * epsilon * epsilon / (3 * 255 * 100 * 100 * kB)
print c_v

C_v = 3 * c_v / m
print C_v
