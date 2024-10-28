# Nombre: Elton Yael Hernández Pérez
# Fecha: 25/10/2024
# Descripción: Programa para la gestión de una cuenta bancaria. Permite consultar saldo, ingresar dinero y retirar dinero,
# actualizando el saldo según las operaciones seleccionadas por el usuario.

# Mensaje inicial para el usuario
print("*** Cuenta de banco ***")

# Inicializa la variable de opción en un valor distinto de 0 para entrar en el ciclo
op = -1

# Inicializa el saldo de la cuenta en 0.00
saldo = 0.00

# Ciclo `while` que se repite mientras la opción sea diferente de 0
while op != 0:
    # Muestra el menú de opciones al usuario
    print("\nSeleccione una opción:")
    print("Consultar saldo [1]")
    print("Ingresar dinero [2]")
    print("Retirar dinero [3]")
    print("Salir [0]")

    # Lee la opción seleccionada por el usuario
    op = int(input("Ingrese su opción: "))

    # Realiza la operación correspondiente según la opción seleccionada
    if op == 1:
        # Opción para consultar el saldo actual
        print(f"Su saldo es de: $ {saldo:.2f}")
    elif op == 2:
        # Opción para ingresar dinero a la cuenta
        ingreso = float(input("Ingrese la cantidad de dinero a ingresar: "))
        saldo += ingreso  # Suma el ingreso al saldo actual
        print(f"Su saldo actual es de: $ {saldo:.2f}")
    elif op == 3:
        # Opción para retirar dinero de la cuenta
        retiro = float(input("Ingrese la cantidad de dinero a retirar: "))
        if retiro <= saldo:
            saldo -= retiro  # Resta el retiro del saldo si hay fondos suficientes
            print(f"Su saldo actual es de: $ {saldo:.2f}")
        else:
            print("Fondos insuficientes para realizar el retiro.")  # Mensaje de error si no hay fondos suficientes
    elif op == 0:
        # Opción para salir del programa
        print("Gracias por utilizar nuestros servicios. Hasta luego.")
    else:
        print("Opción no válida, vuelva a intentar.")  # Mensaje de error para opción no válida

# Mensaje final cuando el programa termina
print("Programa terminado.")
