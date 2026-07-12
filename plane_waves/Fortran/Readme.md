# Shallow water equations: Fortran 
## Plane waves in a layer of constant depth
Considering plane waves on a infinite plane for the shallow water case, in which
the free surface perturbation is given by 
$$
 \eta = \text{Re}[\eta_0 \text{e}^{i(kx+ly-\sigma t)}]
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
 \sigma = \pm \Big\{ f^2 + C_o^2 K^2\Big\}^{1/2}
$$
Lets $\theta=kx+ly-\sigma t + \phi_eta$, then the spatial structure that can be represented by
$$
\begin{align}
\eta &= \eta_0 \cos(\theta)\\
u &= \frac{1}{H_o} \Big[ \frac{k}{K} C\cos(\theta) - \frac{f}{\sigma}\frac{l}{K}C\sin(\theta)\Big] \eta_0\\
v &= \frac{1}{H_o} \Big[ \frac{l}{K} C\cos(\theta) - \frac{f}{\sigma}\frac{k}{K}C\sin(\theta)\Big] \eta_0
\end{align}
$$
Considering that the phase propagation is in the direction dictated by $\vec{k}=(k,l)$ whose components $k$ and $l$
correspond to the along x and along y components of the wavenumber, the modulus $K=\sqrt{k^2 + l^2}$. Such that the
unitary wavevector
$$
  \hat{k} = \frac{1}{K} \vec{k} = \frac{1}{K} (k,l)
$$
Any unitary vector $\hat{s}$ perpendicular to the plane (k,l) will make the vector $\hat{k}$ to rotate if a vectorial multiplication is used
$$
  \hat{s}\times\hat{k} = \frac{1}{K}(-l,k) 
$$
Thus the solution for the plane waves can be written in terms of parallel and perpendicular fluid flow

$$
 u_{||} = \frac{\eta_0}{H_0} C \cos(\theta)
$$
$$
 u_{\perp} = \frac{\eta_0}{H_0} \frac{f}{\sigma}C \sin(\theta)
$$
### Questions that arise
-Compare the expressions given in eqs: 3.8.14 (Pedlosky)
and the implemented in the code, shows that they are equivalent
 -what does it means that the programmed equations do not have
  time?
 -how to change the initial phase of eta? what changes must be
 implemented in the code to incorportate a $phi_eta$ (related
 to the phase)change?
 - lox, loy, l1x, l1y => l1y = lox*l1x*loy/sqrt(d)
   where d = (loy*l1x)^2-(loy*lox)^2+(lox*l1x)^2
-how to set up the wave to be more parallel to the x axis?
-how to change the phase of the initial $\eta$?
-rotate the wave more parallel to they y axis, compute $C = sigma/K$,
 does |C| changes? justify your answer
-what to make the velocity tip more circular and less elliptic?
