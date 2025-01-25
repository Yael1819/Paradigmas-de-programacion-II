import random
import datetime  # Importamos el módulo datetime


# Función para guardar el historial de cada juego
def guardar_historial(juego_numero, intentos, gano):
    try:
        # Obtenemos la fecha y hora actual
        fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        with open("historial_juegos.txt", "a", encoding="utf-8") as archivo:
            archivo.write(f"Fecha y hora: {fecha_hora}\n")  # Agregamos la fecha y hora
            archivo.write(f"Numero Juego: {juego_numero}\n")
            archivo.write("Intentos historial:\n")
            for intento_num, intento in enumerate(intentos, start=1):
                archivo.write(f"Intento {intento_num}: {intento}\n")
            archivo.write(f"Intentos: {len(intentos)}/5\n")
            archivo.write(f"Gano: {gano}\n\n")
    except Exception as e:
        print(f"Error al guardar el historial: {e}")


# Función para ver el historial
def ver_historial():
    try:
        with open("historial_juegos.txt", "r", encoding="utf-8") as archivo:
            lectura_archivo = archivo.read()
            if lectura_archivo:
                print("\n--- Historial de Juegos ---")
                print(lectura_archivo)
            else:
                print("No hay historial de juegos aún.")
    except FileNotFoundError:
        print("El archivo de historial no existe.")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")


# Juego del adivinador
def jugar_adivinador():
    print("***Juego del adivinador***")
    b = 0  # Bandera para saber si el jugador ganó
    intentos = []
    juego_numero = random.randint(1, 100)  # Número del juego aleatorio
    i = 1

    while i <= 5:
        while True:
            try:
                num = int(input(f"Número de intentos: {i}, Ingrese un número (1-100): "))
                if num < 1 or num > 100:
                    print("Por favor, ingrese un número entre 1 y 100.")
                else:
                    break
            except ValueError:
                print("Entrada inválida. Por favor, ingrese un número entero.")

        intentos.append(num)  # Guardamos cada intento en la lista
        if juego_numero > num:
            print("El número a adivinar es mayor.")
        elif juego_numero < num:
            print("El número a adivinar es menor.")
        elif juego_numero == num:
            print("¡Felicidades! ¡Ganaste el juego!")
            b = 1  # Se cambia la bandera si gana
            break
        i = i + 1

    if b == 0:
        print(f"Perdiste, no pudiste adivinar el número: {juego_numero}")
    else:
        print(f"¡Felicidades! ¡Ganaste el juego!")

    # Guardar el historial del juego
    guardar_historial(juego_numero, intentos, b == 1)


def menu():
    while True:
        print("\n--- Menú ---")
        print("1. Jugar una ronda")
        print("2. Ver historial")
        print("3. Salir")
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            jugar_adivinador()
        elif opcion == "2":
            ver_historial()
        elif opcion == "3":
            print("\nGracias por jugar. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intenta nuevamente.")

# Ejecutar el menú
menu()
