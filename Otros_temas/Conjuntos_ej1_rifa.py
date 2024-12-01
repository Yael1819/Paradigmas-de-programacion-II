import random
# Nombre: Elton Yael Hernández Pérez
# Fecha: 30/11/2024
# Descripción:El programa implementa un sistema interactivo para gestionar
# una rifa de una laptop, diseñada específicamente para el grupo 503. Los participantes
# se administran utilizando un
# conjunto (set) en Python, que garantiza que no haya duplicados y facilita
# la gestión de los registros.
# Conjunto que almacenará los participantes registrados
participantes = set()


# Función para mostrar el menú principal
def menu():
    print("\nMenú de la Rifa de la Laptop 503:")
    print("[1] Ver participantes")
    print("[2] Añadir participante")
    print("[3] Eliminar participante")
    print("[4] Seleccionar ganador")
    print("[5] Salir")


# Función para añadir un participante
def añadir_participante():
    nombre = input("\nIngrese el nombre del participante: ").strip()
    if nombre:
        if nombre not in participantes:
            participantes.add(nombre)
            print(f"El participante '{nombre}' ha sido registrado.")
        else:
            print(f"El participante '{nombre}' ya está registrado.")
    else:
        print("El nombre no puede estar vacío.")


# Función para eliminar un participante
def eliminar_participante():
    nombre = input("\nIngrese el nombre del participante a eliminar: ").strip()
    if nombre in participantes:
        participantes.remove(nombre)
        print(f"El participante '{nombre}' ha sido eliminado.")
    else:
        print(f"El participante '{nombre}' no está registrado.")


# Función para seleccionar un ganador
def seleccionar_ganador():
    if participantes:
        ganador = random.choice(list(participantes))
        print(f"\nEl ganador de la laptop 503 es: {ganador}")
    else:
        print("\nNo hay participantes registrados para seleccionar un ganador.")


# Función principal para gestionar el programa
def rifa_laptop():
    while True:
        menu()  # Mostrar el menú
        opcion = input("\nSeleccione una opción: ").strip()

        if opcion == '1':
            # Ver participantes
            print(f"\nNúmero de participantes registrados: {len(participantes)}")
            if participantes:
                print("Participantes registrados:")
                for participante in participantes:
                    print(participante)
            else:
                print("No hay participantes registrados.")

        elif opcion == '2':
            # Añadir participante
            añadir_participante()

        elif opcion == '3':
            # Eliminar participante
            eliminar_participante()

        elif opcion == '4':
            # Seleccionar ganador
            seleccionar_ganador()

        elif opcion == '5':
            # Salir
            print("\nSaliendo de la rifa. ¡Hasta luego!")
            break

        else:
            print("\nOpción inválida. Intente nuevamente.")


# Ejecutar el programa
rifa_laptop()
