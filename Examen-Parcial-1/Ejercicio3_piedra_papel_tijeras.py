# Nombre: Elton Yael Hernández Pérez
# Fecha: 30/10/2024
import random
print("***Juego piedra papel o tijera**")
vicjugador=0
viccpu=0
empate=0
op = -1

while op != 0:
    print(f"Victorias del jugador: {vicjugador},empates: {empate},victorias de la CPU: {viccpu}")
    print("\nSeleccione una opción:")
    print("Piedra. [1]")
    print("Papel. [2]")
    print("Tijeras. [3]")
    print("Salir. [0]")


    op = int(input("Ingrese su opción: "))


    if op == 1:
        cpu = random.randint(1, 3)

        if cpu == 1:
            print("Jugador: piedra. Cpu: piedra, resultado: empate")
            empate=empate+1
        elif  cpu == 2:
            print("Jugador: piedra. Cpu: papel, resultado: gano la cpu")
            viccpu=viccpu+1
        elif cpu == 3:
            print("Jugador: piedra. Cpu: tijera, resultado: gano el jugador")
            vicjugador=vicjugador+1
    elif op == 2:
        cpu = random.randint(1, 3)
        if  cpu == 2:
            print("Jugador: papel. Cpu: papel, resultado: empate")
            empate = empate + 1
        elif cpu == 1:
            print("Jugador: papel. Cpu: piedra, resultado: gano el jugador")
            vicjugador = vicjugador + 1
        elif cpu == 3:
            print("Jugador: papel. Cpu: tijera, resultado: gano la cpu")
            viccpu = viccpu + 1
    elif op == 3:
        cpu = random.randint(1, 3)
        if cpu == 3:
            print("Jugador: tijera. Cpu: tijera, resultado: empate")
            empate = empate + 1
        elif cpu == 1:
            print("Jugador: tijera. Cpu: piedra, resultado: gano la cpu")
            viccpu = viccpu + 1
        elif cpu == 2:
            print("Jugador: tijera. Cpu: papel, resultado: gano el jugador")
            vicjugador = vicjugador + 1
    elif op == 0:

        print("Hasta luego,gracias.....de nada...")
    else:
        print("Opción no válida, vuelva a intentar.")

print("Programa terminado.")
