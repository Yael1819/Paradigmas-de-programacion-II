# Nombre: Elton Yael Hernández Pérez
# Fecha: 23/10/2024
# Descripción:
# Este programa calcula un descuento basado en la cantidad comprada y si el cliente tiene membresía.
# Si la compra es igual o mayor a 1000 y tiene membresía, aplica un 8% de descuento.
# Sin membresía, aplica un 5% de descuento. Si la compra es menor a 1000, no hay descuento.

print("*** Descuentos por ser miembros de 'La Cona' ***")  # Muestra el título del programa.

# Solicita al usuario que ingrese la cantidad de la compra
cuenta = int(input("Ingrese la cantidad comprada: "))

# Verifica si el usuario cuenta con la membresía
cadena = input("¿Cuenta con la membresía (si/no)? : ")
resultado = cadena.lower()  # Convierte la respuesta a minúsculas para consistencia

# Determina si el monto es elegible para un descuento
descuento = (cuenta >= 1000)

# Calcula el descuento y el total según si tiene membresía y el monto de la compra
if cuenta >= 1000 and resultado == "si":
    rebaja = cuenta * 0.08  # Descuento del 8% si es miembro
    total = cuenta - rebaja
    print(f"Su descuento es del 8%, equivalente a ${rebaja:.2f}, y su total es de: ${total:.2f}")

elif cuenta >= 1000 and resultado == "no":
    rebaja = cuenta * 0.05  # Descuento del 5% si no es miembro
    total = cuenta - rebaja
    print(f"Su descuento es del 5%, equivalente a ${rebaja:.2f}, y su total es de: ${total:.2f}")

else:
    # Mensaje si el monto es menor a 1000, sin descuento, e invitación a ser miembro
    print("Se le invita a ser miembro de la tienda para obtener un descuento de hasta un 8%")
    print(f"El total es de: ${cuenta:.2f}")
