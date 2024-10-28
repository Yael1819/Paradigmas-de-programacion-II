## Nombre: Elton Yael Hernández Pérez
# Fecha: 24/10/2024
# Descripción: Este programa calcula la suma acumulativa entre dos números ingresados por el usuario,
# sumando todos los números en el rango desde el número inicial hasta el número final, inclusive.

# Mensaje inicial para el usuario
print("*** Ejercicio que calcula la suma acumulativa entre dos números ***")

# Solicita al usuario el número inicial y final del rango
num1 = int(input("Ingrese el número inicial: "))
num2 = int(input("Ingrese el número final: "))

# Inicializa el contador en el valor del número inicial y el acumulador en 0
i = num1
acum = 0

# Ciclo `while` que recorre desde `num1` hasta `num2`
while i <= num2:
    acum += i       # Suma el valor de `i` a `acum`
    i = i + 1       # Incrementa `i` en 1 en cada iteración

# Imprime el resultado de la suma acumulativa
print(f"La suma de {num1} hasta {num2} es {acum}")
