'''
Nombre:Elton Yael Hernández Pérez
Fecha:20/10/2024
Descripción:Este programa que realiza operaciones básicas con dos números introducidos por el usuario
'''
# Se solicita al usuario que introduzca un número entero
numero1 = int(input("Introduce un número entero: "))

# Se solicita al usuario que introduzca otro número entero
numero2 = int(input("Introduce otro número entero: "))

# Se realizan las operaciones aritméticas básicas
suma = numero1 + numero2  # Suma de los dos números
resta = numero1 - numero2  # Resta de los dos números
mult = numero1 * numero2  # Multiplicación de los dos números
division = numero1 / numero2  # División de los dos números

# Se muestran los resultados de las operaciones realizadas
print(f"El resultado de la suma de {numero1} y {numero2} es: {suma}")
print(f"El resultado de la resta de {numero1} y {numero2} es: {resta}")
print(f"El resultado de la multiplicación de {numero1} y {numero2} es: {mult}")
print(f"El resultado de la división de {numero1} y {numero2} es: {division}")