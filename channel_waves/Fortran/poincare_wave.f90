program poincare_wave
    implicit none

    ! Variables del Namelist
    real :: f0, L_x, L_y, eta0, g, H
    integer :: nn
    namelist /param_fisicos/ f0, L_x, L_y, eta0, g, H, nn

    ! Variables de cálculo
    real :: k, l, omega, c
    real :: x, y, eta, u, v
    integer :: i, j
    integer, parameter :: N = 100 ! Resolución de la grilla (NxN)
    real, parameter :: pi = 3.14159265
    real, parameter :: tt = 0
    real :: x_max, y_max, dx, dy
    
    ! 1. Leer parámetros desde el Namelist
    open(unit=10, file='input.nml', status='old', action='read')
    read(10, nml=param_fisicos)
    close(10)

    print *, "--- Parámetros Cargados ---"
    print *, "Coriolis (f0): ", f0
    print *, "Escala Zonal (L_x): ", L_x
    print *, "Escala Meridional (L_y): ", L_y
    print *, "Amplitud: ", eta0

    ! 2. Calcular números de onda y frecuencia angular (Relación de Dispersión)
    k = 2.0 * pi / L_x
    l = nn * pi / L_y
    c = sqrt(g * H) ! Velocidad de la onda de gravedad somera
    omega = sqrt(f0**2 + (c**2) * (k**2 + l**2))
    
    print *, "Frecuencia de la Onda (omega): ", omega

    ! 3. Configurar la grilla espacial (Plano Infinito aproximado a 2 longitudes de onda)
    x_max = 2.0 * L_x
    y_max = 2.0 * L_y
    dx = x_max / real(N-1)
    dy = y_max / real(N-1)

    ! 4. Calcular y exportar los datos a un archivo
    open(unit=20, file='poincare_data.txt', status='unknown')
    write(20, *) "# X(m) Y(m) Elevacion(eta) U(m/s) V(m/s)"

    do i = 0, N-1
        x = -L_x + real(i) * dx
        do j = 0, N-1
            y = -L_y + real(j) * dy
            
            ! Onda de Poincaré viajando en X (para t = 0)
            eta = eta0 * ( cos(l*y) - L_y*f0*k/nn/pi/omega * sin(l*y) ) * cos(k*x - omega*tt )
            
            ! Velocidades horizontales teóricas asociadas
            u = eta0 / H  * ( c**2 * k / omega * cos(l*y) - L_y*f0/nn/pi * sin(l*y) ) * cos(k*x - omega*tt )
            v = - eta0 / H * L_y / omega / nn / pi * (f0**2 + (c*nn*pi/L_y)**2 )  * sin(l*y) *  sin(k*x - omega*tt)
            
            write(20, '(5(E14.6, 1x))') x, y, eta, u, v
        end do
        write(20, *) ! Línea en blanco (útil para estructuras de datos de Gnuplot/Python)
    end do
    close(20)

    print *, "Datos exportados exitosamente a 'poincare_data.txt'"
end program poincare_wave
