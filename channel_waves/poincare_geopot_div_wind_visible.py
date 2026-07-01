import numpy as np
import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
from matplotlib.patches import Patch

# ============================================================================
# 1. PARÁMETROS FÍSICOS (igual que antes)
# ============================================================================
f0 = -1.0e-4
g = 9.81
H = 100.0
L_x = 500000.0
L_y = 500000.0
amp = 2.0
nn = 3

k = 2.0 * np.pi / L_x
l = nn * np.pi / L_y
c = np.sqrt(g * H)
omega = np.sqrt(f0**2 + c**2 * (k**2 + l**2))

# ============================================================================
# 2. DOMINIO ESPACIAL
# ============================================================================
nx, ny = 150, 150
x_phys = np.linspace(-L_x/2, L_x/2, nx)
y_phys = np.linspace(-L_y/2, L_y/2, ny)
X, Y = np.meshgrid(x_phys, y_phys)
X_km = X / 1000
Y_km = Y / 1000

# ============================================================================
# 3. CÁLCULO DE CAMPOS EN t = 0
# ============================================================================
t = 0.0
fase = k * X - omega * t

eta = amp * (np.cos(l*Y) - L_y * f0 * k / (nn * np.pi * omega) * np.sin(l*Y)) * np.cos(fase)
geopot = eta * g

u = amp / H * (c**2 * k / omega * np.cos(l*Y) - L_y * f0 / (nn * np.pi) * np.sin(l*Y)) * np.cos(fase)
v = -amp / H * L_y / (omega * nn * np.pi) * (f0**2 + (c * nn * np.pi / L_y)**2) * np.sin(l*Y) * np.sin(fase)

div = -amp / H * (c**2 * k / omega * np.cos(l*Y) -
                  L_y * f0 / (nn * np.pi) * np.sin(l*Y) +
                  L_y / (omega * nn * np.pi) * (f0**2 + (c * nn * np.pi / L_y)**2)) * np.sin(fase)

# ============================================================================
# 4. FIGURA CON DOS PANELES
# ============================================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# ============================================================================
# PANEL IZQUIERDO: Geopotencial + vientos (mejorados)
# ============================================================================
im1 = ax1.contourf(X_km, Y_km, geopot, levels=50, cmap='RdBu_r', alpha=0.25)
fig.colorbar(im1, ax=ax1, label='Geopotencial (m²/s²)')

levels_pos = np.linspace(0.1, np.max(geopot), 8)
levels_neg = np.linspace(np.min(geopot), -0.1, 8)
cont_pos = ax1.contour(X_km, Y_km, geopot, levels=levels_pos,
                       colors='red', linewidths=1.5, linestyles='solid')
cont_neg = ax1.contour(X_km, Y_km, geopot, levels=levels_neg,
                       colors='blue', linewidths=1.5, linestyles='dashed')

# --- Vectores de viento (AJUSTADOS) ---
step = 4
X_sub = X_km[::step, ::step]
Y_sub = Y_km[::step, ::step]
U_sub = u[::step, ::step]
V_sub = v[::step, ::step]

# Opción A: Escala reducida (scale=30) y flechas más gruesas
ax1.quiver(X_sub, Y_sub, U_sub, V_sub,
           scale=15, #30,          # <--- Reducido de 200 a 30 (flechas mucho más grandes)
           width=0.008,       # <--- Flechas más gruesas
           headwidth=5,
           headlength=6,
           color='black',
           alpha=0.8)

# Opción B (alternativa): Normalizar vectores y colorear por magnitud
# (descomentar y comentar la de arriba si se prefiere)
# mag = np.sqrt(U_sub**2 + V_sub**2)
# ax1.quiver(X_sub, Y_sub, U_sub/mag, V_sub/mag, mag,
#            scale=20, width=0.01, headwidth=5, headlength=6,
#            cmap='viridis', alpha=0.9)
# fig.colorbar(..., ax=ax1, label='Magnitud (m/s)')

ax1.set_title('Geopotencial (η·g) y vientos', fontsize=12)
ax1.set_xlabel('x (km)')
ax1.set_ylabel('y (km)')
ax1.set_aspect('equal')
ax1.grid(True, linestyle=':', alpha=0.5)

legend_handles = [
    Line2D([0], [0], color='red', linestyle='solid', linewidth=1.5, label='Geopotencial > 0'),
    Line2D([0], [0], color='blue', linestyle='dashed', linewidth=1.5, label='Geopotencial < 0')
]
ax1.legend(handles=legend_handles, loc='upper right')

# ============================================================================
# PANEL DERECHO: Divergencia + tramado + vientos (mejorados)
# ============================================================================
vmax_div = max(abs(div.min()), abs(div.max())) * 0.8
im_div = ax2.contourf(X_km, Y_km, div, levels=50,
                      cmap='RdBu_r', vmin=-vmax_div, vmax=vmax_div)
fig.colorbar(im_div, ax=ax2, label='Divergencia (s⁻¹)')

mask_div_pos = np.ma.masked_where(div <= 0, div)
hatch = ax2.contourf(X_km, Y_km, mask_div_pos, levels=[0, vmax_div],
                     colors='none', hatches=['///'], alpha=0.0)

# Mismos vectores mejorados
ax2.quiver(X_sub, Y_sub, U_sub, V_sub,
           scale=30, width=0.008, headwidth=5, headlength=6,
           color='black', alpha=0.8)

ax2.set_title('Divergencia (sombreado) y vientos', fontsize=12)
ax2.set_xlabel('x (km)')
ax2.set_ylabel('y (km)')
ax2.set_aspect('equal')
ax2.grid(True, linestyle=':', alpha=0.5)

hatch_handle = Patch(facecolor='none', edgecolor='black', hatch='///', label='Divergencia > 0 (tramado)')
ax2.legend(handles=[hatch_handle], loc='upper right')

plt.tight_layout()
plt.savefig('poincare_geopot_div_wind_visible.png', dpi=300, bbox_inches='tight')
plt.show()
