# Nombre: Elton Yael Hernández Pérez
# Fecha: 25/10/2024
# Descripción: Calculadora con opciones de suma, resta, multiplicación, división, división entera y exponenciación.
# El usuario puede elegir la operación que desea realizar entre dos números ingresados. El programa se repite
# hasta que el usuario decida salir.

# Mensaje inicial para el usuario
print("*** Ejercicio de una calculadora ***")

# Solicita al usuario los dos números con los que desea operar
num1 = int(input("Ingrese el primer número: "))
num2 = int(input("Ingrese el segundo número: "))

# Inicializa la variable de opción en un valor distinto de 0 para entrar en el ciclo
op = -1

# Ciclo `while` que se repite mientras la opción sea diferente de 0
while op != 0:
    # Muestra el menú de opciones al usuario
    print("\nSeleccione una opción:")
    print("Suma [1]")
    print("Resta [2]")
    print("Multiplicación [3]")
    print("División [4]")
    print("División entera [5]")
    print("Exponenciación [6]")
    print("Salir [0]")

    # Lee la opción seleccionada por el usuario
    op = int(input("Ingrese su opción: "))

    # Realiza la operación correspondiente según la opción seleccionada
    if op == 1:
        resultado = num1 + num2
        print(f"La suma de {num1} + {num2} = {resultado}")
    elif op == 2:
        resultado = num1 - num2
        print(f"La resta de {num1} - {num2} = {resultado}")
    elif op == 3:
        resultado = num1 * num2
        print(f"La multiplicación de {num1} * {num2} = {resultado}")
    elif op == 4:
        if num2 != 0:  # Evita la división entre cero
            resultado = num1 / num2
            print(f"La división de {num1} / {num2} = {resultado}")
        else:
            print("Error: No se puede dividir entre cero.")
    elif op == 5:
        if num2 != 0:  # Evita la división entera entre cero
            resultado = num1 // num2
            print(f"La división entera de {num1} // {num2} = {resultado}")
        else:
            print("Error: No se puede dividir entre cero.")
    elif op == 6:
        resultado = num1 ** num2
        print(f"La exponenciación de {num1} ** {num2} = {resultado}")
    elif op == 0:
        print("Gracias, hasta luego.")  # Mensaje de despedida
    else:
        print("Opción no válida, por favor ingrese una opción correcta.")  # Manejo de opción no válida

# Mensaje final cuando el programa termina
print("Programa terminado.")
