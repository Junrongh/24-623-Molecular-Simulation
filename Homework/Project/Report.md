Therefore, we have to deduce the Temperature of the simulation system with following: in thermodynamic, 

$$\frac{1}{T}=\left.\frac{\partial S}{\partial U}\right|_{N,V} $$

$S=Enrtopy$, $U=Internal\ Energy$, $N=Number\ of\ Particles$, $V=Volumn$.

In class, to simplify the simulation and the calculation, we only considered system of ideal gas with $N$ particles. The detailed method to measure the temperature of a system:

$$PV=Nk_BT=\sum_{i=1}^Nm_iv_{ix}^2=\sum_{i=1}^Nm_iv_{iy}^2=\sum_{i=1}^Nm_iv_{iz}^2$$

$$T=\frac{\sum_{i=1}^Nm_i(v_{ix}^2+v_{iy}^2+v_{iz}^2)}{3(N-1)k_B}=\frac{2K}{3(N-1)k_B}$$

$K=Kinetic\ Energy$, $k_B=Boltzmann\ Constant$, $v_{ix}, v_{iy}, v_{iz}=Velocity\ in\ x,y,z\ Direction\ of\ particle\ i$

As we know, in MD simulation, $N$, $V$ are very easy to be controled because we can input the number of particles and the propertise of simulation box to define the $N$, $V$. However, to consider $T$, i.e. temperature of the system, is defined with:

Temperature is a physical quantity expressing the subjective perceptions of hot and cold. In microscopic description, temperature is the degree of thermal motion of the objects. Temperature can only be indirectly measured by the propertise change w.r.t. temperature with a thermometer in reality, which is very difficult to manage in MD simulation. 



