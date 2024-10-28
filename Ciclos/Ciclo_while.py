# Nombre: Elton Yael Hernández Pérez
# Fecha: 24/10/2024
# Descripción: Este programa solicita dos números al usuario y utiliza ciclos `while`
# para imprimir los números consecutivos desde 0 hasta el número ingresado,
# y luego, los números pares desde 0 hasta otro número ingresado por el usuario.

# Ejemplo de ciclo `while` que imprime números del 0 al número ingresado
print("*** Ejemplo de ciclo while ***")

# Solicita al usuario un número y lo convierte a entero
num1 = int(input("Ingrese el número: "))

# Inicializa el contador en 0
i = 0

# Imprime el mensaje de salida con el número ingresado
print(f"Los números ingresados por el usuario del 0 al {num1} son: ", end="")

# Ciclo `while` que recorre desde 0 hasta `num1`
while i <= num1:
    print(i, end=" ")  # Imprime el valor de `i` en la misma línea
    i = i + 1          # Incrementa `i` en 1 en cada iteración

# Imprime una línea nueva al finalizar el ciclo
print("\n")
print("Fin de la impresión")  # Mensaje de finalización


# Ejemplo de ciclo `while` que imprime números pares del 0 al número ingresado
print("*** Ejemplo de ciclo while - Números pares ***")

# Solicita al usuario otro número y lo convierte a entero
num2 = int(input("Ingrese el número: "))

# Inicializa el contador en 0
t = 0

# Imprime el mensaje de salida con el número ingresado
print(f"Los números pares ingresados por el usuario del 0 al {num2} son: ", end="")

# Ciclo `while` que recorre desde 0 hasta `num2`
while t <= num2:
    if t % 2 == 0:         # Verifica si `t` es un número par
        print(t, end=" ")  # Imprime el número par en la misma línea
    t = t + 1              # Incrementa `t` en 1 en cada iteración

# Imprime una línea nueva al finalizar el ciclo
print("\n")
print("Fin de la impresión")  # Mensaje de finalización
