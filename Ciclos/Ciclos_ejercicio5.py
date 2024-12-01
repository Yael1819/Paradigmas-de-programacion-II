# Nombre: Elton Yael Hernández Pérez
# Fecha: 7/11/2024
# Descripción: Este programa genera tres tipos de triángulos formados por asteriscos,
# utilizando bucles for y cadenas de texto. Se pueden ajustar las filas del triángulo
# ingresando un número.

GREEN = "\033[32m"
RESET = "\033[0m"

print(f"\n\t{GREEN}| PIRÁMIDE |{RESET}\n")


n = int(input("Ingrese el número de filas: "))

# Variables para construir el triángulo
asterisco = " * "  # Representa un asterisco con espacio adicional para separación
espacio = "   "     # Espacio entre caracteres, ajustable para formato

# Triángulo 1: Imprime asteriscos alineados a la izquierda
print("\nTriángulo 1:")
for i in range(1, n + 1):  # Itera desde 1 hasta n
    print(asterisco * i)  # Imprime i veces el asterisco en cada fila

# Triángulo 2: Imprime asteriscos alineados a la derecha
print("\nTriángulo 2:")
for i in range(1, n + 1):                 # Itera desde 1 hasta n
    espacios = espacio * (n - i)         # Calcula los espacios necesarios para alinear a la derecha
    print(f"{espacios}{asterisco * i}")  # Combina espacios y asteriscos para cada fila

# Triángulo 3: Imprime asteriscos invertidos alineados a la derecha
print("\nTriángulo 3:")
for i in range(n, 0, -1):                # Itera desde n hasta 1 (triángulo invertido)
    espacios = espacio * (n - i)         # Calcula los espacios necesarios para alinear a la derecha
    print(f"{espacios}{asterisco * i}")  # Combina espacios y asteriscos para cada fila
