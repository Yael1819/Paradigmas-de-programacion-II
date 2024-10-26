# Nombre: Elton Yael Hernández Pérez
# Fecha: 18/10/2024
# Descripción: Este programa verifica si una persona forma parte de la comunidad de la UNSIJ,ya sea como profesor o como alumno.

# Mensaje de inicio
print("*** Comunidad UNSIJ ***")

# Verifica si la persona es profesor de la UNSIJ
cadena = input("¿Eres profesor de la UNSIJ (si/no)? : ")
resultado = cadena.lower() == "si"  # Verifica si la respuesta es "si" en minúsculas

# Verifica si la persona es alumno de la UNSIJ
cadena2 = input("¿Eres alumno de la UNSIJ (si/no)? : ")
resultado2 = cadena2.lower() == "si"  # Verifica si la respuesta es "si" en minúsculas

# Verifica si la persona es parte de la comunidad UNSIJ (como profesor o alumno)
es_parte_comunidad = resultado or resultado2

# Imprime si la persona forma parte de la comunidad de la UNSIJ
print(f"¿Formas parte de la comunidad de la UNSIJ? {es_parte_comunidad}")
