# Nombre: Elton Yael Hernández Pérez
# Fecha: 14/10/2024
# Descripción:
# Conversión de tipos de datos (casting) en Python.

# Notas
"""
La conversión de tipos de datos implica manipular datos que no están en el tipo de dato requerido. Ejemplos:
de cadena a entero, de cadena a número flotante, y viceversa.
"""

# *****   Conversión de cadena a entero     *****
var_cadena = "951"
var_int = int(var_cadena)  # Convertimos la cadena a un número entero

# Utiliza la letra "f" antes de las comillas para indicar que la cadena será formateada.
# Esto significa que puedes incluir variables y expresiones dentro de las llaves {}
# y su valor será insertado en el texto final.
print("Conversión de cadena a entero.")
print(f"Número como cadena: {var_cadena}.")
print(f"Número como int más uno: {var_int + 1}.")

# Ejemplo de mal formato o cadena sin conversión
print(f"El número en la cadena es: {var_cadena}")

# *****   Conversión de cadena a flotante     *****
var_cadena = "8.88"
var_float = float(var_cadena)  # Convertimos la cadena a un número flotante
print()
print("Conversión de cadena a flotante.")
print(f"Número como cadena: {var_cadena}.")
print(f"Número como float más cero punto uno: {var_float + 0.1}.")

# *****   Conversión de número a cadena     *****
var_int = 123
var_float = 123.321
print()
print("Conversión de número a cadena.")
print(f"Los números {var_int} y {var_float} se convierten a cadena utilizando str(var_int): '{str(var_int)}', y "
      f"str(var_float): '{str(var_float)}'.")

# *****   Conversión a booleano     *****
# Si el valor es 0, cadena vacía o None, la función bool regresa un valor de False. En caso contrario, regresa True.
print()
print("Conversión a booleanos.")

var_int = 0
es_verdadero = bool(var_int)
print(f"¿El valor de {var_int} es verdadero? {es_verdadero}.")
var_int = -30
es_verdadero = bool(var_int)
print(f"¿El valor de {var_int} es verdadero? {es_verdadero}.")

var_float = 0.0
es_verdadero = bool(var_float)
print(f"¿El valor de {var_float} es verdadero? {es_verdadero}.")
var_float = 0.01
es_verdadero = bool(var_float)
print(f"¿El valor de {var_float} es verdadero? {es_verdadero}.")

var_cadena = ""
es_verdadero = bool(var_cadena)
print(f"¿El valor de una cadena vacía es verdadero? {es_verdadero}.")
var_cadena = None
es_verdadero = bool(var_cadena)
print(f"¿El valor None es verdadero? {es_verdadero}.")
var_cadena = " "
es_verdadero = bool(var_cadena)
print(f"¿El valor de una cadena con un espacio es verdadero? {es_verdadero}.")

# ***** Parte a: Conversión de número a cadena *****
num1 = 3.14159265
num2 = 12
num3 = 0

str1 = str(num1)
str2 = str(num2)
str3 = str(num3)

print("Parte a:")
print(f"El número {num1} convertido en cadena es: '{str1}'")
print(f"El número {num2} convertido en cadena es: '{str2}'")
print(f"El número {num3} convertido en cadena es: '{str3}'")
print()

# Parte b: Indicar valor booleano de los números
bool1 = bool(num1)
bool2 = bool(num2)
bool3 = bool(num3)

print("Parte b:")
print(f"El valor booleano de {num1} es: {bool1}")
print(f"El valor booleano de {num2} es: {bool2}")
print(f"El valor booleano de {num3} es: {bool3}")
print()

# Parte c: Convertir cadenas a números
str_num1 = "10002"
str_num2 = "100.02"
str_num3 = "0"

int_num1 = int(str_num1)     # Convierte la cadena a un entero
float_num2 = float(str_num2) # Convierte la cadena a un flotante
int_num3 = int(str_num3)     # Convierte la cadena a un entero

print("Parte c:")
print(f"La cadena '{str_num1}' convertida a entero es: {int_num1}")
print(f"La cadena '{str_num2}' convertida a flotante es: {float_num2}")
print(f"La cadena '{str_num3}' convertida a entero es: {int_num3}")
print()

# Parte d: Indicar valor booleano de las cadenas convertidas
bool_str1 = bool(str_num1)
bool_str2 = bool(str_num2)
bool_str3 = bool(str_num3)

print("Parte d:")
print(f"El valor booleano de la cadena '{str_num1}' es: {bool_str1}")
print(f"El valor booleano de la cadena '{str_num2}' es: {bool_str2}")
print(f"El valor booleano de la cadena '{str_num3}' es: {bool_str3}")
