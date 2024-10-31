# Nombre: Elton Yael Hernández Pérez
# Fecha: 30/10/2024
print("***programa para calcular el area y perimetro**")
op = -1
while op != 0:

    print("\nSeleccione una opción:")
    print("Calcular el área de un rectángulo. [1]")
    print("Calcular el perímetro de un rectángulo. [2]")
    print(" Calcular el área de un círculo. [3]")
    print(" Calcular el perímetro de un círculo. [4]")
    print("Salir [0]")


    op = int(input("Ingrese su opción: "))


    if op == 1:
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        area = base * altura
        print(f"El área del rectángulo es: {area:.2f}")
    elif op == 2:
        base = float(input("Ingrese la base del rectángulo: "))
        altura = float(input("Ingrese la altura del rectángulo: "))
        perimetro= 2*(base + altura)
        print(f"El perímetro del rectángulo es: {perimetro:.2f}")
    elif op == 3:
        radio = float(input("Ingrese el radio del círculo: "))
        pi = 3.1416
        area = pi * radio ** 2
        print(f"El área del círculo es: {area:.2f}")

    elif op == 4:
        radio = float(input("Ingrese el radio del círculo: "))
        pi = 3.1416
        perimetro = 2 * pi * radio
        print(f"El perímetro del círculo es: {perimetro:.2f}")

    elif op == 0:

        print("Gracias por utilizar nuestros servicios. Hasta luego.")
    else:
        print("Opción no válida, vuelva a intentar.")

print("Programa terminado.")