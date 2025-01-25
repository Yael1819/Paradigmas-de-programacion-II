import random
import datetime

# Set para almacenar los participantes
participantes = set()


# Función para mostrar el menú principal
def menu():
    print("\nMenú de la Rifa de la Laptop 503:")
    print("[1] Ver participantes")
    print("[2] Añadir participante")
    print("[3] Eliminar participante")
    print("[4] Seleccionar ganador")
    print("[5] Ver historial de ganadores")
    print("[6] Salir")


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

        # Guardar el historial del ganador con fecha y hora
        fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        numero_ganador = len(participantes)  # El número de ganador es el total de participantes

        try:
            with open("historial_ganadores.txt", "a", encoding="utf-8") as archivo:
                archivo.write(f"Fecha y hora: {fecha_hora}\n")
                archivo.write(f"Nombre del ganador: {ganador}\n")
                archivo.write(f"Número de ganador: {numero_ganador}\n\n")
        except Exception as e:
            print(f"Error al guardar el historial: {e}")
    else:
        print("\nNo hay participantes registrados para seleccionar un ganador.")


# Función para ver el historial de ganadores
def ver_historial():
    try:
        with open("historial_ganadores.txt", "r", encoding="utf-8") as archivo:
            lectura_archivo = archivo.read()
            if lectura_archivo:
                print("\n--- Historial de Ganadores ---")
                print(lectura_archivo)
            else:
                print("No hay historial de ganadores aún.")
    except FileNotFoundError:
        print("No se ha encontrado el archivo de historial.")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")


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
            # Ver historial de ganadores
            ver_historial()

        elif opcion == '6':
            # Salir
            print("\nSaliendo de la rifa. ¡Hasta luego!")
            break

        else:
            print("\nOpción inválida. Intente nuevamente.")


# Ejecutar el programa
rifa_laptop()
