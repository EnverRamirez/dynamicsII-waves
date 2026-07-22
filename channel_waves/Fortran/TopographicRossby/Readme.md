# Shallow Water Equations: Topographic Rossby Waves (Small Slope)

## Channel Geometry & Topography

Consider a shallow water system within a channel with a weak linear bottom slope in the $y$-direction. The mean fluid depth $H_0(y)$ is given by:

$$H_0(y) = D_0 \left( 1 - \frac{s y}{L} \right)$$

where $s \ll 1$ is a small dimensionless slope parameter and $L$ is the characteristic channel width.

> **Note on Kelvin Waves:** To the lowest order in $s$ ($\mathcal{O}(1)$), the small slope does not alter the fundamental characteristics of the Kelvin wave.

---

## Dispersion Relation

By linearized shallow water theory in this $f$-plane, the only source of meridional variation is the bottom slope. Furthermore, by neglecting terms of order $\mathcal{O}(s^2/L^2)$ since $s \ll 1$, we obtain the fundamental cubic dispersion relation for gravity-topographic waves:

$$\sigma^3 - C_0^2 \left( k^2 + \frac{n^2 \pi^2}{L^2} + \frac{f^2}{C_0^2} \right) \sigma - \frac{f k s C_0^2}{L} = 0$$

where $C_0 = \sqrt{g D_0}$ is the shallow water wave speed, $f$ is the Coriolis parameter, $k$ is the zonal wavenumber, and $n$ is the meridional mode number.

---

## Limiting Solutions

### 1. High-Frequency Limit: Poincaré Modes

In the high-frequency limit ($\sigma \gg s f$), the topographic term becomes negligible. The dispersion relation simplifies to the classic Poincaré (inertia-gravity) wave modes:

$$\sigma^2 = f^2 + C_0^2 \left( k^2 + \frac{n^2 \pi^2}{L^2} \right) + \mathcal{O}(s)$$

These high-frequency modes are virtually unmodified by the slight bottom slope.

### 2. Low-Frequency Limit: Topographic Rossby Modes

For low frequencies ($\sigma = \mathcal{O}(s)$), the cubic term $\sigma^3$ can be neglected relative to the linear term. Rearranging for $\sigma$ yields the dispersion relation for **Topographic Rossby Waves**:

$$\sigma = -\frac{f}{L} \frac{k s}{k^2 + \dfrac{n^2 \pi^2}{L^2} + \dfrac{f^2}{C_0^2}},  n=1,2,\cdots$$

Key properties of these waves:

* **Phase Speed ($c = \sigma / k$):** Always negative ($c < 0$), meaning wave crests propagate westward (leaving shallower water to the right in the Northern Hemisphere).
* **Restoring Mechanism:** Potential vorticity conservation over changing depth replaces the planetary $\beta$-effect ($\beta_{\text{eff}} = f s / L$).

- 
