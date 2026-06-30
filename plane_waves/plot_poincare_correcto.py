import numpy as np
import matplotlib.pyplot as plt

# 1. Parámetros físicos (Ajustados para que la elipse sea claramente visible)
f0 = 1.0e-4          # Coriolis (s^-1)
g = 9.81             # Gravedad (m/s^2)
H = 100.0            # Profundidad (m)
L_x = 500000.0       # Escala Zonal (m)
L_y = 500000.0       # Escala Meridional (m)
amp = 2.0            # Amplitud (m)

# 2. Relación de dispersión
k = 2.0 * np.pi / L_x
l = 2.0 * np.pi / L_y
c = np.sqrt(g * H)
omega = np.sqrt(f0**2 + (c**2) * (k**2 + l**2))

# 3. Simular el paso del tiempo en un punto fijo (x=0, y=0)
periodo = 2.0 * np.pi / omega
tiempos = np.linspace(0, periodo, 32) # 32 vectores para ver el giro limpio

u_points = []
v_points = []

# Amplitudes teóricas de la velocidad de Poincaré
# U_amp y V_amp derivadas de las ecuaciones de aguas someras con Coriolis
fac = (amp * g) / (omega**2 - f0**2)

for t in tiempos:
    # Fase temporal (en x=0, y=0 para ver la oscilación local pura)
    fase = - omega * t
    
    # Componentes con su desfase real de 90 grados (Coriolis fuerza el giro)
    u = fac * (k * omega * np.cos(fase) - l * f0 * np.sin(fase))
    v = fac * (l * omega * np.cos(fase) + k * f0 * np.sin(fase))
    
    u_points.append(u)
    v_points.append(v)

u_points = np.array(u_points)
v_points = np.array(v_points)

# 4. Gráfico
plt.figure(figsize=(8, 8))

# Dibujar todos los vectores saliendo del origen
plt.quiver(np.zeros_like(tiempos), np.zeros_like(tiempos), u_points, v_points, 
           angles='xy', scale_units='xy', scale=1, color='blue', alpha=0.3,
           label='Vectores de corriente (t)')

# Dibujar la línea de la elipse
plt.plot(u_points, v_points, 'r--', linewidth=2, label='Elipse de Poincaré')

# Resaltar el primer vector (t=0) para ver dónde empieza
plt.quiver(0, 0, u_points[0], v_points[0], angles='xy', scale_units='xy', scale=1, 
           color='darkblue', width=0.007, label='Corriente inicial (t=0)')

# Estética del gráfico
plt.title('Elipse de Velocidad de una Onda de Poincaré Corregida', fontsize=12)
plt.xlabel('Velocidad Zonal U (m/s)')
plt.ylabel('Velocidad Meridional V (m/s)')
plt.axhline(0, color='black', linewidth=0.8, alpha=0.5)
plt.axvline(0, color='black', linewidth=0.8, alpha=0.5)
plt.grid(True, linestyle=':', alpha=0.6)
plt.axis('equal')
plt.legend(loc='best')

# Ajustar límites dinámicamente para que la elipse no se corte
max_val = max(np.max(np.abs(u_points)), np.max(np.abs(v_points))) * 1.2
plt.xlim(-max_val, max_val)
plt.ylim(-max_val, max_val)

plt.show()
