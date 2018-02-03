###		Original Verlet

$$\begin{align} 
\dot {r_i}&=v_i\\
\dot {v_i}&=F_i/m_i-\eta v_i\\
\end{align}$$

$$\begin{align} 
& 1. v_{i}(t+\Delta t/2)=v_{i}(t)+F_{i}(t)\Delta t/(2m_i) \\ 
& 2. r_{i}(t+\Delta t)=r_{i}(t)+v_{i}(t+\Delta t/2)\Delta t \\ 
& 3. v_{i}(t+\Delta t)=v_{i}(t+\Delta t/2)+F_{i}(t+\Delta t)\Delta t/(2m_i) \\ 
\end{align}$$

###		Berendsen Thermostat

Add the velocity rescale, i.e.$v_{new}(t)=\lambda v_{old}(t)$ to every atom.

$$\begin{align} 
& 1. v_i(t) \to K(t) \to T(t) \to \lambda(t) \\
& 2. v_{i}(t+\Delta t/2)=(v_{i,x}(t)+F_{i,x}(t)\Delta t/(2m_i))\cdot \lambda(t) \\ 
& 3. r_{i}(t+\Delta t)=r_{i}(t)+v_{i,x}(t+\Delta t/2)\Delta t \\ 
& 4. v_i(t+\Delta t/2) \to K(t+\Delta t/2) \to T(t+\Delta t/2) \to \lambda(t+\Delta t/2)\\
& 5. v_{i}(t+\Delta t)=(v_{i}(t+\Delta t/2)+F_{i}(t+\Delta t)\Delta t/(2m_i))\cdot \lambda(t+\Delta t/2) \\ 
\end{align}$$

###		Anderson Thermostat

$$\begin{align} 
& 1. v_{i}(t+\Delta t/2)=v_{i}(t)+F_{i}(t)\Delta t/(2m_i) \\ 
& 2. r_{i}(t+\Delta t)=r_{i}(t)+v_{i}(t+\Delta t/2)\Delta t \\ 
& 3. v_{i}(t+\Delta t)=v_{i}(t+\Delta t/2)+F_{i}(t+\Delta t)\Delta t/(2m_i) \\
& 4. v_{i}(t+\Delta t)=randGaussian(0, v_{T_{set}}, \sigma)\ if\ rand<(\tau \Delta t) \\ 
\end{align}$$

###		Nose-Hoover Thermostat


$$\begin{align} 
\dot {r_i}&=v_i\\
\dot {v_i}&=F_i/m_i-\eta v_i\\
\dot \eta&=\frac {1}{{\tau_T}^2}\left(\frac {T}{T_{set}}-1\right)
\end{align}$$


$$\begin{align}
&1. v_i(t+\Delta t/2)=v_i(t)+[F_i(t)/m_i-\eta (t)v_i(t)]\Delta t/2\\
&2. r_i(t+\Delta t)=r_i(t)+v_i(t+\Delta t/2)\Delta t\\
&3. \eta (t+\Delta t)=\eta (t)+\frac{\Delta t}{{\tau_T}^2}\left[\frac{T(t)}{T_{set}}-1\right]\\
&4. v_i(t+\Delta t)=\frac {v_i(t+\Delta t/2)+F_i(t+\Delta t)\Delta t/(2m_i)}{1+\eta (t+\Delta t)\Delta t/2}
\end{align}$$