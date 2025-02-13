# Nombre: Elton Yael Hernández Pérez
# Fecha: 14/10/2024
# En este archivo se ejemplifica el uso de variables en Python.

# Notas:
# En Python, todo es un objeto.
# Variable - una variable es un nombre que almacena un valor guardado en la memoria temporal.

# Toda variable requiere un valor inicial
semestre = 3        # Es una variable que apunta a un objeto de tipo int con valor de 3
print(semestre)     # Imprime el valor de la variable
semestre = 4        # La variable ya no apunta al objeto anterior, sino a uno nuevo, por lo que se pierde la referencia
print(semestre)

# Se crean varias variables para ejemplificar su uso
nombre = "Elton"    # Variable de tipo String
altura = 1.73       # Variable de tipo Float
edad = 20           # Variable de tipo Int

# Se modifican los valores de las variables y se mandan a imprimir
print()
print("Valores modificados:")
print("Nombre:", nombre)
print("Semestre:", semestre)
print("Altura:", altura, "m.")
print("Edad:", edad, "años.")

# En Python, las variables son dinámicas, por lo que pueden almacenar otro tipo de dato en cualquier momento
edad = "treinta y uno"  # 'edad' antes tenía el valor de 20 (Int)
print()
print("Edad (con otro tipo de dato):", edad)

# Reglas para los nombres de las variables en Python:
# - Utilizar únicamente letras (mayúsculas o minúsculas), números y el guion bajo (_).
# - La variable no puede iniciar con números.
# - No se pueden utilizar palabras reservadas, ejemplos: if, else, True, class.
# - Es sensible a mayúsculas y minúsculas. Por ejemplo, las palabras "Hola", "hola" y "HOLA" son consideradas diferentes.

# Buenas prácticas:
# - Utilizar minúsculas para las palabras.
# - Separar las palabras con el guion bajo (_).
# - Utilizar nombres descriptivos de acuerdo a su uso. Por ejemplo: edad, en lugar de 'e'.

# Ejemplos correctos y con buenas prácticas
fecha_nacimiento = "4 de mayo del 2004"
clase = "Paradigmas de programación II"
horas_estudio = 8
nombre = "Elton"
es_estudiante = True

# Ejemplos incorrectos (líneas comentadas porque marcan error) o de malas prácticas
f = "4 de mayo del 2004"        # No es descriptivo
fechanacimiento = "1 de enero del 2000"  # Falta el guion bajo para separar palabras
# class = "Paradigmas de programación II"  # 'class' es una palabra reservada en Python
# 8horas_estudio = 8                       # No puede comenzar con un número
Nombre = "E l t o n"           # No sigue la convención de minúsculas
NOMBRE = "ELTON"               # Es preferible utilizar minúsculas

# Notar que las variables 'nombre', 'Nombre' y 'NOMBRE' son distintas
print()
print("Las variables son sensibles a mayúsculas y minúsculas:")
print("Variable nombre:", nombre)
print("Variable Nombre:", Nombre)
print("Variable NOMBRE:", NOMBRE)
