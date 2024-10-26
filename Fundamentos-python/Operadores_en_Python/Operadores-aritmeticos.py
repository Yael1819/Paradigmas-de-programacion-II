"""
# Nombre: Elton Yael Hernández Pérez
# Fecha: 18/10/2024
# Descripción: Este programa realiza operaciones básicas entre dos números ingresados por el usuario.
"""

# Solicita al usuario que introduzca el primer número decimal y lo convierte a entero
numero1 = int(input("Introduce un número decimal: "))

# Solicita al usuario que introduzca el segundo número decimal y lo convierte a entero
numero2 = int(input("Introduce otro número decimal: "))

# Calcula la suma de los dos números
suma = numero1 + numero2

# Calcula la resta del primer número menos el segundo
resta = numero1 - numero2

# Calcula la división del primer número entre el segundo
division = numero1 / numero2

# Calcula la multiplicación de los dos números
mult = numero1 * numero2

# Calcula el módulo (residuo) de la división del primer número entre el segundo
modulo = numero1 % numero2

# Calcula la potenciación del primer número elevado al segundo número
doble_aste = numero1 ** numero2

# Calcula la división entera del primer número entre el segundo (sin decimales)
diagonal = numero1 // numero2

# Muestra el resultado de la suma
print(f"El resultado de la suma entre {numero1} y {numero2} es: {suma}")

# Muestra el resultado de la resta
print(f"El resultado de la resta entre {numero1} y {numero2} es: {resta}")

# Muestra el resultado de la multiplicación
print(f"El resultado de la multiplicación entre {numero1} y {numero2} es: {mult}")

# Muestra el resultado de la división con tres decimales
print(f"El resultado de la división entre {numero1} y {numero2} es: {division:.3f}")

# Muestra el resultado del módulo (residuo)
print(f"El residuo de dividir {numero1} entre {numero2} es: {modulo}")

# Muestra el resultado de la potenciación
print(f"El resultado de {numero1} elevado a la potencia de {numero2} es: {doble_aste}")

# Muestra el resultado de la división entera
print(f"El resultado de la división entera entre {numero1} y {numero2} es: {diagonal}")
