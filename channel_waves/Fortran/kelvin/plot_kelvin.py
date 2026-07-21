import numpy as np
import matplotlib.pyplot as plt

# Cargar datos generados por Fortran
data = np.loadtxt('kelvin_data.txt')

X = data[:, 0]
Y = data[:, 1]
Eta = data[:, 2]

# Reestructurar en matrices 2D (100x100)
N = int(np.sqrt(len(X)))
X = X.reshape((N, N))
Y = Y.reshape((N, N))
Eta = Eta.reshape((N, N))

# Graficar
#plt.figure(figsize=(8, 6))
plt.figure(figsize=(10, 4)) #Cambiar el aspect ratio
contour = plt.contourf(X/1000, Y/1000, Eta, cmap='RdBu', levels=50)
plt.colorbar(contour, label='Elevación de la superficie (m)')
plt.title('Onda de Poincaré en el canal (t=0)')
plt.xlabel('Distancia X (km)')
plt.ylabel('Distancia Y (km)')

#plt.gca().set_aspect(-1.0)  # figura alargada em el eje, si < 1 en x; si > 1 alargada en y

plt.grid(True, linestyle='--', alpha=0.5)
plt.savefig('kelvin_wave.png')
plt.show()
