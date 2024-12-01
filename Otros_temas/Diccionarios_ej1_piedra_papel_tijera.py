# Nombre: Elton Yael Hernández Pérez
# Fecha: 1/12/2024
# Descripción: Programa para jugar a Piedra, Papel o Tijera usando diccionarios

import random

# Reglas del juego utilizando un diccionario
reglas = {
    "piedra": {"gana_a": "tijera", "pierde_con": "papel"},
    "papel": {"gana_a": "piedra", "pierde_con": "tijera"},
    "tijera": {"gana_a": "papel", "pierde_con": "piedra"}
}

# Resultados de las partidas
resultados = {"Jugador": 0, "Computadora": 0, "Empates": 0}


# Función para jugar una ronda
def jugar_ronda():
    opciones = list(reglas.keys())
    jugador = input("\nElige: piedra, papel o tijera: ").strip().lower()

    if jugador not in opciones:
        print("Opción inválida. Intenta nuevamente.")
        return

    computadora = random.choice(opciones)
    print(f"La computadora eligió: {computadora}")

    if jugador == computadora:
        print("¡Es un empate!")
        resultados["Empates"] += 1
    elif reglas[jugador]["gana_a"] == computadora:
        print("¡Ganaste esta ronda!")
        resultados["Jugador"] += 1
    else:
        print("La computadora gana esta ronda.")
        resultados["Computadora"] += 1


# Función principal del juego
def piedra_papel_tijera():
    while True:
        print("\n--- Menú ---")
        print("1. Jugar una ronda")
        print("2. Ver resultados")
        print("3. Salir")
        opcion = input("Selecciona una opción: ").strip()

        if opcion == "1":
            jugar_ronda()
        elif opcion == "2":
            print("\nResultados actuales:")
            for clave, valor in resultados.items():
                print(f"{clave}: {valor}")
        elif opcion == "3":
            print("\nGracias por jugar. ¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intenta nuevamente.")


# Ejecutar el programa
piedra_papel_tijera()
