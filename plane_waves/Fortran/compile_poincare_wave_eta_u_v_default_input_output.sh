#The poincare_wave_eta_u_v_default_input_output.f90 version accepts optional arguments for:
# a) the input namelist and 
# b) the output txt file containing the plane waves
#
#    ! Variables para nombre de los archivos
#    character(len=256) :: input_namelist, output_txt_file
#
# By default the program reads the input.nml file
#
#   arg_count = command_argument_count()
#   if ( arg_count == 1 ) then
#         call get_command_argument(1, input_namelist)
#   else
#         input_namelist = 'input.nml'
#   end if
#
#   output_txt_file = 'default_output.txt'
#
# Inside the namelist, a variable (output_txt_file) for the output text file is reserved
# but defined earlier for runs in the absence of this variable
#
#    ! Variables del Namelist
#    real :: f0, L_x, L_y, amp, g, H
#    namelist /param_fisicos/ f0, L_x, L_y, amp, g, H, output_txt_file
#
# With this configuration, appropriate names for the experiments can be used, for example
# distinguish between runs with NH Coriolis againsts SH Coriolis, or experiments with the
# phase rotated towards a index, or even experiments with different depths
#
# The code is run as follows
# ./poincare_wave_eta_u_v_default_input_output.exe (default input input.nml and default output default_output.txt)
#
# ./poincare_wave_eta_u_v_default_input_output.exe doubling_coriolis.nml
#
# ./poincare_wave_eta_u_v_default_input_output.exe increasing_H.nml increasing_H.txt

gfortran poincare_wave_eta_u_v_default_input_output.f90 -o poincare_wave_eta_u_v_default_input_output.exe
./poincare_wave_eta_u_v_default_input_output.exe 

