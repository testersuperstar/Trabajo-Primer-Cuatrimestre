class Miembro:
    def __init__(self, nombre, dni):
        self.nombre = nombre
        self.dni = dni
        self.libros_prestados = []

    def tomar_libro(self, libro):
        self.libros_prestados.append(libro)

    def devolver_libro(self, libro):
        self.libros_prestados.remove(libro)

    def __str__(self):
        libros = [libro.titulo for libro in self.libros_prestados]

        return f"{self.nombre} - DNI: {self.dni} | Libros: {libros}"