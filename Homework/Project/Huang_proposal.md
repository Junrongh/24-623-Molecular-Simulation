#####	<div align="right">24-623 Junrong Huang, Hongyi Liang</di>

#### Project Proposal: Compare different thermostats for NVT MD simulations

-

#####	Description of Problem considered

In MD simulation, we use obtain ensemble average from trajectory

$$<A>=\int A(p(t), r(t))dt$$

$A=Property$, $P=Probability$, $p=momenta$, $r=position$

The $A$, properties of a system normally including: $N$, number of particles; $V$, volume; $E$, energy; $\mu$, chemical potential; $P$, pressure; $T$, temperature. 

$NVT$ MD simulation, also known as canonical ensemble as one of the most popular ensembles, is controlled by three constant descriptors: $NVT$. Based on these basic descriptors we can deduce other thermal variables with methods of statistic mechanics. The NVT MD simulation is well used in lots of area because the three given descriptors, i.e. $NVT$, are easy to be controlled in reality. If we use other ensemble methods, for e.g., the $NVE$ MD simulation, it is easy to control Energy conservation with Newton's law of motion. However, we are not be able to measure the energy of a system directly in reality, which means this simulation is not easy for implementation in reality experiments.

As we know, in MD simulation, $N$, $V$ are very easy to be controlled because we can input the number of particles and the properties of simulation box to define the $N$, $V$. However, to consider $T$, i.e. temperature of the system, a physical quantity expressing the subjective perceptions of hot and cold that can only be indirectly measured by the properties change w.r.t. temperature with a thermometer in reality, is very difficult to manage in MD simulation. In this case study, we attempt to implement several ways of thermostats for $NVT$ MD simulation. Including:

-	Velocity Rescaling
-	Berendsen Thermostat
-	Anderson Thermostat
-	Nose-Hoover Thermostat(which we have already implemented in HW4)

We will implement the codes for all these thermostats methods and compare their results in physical meanings.

#####	Papers and Reference

-	[Molecular dynamics with coupling to an external bathH. J. C. Berendsen, J. P. M. Postma, W. F. van Gunsteren, A. DiNola, and J. R. Haak](https://doi.org/10.1063/1.448118)

-	[Molecular dynamics simulations at constant pressure and/or temperature Andersen, H. C. (1980). The Journal of Chemical Physics. 72 (4): 2384.](http://aip.scitation.org/doi/10.1063/1.439486)

-	[Kinetic moments method for the canonical ensemble distribution
William G.Hoover. Brad LeeHolian.](http://www.sciencedirect.com/science/article/pii/0375960195009736?via%3Dihub)