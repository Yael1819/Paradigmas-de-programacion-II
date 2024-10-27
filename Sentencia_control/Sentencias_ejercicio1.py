# Nombre: Elton Yael Hernández Pérez
# Fecha: 23/10/2024
# Descripción: Este programa compara dos números ingresados por el usuario
# y determina cuál es menor. Si son iguales, también lo indica.

print("*** Programa para determinar cuál de los dos números es menor ***")  # Muestra el título del programa.

# Solicitar la entrada de los dos números
num1 = int(input("Ingrese un número: "))  # Primer número ingresado por el usuario
num2 = int(input("Ingrese otro número: "))  # Segundo número ingresado por el usuario

# Comparar los números e imprimir el resultado
if num1 < num2:
    print(f"El número {num1} es menor que {num2}")  # Indica que num1 es menor
elif num2 < num1:
    print(f"El número {num2} es menor que {num1}")  # Indica que num2 es menor
else:
    print("Ambos números son iguales.")  # Mensaje si ambos números son iguales
