import numpy as np
import matplotlib.pyplot as plt

# Cargar datos generados por Fortran
#data = np.loadtxt('poincare_data_2H0.txt')
namelist_txt='default_output'
data = np.loadtxt(namelist_txt+'.txt')

X   = data[:, 0]
Y   = data[:, 1]
Eta = data[:, 2]
U   = data[:, 3]  # <-- NEW: Read u-velocity (adjust index if needed)
V   = data[:, 4]  # <-- NEW: Read v-velocity (adjust index if needed)

# Reestructurar en matrices 2D (100x100)
N = int(np.sqrt(len(X)))
X   = X.reshape((N, N))
Y   = Y.reshape((N, N))
Eta = Eta.reshape((N, N))
U   = U.reshape((N, N))    # <-- NEW: Reshape U
V   = V.reshape((N, N))    # <-- NEW: Reshape V

# Graficar
plt.figure(figsize=(8, 6))

# 1. Base Elevation Contour
contour = plt.contourf(X/1000, Y/1000, Eta, cmap='RdBu', levels=50)
plt.colorbar(contour, label='Elevación de la superficie (m)')

# 2. NEW: Overlay Wind/Velocity Vectors (Quiver)
# Slicing [::step, ::step] skips grid points so arrows don't overlap densely.
step = 4  # Plots every 4th vector (change to 3 or 5 to adjust density)
step = 5
step = 3
#step = 7
quiver = plt.quiver(
    X[::step, ::step]/1000, 
    Y[::step, ::step]/1000, 
    U[::step, ::step], 
    V[::step, ::step], 
    color='black', 
    scale=5.0,        # Adjust arrow lengths (higher scale = shorter arrows)
    width=0.003       # Thickness of the arrow shaft
)

# 3. NEW: Add a Legend Key for Vector Magnitude
# This creates a reference scale arrow outside the main plot area
plt.quiverkey(quiver, X=0.85, Y=1.05, U=0.55, label='0.55 m/s', labelpos='E')

plt.title('Onda de Poincaré en el Plano Infinito (t=0)')
plt.xlabel('Distancia X (km)')
plt.ylabel('Distancia Y (km)')
plt.grid(True, linestyle='--', alpha=0.5)
#plt.savefig('./Figs/poincare_wave_eta_u_v_2H0.png')
plt.savefig('./Figs/'+namelist_txt+'.png')
plt.show()

