# Nombre: Elton Yael Hernández Pérez
# Fecha: 30/10/2024
print("***Licenciatura en informatica***")
num = int(input("Ingrese  un número: "))
i=1
while i <= num:
    print(i, end=" ,")
    i = i + 1
    if i%3 == 0 and i%5 == 0:
        print("Licenciatura en Informática")
        i = i + 1
    if i%3 == 0 :
        print("Licenciatura")
        i = i + 1

    if i%5 == 0:
        print("Informática")
        i = i + 1