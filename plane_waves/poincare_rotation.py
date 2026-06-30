import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.patches import Ellipse

# ============================================================================
# 1. PARÁMETROS FÍSICOS (misma configuración que el script original)
# ============================================================================
f0 = 1.0e-4          # Coriolis (s^-1)
g = 9.81             # Gravedad (m/s^2)
H = 100.0            # Profundidad (m)
L_x = 500000.0       # Escala Zonal (m)
L_y = 500000.0       # Escala Meridional (m)
amp = 2.0            # Amplitud de elevación (m)

k = 2.0 * np.pi / L_x
l = 2.0 * np.pi / L_y
c = np.sqrt(g * H)
omega = np.sqrt(f0**2 + c**2 * (k**2 + l**2))
periodo = 2.0 * np.pi / omega
fac = (amp * g) / (omega**2 - f0**2)

# ============================================================================
# 2. DISCRETIZACIÓN TEMPORAL
# ============================================================================
n_frames = 64                     # Más frames = animación más suave
tiempos = np.linspace(0, periodo, n_frames, endpoint=False)

# Pre-cálculo de u, v y eta en el punto fijo (x=0, y=0)
u_points = []
v_points = []
eta_points = []

for t in tiempos:
    fase = - omega * t
    u = fac * (k * omega * np.cos(fase) - l * f0 * np.sin(fase))
    v = fac * (l * omega * np.cos(fase) + k * f0 * np.sin(fase))
    eta = amp * np.cos(fase)      # elevación en el punto fijo
    
    u_points.append(u)
    v_points.append(v)
    eta_points.append(eta)

u_points = np.array(u_points)
v_points = np.array(v_points)
eta_points = np.array(eta_points)

# ============================================================================
# 3. PREPARACIÓN DE LA FIGURA
# ============================================================================
fig = plt.figure(figsize=(14, 6))

# --- Panel izquierdo: Espacio físico (x, y) con perfil de eta ---
ax1 = fig.add_subplot(1, 2, 1)
ax1.set_title('Onda de Poincaré en el espacio (x, y)', fontsize=12)
ax1.set_xlabel('x (km)')
ax1.set_ylabel('y (km)')
ax1.set_aspect('equal')

# Dominio espacial para graficar la onda
x_phys = np.linspace(-L_x/2, L_x/2, 80)
y_phys = np.linspace(-L_y/2, L_y/2, 80)
X, Y = np.meshgrid(x_phys, y_phys)

# Elevación instantánea (se actualizará en cada frame)
eta_field = np.zeros_like(X)
im = ax1.imshow(eta_field, extent=[x_phys.min(), x_phys.max(), 
                                   y_phys.min(), y_phys.max()],
                origin='lower', cmap='RdBu_r', vmin=-amp, vmax=amp,
                interpolation='bilinear')
fig.colorbar(im, ax=ax1, label='η (m)')

# Punto fijo donde medimos la velocidad (marcado con estrella)
ax1.plot(0, 0, 'k*', markersize=12, label='Punto fijo (x=0, y=0)')

# --- Panel derecho: Elipse de velocidad ---
ax2 = fig.add_subplot(1, 2, 2)
ax2.set_title('Elipse de velocidad de Poincaré', fontsize=12)
ax2.set_xlabel('Velocidad zonal U (m/s)')
ax2.set_ylabel('Velocidad meridional V (m/s)')
ax2.set_aspect('equal')
ax2.axhline(0, color='black', linewidth=0.8, alpha=0.5)
ax2.axvline(0, color='black', linewidth=0.8, alpha=0.5)
ax2.grid(True, linestyle=':', alpha=0.6)

# Dibujar la elipse teórica completa (trayectoria)
ax2.plot(u_points, v_points, 'r--', linewidth=1.5, alpha=0.6, label='Elipse teórica')

# Vector de velocidad actual (flecha desde origen)
quiver = ax2.quiver(0, 0, u_points[0], v_points[0], 
                    angles='xy', scale_units='xy', scale=1,
                    color='darkblue', width=0.010, label='Vector velocidad')

# Punto actual sobre la elipse
punto_actual, = ax2.plot(u_points[0], v_points[0], 'bo', markersize=8, 
                         label='Estado actual')

# Límites dinámicos
max_val = max(np.max(np.abs(u_points)), np.max(np.abs(v_points))) * 1.3
ax2.set_xlim(-max_val, max_val)
ax2.set_ylim(-max_val, max_val)
ax2.legend(loc='upper left')

# ============================================================================
# 4. FUNCIÓN DE ACTUALIZACIÓN PARA LA ANIMACIÓN
# ============================================================================
def update(frame):
    t = tiempos[frame]
    fase = - omega * t
    
    # --- Actualizar campo de eta en el panel izquierdo ---
    eta_field = amp * np.cos(k * X + l * Y + fase)
    im.set_array(eta_field)
    ax1.set_title(f'Onda de Poincaré (t = {t/periodo:.2f} T)', fontsize=12)
    
    # --- Actualizar vector y punto en el panel derecho ---
    u = u_points[frame]
    v = v_points[frame]
    
    # Nuevo vector
    quiver.set_UVC(u, v)
    
    # Nueva posición del punto
    punto_actual.set_data([u], [v])
    
    # Color según elevación (azul = valle, rojo = cresta)
    eta_actual = eta_points[frame]
    if eta_actual > 0:
        punto_actual.set_color('red')
        quiver.set_color('darkred')
    else:
        punto_actual.set_color('blue')
        quiver.set_color('darkblue')
    
    # Título con valores instantáneos
    ax2.set_title(f'U = {u:.3f}, V = {v:.3f}, η = {eta_actual:.2f} m', fontsize=11)
    
    return [im, quiver, punto_actual]

# ============================================================================
# 5. CREAR Y MOSTRAR LA ANIMACIÓN
# ============================================================================
ani = animation.FuncAnimation(fig, update, frames=n_frames, 
                              interval=60, blit=True, repeat=True)

plt.tight_layout()
plt.show()

# (Opcional) Guardar la animación como GIF o MP4
# ani.save('poincare_rotation.gif', writer='pillow', fps=20)
# ani.save('poincare_rotation.mp4', writer='ffmpeg', fps=20)
