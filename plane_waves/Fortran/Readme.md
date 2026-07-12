# Shallow water equations: Fortran 
## Plane waves in a layer of constant depth
Considering plane waves on a infinite plane for the shallow water case, in which
the free surface perturbation is given by 
$$
\begin{equation}
 \eta = \text{Re}\[\eta_0 \text{e}^{i(kx+ly-\sigma t)}]
\end{equation}
$$
The equation governing the evolution of $\eta$ is given by eq 3.6.9 in Pedlosky
$$
 \partial_t \Big[ \Big( \partial_{tt} + f^2 \Big)\eta - \nabla \cdot (C_o^2\nabla \eta) \Big] - gfJ(H_o,\eta) = 0
$$
For the plane wave to be solution of 3.6.9 in the case of constant $H_o$ we obtain that
$$
  \sigma\eta_0\Big[f^2 - \sigma^2 + C_o^2 K^2 \Big] =0
$$
the trivial solution is $\eta_0=0$ in this case the pressure gradient are zero and there is no motion.
Another solution corresponds to the $\sigma=0$, which corresponds to the stationary purely geostrophic mode
in this case, the motion is perpendicular to the gradients of $\eta$ ($\nabla\eta$).  The other modes are the
inertia gravity modes.

### Inertia gravity waves
The waves in this case have the dispersion relation given by
$$
 \sigma = \pm \Big{ f^2 + C_o^2 K^2\Big}^{1/2}
$$
Lets $\theta=kx+ly-\sigma t + \phi_eta$, then the spatial structure that can be represented by
$$
\begin{subequations}
\begin{align}
\eta &= \eta_0 \cos(\theta)\\
u &= \frac{1}{H_o} \Big[ \frac{k}{K} C\cos(\theta) - \frac{f}{\sigma}\frac{l}{K}C\sin(\theta)\Big] \eta_0
v &= \frac{1}{H_o} \Big[ \frac{l}{K} C\cos(\theta) - \frac{f}{\sigma}\frac{k}{K}C\sin(\theta)\Big] \eta_0
\end{align}
\end{subequations}
$$

