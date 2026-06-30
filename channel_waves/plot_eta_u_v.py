import numpy as np
import matplotlib.pyplot as plt

# ============================================================================
# 1. CARREGAR DADOS GERADOS PELO FORTRAN
# ============================================================================
# Estrutura: X(m) Y(m) Elevacion(eta) U(m/s) V(m/s)
data = np.loadtxt('poincare_data.txt')

X = data[:, 0]      # Posição X em metros
Y = data[:, 1]      # Posição Y em metros
Eta = data[:, 2]    # Elevação da superfície (m)
U = data[:, 3]      # Velocidade zonal (m/s)
V = data[:, 4]      # Velocidade meridional (m/s)

# ============================================================================
# 2. REESTRUTURAR EM MATRIZES 2D
# ============================================================================
N = int(np.sqrt(len(X)))  # Deve ser 100x100
X = X.reshape((N, N))
Y = Y.reshape((N, N))
Eta = Eta.reshape((N, N))
U = U.reshape((N, N))
V = V.reshape((N, N))

# Converter X e Y para quilômetros para melhor visualização
X_km = X / 1000
Y_km = Y / 1000

# ============================================================================
# 3. CRIAR FIGURA COM DOIS PAINÉIS
# ============================================================================
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(15, 6))

# --- Painel 1: Apenas Elevação da superfície ---
contour1 = ax1.contourf(X_km, Y_km, Eta, cmap='RdBu', levels=50)
plt.colorbar(contour1, ax=ax1, label='Elevação da superfície (m)')
ax1.set_title('Onda de Poincaré - Elevação (t=0)', fontsize=12)
ax1.set_xlabel('Distância X (km)')
ax1.set_ylabel('Distância Y (km)')
ax1.grid(True, linestyle='--', alpha=0.5)
ax1.set_aspect('equal')

# --- Painel 2: Elevação + Vetores de Velocidade ---
# Subamostragem para não poluir o gráfico
step = 5  # A cada 5 pontos (ajuste conforme necessidade)

X_sub = X_km[::step, ::step]
Y_sub = Y_km[::step, ::step]
U_sub = U[::step, ::step]
V_sub = V[::step, ::step]

# Calcular magnitude da velocidade para colorir os vetores
magnitude = np.sqrt(U_sub**2 + V_sub**2)

# Plot da elevação como fundo (com transparência)
contour2 = ax2.contourf(X_km, Y_km, Eta, cmap='RdBu', levels=50, alpha=0.6)
plt.colorbar(contour2, ax=ax2, label='Elevação da superfície (m)')

# Plot dos vetores de velocidade (vento)
# A cor representa a magnitude da velocidade
quiver = ax2.quiver(X_sub, Y_sub, U_sub, V_sub, magnitude,
                    cmap='viridis', scale=30, width=0.003, 
                    headwidth=4, headlength=5, alpha=0.9)

# Adicionar barra de cores para a magnitude da velocidade
cbar_quiver = plt.colorbar(quiver, ax=ax2, label='Magnitude da velocidade (m/s)')

ax2.set_title('Elevação + Vetores de Velocidade (t=0)', fontsize=12)
ax2.set_xlabel('Distância X (km)')
ax2.set_ylabel('Distância Y (km)')
ax2.grid(True, linestyle='--', alpha=0.5)
ax2.set_aspect('equal')

plt.tight_layout()
plt.savefig('poincare_wave_with_velocity.png', dpi=300, bbox_inches='tight')
plt.show()

# ============================================================================
# 4. GRÁFICO ADICIONAL: VETORES DE VELOCIDADE EM DESTAQUE
# ============================================================================
# Criar uma figura adicional mostrando apenas os vetores com maior destaque
fig2, ax3 = plt.subplots(1, 1, figsize=(10, 8))

# Usar um step menor para mais vetores ou maior para menos
step_destaque = 4
X_sub2 = X_km[::step_destaque, ::step_destaque]
Y_sub2 = Y_km[::step_destaque, ::step_destaque]
U_sub2 = U[::step_destaque, ::step_destaque]
V_sub2 = V[::step_destaque, ::step_destaque]

# Plotar a elevação com transparência
contour3 = ax3.contourf(X_km, Y_km, Eta, cmap='RdBu', levels=50, alpha=0.5)
plt.colorbar(contour3, ax=ax3, label='Elevação (m)')

# Plotar vetores em branco para melhor contraste
quiver2 = ax3.quiver(X_sub2, Y_sub2, U_sub2, V_sub2,
                     color='black', scale=25, width=0.004,
                     headwidth=5, headlength=6, alpha=0.8)

# Adicionar contorno de η = 0 para destacar cristas e vales
ax3.contour(X_km, Y_km, Eta, levels=[0], colors='white', 
            linewidths=2, alpha=0.8, linestyles='-')

ax3.set_title('Vetores de Velocidade da Onda de Poincaré', fontsize=14)
ax3.set_xlabel('Distância X (km)')
ax3.set_ylabel('Distância Y (km)')
ax3.grid(True, linestyle='--', alpha=0.3)
ax3.set_aspect('equal')

plt.tight_layout()
plt.savefig('poincare_velocity_vectors.png', dpi=300, bbox_inches='tight')
plt.show()

# ============================================================================
# 5. INFORMAÇÕES ESTATÍSTICAS DOS DADOS
# ============================================================================
print("\n" + "="*60)
print("INFORMAÇÕES DOS DADOS DA ONDA DE POINCARÉ")
print("="*60)
print(f"Dimensão da grade: {N} x {N}")
print(f"Número total de pontos: {N*N}")
print(f"\nElevação (η):")
print(f"  Máximo:  {np.max(Eta):.4f} m")
print(f"  Mínimo:  {np.min(Eta):.4f} m")
print(f"  Amplitude: {np.max(Eta) - np.min(Eta):.4f} m")
print(f"\nVelocidade Zonal (U):")
print(f"  Máximo:  {np.max(U):.6f} m/s")
print(f"  Mínimo:  {np.min(U):.6f} m/s")
print(f"\nVelocidade Meridional (V):")
print(f"  Máximo:  {np.max(V):.6f} m/s")
print(f"  Mínimo:  {np.min(V):.6f} m/s")
print(f"\nMagnitude da Velocidade:")
print(f"  Máximo:  {np.max(np.sqrt(U**2 + V**2)):.6f} m/s")
print("="*60)

# ============================================================================
# 6. VERIFICAR RELAÇÃO DE FASE ENTRE η E VELOCIDADE
# ============================================================================
# Amostrar alguns pontos para verificar a relação de fase
print("\nVerificação da relação de fase (η e componentes da velocidade):")
print("-"*60)

# Escolher alguns pontos ao longo de uma linha (ex: x=0)
idx_center = N // 2
y_indices = np.arange(0, N, 10)  # A cada 10 pontos

print("  y (km) |  η (m)  |  U (m/s)  |  V (m/s)  |  Relação")
print("-"*60)
for yi in y_indices:
    eta_val = Eta[idx_center, yi]
    u_val = U[idx_center, yi]
    v_val = V[idx_center, yi]
    # Verificar se η e U estão em fase (ou defasados)
    relacao = "Em fase" if (eta_val > 0 and u_val > 0) or (eta_val < 0 and u_val < 0) else "Defasado"
    print(f"  {Y_km[idx_center, yi]:6.1f} | {eta_val:7.3f} | {u_val:9.6f} | {v_val:9.6f} | {relacao}")
