# Nombre: Elton Yael Hernández Pérez
# Fecha: 21/10/2024
# Descripción: Este programa solicita al usuario los datos de un profesor, incluyendo nombre, número de cubículo, horas de clase impartidas a la semana y si tiene más de 5 años trabajando en la UNSIJ. Los datos se ingresan por teclado y se convierten a los tipos de datos adecuados.

# Solicitar datos de los profesores
nombre = input("Ingrese el nombre del profesor: ")
numero_cubiculo = int(input("Ingrese el número de cubículo: "))
horas_clase_semana = float(input("Ingrese las horas de clase a la semana (formato con 3 decimales): "))
tiene_mas_5_anios = input("¿Tiene más de 5 años en la UNSIJ? (sí/no): ").strip().lower() == "sí"

# Mostrar los datos en consola
print("\n--- Datos del Profesor ---")
print(f"Nombre: {nombre}")
print(f"Número de cubículo: {numero_cubiculo}")
print(f"Horas de clase a la semana: {horas_clase_semana:.3f}")
print(f"Tiene más de 5 años en la UNSIJ: {tiene_mas_5_anios}")