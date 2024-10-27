# Nombre: Elton Yael Hernández Pérez
# Fecha: 23/10/2024
# Descripción: Este programa identifica la estación del año en función del número de mes ingresado.
# Compara el mes con varios rangos para determinar si es primavera, verano, otoño o invierno.

print("*** Programa que determina la estación del año ***")
# Solicita al usuario que ingrese el número de un mes (1-12)
num1 = int(input("Ingrese el número del mes: "))

# Determina la estación en función del número del mes
if num1 == 3 or num1 == 4 or num1 == 5:
    print("Primavera")  # Meses de marzo, abril, mayo
elif num1 == 6 or num1 == 7 or num1 == 8:
    print("Verano")  # Meses de junio, julio, agosto
elif num1 == 9 or num1 == 10 or num1 == 11:
    print("Otoño")  # Meses de septiembre, octubre, noviembre
elif num1 == 12 or num1 == 1 or num1 == 2:
    print("Invierno")  # Meses de diciembre, enero, febrero
else:
    print("Fuera de rango: mes incorrecto")  # Mensaje para valores fuera del rango 1-12
