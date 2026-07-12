import numpy as np
import matplotlib.pyplot as plt

# Cargar datos generados por Fortran
data = np.loadtxt('rotate_the_phase_poincare_data.txt')

X = data[:, 0]
Y = data[:, 1]
Eta = data[:, 2]

# Reestructurar en matrices 2D (100x100)
N = int(np.sqrt(len(X)))
X = X.reshape((N, N))
Y = Y.reshape((N, N))
Eta = Eta.reshape((N, N))

N_sub = int(N/4)
print(N_sub)

X_sub = X[N_sub:N-N_sub,:]
Y_sub = Y[N_sub:N-N_sub,:]
Eta_sub = Eta[N_sub:N-N_sub,:]

# Graficar
plt.figure(figsize=(8, 6))
contour = plt.contourf(X_sub/1000, Y_sub/1000, Eta_sub, cmap='RdBu', levels=50)
plt.colorbar(contour, label='Elevación de la superficie (m)')
plt.title('Onda de Poincaré en el Plano Infinito (t=0)')
plt.xlabel('Distancia X (km)')
plt.ylabel('Distancia Y (km)')
plt.grid(True, linestyle='--', alpha=0.5)
plt.savefig('./Figs/rotate_the_phase_poincare_wave.png')
plt.show()
