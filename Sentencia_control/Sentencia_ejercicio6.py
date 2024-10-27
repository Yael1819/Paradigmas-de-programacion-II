# Nombre: Elton Yael Hernández Pérez
# Fecha: 24/10/2024
# Descripción: Programa para calcular el costo total del tour turístico Ecoturixtlán

print("*** Tour turístico Ecoturixtlán ***")  # Muestra el título del programa

# a) Solicitar el nombre de la persona a cargo
nombre = input("Ingresa el nombre del cliente: ")

# b) Definir precios constantes para el boleto de adulto y de niño
precioadul = 200.00  # Precio de boleto para adultos
precioniño = 100.00  # Precio de boleto para niños

# c) Solicitar el número de adultos y niños
numadul = int(input("Ingresa el número de adultos: "))  # Número de boletos para adultos
numniño = int(input("Ingresa el número de niños: "))  # Número de boletos para niños

# d) Preguntar el día de la semana
dia = input("Ingresa el día de la semana: ").lower()  # Día en minúsculas para facilitar comparaciones

# e) Calcular el costo total sin descuento
costadul = numadul * precioadul  # Costo total para adultos
costaniño = numniño * precioniño  # Costo total para niños
costototal = costadul + costaniño  # Costo total sin aplicar descuentos

# Aplicar descuento si la visita es lunes, martes o jueves
if dia in ["lunes", "martes", "jueves"]:
    descuento = costototal * 0.10  # Descuento del 10% en ciertos días
    costototal -= descuento  # Se resta el descuento al costo total
else:
    descuento = 0.0  # Sin descuento para otros días

# f) Mostrar los detalles del cliente, el día, y el costo total
print(f"\nGracias por tu visita, {nombre}, este día {dia}. El costo total es de $ {costototal:.2f}")  # Mensaje final con detalles
