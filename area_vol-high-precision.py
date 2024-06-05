from decimal import Decimal, getcontext
import math

# Definir a precisão desejada
getcontext().prec = 50

# Ler os parâmetros do arquivo de entrada
with open('input.dat', 'r') as file:
    line = file.readline()
    values = line.split()
    a = Decimal(values[0])
    b = Decimal(values[1])
    c = Decimal(values[2])
    cos_alpha = Decimal(values[3])
    cos_beta = Decimal(values[4])
    cos_gamma = Decimal(values[5])

# Calcular os senos dos ângulos
sin_alpha = (Decimal(1) - cos_alpha**2).sqrt()
sin_beta = (Decimal(1) - cos_beta**2).sqrt()
sin_gamma = (Decimal(1) - cos_gamma**2).sqrt()

# Calcular as áreas das faces
area_ab = a * b * sin_gamma
area_bc = b * c * sin_alpha
area_ac = a * c * sin_beta

# Calcular o volume
volume = a * b * c * (Decimal(1) + 2 * cos_alpha * cos_beta * cos_gamma - cos_alpha**2 - cos_beta**2 - cos_gamma**2).sqrt()

# Escrever os resultados no arquivo de saída
with open('areas.txt', 'w') as file:
    file.write(f"Área da face ab: {area_ab} Å²\n")
    file.write(f"Área da face bc: {area_bc} Å²\n")
    file.write(f"Área da face ac: {area_ac} Å²\n")
    file.write(f"Volume da célula unitária: {volume} Å³\n")

print("Arquivo areas.txt criado com sucesso.")

