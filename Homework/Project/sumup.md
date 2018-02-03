###		Velocity Rescaling

The velocity is simply scaled at each time step,

$$v_i^{new}=c_t v_i^{old}$$

where

$$c_t=\sqrt{\frac{T_0}{T}}$$

This procedure leads to rapid energy transfer between different degrees of freedom of the particle. Resetting of velocities may be required from time to time.

###		Berendsen Thermostat

To maintain the temperature the system is coupled weakly to an external heat bath with a fixed temperature($T_0$)

The equation of motion is modified to obtain the desired temperature

$$\dot r_i(t)=\dot v_i(t)$$
$$m_i\dot v_i(t)=\dot F_i(t)-\gamma (t)m_i\dot v_i(t)$$
$$\gamma (t)=\frac{1}{2\tau}(1-\frac{T_0}{T(t)})$$

The velocities are scaled at each step by the scaling factor $c_t$:

$$c_t=\sqrt{1-\frac{\delta t}{\tau}(1-\frac{T_0}{T(t)})}$$

where

$\gamma$ - heat flow variable

$T$ - Instanous kinetic temperature

$T_0$ - Thermostat temperature

$\tau$ - Time constant of the coupling to the heat bath

The value of $\tau$ reveals the strength of coupling between the system and the bath. To achieve good temperature control this value has to be chosen with care.
 
when $\tau \to \infty$ - Berendsen thermostat does not work (sampling microcanonical ensemble)

when $\tau = \delta t$ - Berendsen thermostat turns into a simple scaling scheme

when $\tau$ is very small the coupling to the heat bath is large and there is a significant energy exchange between the system and the thermal bath efficient does not lead to the canonical distribution

###		Andersen Thermostat

The Andersen approach couples velocity of a particle to a heat bath via stochastic collisions
Procedure of Andersen algorithm:

starting from intial conditions integrate the equations of motion for $\delta t$

particles that undergo collisions with the heat bath are selected
the probability of selecting a praticle during the integration time step $\delta t$ is $v\delta t$, where v is the probability of collision

new velocites for selected particles are chosen at random from Maxwell- Boltzmann distribution at the desired temperature; all other particles remain unaffected

generate canonical ensemble: less realistic dynamics and thus not used for computing dynamic quantities (e.g. diffusion coefficients, lifetime of water hydrogen bonds)

###		Nóse-Hoover Thermostat

Nose-Hoover:

- allows the temperature to fluctuate about the average value and controls the oscillations of

- may oscillate for a system far from equilibrium thus it is not recommended for the initial stages of simulations

- leads to canonical distribution


$$m_i\dot v_i=F_i-m_i\gamma_iv_i+R(t)$$
$$<R_i(t)R_j(t+\tau)=2m_i\gamma_ikT_0\delta(\tau)\delta_{ij}>$$

$$\left(\frac{dT}{dt}\right)_{bath}=2\gamma(T_0-T)$$

$$m_i\dot v_i=F_i+m_i\gamma\left(\frac{T_0}{T}-1\right)$$

$$\lambda=1+\frac{\Delta t}{2\tau_T}\left(\frac{T_0}{T}-1\right)$$

$$\lambda=\left[1+\frac{\Delta t}{\tau_T}\left(\frac{T_0}{T}-1\right)\right]^{1/2}$$


$$\dot r_i(t)=\dot v_i(t)$$
$$m_i\dot v_i(t)=F_i(t)-\zeta(t)m_i\dot v_i(t)$$
The heat flow variable has its own equation of motion enabling fluctuations of temperature:
$$m_t\dot \zeta_t(t)=2v^Tmv-gk_BT_0$$

$$H(r_i, p_i, \zeta)=K(p_i)+U(r_i)+\frac{1}{2}(m_t\zeta_t^2)+\frac{3}{2}Nk_BT_0x_t$$