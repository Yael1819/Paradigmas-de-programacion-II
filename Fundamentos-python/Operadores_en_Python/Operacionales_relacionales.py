# Nombre: Elton Yael Hernández Pérez
# Fecha: 18/10/2024
# Descripción: Este programa compara dos números decimales ingresados por el usuario y determina sus relaciones (mayor que, menor que, igual, etc.).

# Solicita al usuario que introduzca dos números decimales y los convierte a tipo float
numero1 = float(input("Introduce un número decimal: "))  # Primer número ingresado
numero2 = float(input("Introduce otro número decimal: "))  # Segundo número ingresado

# Compara si el primer número es mayor que el segundo
mayor1 = numero1 > numero2
print(f"Es {mayor1} que {numero1} es mayor que {numero2}.")  # Imprime el resultado de la comparación

# Compara si el segundo número es mayor que el primero
mayor2 = numero2 > numero1
print(f"Es {mayor2} que {numero1} es menor que {numero2}.")  # Imprime el resultado de la comparación

# Compara si los dos números son iguales
igual = (numero2 == numero1)
print(f"Es {igual} que {numero1} es igual a {numero2}.")  # Imprime el resultado de la comparación

# Compara si el primer número es mayor o igual que el segundo
igualmayor = numero1 >= numero2
print(f"Es {igualmayor} que {numero1} es mayor o igual que {numero2}.")  # Imprime el resultado

# Compara si el primer número es menor o igual que el segundo
igualmenor = numero1 <= numero2
print(f"Es {igualmenor} que {numero1} es menor o igual que {numero2}.")  # Imprime el resultado



