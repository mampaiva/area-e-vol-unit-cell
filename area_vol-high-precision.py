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
    alpha = Decimal(values[3])  # Ângulo em graus
    beta = Decimal(values[4])   # Ângulo em graus
    gamma = Decimal(values[5])  # Ângulo em graus

# Converter ângulos para radianos
alpha_rad = alpha * Decimal(math.pi) / Decimal(180)
beta_rad = beta * Decimal(math.pi) / Decimal(180)
gamma_rad = gamma * Decimal(math.pi) / Decimal(180)

# Calcular os cossenos e senos dos ângulos
cos_alpha = Decimal(math.cos(float(alpha_rad)))
cos_beta = Decimal(math.cos(float(beta_rad)))
cos_gamma = Decimal(math.cos(float(gamma_rad)))
sin_alpha = Decimal(math.sin(float(alpha_rad)))
sin_beta = Decimal(math.sin(float(beta_rad)))
sin_gamma = Decimal(math.sin(float(gamma_rad)))

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
