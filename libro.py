class Libro:
    def __init__(self, titulo, autor, isbn):
        self.titulo = titulo
        self.autor = autor
        self.isbn = isbn
        self.disponible = True
        self.prestado_a = None

    def prestar(self, miembro):
        self.disponible = False
        self.prestado_a = miembro

    def devolver(self):
        self.disponible = True
        self.prestado_a = None

    def __str__(self):
        estado = "Disponible" if self.disponible else f"Prestado a {self.prestado_a.nombre}"

        return f"{self.titulo} - {self.autor} | ISBN: {self.isbn} | {estado}"