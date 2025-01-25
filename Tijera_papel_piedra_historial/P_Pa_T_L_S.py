import random
import datetime  # Importamos el módulo datetime

# Reglas del juego utilizando un diccionario
reglas = {
    "piedra": {"gana_a": ["tijera", "lagarto"], "pierde_con": ["papel", "spock"]},
    "papel": {"gana_a": ["piedra", "spock"], "pierde_con": ["tijera", "lagarto"]},
    "tijera": {"gana_a": ["papel", "lagarto"], "pierde_con": ["piedra", "spock"]},
    "lagarto": {"gana_a": ["papel", "spock"], "pierde_con": ["piedra", "tijera"]},
    "spock": {"gana_a": ["tijera", "piedra"], "pierde_con": ["papel", "lagarto"]},
}

# Resultados de las partidas
resultados = {"Jugador": 0, "Computadora": 0, "Empates": 0}

# Función para jugar una ronda
def jugar_ronda():
    global resultados  # Usamos la variable global resultados
    opciones = list(reglas.keys())
    jugador = input("\nElige: piedra, papel, tijera, lagarto o spock: ").strip().lower()

    if jugador not in opciones:
        print("Opción inválida. Intenta nuevamente.")
        return

    computadora = random.choice(opciones)
    print(f"La computadora eligió: {computadora}")

    # Determinar el resultado
    if jugador == computadora:
        print("¡Es un empate!")
        resultados["Empates"] += 1
        ganador = "Empate"
    elif computadora in reglas[jugador]["gana_a"]:
        print("¡Ganaste esta ronda!")
        resultados["Jugador"] += 1
        ganador = "Jugador"
    else:
        print("La computadora gana esta ronda.")
        resultados["Computadora"] += 1
        ganador = "Computadora"

    # Obtener la fecha y hora actuales
    fecha_hora = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    # Guardar el historial en el archivo
    try:
        with open("historial_juego.txt", "a", encoding="utf-8") as archivo:
            archivo.write(f"Fecha y hora: {fecha_hora}\n")
            archivo.write(f"CPU: escogió {computadora}\nJugador: escogió {jugador}\nGanador: {ganador}\n")
            archivo.write(f"Resultado actual -> Jugador: {resultados['Jugador']}, Computadora: {resultados['Computadora']}, Empates: {resultados['Empates']}\n\n")
    except Exception as e:
        print(f"Error al guardar el historial: {e}")

    # Mostrar el resultado actual en consola
    print(f"\nResultado actual -> Jugador: {resultados['Jugador']}, Computadora: {resultados['Computadora']}, Empates: {resultados['Empates']}")

# Función para ver el historial del archivo
def ver_historial():
    try:
        with open("historial_juego.txt", "r", encoding="utf-8") as archivo:
            lectura_archivo = archivo.read()
            if lectura_archivo:
                print("\n--- Historial de partidas ---")
                print(lectura_archivo)
            else:
                print("No hay historial de partidas aún.")
    except FileNotFoundError:
        print("El archivo no existe.")
    except Exception as e:
        print(f"Error al leer el archivo: {e}")

# Función principal del juego
def piedra_papel_tijera_lagarto_spock():
    while True:
        print("\n--- Menú ---")
        print("1. Jugar una ronda")
        print("2. Ver historial")
        print("3. Salir")
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            jugar_ronda()

        elif opcion == "2":
            ver_historial()
        elif opcion == "3":
            print("\nGracias por jugar. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intenta nuevamente.")

# Ejecutar el programa
piedra_papel_tijera_lagarto_spock()
