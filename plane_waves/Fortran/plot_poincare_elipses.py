import numpy as np
import matplotlib.pyplot as plt

# 1. Cargar los datos base de Fortran
data = np.loadtxt('poincare_data.txt')
X_raw = data[:, 0]
Y_raw = data[:, 1]
N = int(np.sqrt(len(X_raw)))

# Reestructurar en matrices 2D
X = X_raw.reshape((N, N))
Y = Y_raw.reshape((N, N))

# 2. Parámetros físicos (Deben coincidir con tu input.nml para recrear el tiempo)
f0 = 1.0e-4
g = 9.81
H = 100.0
L_x = 500000.0
L_y = 500000.0
amp = 2.0

k = 2.0 * np.pi / L_x
l = 2.0 * np.pi / L_y
omega = np.sqrt(f0**2 + (g * H) * (k**2 + l**2))

# 3. Simular el paso del tiempo (un período completo de la onda T = 2*pi/omega)
periodo = 2.0 * np.pi / omega
tiempos = np.linspace(0, periodo, 24) # 24 pasos de tiempo

# Elegimos un punto central en el espacio para ver la rotación de los vectores
idx_x, idx_y = N // 2, N // 2
x0, y0 = X[idx_x, idx_y], Y[idx_x, idx_y]

# Listas para guardar la punta del vector (trayectoria elíptica)
u_points = []
v_points = []

plt.figure(figsize=(10, 8))

# 4. Calcular U y V a lo largo del tiempo para ese punto en el espacio
for t in tiempos:
    # Ecuación analítica de la onda de Poincaré variando en el tiempo
    # u = Re( U * exp(i(kx + ly - wt)) )
    fase = k * x0 + l * y0 - omega * t
    
    u = (amp * g / (omega**2 - f0**2)) * (k * omega * np.cos(fase))
    v = (amp * g / (omega**2 - f0**2)) * (l * f0 * np.sin(fase))
    
    u_points.append(u)
    v_points.append(v)

# Convertir a arrays
u_points = np.array(u_points)
v_points = np.array(v_points)

# 5. Graficar las flechas de velocidad (Vectores rotando)
# Graficamos los vectores saliendo del origen (0,0) para ver el giro
plt.quiver(np.zeros_like(tiempos), np.zeros_like(tiempos), u_points, v_points, 
           angles='xy', scale_units='xy', scale=0.01, color='blue', alpha=0.4,
           label='Vectores de velocidad en el tiempo')

# Graficar la línea que une las puntas de los vectores (La Elipse de Poincaré)
plt.plot(u_points, v_points, 'r--', linewidth=2, label='Trayectoria Elíptica')

# Resaltar el vector inicial (t = 0)
plt.quiver(0, 0, u_points[0], v_points[0], angles='xy', scale_units='xy', scale=0.01, 
           color='red', width=0.007, label='Vector Inicial (t=0)')

# Configuraciones del gráfico
plt.title('Rotación Elíptica del Vector de Velocidad (Onda de Poincaré)', fontsize=14)
plt.xlabel('Velocidad Zonal U (m/s)', fontsize=12)
plt.ylabel('Velocidad Meridional V (m/s)', fontsize=12)
plt.axhline(0, color='black',linewidth=0.5)
plt.axvline(0, color='black',linewidth=0.5)
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(loc='upper right')
plt.axis('equal')

plt.savefig('elipse_poincare.png')
plt.show()
