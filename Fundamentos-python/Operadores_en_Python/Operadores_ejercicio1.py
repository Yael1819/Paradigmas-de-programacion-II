# Nombre: Elton Yael Hernández Pérez
# Fecha: 18/10/2024
# Descripción: Este programa verifica si una compra califica para una bonificación
# del Buen Fin, basada en el gasto y si la compra fue a meses sin intereses.

# Mensaje de inicio
print("Bonificación Buen Fin")

# Solicita al usuario que ingrese la cantidad gastada
gasto = int(input("Ingrese la cantidad gastada: "))

# Verifica si el gasto es mayor o igual a 5000
entra = (gasto >= 5000)

# Pregunta si la compra fue a meses sin intereses
cadena = input("¿La compra fue a meses sin intereses? (si/no): ")
resultado = cadena.lower() == "si"  # Verifica si la respuesta es "si" en minúsculas

# Determina si la compra califica para la bonificación
bonificacion = resultado and entra

# Imprime si la compra califica para la bonificación
print(f"La compra califica para la bonificación? {bonificacion}")
