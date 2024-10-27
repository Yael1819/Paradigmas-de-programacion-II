# Nombre: Elton Yael Hernández Pérez
# Fecha: 24/10/2024
# Descripción:
# Este programa calcula el promedio final de una materia utilizando las calificaciones
# de tres parciales y un examen ordinario. Evalúa si el promedio es suficiente para aprobar.

print("*** Programa para calcular el promedio de la materia ***")  # Muestra el título del programa.

# Solicitar las calificaciones de los tres parciales
par1 = float(input("Ingrese la calificación del parcial 1: "))
par2 = float(input("Ingrese la calificación del parcial 2: "))
par3 = float(input("Ingrese la calificación del parcial 3: "))

# Solicitar la calificación del examen ordinario
ordi = float(input("Ingrese la calificación del ordinario: "))

# Calcular el aporte del examen ordinario (mitad del valor) y el promedio de los parciales
ordi = ordi / 2  # Ajusta la calificación del ordinario dividiéndola entre 2
promedio = (par1 + par2 + par3) / 6  # Calcula el promedio de los parciales
promedio = promedio + ordi  # Suma el valor ajustado del ordinario al promedio

# Evaluar si el promedio es suficiente para aprobar
if promedio >= 6:
    print(f"Su calificación es de {promedio:.1f}. ¡Felicidades! Aprobaste")  # Mensaje si aprueba
else:
    print(f"Su calificación es de {promedio:.1f}. Lo siento, no aprobaste.")  # Mensaje si no aprueba
