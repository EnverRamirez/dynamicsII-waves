import numpy as np
import matplotlib.pyplot as plt

# Cargar datos generados por Fortran
data = np.loadtxt('kelvin_data.txt')

X = data[:, 0]
Y = data[:, 1]
Eta = data[:, 2]
U   = data[:, 3]  
V   = data[:, 4]  

# Reestructurar en matrices 2D (100x100)
N = int(np.sqrt(len(X)))
X = X.reshape((N, N))
Y = Y.reshape((N, N))
Eta = Eta.reshape((N, N))
U   = U.reshape((N, N)) 
V   = V.reshape((N, N))

# Graficar
#plt.figure(figsize=(8, 6))
plt.figure(figsize=(10, 4)) #Cambiar el aspect ratio
contour = plt.contourf(X/1000, Y/1000, Eta*9.81, cmap='RdBu_r', levels=50)
plt.colorbar(contour, label='Geopotencial (m2/s2)')

#superponer el flujo
step=3
step=5
step=4
#step=3
quiver = plt.quiver(
    X[::step, ::step]/1000, 
    Y[::step, ::step]/1000, 
    U[::step, ::step], 
    V[::step, ::step], 
    color='black', 
    headwidth=5,
    headlength=9,
    scale=30.0,        # Adjust arrow lengths (higher scale = shorter arrows)
    width=0.008       # Thickness of the arrow shaft
)
# Adicionar uma leyenda para el vector de flujo
plt.quiverkey(quiver, X=0.085, Y=1.05, U=0.25, label='0.25 m/s', labelpos='E')

plt.title('Onda de Kelvin en el canal (t=0)')
plt.xlabel('Distancia X (km)')
plt.ylabel('Distancia Y (km)')

#plt.gca().set_aspect(-1.0)  # figura alargada em el eje, si < 1 en x; si > 1 alargada en y

plt.grid(True, linestyle='--', alpha=0.5)
plt.savefig('kelvin_wave_geopot_u_v.png')
plt.show()
