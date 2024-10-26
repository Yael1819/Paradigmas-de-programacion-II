# Nombre: Elton Yael Hernández Pérez
# Fecha: 18/10/2024
# Descripción: Este programa evalúa respuestas de "sí" o "no" y muestra el resultado de varias operaciones lógicas.

# Solicita al usuario que ingrese "si" o "no" y convierte la entrada a minúsculas
cadena = input("Ingrese si/no: ")
resultado = cadena.lower() == "si"  # Verifica si la entrada es "si"
print(f"El resultado es 'si'? {resultado}")  # Imprime el resultado de la comparación

# Solicita al usuario que ingrese "si" o "no" nuevamente
cadena2 = input("Ingrese si/no: ")
resultado2 = cadena2.lower() == "si"  # Verifica si la entrada es "si"
print(f"El resultado es 'si'? {resultado2}")  # Imprime el resultado de la comparación

# Evalúa si ambos resultados son verdaderos
print(f"¿Los dos valores son verdaderos? {resultado and resultado2}")

# Evalúa si al menos uno de los dos resultados es verdadero
print(f"¿Alguno de los dos valores es verdadero? {resultado or resultado2}")

# Muestra el valor del primer resultado negado
print(f"El valor del primer resultado con 'not' es {not resultado}")

# Muestra el valor del segundo resultado negado
print(f"El valor del segundo resultado con 'not' es {not resultado2}")
