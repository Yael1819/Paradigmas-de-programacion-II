# Nombre: Elton Yael Hernández Pérez
# Fecha: 26/10/2024
# Descripción:
# Este programa realiza un sistema de autenticación simple.
# Compara los datos ingresados por el usuario con las credenciales almacenadas, si coinciden, el resultado indica un acceso correcto.

print("*** Sistema de autenticación ***")  # Muestra el título del sistema de autenticación.

usser = "alumno"     # Usuario válido predefinido
contra = "python"    # Contraseña válida predefinida

# Solicita al usuario que ingrese su nombre de usuario
cadena = input("Ingresa tu usuario: ")

# Solicita al usuario que ingrese su contraseña
cadena2 = input("Ingresa tu contraseña: ")

# Verifica si el usuario y la contraseña ingresados coinciden con los valores almacenados
resultado = cadena == usser and cadena2 == contra

# Muestra el resultado de la autenticación (True si es correcto, False si es incorrecto)
print(f"¿El acceso es correcto? {resultado}")
