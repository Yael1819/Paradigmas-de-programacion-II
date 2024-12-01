# Nombre: Elton Yael Hernández Pérez
# Fecha: 7/11/2024
# Descripción: Programa para generar tres tipos de triángulos de asteriscos con funciones.


def triangulo_izquierda(n, asterisco):
    #Genera un triángulo alineado a la izquierda.
    print("\nTriángulo 1:")
    for i in range(1, n + 1):
        print(asterisco * i)

def triangulo_derecha(n, asterisco, espacio):
    #Genera un triángulo alineado a la derecha.
    print("\nTriángulo 2:")
    for i in range(1, n + 1):
        espacios = espacio * (n - i)
        print(f"{espacios}{asterisco * i}")

def triangulo_invertido(n, asterisco, espacio):
    #Genera un triángulo invertido alineado a la derecha.
    print("\nTriángulo 3:")
    for i in range(n, 0, -1):
        espacios = espacio * (n - i)
        print(f"{espacios}{asterisco * i}")

def main():
    #Función principal para ejecutar el programa.

    GREEN = "\033[32m"
    RESET = "\033[0m"
    print(f"\n\t{GREEN}| PIRÁMIDE |{RESET}\n")

    n = int(input("Ingrese el número de filas: "))
    asterisco = " * "  # Representa un asterisco con separación
    espacio = "   "    # Espacios ajustables para formato

    triangulo_izquierda(n, asterisco)
    triangulo_derecha(n, asterisco, espacio)
    triangulo_invertido(n, asterisco, espacio)

# Llamada directa a la función principal
main()
