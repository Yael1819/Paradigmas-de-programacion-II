# Nombre: Elton Yael Hernández Pérez
# Fecha: 26/10/2024
# Descripción:
# Este programa evalúa una expresión booleana basada en cuatro entradas del usuario.
# Convierte cada entrada a un valor booleano y aplica la expresión (exp1 o exp2) y (exp3 o exp4),
# devolviendo el resultado final de esta evaluación.

print("*** Expresión booleana (exp1 o exp2) y (exp3 o exp4) ***")  # Muestra el título de la expresión.

# Solicita los valores de las cuatro expresiones y verifica si son "v" (verdadero)
exp1 = input("Ingrese un valor (v/f) : ")
rest1 = exp1.lower() == "v"  # Convierte exp1 a un valor booleano basado en si es "v" o "f"

exp2 = input("Ingrese un valor (v/f) : ")
rest2 = exp2.lower() == "v"  # Convierte exp2 a un valor booleano

exp3 = input("Ingrese un valor (v/f) : ")
rest3 = exp3.lower() == "v"  # Convierte exp3 a un valor booleano

exp4 = input("Ingrese un valor (v/f) : ")
rest4 = exp4.lower() == "v"  # Convierte exp4 a un valor booleano

# Aplica la expresión booleana compuesta usando los valores booleanos de cada entrada
resultado = (rest1 or rest2) and (rest3 or rest4)

# Muestra el resultado de la evaluación booleana
print(f"El resultado de la expresión booleana es: {resultado}")
