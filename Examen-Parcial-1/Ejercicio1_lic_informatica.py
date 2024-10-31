# Nombre: Elton Yael Hernández Pérez
# Fecha: 30/10/2024
print("***Licenciatura en Informática***")
num = int(input("Ingrese un número: "))
i = 1

while i <= num:

    if i % 3 == 0 and i % 5 == 0:
        print("Licenciatura en Informática", end="\n")
    elif i % 3 == 0:
        print("Licenciatura ",end=",")
    elif i % 5 == 0:
        print("Informática",end=",")
    else:

        print(i, end=", ")

    i += 1
