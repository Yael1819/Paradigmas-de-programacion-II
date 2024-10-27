# Nombre: Elton Yael Hernández Pérez
# Fecha: 23/10/2024
# Descripción:
# Este programa clasifica la edad de una persona en diferentes categorías.
# Pide la edad al usuario y la compara con distintos rangos para determinar
# si es un infante, joven, adulto joven, adulto maduro o adulto mayor.

print("*** Rango de edades ***")  # Muestra el título del programa.

# Solicita al usuario que ingrese su edad
edad = int(input("Ingrese un número: "))

# Clasificación por rangos de edad
if edad >= 0 and edad < 14:
    print("Infante o adolescente")  # Edad entre 0 y 13 años
elif edad >= 14 and edad < 24:
    print("Joven")  # Edad entre 14 y 23 años
elif edad >= 24 and edad < 44:
    print("Adulto joven")  # Edad entre 24 y 43 años
elif edad >= 44 and edad < 60:
    print("Adulto maduro")  # Edad entre 44 y 59 años
elif edad >= 60:
    print("Adulto mayor")  # Edad de 60 años en adelante
else:
    print("Edad no válida")  # Mensaje si se ingresa una edad negativa

