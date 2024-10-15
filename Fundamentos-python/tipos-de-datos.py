# Nombre: Elton Yael Hernández Pérez
# Fecha: 14/10/2024
# Descripción:
# Usos de los tipos básicos de datos en Python.

# Notas:
"""
En Python, no se requiere indicar el tipo de la variable en su declaración.
Los valores básicos que pueden almacenar las variables son:
- Int
- Float
- String (str)
- Boolean: True o False (con inicial mayúscula).
- None: Tipo especial que representa una ausencia de valor.
"""

# Uso de constantes.
'''
En Python, a diferencia de otros lenguajes de programación, no existe un tipo específico para definir constantes.
Se utiliza una convención de colocar las variables en mayúsculas y no modificarlas.
'''
VARIABLE_CONSTANTE = 3.1416
print("Ejemplo de convención de una constante:", VARIABLE_CONSTANTE)

# Definimos el presupuesto diario
presupuesto_diario = 100.0

# Lista de días de la semana
dias_semana = ["lunes", "martes", "miércoles", "jueves", "viernes", "sábado", "domingo"]

for dia in dias_semana:
    print("\n*** Gastos diarios ***")
    print(f"Día: {dia}")

    # Pedimos al usuario ingresar sus gastos para el día actual
    pasaje = float(input("Pasaje: "))
    comida = float(input("Comida: "))
    otros = float(input("Otros gastos: "))

    # Calculamos el gasto total
    gasto_total = pasaje + comida + otros

    # Verificamos si el gasto total supera el presupuesto
    es_mayor = gasto_total > presupuesto_diario

    # Mostramos los resultados
    print(f"¿Fue mayor a mi presupuesto?: {es_mayor}")
