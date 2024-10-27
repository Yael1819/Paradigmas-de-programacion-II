# Nombre: Elton Yael Hernández Pérez
# Fecha: 23/10/2024
# Descripción:
# Este programa determina si un número ingresado por el usuario es par o impar.
# Utiliza la operación de módulo para evaluar la paridad del número
# y muestra un mensaje acorde al resultado.

print("*** Número par o impar ***")  # Muestra el título del programa.

# Solicita al usuario que ingrese un número
num = int(input("Ingrese un número: "))

# Verifica si el número es par o impar usando la operación módulo
if num % 2 == 0:
    print("Su número es par")  # Muestra un mensaje si el número es par
else:
    print("Su número es impar")  # Muestra un mensaje si el número es impar
