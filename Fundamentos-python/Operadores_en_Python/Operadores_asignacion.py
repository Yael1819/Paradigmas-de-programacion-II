"""
Nombre: Elton Yael Hernández Pérez
Fecha: 17/10/2024
Descripción: Este programa demuestra la asignación múltiple y encadenada de variables,
el intercambio de variables, y la entrada de múltiples valores.
"""

# Asignación múltiple: se asignan varios valores a múltiples variables en una sola línea
n1, n2 = 7, 10      # n1 se asigna a 7 y n2 a 10
n3, cadenas, n4 = 11, "hola", 9  # n3 se asigna a 11, cadenas a "hola", y n4 a 9
suma, resta = n1 + n2, n1 - n2   # Calcula la suma y la resta de n1 y n2

# Asignación encadenada: se asigna el mismo valor a múltiples variables
n5 = n6 = n7 = 12  # n5, n6 y n7 se asignan el valor 12

# Imprime los resultados de la asignación múltiple
print("Asignación múltiple")
print(n1)      # Imprime el valor de n1
print(n2)      # Imprime el valor de n2
print(n3)      # Imprime el valor de n3
print(cadenas)  # Imprime el valor de cadenas
print(n4)      # Imprime el valor de n4
print(suma)    # Imprime el resultado de la suma
print(resta)   # Imprime el resultado de la resta

# Imprime los resultados de la asignación encadenada
print("# Asignación encadenada")
print(n5)      # Imprime el valor de n5
print(n6)      # Imprime el valor de n6
print(n7)      # Imprime el valor de n7

# Intercambio de variables
print("Intercambio de variables")
n8 = int(input("Ingrese un número: "))  # Solicita un número y lo asigna a n8
n9 = int(input("Ingrese un número: "))  # Solicita otro número y lo asigna a n9
print(n8, n9)  # Imprime los valores originales de n8 y n9
n8, n9 = n9, n8  # Intercambia los valores de n8 y n9
print(n8, n9)  # Imprime los valores intercambiados

# Entrada de múltiples valores
print("Múltiples valores de entrada")
n10, n11 = int(input("Ingrese un número: ")), int(input("Ingrese un número: "))  # Solicita dos números
print(n10)  # Imprime el primer número ingresado
print(n11)  # Imprime el segundo número ingresado
