# Nombre: Elton Yael Hernández Pérez
# Fecha: 23/10/2024
# Descripción:
# Este programa determina si una persona puede acceder al bar "La Negra".
# Para ello, verifica que la edad sea igual o mayor a 18 y que el presupuesto sea de al menos 250.

print("*** Acceso al bar 'La Negra' ***")  # Muestra el título del programa.XD

# Solicita al usuario que ingrese su edad
edad = int(input("Ingrese su edad: "))

# Solicita al usuario que ingrese su presupuesto
pre = int(input("Ingrese su presupuesto: "))

# Verifica si cumple con los requisitos de edad y presupuesto para ingresar
if edad >= 18 and pre >= 250:
    print("¡Bienvenido a tu mejor bar!")  # Mensaje de bienvenida si cumple con los requisitos
else:
    print("¡Lo sentimos, ya estamos por cerrar!")  # Mensaje si no cumple con los requisitos
