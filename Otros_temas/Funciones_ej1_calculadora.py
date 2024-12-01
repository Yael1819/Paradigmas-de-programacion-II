# Nombre: Elton Yael Hernández Pérez
# Fecha: 7/11/2024
# Descripción: Calculadora básica con operaciones aritméticas.

# Función que realiza la operación seleccionada
def operacion(num1, num2, op):
    resultado = 0  # Inicializa la variable resultado

    # Condicional para determinar la operación
    if op == 1:  # Suma
        resultado = num1 + num2
    elif op == 2:  # Resta
        resultado = num1 - num2
    elif op == 3:  # Multiplicación
        resultado = num1 * num2
    elif op == 4:  # División
        if num2 != 0:  # Verifica que el divisor no sea cero
            resultado = num1 / num2
        else:
            print("Error: No se puede dividir entre cero.")  # Muestra mensaje de error
    elif op == 5:  # División entera
        if num2 != 0:  # Verifica que el divisor no sea cero
            resultado = num1 // num2
        else:
            print("Error: No se puede dividir entre cero.")  # Muestra mensaje de error
    elif op == 6:  # Exponenciación
        resultado = num1 ** num2  # Calcula num1 elevado a la potencia de num2

    return resultado  # Devuelve el resultado de la operación


# Función que muestra el menú y gestiona las operaciones
def menu():
    op = -1  # Inicializa la opción seleccionada con un valor no válido
    while op != 0:  # Bucle que se repite mientras el usuario no elija salir
        # Imprime las opciones del menú
        print("\nSeleccione una opción:")
        print("Suma [1]")
        print("Resta [2]")
        print("Multiplicación [3]")
        print("División [4]")
        print("División entera [5]")
        print("Exponenciación [6]")
        print("Salir [0]")

        # Solicita al usuario ingresar la opción
        op = int(input("Ingrese su opción: "))

        # Si la opción es salir, rompe el bucle
        if op == 0:
            break

        # Solicita los números para realizar la operación
        num1 = int(input("Ingrese el primer número: "))  # Primer número
        num2 = int(input("Ingrese el segundo número: "))  # Segundo número

        # Llama a la función operacion con los valores ingresados y la opción seleccionada
        resultado = operacion(num1, num2, op)

        # Muestra el resultado de la operación
        print(f"El resultado es: {resultado}")

    # Mensaje final cuando el usuario decide salir
    print("Programa terminado.")


# Llamada principal para ejecutar el programa
menu()
