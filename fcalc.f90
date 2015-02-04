

subroutine calc_force(pos, force, N)
  integer :: N 
  real(8), intent(in) :: pos(N, 3)
  real(8), intent(inout) :: force(N, 3)
!f2py intent(in, out) force        
  real(8) :: delta_r(3), dr2
  integer :: i, j
  force = 0._8
  do i = 1, N
    do j = 1, i-1
      delta_r = pos(i,:) - pos(j,:)
      dr2 = sum(delta_r**2)
      F=24*(2/dr2**7 - 1/dr**4)
      Force(i,:) = Force(i,:) - F*delta_r 
      Force(j,:) = Force(j,:) + F*delta_r
    end do
  end do
end subroutine
