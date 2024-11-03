# Nombre: Elton Yael Hernández Pérez
# Fecha: 30/10/2024

import random
print("***Juego del adivinador**")
i=1
b=0
adivina = random.randint(1, 100)
while i <= 5:

    num = int(input(f"Número de intentos: {i},Ingrese un número(1-100):"))
    if adivina > num:
        print("El número a adivinar es mayor.")
    elif adivina < num:
        print("El número a adivinar es menor.")
    elif adivina == num:
        print("¡Felicidades! ¡Ganaste el juego!")
        b=1
        break
    i = i + 1
if b == 0:
    print(f"Perdiste ,no pudiste adivinar el número :{adivina} ")
print("Fin del juego")
