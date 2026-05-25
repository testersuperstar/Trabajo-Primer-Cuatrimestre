from libro import Libro
from miembro import Miembro

from excepciones import (
    NombreInvalidoError,
    DNIInvalidoError,
    ISBNInvalidoError,
    AutorInvalidoError
)


class Biblioteca:

    def __init__(self):

        self.libros = []
        self.miembros = []

    # =========================
    # VALIDACIONES
    # =========================

    def validar_nombre(self, nombre):

        if not nombre.replace(" ", "").isalpha():

            raise NombreInvalidoError(
                "ERROR: El nombre no debe contener números."
            )

    def validar_dni(self, dni):

        if not dni.isdigit():

            raise DNIInvalidoError(
                "ERROR: El DNI solo debe contener números."
            )

        if len(dni) < 8:

            raise DNIInvalidoError(
                "ERROR: El DNI debe tener al menos 8 dígitos."
            )

    def validar_isbn(self, isbn):

        if not isbn.isdigit():

            raise ISBNInvalidoError(
                "ERROR: El ISBN debe contener solo números."
            )

    def validar_autor(self, autor):

        if not autor.replace(" ", "").isalpha():

            raise AutorInvalidoError(
                "ERROR: El autor no debe contener números."
            )

    # =========================
    # AGREGAR LIBRO
    # =========================

    def agregar_libro(self):

        try:

            titulo = input("Ingrese título: ")

            autor = input("Ingrese autor: ")
            self.validar_autor(autor)

            isbn = input("Ingrese ISBN: ")
            self.validar_isbn(isbn)

            libro = Libro(
                titulo,
                autor,
                isbn
            )

            self.libros.append(libro)

            print("Libro agregado correctamente.")

        except (
            AutorInvalidoError,
            ISBNInvalidoError
        ) as error:

            print(error)

    # =========================
    # AGREGAR MIEMBRO
    # =========================

    def agregar_miembro(self):

        try:

            nombre = input("Ingrese nombre: ")
            self.validar_nombre(nombre)

            dni = input("Ingrese DNI: ")
            self.validar_dni(dni)

            miembro = Miembro(
                nombre,
                dni
            )

            self.miembros.append(miembro)

            print("Miembro agregado correctamente.")

        except (
            NombreInvalidoError,
            DNIInvalidoError
        ) as error:

            print(error)

    # =========================
    # BUSCAR LIBRO
    # =========================

    def buscar_libro(self, isbn):

        for libro in self.libros:

            if libro.isbn == isbn:
                return libro

        return None

    # =========================
    # BUSCAR MIEMBRO
    # =========================

    def buscar_miembro(self, dni):

        for miembro in self.miembros:

            if miembro.dni == dni:
                return miembro

        return None

    # =========================
    # PRESTAR LIBRO
    # =========================

    def prestar_libro(self):

        isbn = input("Ingrese ISBN del libro: ")
        dni = input("Ingrese DNI del miembro: ")

        libro = self.buscar_libro(isbn)
        miembro = self.buscar_miembro(dni)

        if libro is None:

            print("Libro no encontrado.")
            return

        if miembro is None:

            print("Miembro no encontrado.")
            return

        if not libro.disponible:

            print("El libro no está disponible.")
            return

        libro.prestar(miembro)

        miembro.libros_prestados.append(libro)

        print("Libro prestado correctamente.")

    # =========================
    # DEVOLVER LIBRO
    # =========================

    def devolver_libro(self):

        isbn = input("Ingrese ISBN del libro: ")
        dni = input("Ingrese DNI del miembro: ")

        libro = self.buscar_libro(isbn)
        miembro = self.buscar_miembro(dni)

        if libro is None or miembro is None:

            print("Datos incorrectos.")
            return

        if libro.disponible:

            print("El libro ya estaba disponible.")
            return

        libro.devolver()

        miembro.libros_prestados.remove(libro)

        print("Libro devuelto correctamente.")

    # =========================
    # MOSTRAR LIBROS
    # =========================

    def mostrar_libros(self):

        print("\n===== LIBROS =====")

        for libro in self.libros:

            if libro.disponible:

                estado = "Disponible"

            else:

                estado = (
                    f"Prestado a "
                    f"{libro.prestado_a.nombre}"
                )

            print(
                f"Título: {libro.titulo} | "
                f"Autor: {libro.autor} | "
                f"ISBN: {libro.isbn} | "
                f"Estado: {estado}"
            )

    # =========================
    # MOSTRAR MIEMBROS
    # =========================

    def mostrar_miembros(self):

        print("\n===== MIEMBROS =====")

        for miembro in self.miembros:

            libros = []

            for libro in miembro.libros_prestados:

                libros.append(libro.titulo)

            print(
                f"Nombre: {miembro.nombre} | "
                f"DNI: {miembro.dni} | "
                f"Libros prestados: {libros}"
            )
