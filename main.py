from biblioteca import Biblioteca

biblioteca = Biblioteca()

while True:

    print("\n===== SISTEMA BIBLIOTECA =====")
    print("1. Agregar libro")
    print("2. Agregar miembro")
    print("3. Prestar libro")
    print("4. Devolver libro")
    print("5. Mostrar libros")
    print("6. Mostrar miembros")
    print("7. Salir")

    opcion = input("Seleccione una opción: ")

    if opcion == "1":

        biblioteca.agregar_libro()

    elif opcion == "2":

        biblioteca.agregar_miembro()

    elif opcion == "3":

        biblioteca.prestar_libro()

    elif opcion == "4":

        biblioteca.devolver_libro()

    elif opcion == "5":

        biblioteca.mostrar_libros()

    elif opcion == "6":

        biblioteca.mostrar_miembros()

    elif opcion == "7":

        print("Saliendo del sistema...")
        break

    else:

        print("Opción incorrecta.")