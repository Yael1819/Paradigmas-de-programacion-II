# Nombre: Elton Yael Hernández Pérez
# Fecha: 7/11/2024
# Descripción: Programa para gestionar una lista de películas por ver con un menú interactivo.

# Lista donde se almacenarán las películas
peliculas = []

# Variable para controlar la opción seleccionada por el usuario
op = -1
while op != 0:  # Mientras el usuario no elija la opción de salir
    # Mostrar el menú principal
    print("\nMenú principal:")
    print("[1] Películas por ver")  # Opción para ver las películas pendientes
    print("[2] Películas por ver ordenadas de la A-Z")  # Opción para ordenar las películas de A-Z
    print("[3] Películas por ver ordenadas de la Z-A")  # Opción para ordenar las películas de Z-A
    print("[4] Añadir una película por ver")  # Opción para añadir una película
    print("[5] Añadir varias películas")  # Opción para añadir varias películas a la vez
    print("[6] Eliminar películas")  # Opción para eliminar una o varias películas
    print("[0] Salir")  # Opción para salir del programa

    op = int(input("Ingrese su opción: "))  # Solicita al usuario que ingrese su opción

    if op == 1:
        # Mostrar las películas por ver
        print("\nPelículas por ver:")
        if peliculas:  # Verifica si la lista de películas no está vacía
            for i, pelicula in enumerate(peliculas, 1):  # Recorre la lista de películas con índice
                print(f"{i}. {pelicula}")  # Muestra el índice y el nombre de cada película
        else:
            print("No hay películas en la lista.")  # Si la lista está vacía

    elif op == 2:
        # Mostrar las películas ordenadas de A-Z
        print("\nPelículas ordenadas de la A-Z:")
        if peliculas:  # Verifica si hay películas en la lista
            # Usa la función sorted() para ordenar las películas de A-Z
            for pelicula in sorted(peliculas):
                print(pelicula)  # Muestra cada película ordenada
        else:
            print("No hay películas en la lista.")  # Si la lista está vacía

    elif op == 3:
        # Mostrar las películas ordenadas de Z-A
        print("\nPelículas ordenadas de la Z-A:")
        if peliculas:  # Verifica si hay películas en la lista
            # Usa la función sorted() con reverse=True para ordenar de Z-A
            for pelicula in sorted(peliculas, reverse=True):
                print(pelicula)  # Muestra cada película ordenada
        else:
            print("No hay películas en la lista.")  # Si la lista está vacía

    elif op == 4:
        # Añadir una película
        nueva_pelicula = input(
            "\nIngrese el nombre de la película: ").strip()  # Solicita el nombre de la película y elimina espacios al inicio y al final
        if nueva_pelicula:  # Si el nombre no está vacío
            peliculas.append(nueva_pelicula)  # Añade la película a la lista
            print(f"La película '{nueva_pelicula}' ha sido añadida.")  # Confirma la adición
        else:
            print("El nombre de la película no puede estar vacío.")  # Si el nombre está vacío

    elif op == 5:
        # Añadir varias películas
        nuevas_peliculas = input("\nIngrese los nombres de las películas separados por comas: ").split(
            ",")  # Solicita varios nombres separados por comas
        nuevas_peliculas = [pelicula.strip() for pelicula in nuevas_peliculas if
                            pelicula.strip()]  # Elimina espacios extra y vacíos de los nombres
        if nuevas_peliculas:  # Si hay películas válidas
            peliculas.extend(nuevas_peliculas)  # Añade todas las nuevas películas a la lista
            print(f"Las películas han sido añadidas: {', '.join(nuevas_peliculas)}")  # Muestra las películas añadidas
        else:
            print("No se añadieron películas.")  # Si no se proporcionaron películas válidas

    elif op == 6:
        # Eliminar películas
        if peliculas:  # Si la lista no está vacía
            print("\nSubmenú de eliminación:")  # Muestra el encabezado del submenú
            print("[1] Eliminar por nombre de película")  # Opción para eliminar por nombre
            print("[2] Eliminar por índice de lista")  # Opción para eliminar por índice
            print("[0] Salir")  # Opción para salir del submenú

            subop = int(input("Ingrese su opción: "))  # Solicita la opción de eliminación

            if subop == 1:
                # Eliminar por nombre
                pelicula_a_eliminar = input(
                    "\nIngrese el nombre de la película a eliminar: ").strip()  # Solicita el nombre de la película
                if pelicula_a_eliminar in peliculas:  # Verifica si la película está en la lista
                    peliculas.remove(pelicula_a_eliminar)  # Elimina la película
                    print(f"La película '{pelicula_a_eliminar}' ha sido eliminada.")  # Confirma la eliminación
                else:
                    print(
                        f"La película '{pelicula_a_eliminar}' no está en la lista.")  # Si la película no está en la lista

            elif subop == 2:
                # Eliminar por índice
                indice = input(
                    "\nIngrese el índice de la película a eliminar (1 basado): ").strip()  # Solicita el índice de la película
                if indice.isdigit():  # Verifica si el índice es un número
                    indice = int(indice)  # Convierte el índice a entero
                    if 1 <= indice <= len(peliculas):  # Verifica si el índice es válido
                        pelicula_eliminada = peliculas.pop(indice - 1)  # Elimina la película por su índice (1 basado)
                        print(f"La película '{pelicula_eliminada}' ha sido eliminada.")  # Confirma la eliminación
                    else:
                        print("Índice fuera de rango.")  # Si el índice está fuera del rango de la lista
                else:
                    print("Debe ingresar un número válido.")  # Si el índice no es un número válido
        else:
            print("\nLa lista de películas está vacía.")  # Si la lista de películas está vacía

    elif op == 0:
        print("\nSaliendo del programa. ¡Hasta luego!")  # Mensaje de despedida al salir del programa

    else:
        print("\nOpción inválida. Intente nuevamente.")  # Si la opción no es válida


