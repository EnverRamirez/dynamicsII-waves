import numpy as np
import matplotlib.pyplot as plt

# ============================================================================
# 1. CARREGAR DADOS GERADOS PELO FORTRAN
# ============================================================================
data = np.loadtxt('poincare_data.txt')

X = data[:, 0]
Y = data[:, 1]
Eta = data[:, 2]

# Se os dados incluírem U e V, descomente as linhas abaixo
# Caso contrário, precisamos calcular U e V a partir de Eta
try:
    # Tentar carregar U e V se existirem no arquivo
    if data.shape[1] >= 4:
        U = data[:, 3]
        V = data[:, 4]
    else:
        raise ValueError("Arquivo não contém U e V")
except:
    # Se não houver U e V, calculamos a partir da relação de dispersão
    print("Calculando U e V a partir de Eta...")
    # Parâmetros físicos (ajuste para os dados do Fortran)
    f0 = 1.0e-4          # Coriolis (s^-1)
    g = 9.81             # Gravidade (m/s^2)
    H = 100.0            # Profundidade (m)
    L_x = 500000.0       # Escala Zonal (m)
    L_y = 500000.0       # Escala Meridional (m)
    amp = 2.0            # Amplitude (m)
    
    k = 2.0 * np.pi / L_x
    l = 2.0 * np.pi / L_y
    c = np.sqrt(g * H)
    omega = np.sqrt(f0**2 + c**2 * (k**2 + l**2))
    
    # Calcular U e V a partir de Eta (onda plana no instante t=0)
    fase = k * X + l * Y
    fac = amp * g / (omega**2 - f0**2)
    U = fac * (k * omega * np.cos(fase) - l * f0 * np.sin(fase))
    V = fac * (l * omega * np.cos(fase) + k * f0 * np.sin(fase))

# ============================================================================
# 2. REESTRUTURAR OS DADOS EM MATRIZES 2D
# ============================================================================
N = int(np.sqrt(len(X)))
X = X.reshape((N, N))
Y = Y.reshape((N, N))
Eta = Eta.reshape((N, N))
U = U.reshape((N, N))
V = V.reshape((N, N))

# ============================================================================
# 3. CRIAR A FIGURA COM DOIS PAINÉIS
# ============================================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 6))

# --- Painel 1: Elevação da superfície (Eta) ---
contour = ax1.contourf(X/1000, Y/1000, Eta, cmap='RdBu', levels=50)
plt.colorbar(contour, ax=ax1, label='Elevação da superfície (m)')
ax1.set_title('Onda de Poincaré (t=0)')
ax1.set_xlabel('Distância X (km)')
ax1.set_ylabel('Distância Y (km)')
ax1.grid(True, linestyle='--', alpha=0.5)

# --- Painel 2: Elevação + Vetores de vento/velocidade ---
# Subamostragem para não poluir o gráfico com muitos vetores
step = 4  # A cada 4 pontos (ajuste conforme necessidade)

# CORREÇÃO: Extrair as submatrizes corretamente
X_sub = X[::step, ::step] / 1000
Y_sub = Y[::step, ::step] / 1000
U_sub = U[::step, ::step]
V_sub = V[::step, ::step]

# Calcular magnitude APÓS a subamostragem
magnitude_sub = np.sqrt(U_sub**2 + V_sub**2)

# Plot da elevação como fundo
contour2 = ax2.contourf(X/1000, Y/1000, Eta, cmap='RdBu', levels=50, alpha=0.6)
plt.colorbar(contour2, ax=ax2, label='Elevação da superfície (m)')

# Plot dos vetores de velocidade (vento)
# Usar cores para representar a magnitude da velocidade
quiver = ax2.quiver(X_sub, Y_sub, U_sub, V_sub, magnitude_sub,
                    cmap='viridis', scale=50, width=0.003, 
                    headwidth=4, headlength=5, alpha=0.8)

# Adicionar barra de cores para a magnitude da velocidade
cbar_quiver = plt.colorbar(quiver, ax=ax2, label='Magnitude da velocidade (m/s)')

ax2.set_title('Elevação + Vetores de Velocidade')
ax2.set_xlabel('Distância X (km)')
ax2.set_ylabel('Distância Y (km)')
ax2.grid(True, linestyle='--', alpha=0.5)

# ============================================================================
# 4. VERSÃO SIMPLIFICADA (APENAS UM PAINEL COM TUDO)
# ============================================================================
# Se preferir um único gráfico com tudo junto, descomente as linhas abaixo:
"""
fig2, ax3 = plt.subplots(1, 1, figsize=(10, 8))
contour3 = ax3.contourf(X/1000, Y/1000, Eta, cmap='RdBu', levels=50, alpha=0.7)
plt.colorbar(contour3, ax=ax3, label='Elevação (m)')

# Vetores de velocidade
step2 = 5
X_sub2 = X[::step2, ::step2] / 1000
Y_sub2 = Y[::step2, ::step2] / 1000
U_sub2 = U[::step2, ::step2]
V_sub2 = V[::step2, ::step2]

quiver2 = ax3.quiver(X_sub2, Y_sub2, U_sub2, V_sub2, 
                     color='white', scale=50, width=0.005,
                     headwidth=4, headlength=5, alpha=0.9)

ax3.set_title('Onda de Poincaré - Elevação e Vetores de Velocidade')
ax3.set_xlabel('Distância X (km)')
ax3.set_ylabel('Distância Y (km)')
ax3.grid(True, linestyle='--', alpha=0.5)
"""

# ============================================================================
# 5. ADICIONAR LINHAS DE CRISTA E VALE (OPCIONAL)
# ============================================================================
# Para visualizar melhor as cristas e vales
# Descomente se quiser adicionar contornos para η = 0
"""
ax2.contour(X/1000, Y/1000, Eta, levels=[0], colors='black', linewidths=1, alpha=0.5)
ax1.contour(X/1000, Y/1000, Eta, levels=[0], colors='black', linewidths=1, alpha=0.5)
"""

# ============================================================================
# 6. SALVAR E MOSTRAR
# ============================================================================
plt.tight_layout()
plt.savefig('poincare_wave_with_wind.png', dpi=300, bbox_inches='tight')
plt.show()

# ============================================================================
# 7. INFORMAÇÕES ADICIONAIS SOBRE OS DADOS
# ============================================================================
print(f"\nInformações dos dados:")
print(f"  Dimensão da grade: {N} x {N}")
print(f"  Número total de pontos: {N*N}")
print(f"  Número de vetores plotados: {len(X_sub.ravel())}")
print(f"  Amplitude máxima de η: {np.max(np.abs(Eta)):.3f} m")
print(f"  Velocidade máxima: {np.max(np.sqrt(U**2 + V**2)):.3f} m/s")
