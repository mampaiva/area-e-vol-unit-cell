program calc_areas
    implicit none

    ! Declaração de variáveis
    real(8) :: a, b, c
    real(8) :: cos_alpha, cos_beta, cos_gamma
    real(8) :: sin_alpha, sin_beta, sin_gamma
    real(8) :: volume
    real(8) :: area_ab, area_bc, area_ac
    integer :: iunit

    ! Abrir o arquivo de entrada para leitura
    iunit = 20
    open(unit=iunit, file='input.dat', status='old')

    ! Ler os parâmetros do arquivo de entrada
    read(iunit, *) a, b, c, cos_alpha, cos_beta, cos_gamma

    ! Fechar o arquivo de entrada
    close(iunit)

    ! Calcular os senos dos ângulos
    sin_alpha = sqrt(1.0d0 - cos_alpha**2)
    sin_beta = sqrt(1.0d0 - cos_beta**2)
    sin_gamma = sqrt(1.0d0 - cos_gamma**2)

    ! Calcular as áreas das faces
    area_ab = a * b * sin_gamma
    area_bc = b * c * sin_alpha
    area_ac = a * c * sin_beta

    ! Calcular o volume
    volume = a * b * c * sqrt(1.0d0 + 2.0d0 * cos_alpha * cos_beta * cos_gamma - &
             cos_alpha**2 - cos_beta**2 - cos_gamma**2)

    ! Abrir o arquivo de saída para escrita
    iunit = 10
    open(unit=iunit, file='areas.dat', status='replace')

    ! Escrever os resultados no arquivo de saída
    write(iunit, '(A, F8.2, A)') 'Área da face ab: ', area_ab, ' Å²'
    write(iunit, '(A, F8.2, A)') 'Área da face bc: ', area_bc, ' Å²'
    write(iunit, '(A, F8.2, A)') 'Área da face ac: ', area_ac, ' Å²'
    write(iunit, '(A, F10.2, A)') 'Volume da célula unitária: ', volume, ' Å³'

    ! Fechar o arquivo de saída
    close(iunit)

    print *, "Arquivo areas.txt criado com sucesso."

end program calc_areas
