# Nombre: Elton Yael Hernández Pérez
# Fecha: 24/10/2024
# Descripción: Este programa calcula la suma acumulativa desde 0 hasta un número ingresado por el usuario,
# mostrando cada número en el rango y luego la suma total de dichos números.

# Mensaje inicial para el usuario
print("*** Ejercicio que calcula la suma acumulativa ***")

# Solicita al usuario un número entero
num1 = int(input("Ingrese el número: "))

# Inicializa el contador y el acumulador
i = 0
acum = 0

# Ciclo `while` que recorre desde 0 hasta `num1`
while i <= num1:
    print(i, end=" ")   # Imprime cada número en la misma línea
    acum += i           # Suma el valor de `i` a `acum`
    i = i + 1           # Incrementa `i` en 1 en cada iteración

# Imprime el resultado de la suma acumulativa
print(f"\nLa suma de 0 hasta {num1} es {acum}")
